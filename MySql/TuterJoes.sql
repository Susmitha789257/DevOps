create database joes;
drop database joes;
create database tutorjoes; 
show databases;
use tutorjoes;
create table users
(id int not null auto_increment,
name varchar(50) not null,
age int not null,
primary key(ID)
);
show tables;
describe users;
alter table users add gender varchar(10) not null after age; 
alter table users add city varchar(10) not null,add contact varchar(50) not null;
alter table users modify city varchar(50) not null;
alter table students1 rename to students;
select * from students;
insert into students values(null,'ram',25,'male','salem','9908609005');
insert into students (name,age,gender,city,contact) values
('sham',25,'male','salem','9908609005'),
('sham',25,'male','salem','9908609005');
delete from students where id=4;
update students set city="chittoor" where id=3;
update students set city="chittoor",age=88 where id=2;
truncate table students;
INSERT INTO students (name, age, gender, city, contact) VALUES
('Sam', 23, 'Male', 'Namakal', '723467'),
('Ram', 25, 'Male', 'Salem', '9908609005'),
('John', 22, 'Male', 'Chennai', '9876543210'),
('Arun', 24, 'Male', 'Coimbatore', '8901234567'),
('Sita', 21, 'Female', 'Madurai', '9234567890'),
('Kiran', 26, 'Male', 'Trichy', '8123456789'),
('Meena', 23, 'Female', 'Erode', '9345678901'),
('Raj', 27, 'Male', 'Tiruppur', '8456789012'),
('Divya', 24, 'Female', 'Dindigul', '7567890123'),
('Vimal', 22, 'Male', 'Thanjavur', '6789012345'),
('Swetha', 25, 'Female', 'Kanchipuram', '5678901234'),
('Gokul', 28, 'Male', 'Villupuram', '4567890123'),
('Priya', 21, 'Female', 'Puducherry', '3456789012'),
('Karthik', 29, 'Male', 'Theni', '2345678901'),
('Latha', 23, 'Female', 'Virudhunagar', '1234567890'),
('Senthil', 24, 'Male', 'Tirunelveli', '9123456780'),
('Anita', 22, 'Female', 'Thoothukudi', '8234567891'),
('Balaji', 26, 'Male', 'Nagapattinam', '7345678902'),
('Preethi', 25, 'Female', 'Vellore', '6456789013'),
('Ravi', 27, 'Male', 'Cuddalore', '5567890124'),
('Anil', 23, 'Male', 'Dharmapuri', '4678901235'),
('Gayathri', 22, 'Female', 'Krishnagiri', '3789012346'),
('Vinoth', 24, 'Male', 'Ariyalur', '2890123457'),
('Kavya', 21, 'Female', 'Perambalur', '1901234568'),
('Madhan', 25, 'Male', 'Karur', '8012345679'),
('Sundar', 22, 'Male', 'Ramanathapuram', '9023456781'),
('Nisha', 24, 'Female', 'Sivaganga', '1034567892'),
('Aravind', 26, 'Male', 'Tiruvannamalai', '2145678903'),
('Jaya', 23, 'Female', 'Kanyakumari', '3256789014'),
('Saravanan', 25, 'Male', 'Pudukottai', '4367890125'),
('Keerthi', 22, 'Female', 'Chidambaram', '5478901236'),
('Manoj', 24, 'Male', 'Mayiladuthurai', '6589012347'),
('Deepa', 21, 'Female', 'Thiruvallur', '7690123458'),
('Harish', 26, 'Male', 'Namakkal', '8701234569'),
('Ragini', 25, 'Female', 'Salem', '9812345670'),
('Ganesh', 27, 'Male', 'Coimbatore', '1923456781'),
('Vani', 23, 'Female', 'Madurai', '2034567892'),
('Rahul', 22, 'Male', 'Trichy', '3145678903'),
('Monika', 24, 'Female', 'Erode', '4256789014'),
('Ashwin', 26, 'Male', 'Tiruppur', '5367890125'),
('Sanjay', 21, 'Male', 'Dindigul', '6478901236'),
('Rekha', 24, 'Female', 'Thanjavur', '7589012347'),
('Surya', 22, 'Male', 'Kanchipuram', '8690123458'),
('Naveen', 25, 'Male', 'Villupuram', '9701234569'),
('Sowmya', 23, 'Female', 'Puducherry', '9812345670'),
('Vijay', 22, 'Male', 'Theni', '1923456781'),
('Pooja', 26, 'Female', 'Virudhunagar', '2034567892'),
('Kishore', 24, 'Male', 'Tirunelveli', '3145678903'),
('Varsha', 21, 'Female', 'Thoothukudi', '4256789014'),
('Sathish', 25, 'Male', 'Nagapattinam', '5367890125');
select * from students;
select name,age,city from students where city="salem" and age>=25;
select name,age,city from students where (city="Dindigul" or city="salem") and age>=21 order by city;
select city from students;
select count(distinct city) from students;
select * from students order by id desc limit 0,2;
select max(age) from  students;
select min(age) from students;
select round(avg(age),0) from students;
select sum(age) from students;
select gender,count(id) as total from students group by gender;
select city,count(id) as total from students group by city;
select name from students where name like "RA%" ;
select name from students where name like "%hA" ;
select name from students where name like "%A%" ;
select * from students where city="namakal" or city="salem";
select * from students where city in("salem","namakal");
select * from students where city not in("salem","namakal");
select name from students where name not like "ra%";
select name,age from students where age between 21 and 22 ;
select name,age from students where age not between 21 and 22 ;
create table attendance(
aid int not null auto_increment,
id int not null,
adate date not null,
astatus varchar(10) not null,
primary key(aid) 
);
truncate table attendance;
INSERT INTO attendance (id, adate, astatus) VALUES
(1, '2024-03-01', 'P'), (2, '2024-03-01', 'A'), (3, '2024-03-01', 'P'), (4, '2024-03-01', 'A'),
(1, '2024-03-02', 'A'), (2, '2024-03-02', 'P'), (3, '2024-03-02', 'A'), (4, '2024-03-02', 'P'),
(1, '2024-03-03', 'P'), (2, '2024-03-03', 'P'), (3, '2024-03-03', 'A'), (4, '2024-03-03', 'A'),
(1, '2024-03-04', 'A'), (2, '2024-03-04', 'A'), (3, '2024-03-04', 'P'), (4, '2024-03-04', 'P');
select * from attendance;
select * from students;
select * from attendance where id=1;
select id,count(adate) as working from attendance group by id;
select id,count(adate) as working,count(if(astatus="p",1,null)) as present from attendance group by id;
select * from attendance where id=3;
create table emp(
id int unsigned not null auto_increment,
name varchar(45) not null,
design varchar(45) not null,
dob date not null,
primary key (ID)
);
drop table emp;
insert into emp (name,design,dob) values ('ram','manager','2018-09-10'),('sam','hr','2018-09-10'),('tom','amc','2018-09-11'),('ravi','sales','2018-09-23'),('kumar','sales','2018-10-02');
select * from emp;
create table salary(
sid int not null auto_increment,
id int not null,
sdate date not null,
amt int not null,
primary key(sid)
);
truncate table salary;
insert into salary(id,sdate,amt) values(1,'2018-09-01',10000),(2,'2018-09-01',7500),(3,'2018-09-01',6000),(4,'2018-09-01',4000);
select * from emp;
select * from salary;
select emp.name,emp.design,salary.sdate,salary.amt from emp inner join salary on emp.id=salary.id;
select emp.name,emp.design,salary.sdate,salary.amt from emp left join salary on emp.id=salary.id;
select emp.name,emp.design,salary.sdate,salary.amt from emp right join salary on emp.id=salary.id;
insert into salary(id,sdate,amt) values(6,'2018-09-01',4000);
select * from students;
select * from attendance;
select students.name,attendance.adate,attendance.astatus from students inner join attendance on students.id=attendance.id;
select distinct city from students;
select name,city from students;
/* SALEM=100
NAMAKAL=150
chennai=300
hosur=350
dhar=450
 */
 update students set city="SALEM" where id>20;
 select name,city,
 (
	CASE
		when city="salem" then 100
        when city="namakal" then 150
        when city="chennai" then 300
        when city="hosur" then 350
        when city="dhar" then 450 
        else 0
    END
) as amt from students;

SET SQL_SAFE_UPDATES = 0;
update students set city='bangalore' where city='salem';
SET SQL_SAFE_UPDATES = 1;
/* part-2*/
show databases;
use tutorjoes;
show tables;
select * from students;
alter table students add comm varchar(20) not null,add cid int not null,add rollno varchar(20);
update students set ROLLNO="A1025" WHERE ID=25;
update students set comm="BC" WHERE ID=45;
set sql_safe_updates=1;
update students set comm=case when id<=5 then 'mbc' else 'sc' end;
set sql_safe_updates=0;
create table course(
cid int not null auto_increment,
cname varchar(30),
primary key(cid)
);
SELECT * FROM marks;
select students.name,students.rollno,students.cid from students;
select students.name,students.rollno,course.cname from students inner join course on students.cid=course.cid;
select students.name,students.rollno,course.cname,marks.m1,marks.m2,marks.m3 from students inner join course on students.cid=course.cid inner join marks on students.id=marks.id;
select students.name,students.rollno,course.cname as course ,marks.m1,marks.m2,marks.m3,(marks.m1+marks.m2+marks.m3) as total,round((marks.m1+marks.m2+marks.m3)/3,2) as average
from students inner join course on students.cid=course.cid inner join marks on students.id=marks.id;

select students.name,students.rollno,course.cname as course ,marks.m1,marks.m2,marks.m3,(marks.m1+marks.m2+marks.m3) as total,round((marks.m1+marks.m2+marks.m3)/3,2) as average,
case when marks.m1>=35 and marks.m2>=35 and marks.m3>=35 then 'pass' else 'fail' end as result,
case when marks.m1>=35 and marks.m2>=35 and marks.m3>=35 then 
case when round((marks.m1+marks.m2+marks.m3)/3,0)>=90 and round((marks.m1+marks.m2+marks.m3)/3,0)<=100 then 'A' 
	when round((marks.m1+marks.m2+marks.m3)/3,0)>=80 and round((marks.m1+marks.m2+marks.m3)/3,0)<=89 then 'b' 
    else 'c' end
    else 'no grade'
end as grade
from students inner join course on students.cid=course.cid inner join marks on students.id=marks.id;

create view reports as
select students.name,students.rollno,course.cname as course ,marks.m1,marks.m2,marks.m3,(marks.m1+marks.m2+marks.m3) as total,round((marks.m1+marks.m2+marks.m3)/3,2) as average,
case when marks.m1>=35 and marks.m2>=35 and marks.m3>=35 then 'pass' else 'fail' end as result,
case when marks.m1>=35 and marks.m2>=35 and marks.m3>=35 then 
case when round((marks.m1+marks.m2+marks.m3)/3,0)>=90 and round((marks.m1+marks.m2+marks.m3)/3,0)<=100 then 'A' 
	when round((marks.m1+marks.m2+marks.m3)/3,0)>=80 and round((marks.m1+marks.m2+marks.m3)/3,0)<=89 then 'b' 
    else 'c' end
    else 'no grade'
end as grade
from students inner join course on students.cid=course.cid inner join marks on students.id=marks.id where course.cname='mba' having result="PASS" and (average>=70 and average<=100);
select * from reports;
select * from students;
select * from marks;
select students.name,students.rollno,marks.m1,marks.m2,marks.m3 from students inner join marks on students.id=marks.id;

update marks inner join students on students.id=marks.id set m1=100,m2=100,m3=100 where stuents.rollno='A1001';
/*Triggers*/
/*
create trigger trigger_name trigger_time trigger_event
on table_name
for each row
begin
...
end;
before,after
insert update and delete
*/
show tables;
select * from product;
select * from price_logs;

  