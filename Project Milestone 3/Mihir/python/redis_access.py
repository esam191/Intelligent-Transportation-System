import redis        # pip install redis
ip="34.132.201.110"
r = redis.Redis(host=ip, port=6379, db=0,password='SOFE4630U')
#string to bite is called deserialization 
v=r.get('key1');
print(v);
#string to bite is called serialization 
r.set('key1','30'.encode('utf-8')); 

