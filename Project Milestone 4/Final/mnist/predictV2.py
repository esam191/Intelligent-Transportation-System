# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import argparse
import json
import logging
import os

import apache_beam as beam
import tensorflow as tf
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions



def singleton(cls):
  instances = {}
  def getinstance(*args, **kwargs):
    if cls not in instances:
      instances[cls] = cls(*args, **kwargs)
    return instances[cls]
  return getinstance



@singleton
class Model():

  def __init__(self, checkpoint):
    with tf.Graph().as_default() as graph:
      sess = tf.compat.v1.InteractiveSession()
      saver = tf.compat.v1.train.import_meta_graph(os.path.join(checkpoint, 'export.meta'))
      saver.restore(sess, os.path.join(checkpoint, 'export'))

      inputs = json.loads(tf.compat.v1.get_collection('inputs')[0])
      outputs = json.loads(tf.compat.v1.get_collection('outputs')[0])

      self.x = graph.get_tensor_by_name(inputs['image'])
      self.p = graph.get_tensor_by_name(outputs['scores'])
      self.input_key = graph.get_tensor_by_name(inputs['key'])
      self.output_key = graph.get_tensor_by_name(outputs['key'])
      self.sess = sess


class PredictDoFn(beam.DoFn):

  def process(self, element, checkpoint):
    model = Model(checkpoint)
    input_key = int(element['key'])
    image = element['image'].split(',')
    output_key, pred = model.sess.run(
        [model.output_key, model.p],
        feed_dict={model.input_key: [input_key], model.x: [image]})
    result = {}
    result['imageKey'] = (int)(output_key[0])
    for i, val in enumerate(pred[0].tolist()):
      result['pred%d' % i] = val
    return [result]

def _to_dictionary(line):
    result = {}
    result['key'], result['image'] = line.split(':')
    return result


def run(argv=None):
  parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument('--input', dest='input', required=True,
                      help='Input file to process.')
  parser.add_argument('--output', dest='output', required=True,
                      help='Output file to write results to.')
  parser.add_argument('--model', dest='model', required=True,
                      help='Checkpoint file of the model.')
  parser.add_argument('--source', dest='source', required=True,
                      help='Data source location (text|mysql).')
  known_args, pipeline_args = parser.parse_known_args(argv)
  pipeline_options = PipelineOptions(pipeline_args)
  pipeline_options.view_as(SetupOptions).save_main_session = True;
  with beam.Pipeline(options=pipeline_options) as p:
    if known_args.source == 'text':
        images = (p | 'ReadFromText' >> beam.io.ReadFromText(known_args.input)
            | 'ConvertToDict'>> beam.Map(_to_dictionary))
        predictions = images | 'Prediction' >> beam.ParDo(PredictDoFn(), known_args.model)
        predictions | 'WriteToText' >> beam.io.WriteToText(known_args.output)
    elif known_args.source == 'mysql':
        from beam_nuggets.io import relational_db
        input_config = relational_db.SourceConfiguration(
            drivername='mysql+pymysql', host=known_args.input,  
            port=3306,                  username='user',
            password='SOFE4630U',       database='myDB',
        )
        output_config = relational_db.SourceConfiguration(
            drivername='mysql+pymysql', host=known_args.output,  
            port=3306,                  username='user',
            password='SOFE4630U',       database='myDB',
        )
        images= (p | "Read from SQL">>relational_db.ReadFromDB(source_config=input_config,
            table_name='images',query='select * from images'));
        predictions = (images | 'Prediction' >> beam.ParDo(PredictDoFn(), known_args.model));
        table_config = relational_db.TableConfiguration(
            name='results',
            create_if_missing=True,
            primary_key_columns=['imageKey']
        )
        predictions| "To SQL">> relational_db.Write(source_config=output_config,table_config=table_config)
        
if __name__ == '__main__':
  logging.getLogger().setLevel(logging.INFO)
  run()