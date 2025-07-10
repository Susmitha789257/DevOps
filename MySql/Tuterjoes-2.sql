use tutorjoes;
show tables;
select * from students;
select * from course;
select * from marks;
create table marks(
mid int not null auto_increment,
id int not null,
m1 int not null,
m2 int not null,
m3 int not null,
primary key(mid)
);
insert into students (id,name,age,gender,city,contact,comm,cid,rollno) values(null,"susmitha",23,"F","chittoor",9908609005,"SC",1,"A100");
describe students;
truncate students;
select * from students;
INSERT INTO students (id, name, age, gender, city, contact, comm, cid, rollno)
VALUES 
(NULL, "Susmitha", 23, "F", "Chittoor", 9908609005, "SC", 1, "A100"),
(NULL, "Karthik", 21, "M", "Chennai", 9876543210, "MBC", 2, "A101"),
(NULL, "Priya", 22, "F", "Madurai", 9845123678, "CA", 3, "A102"),
(NULL, "Rahul", 24, "M", "Coimbatore", 9786054321, "SC", 1, "A103"),
(NULL, "Anjali", 20, "F", "Tirupati", 9638527410, "MBC", 2, "A104"),
(NULL, "Vikram", 23, "M", "Salem", 9567843210, "CA", 3, "A105"),
(NULL, "Meena", 22, "F", "Vellore", 9456789012, "SC", 1, "A106"),
(NULL, "Arun", 21, "M", "Erode", 9345678901, "MBC", 2, "A107"),
(NULL, "Divya", 23, "F", "Chittoor", 9234567890, "CA", 3, "A108"),
(NULL, "Sathish", 24, "M", "Tiruvannamalai", 9123456789, "SC", 1, "A109");
insert into course (cname)values("SC"),("MBC"),("CA");
INSERT INTO marks (id, m1, m2, m3) VALUES
(1, 56, 57, 87),
(2, 78, 65, 80),
(3, 45, 50, 60),
(4, 90, 88, 92),
(5, 70, 75, 80),
(6, 55, 60, 65),
(7, 85, 82, 90),
(8, 60, 62, 58),
(9, 77, 73, 79),
(10, 66, 68, 70);
select students.name,students.rollno,course.cname from students inner join course on students.cid=course.cid;
select students.name,students.rollno,course.cname,marks.m1,marks.m2,marks.m3 from students inner join course on students.cid=course.cid inner join marks on students.id=marks.id;
create view reports as
select students.name,students.rollno,course.cname,marks.m1,marks.m2,marks.m3,(marks.m1+marks.m2+marks.m3) as total,round((marks.m1+marks.m2+marks.m3)/3,0) as average,(
case 
  when (marks.m1>=35)and(marks.m2>=35)and(marks.m3>=35) then "P"
  else "F"
end
) as result,(
case 
  when (marks.m1>=35)and(marks.m2>=35)and(marks.m3>=35) then 
   Case when round((marks.m1+marks.m2+marks.m3)/3,0)>=90 and round((marks.m1+marks.m2+marks.m3)/3,0)<=100 then "A" 
   when round((marks.m1+marks.m2+marks.m3)/3,0)>=80 and round((marks.m1+marks.m2+marks.m3)/3,0)<=89 then "B"
   else "c"
   end
  else "No Grade"
end
) as Grade from students inner join course on students.cid=course.cid inner join marks on students.id=marks.id where course.cname="MBC" having result="P"
and (average>=70 and average<=100);
update marks set m1=99,m2=99,m3=99 where id=3;
set sql_safe_updates=1;
show full tables;
show databases;
select * from reports;
drop view reports;
select * from students;
select * from marks;
select students.name,students.rollno,marks.m1,marks.m2,marks.m3 from students inner join marks on students.id=marks.id;
update marks inner join students on marks.id=students.id set m1=100,m2=100,m3=100 where students.rollno="A100";
set sql_safe_updates=0;
set sql_safe_updates=1;
create table product(
pid int not null auto_increment,
pname varchar(30) not null,
rate int not null,
primary key(pid)
);
insert into product (pname,rate)values("pen",25),("box",10),("pendrive",500),("mouse",250),("keyboard",10);
select * from product;
select * from price_logs;
create table price_logs(
id int not null auto_increment,
pid int not null,
price int not null,
new_price int not null,
primary key(id)
);
/*
Create trigger trigger_name trigger_time trigger_event
on table_name for each row begin ------- end;
before,after
insert,update and delete
*/
select * from students;
delimiter $$

create trigger before_update before update on product for each row
begin
insert into price_logs (pid,price,new_price)values(old.pid,old.rate,new.rate);
end$$
delimiter ;
select * from product;
update product set rate=100 where pid=5;
drop trigger before_products;
show triggers;
select * from price_logs;


