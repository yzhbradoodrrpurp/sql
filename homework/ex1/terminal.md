```shell
yzhbradoodrrpurp@yzhbradoodrrpurps-MacBook sql % cd homework/ex1
yzhbradoodrrpurp@yzhbradoodrrpurps-MacBook ex1 % createdb ex1
zsh: command not found: createdb
yzhbradoodrrpurp@yzhbradoodrrpurps-MacBook ex1 % source ~/.zshrc
yzhbradoodrrpurp@yzhbradoodrrpurps-MacBook ex1 % pg_ctl \
  -D "$HOME/Library/Application Support/Postgres/var-18" \
  -l "$HOME/Library/Application Support/Postgres/var-18/server.log" \
  start
waiting for server to start.... done
server started
yzhbradoodrrpurp@yzhbradoodrrpurps-MacBook ex1 % createdb ex1
yzhbradoodrrpurp@yzhbradoodrrpurps-MacBook ex1 % psql -v ON_ERROR_STOP=1 -d ex1 \
  -f create_schema.sql \
  -f insert_data.sql \
  -f e2c.txt \
  -f e2i.txt \
  -f answers.sql
psql:create_schema.sql:1: NOTICE:  table "prereq" does not exist, skipping
DROP TABLE
psql:create_schema.sql:2: NOTICE:  table "time_slot" does not exist, skipping
DROP TABLE
psql:create_schema.sql:3: NOTICE:  table "advisor" does not exist, skipping
DROP TABLE
psql:create_schema.sql:4: NOTICE:  table "takes" does not exist, skipping
DROP TABLE
psql:create_schema.sql:5: NOTICE:  table "student" does not exist, skipping
DROP TABLE
psql:create_schema.sql:6: NOTICE:  table "teaches" does not exist, skipping
DROP TABLE
psql:create_schema.sql:7: NOTICE:  table "section" does not exist, skipping
DROP TABLE
psql:create_schema.sql:8: NOTICE:  table "instructor" does not exist, skipping
DROP TABLE
psql:create_schema.sql:9: NOTICE:  table "course" does not exist, skipping
DROP TABLE
psql:create_schema.sql:10: NOTICE:  table "department" does not exist, skipping
DROP TABLE
psql:create_schema.sql:11: NOTICE:  table "classroom" does not exist, skipping
DROP TABLE
CREATE TABLE
CREATE TABLE
CREATE TABLE
CREATE TABLE
CREATE TABLE
CREATE TABLE
CREATE TABLE
CREATE TABLE
CREATE TABLE
CREATE TABLE
CREATE TABLE
DELETE 0
DELETE 0
DELETE 0
DELETE 0
DELETE 0
DELETE 0
DELETE 0
DELETE 0
DELETE 0
DELETE 0
DELETE 0
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
psql:e2c.txt:1: NOTICE:  table "hourlog" does not exist, skipping
DROP TABLE
psql:e2c.txt:2: NOTICE:  table "project" does not exist, skipping
DROP TABLE
psql:e2c.txt:3: NOTICE:  drop cascades to 3 other objects
DETAIL:  drop cascades to constraint course_dept_name_fkey on table course
drop cascades to constraint instructor_dept_name_fkey on table instructor
drop cascades to constraint student_dept_name_fkey on table student
DROP TABLE
psql:e2c.txt:4: NOTICE:  table "employee" does not exist, skipping
DROP TABLE
CREATE TABLE
CREATE TABLE
ALTER TABLE
ALTER TABLE
CREATE TABLE
CREATE TABLE
BEGIN
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
COMMIT
          title           
--------------------------
 Robotics
 Image Processing
 Database System Concepts
(3 rows)

  id   
-------
 44553
(1 row)

 highest_salary 
----------------
       95000.00
(1 row)

  id   |   name   | dept_name |  salary  
-------+----------+-----------+----------
 22222 | Einstein | Physics   | 95000.00
(1 row)

 course_id | sec_id | enrollment 
-----------+--------+------------
 CS-101    | 1      |          6
 CS-347    | 1      |          2
 PHY-101   | 1      |          1
(3 rows)

 maximum_enrollment 
--------------------
                  6
(1 row)

 course_id | sec_id | enrollment 
-----------+--------+------------
 CS-101    | 1      |          6
(1 row)

  ssn  | name  |  salary  
-------+-------+----------
 10001 | Zhao  | 20000.00
 20001 | Singh | 19000.00
 30001 | Sun   | 15000.00
 40001 | Li    | 14800.00
(4 rows)

 name |  ssn  
------+-------
 Zhao | 10001
 Sun  | 30001
(2 rows)

 name  |  ssn  
-------+-------
 Zhao  | 10001
 Singh | 20001
(2 rows)

 name |  ssn  
------+-------
 Zhou | 30002
 Wu   | 30003
(2 rows)

 name  |  ssn  
-------+-------
 Zhao  | 10001
 Singh | 20001
(2 rows)

 name |  ssn  
------+-------
 Zhao | 10001
(1 row)

yzhbradoodrrpurp@yzhbradoodrrpurps-MacBook ex1 % 
```

