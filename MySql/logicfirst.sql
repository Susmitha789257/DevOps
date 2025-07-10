/* 
Logic First part-1
multi line comment
*/
-- single line comment
show character set;
create database logicfirst;
use logicfirst;
drop schema logicfirst;
drop schema if exists logicfirst;
create database if not exists logicfirst;
show tables;
create table student(
id int primary key,
name varchar(30),
gpa decimal(3,2)
);
describe student;
drop table employee;
select * from student;
alter table student add department varchar(10);
alter table student drop column department;
insert into student values(1,"susmitha",7.9);
truncate table employee;
insert into student (id,name,gpa) values (3,"akanksha",9.4);
select id,name from student;
create table employee(
empid int primary key,
ename varchar(30),
jobdesc varchar(20),
salary int
);
insert into employee (empid,ename,jobdesc)values(1,"r%am",'admin'),
(2,'haroni','manager');
select * from employee where ename<>'harini';
select * from employee where salary not between 1000 and 10000;
select * from employee where ename like "%i%";
select * from employee where ename like "_%n%_";
SELECT * FROM employee WHERE ename LIKE '%\%%';
update employee set jobdesc="k";
set sql_safe_updates=1;
SELECT * FROM employee order by (case
when jobdesc="ceo" then 1
else 100
end);
-- string functions
 select ucase(ename)as name,salary from employee ;
 select ename,char_length(ename) as length from employee;
select ename, concat('rs.',format(salary,0)) as length from employee;
select ename,left(jobdesc,3) from employee;
-- date functions
alter table employee add column hiredate date;
select * from employee;
update employee set hiredate="2018-07-09";
set sql_safe_updates=0;
select now();
SELECT date(now());
select curdate();
select date_FORMAT(curdate(),"%D/%M/%Y")as date;
select datediff(curdate(),"2024-05-23");
select date_add(curdate(),interval 1 month);
select jobdesc,count(empid) as count from employee group by jobdesc having count>0;
-- constrains
-- table(not null, default 'unassigned',unique,check(salary>100),auto_increment)
select * from employee;
alter table employee modify hiredate date default '2002-01-01';
alter table employee alter hiredate set default '2002-01-01';
alter table employee alter column hiredate set default "2002-02-02";
describe employee;
alter table employee alter hiredate drop default;
alter table employee add check(salary>100);
alter table employee add constraint sal check(salary>100);
alter table employee add constraint salary check (salary>1000);
select * from information_schema.check_constraints;
select * from information_schema.table_constraints;
show databases;
SELECT 
    cc.constraint_name,
    cc.check_clause,
    tc.table_name
FROM 
    information_schema.check_constraints cc
JOIN 
    information_schema.table_constraints tc 
    ON cc.constraint_name = tc.constraint_name
WHERE 
    tc.table_name = 'employee'
    AND cc.check_clause LIKE '%> 1000%';
alter table employee drop check salary;
alter table employee add constraint fk foreign key(Branch_id) references branch(branch_id) on delete set null;
-- on delete set null,cascade





