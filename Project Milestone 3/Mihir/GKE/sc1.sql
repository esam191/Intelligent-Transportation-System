CREATE DATABASE IF NOT EXISTS myDB;
USE myDB;

DROP TABLE IF EXISTS test;


CREATE TABLE IF NOT EXISTS test (
  id serial NOT NULL PRIMARY KEY,
  name varchar(100),
  email varchar(200),
  department varchar(200),
  modified timestamp default CURRENT_TIMESTAMP NOT NULL,
  INDEX `modified_index` (`modified`)
);
USE myDB;
INSERT INTO test (name, email, department) VALUES ('alice', 'alice@abc.com', 'eng.');
INSERT INTO test (name, email, department) VALUES ('bob1', 'bob1@abc.com', 'sales');
INSERT INTO test (name, email, department) VALUES ('bob2', 'bob2@abc.com', 'sales');
INSERT INTO test (name, email, department) VALUES ('bob3', 'bob3@abc.com', 'sales');
INSERT INTO test (name, email, department) VALUES ('bob4', 'bob4@abc.com', 'sales');
INSERT INTO test (name, email, department) VALUES ('bob5', 'bob5@abc.com', 'sales');
INSERT INTO test (name, email, department) VALUES ('bob6', 'bob6@abc.com', 'sales');
INSERT INTO test (name, email, department) VALUES ('bob7', 'bob7@abc.com', 'sales');
INSERT INTO test (name, email, department) VALUES ('bob8', 'bob8@abc.com', 'sales');
INSERT INTO test (name, email, department) VALUES ('bob9', 'bob9@abc.com', 'sales');

