create database DailyTimeTable;
Drop database DailyTimeTable;
create database Daily_Time_Sheet_2025;
USE Daily_Time_Sheet_2025;
create table DailyTimeTable(
S_NO int not null auto_increment primary key,
START_TIME TIME not null unique,
END_TIME TIME not null unique,
TASK VARCHAR(50) NOT NULL,
HOURS_MINUTES TIME AS (SEC_TO_TIME(MOD(TIME_TO_SEC(END_TIME)+86400-TIME_TO_SEC(START_TIME),86400))) STORED,
LEVEL int default 0
);

create table DailyTimeTable1(
S_NO int not null auto_increment primary key,
START_TIME TIME not null unique,
END_TIME TIME not null unique,
TASK VARCHAR(50) NOT NULL,
HOURS_MINUTES TIME AS (SEC_TO_TIME(MOD(TIME_TO_SEC(END_TIME)+86400-TIME_TO_SEC(START_TIME),86400))) STORED,
LEVEL int default 0
);

describe DailyTimeTable;
drop table DailyTimeTable1;
INSERT INTO DailyTimeTable (START_TIME,END_TIME,TASK)VALUES("22:00:00","22:30:00","TO DO LIST & JOURNALING & Motivation Reading");
INSERT INTO DailyTimeTable (START_TIME,END_TIME,TASK)VALUES
("22:30:00","23:00:00","BOOK READING"),("23:00:00","7:00:00","HAPPY SLEEP");
SELECT * FROM DailyTimeTable1;
UPDATE dailytimetable set task="PYTHON_TERRAFORM" where S_NO=9;
INSERT INTO DailyTimeTable1 (START_TIME, END_TIME, TASK) VALUES
('07:00:00', '07:30:00', 'Get-Ready & Cooking'),
('07:30:00', '08:00:00', 'MEDITATION'),
('08:00:00', '10:00:00', 'GYM_WORKOUT'),
('10:00:00', '10:30:00', 'BATHING'),
('10:30:00', '11:00:00', 'TIFFEN & GET READY'),
('11:00:00', '11:30:00', 'Cooking Help'),
('11:30:00', '14:00:00', 'PYTHON_MYSQL'),
('14:00:00', '14:30:00', 'LUNCH'),
('14:30:00', '21:00:00', 'DEVOPS'),
('21:00:00', '22:00:00', 'WARM BATH & DINNER & WASH PLATES'),
('22:00:00', '22:30:00', 'MOTIVATION'),
('22:30:00', '23:00:00', 'BOOK_READING'),
('23:00:00', '23:30:00', 'REVIEW'),
('23:30:00', '07:00:00', 'HAPPY SLEEP');

update DailyTimeTable set level=1 where S_NO in(1,2,5,6,7,9,11,12);
update DailyTimeTable1 set level=3 where S_NO in(2,3);
select * from DailyTimeTable1;
delete from DailyTimeSheet where DAILY_DATE=CURDATE();
select date_format(START_TIME,"%l:%i %p") as Start,date_format(END_TIME,"%l:%i %p") as End,TASK,(
case
when hour(HOURS_MINUTES)=0 then concat(minute(HOURS_MINUTES),"M")
when minute(HOURS_MINUTES)=0 then concat(hour(HOURS_MINUTES)," HOUR",if (hour(HOURS_MINUTES)>1,"S",""))
else concat(hour(HOURS_MINUTES)," HOUR",if (hour(HOURS_MINUTES)>1,"S",""),minute(HOURS_MINUTES),"M")
end) as HOURS_MINUTES from DailyTimeTable;
DROP TABLE DailyTimeSheet;
create table DailyTimeSheet(
DAILY_DATE date PRIMARY KEY default (CURRENT_DATE),
DAILY_DAY varchar(3) generated always as (LEFT(DAYNAME(DAILY_DATE),3)) stored,
MEDITATION INT default 0,
GYM_WORKOUT int default 0,
COMMUNICATION int default 0,
APTITUDE int default 0,
MYSQL_HTML_CSS int default 0,
BLOCK_1 INT default 0,
BLOCK_2 int default 0,
BLOCK_3 int default 0,
PYTHON_JAVASCRIPT int generated always as ((BLOCK_1+BLOCK_2+BLOCK_3)/3) stored,
TODO_JOURNAL_MOTIREAD int default 0,
BOOK_READING INT default 0,
TASK varchar(150) default '----------',
HOURS decimal(3,1) default 0,
OFFICE_OTHER int default 0,
Overall_Percentage DECIMAL(5,2) generated always as (round((0.5*MEDITATION+2*GYM_WORKOUT+1*COMMUNICATION+1*APTITUDE+2*MYSQL_HTML_CSS+6*PYTHON_JAVASCRIPT+0.5*TODO_JOURNAL_MOTIREAD+0.5*BOOK_READING+HOURS*OFFICE_OTHER)/(CASE WHEN DAILY_DAY IN ('Sat', 'Sun') THEN 10 ELSE 13 END),2)) stored
);
select * from DailyTimeSheet;
INSERT INTO DailyTimeSheet 
  (DAILY_DATE, MEDITATION, GYM_WORKOUT, COMMUNICATION, APTITUDE, MYSQL_AWS, BLOCK_1, BLOCK_2, BLOCK_3, TODO_JOURNAL_MOTIREAD, BOOK_READING)
VALUES
  ('2025-07-02', 100, 110, 50, 0, 50, 50, 100, 100, 0, 0),
  ('2025-07-03', 0, 0, 0, 0, 100, 100, 100, 100, 0, 0),
  ('2025-07-04', 0, 0, 0, 0, 100, 80, 70, 90, 0, 0),
  ('2025-07-05', 0, 100, 0, 0, 0, 0, 0, 0, 0, 0),
  ('2025-07-06', 100, 0, 0, 0, 100, 0, 0, 0, 0, 0);

describe dailytimesheet;
create table DailyTimeSheet1(
DAILY_DATE date PRIMARY KEY default (CURRENT_DATE),
DAILY_DAY varchar(3) generated always as (LEFT(DAYNAME(DAILY_DATE),3)) stored,
MEDITATION INT default 0,
GYM_WORKOUT int default 0,
PYTHON_MYSQL int default 0,
BLOCK_1 INT default 0,
BLOCK_2 int default 0,
BLOCK_3 int default 0,
BLOCK_4 int default 0,
DEVOPS int generated always as ((BLOCK_1+BLOCK_2+BLOCK_3+BLOCK_4)/4) stored,
MOTIVATION int default 0,
BOOK_READING INT default 0,
REVIEW INT default 0,
TASK varchar(150) default '----------',
HOURS decimal(3,1) default 0,
OFFICE_OTHER int default 0,
Overall_Percentage DECIMAL(5,2) generated always as (round((0.5*MEDITATION+2*GYM_WORKOUT+2*PYTHON_MYSQL+8*DEVOPS+0.5*MOTIVATION+0.5*BOOK_READING+0.5*REVIEW+HOURS*OFFICE_OTHER)/(CASE WHEN DAILY_DAY IN ('Sat', 'Sun') THEN 10 ELSE 13 END),2)) stored
);

DROP TABLE dailytimesheet,DAILYTIMETABLE;
SHOW TABLES;
select * from dailytimesheet1;
SHOW COLUMNS FROM DailyTimeSheet1;
INSERT INTO DailyTimeSheet (DAILY_DATE,MEDITATION,GYM_WORKOUT,COMMUNICATION,APTITUDE,MYSQL_HTML_CSS,BLOCK_1,BLOCK_2,BLOCK_3,
    TODO_JOURNAL_MOTIREAD,BOOK_READING,TASK,HOURS,OFFICE_OTHER
) VALUES ("2025-05-14",0, 100,150, 0,0,0,0,0, 0, 0,'ADC-BDIa0 & BDIc0',2,80),
("2025-05-15", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'ADC - KT', 4, 70),
("2025-05-17", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'kitchen clean', 3, 80),
("2025-05-18", 0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 'cloth wash', 1, 80);

INSERT INTO DailyTimeSheet (
    DAILY_DATE, MEDITATION, GYM_WORKOUT, COMMUNICATION, APTITUDE,
    MYSQL_HTML_CSS, BLOCK_1, BLOCK_2, BLOCK_3,
    TODO_JOURNAL_MOTIREAD, BOOK_READING,
    TASK, HOURS, OFFICE_OTHER
) VALUES
("2025-05-19", 0, 100, 225, 80, 15, 0, 0, 0, 0, 50, 'FTP & EMAIL', 5, 90),
("2025-05-20", 0, 80, 150, 0, 125, 0, 0, 0, 35, 90, 'ADC - KT', 4, 80),
("2025-05-21", 0, 110, 150, 40, 100, 30, 30, 30, 0, 100, 'FTP & EMAIL', 1, 80),
("2025-05-22", 0, 100, 100, 0, 50, 0, 0, 0, 0, 0, 'Overall % in time sheet & personal guidance', 6, 80),
("2025-05-23", 0, 100, 0, 0, 300, 0, 0, 0, 85, 100, 'ADC - KT', 1, 95),
("2025-05-24", 0, 100, 0, 0, 250, 0, 0, 0, 0, 10, 'Time Sheet Update', 0.5, 100),
("2025-05-25", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Review', 1, 100),
("2025-05-26", 0, 95, 200, 90, 15, 10, 10, 10, 0, 80, 'JOB-Clone 150HW & Temple & MOTIVATION', 4, 90),
("2025-05-27", 0, 60, 0, 0, 0, 0, 0, 0, 0, 15, 'Motivation & Inter bio', 6.5, 100),
("2025-05-28", 0, 60, 0, 0, 0, 0, 0, 0, 0, 0, 'Siva Conversation', 6, 80),
("2025-05-29", 110, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Sasi Conversation & Fixed Mindset', 5, 80),
("2025-05-30", 60, 100, 100, 0, 200, 0, 0, 0, 100, 0, 'Motivation', 1, 100),
("2025-05-31", 0, 65, 70, 0, 75, 0, 0, 0, 0, 80, 'Hardwork motivation', 0.5, 100),
("2025-06-01", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'NO-WORK', 1, 1),
("2025-06-02", 100, 100, 100, 0, 75, 60, 60, 60, 100, 100, 'temple & metting', 1, 100);
select * from DailyTimeSheet;
alter table Dailytimesheet change column PYTHON_JAVASCRIPT PYTHON_TERRAFORM  int generated always as ((BLOCK_1+BLOCK_2+BLOCK_3)/3) stored;
ALTER TABLE Dailytimesheet DROP COLUMN Overall_Percentage;
SHOW CREATE TABLE Dailytimesheet;
INSERT INTO DailyTimeSheet (
    DAILY_DATE, MEDITATION, GYM_WORKOUT, COMMUNICATION, APTITUDE,
    MYSQL_HTML_CSS, BLOCK_1, BLOCK_2, BLOCK_3,
    TODO_JOURNAL_MOTIREAD, BOOK_READING,
    TASK, HOURS, OFFICE_OTHER
) VALUES
("2025-06-03", 0, 100, 100, 0, 0, 0, 0, 0, 100, 100, "Time Sheet Update last", 7, 80),
("2025-06-04", 0, 100, 50, 0, 0, 0, 0, 0, 0, 0, "Chat-GPT, Nissan Credit", 3, 80),
("2025-06-05", 100, 100, 150, 80, 60, 50, 50, 50, 100, 100, "meeting", 0.5, 100),
("2025-06-06", 70, 100, 100, 100, 0, 0, 0, 0, 40, 0, "meeting & Time sheet python split  blocks", 5, 100),
("2025-06-07", 0, 100, 10, 0, 0, 0, 0, 0, 100, 0, "room cleaning with guilt and ChatGpt Motivation", 5, 100),
("2025-06-08", 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, "Week and Month Time Sheet", 9.5, 100),
("2025-06-09", 0, 80, 200, 0, 100, 0, 0, 0, 0, 0, "meeting , temple, Time Sheet Review", 5, 100),
("2025-06-10", 0, 90, 0, 0, 75, 80, 50, 0, 100, 100, "CVENT", 0.5, 100),
("2025-06-11", 100, 100, 0, 0, 50, 80, 80, 25, 100, 100, "meeting", 0.5, 100),
("2025-06-12", 100, 120, 100, 0, 160, 0, 0, 0, 100, 100, "meeting video,Dealer deck", 3.5, 100),
("2025-06-13", 100, 100, 100, 50, 50, 50, 65, 35, 100, 100, "METTING", 0.5, 50),
("2025-06-14", 100, 90, 150, 50, 50, 90, 90, 100, 50, 0, "------------", 0, 0),
("2025-06-15", 100, 0, 0, 0, 30, 50, 0, 0, 0, 0, "------------", 0, 0),
("2025-06-16", 0, 80, 270, 0, 0, 75, 95, 70, 50, 0, "Week Review,Rebuild useing ChatGPT, Time Sheet update,motivation", 2, 95),
("2025-06-17", 0, 80, 150, 0, 50, 20, 50, 90, 50, 0, "motivation & Thoughts into paper & CVENT", 2, 80),
("2025-06-18", 100, 110, 100, 0, 50, 0, 0, 30, 0, 0, "Git & CVENT & PRIME", 6, 75),
("2025-06-19", 60, 120, 50, 0, 50, 70, 90, 50, 0, 0, "CVENT", 0.5, 100),
("2025-06-20", 0, 60, 0, 0, 50, 70, 70, 70, 0, 0, "meeting & Telnet", 1.5, 100),
("2025-06-21", 0, 30, 0, 0, 0, 0, 0, 0, 0, 0, "------------", 0, 0),
("2025-06-22", 0, 50, 0, 0, 0, 0, 0, 0, 0, 0, "REVIEW", 2.5, 90);
update DailyTimeSheet set task="" where DAILY_DATE=current_date();
show columns from DailyTimeSheet;
drop table DailyTimeSheet;
TRUNCATE DailyTimeSheet;
SELECT * FROM DailyTimeTable;
SELECT * FROM DailyTimeSheet;
delete from dailytimesheet1 where daily_date=curdate();
/*CREATE TABLE PYTHON(
DAILY_DATE date PRIMARY KEY DEFAULT (CURRENT_DATE),
BLOCK_1 INT,
BLOCK_2 int,
BLOCK_3 int,
BLOCK_AVERAGE FLOAT as ((BLOCK_1+BLOCK_2+BLOCK_3)/3) stored,
CONSTRAINT PYTHON FOREIGN KEY(DAILY_DATE) REFERENCES DailyTimeSheet(DAILY_DATE) ON DELETE CASCADE ON UPDATE CASCADE
);*/
SELECT * FROM dailytimetable;
select * from DailyTimeSheet;
/*
create table OFFICE_OTHER(
DAILY_DATE date PRIMARY KEY DEFAULT (CURRENT_DATE),
TASK varchar(150),
HOURS time,
PERCENTAGE int,
constraint OFFICE_OTHER foreign key (DAILY_DATE) references DailyTimeSheet(DAILY_DATE) on delete cascade on update cascade
);*/
ALTER TABLE DailyTimeSheet
DROP COLUMN DAILY_DAY;

ALTER TABLE DailyTimeSheet
ADD COLUMN DAILY_DAY VARCHAR(3)
    GENERATED ALWAYS AS (LEFT(DAYNAME(DAILY_DATE), 3)) STORED;
INSERT INTO DailyTimeSheet (
   TASK,
    HOURS,
    OFFICE_OTHER
)
VALUES (
    'super',13,76
);
select curdate();
truncate DailyTimeSheet;
describe DailyTimeSheet;
select * from DailyTimeSheet;
drop table oppa;
select CURRENT_TIMESTAMP();
show tables;
use daily_time_sheet_2025;
CREATE TABLE time_sheet (
    A INT,
    B INT,
    C INT
);
truncate time_sheet;
select * from time_sheet;
drop table time_sheet;

create table time_sheet(
DAILY_DATE date PRIMARY KEY default (CURRENT_DATE),
DAILY_DAY varchar(3) generated always as (LEFT(DAYNAME(DAILY_DATE),3)) stored,
MEDITATION INT default 0,
GYM_WORKOUT int default 0,
PYTHON_MYSQL int default 0,
BLOCK_1 INT default 0,
BLOCK_2 int default 0,
BLOCK_3 int default 0,
BLOCK_4 int default 0,
DEVOPS int generated always as ((BLOCK_1+BLOCK_2+BLOCK_3+BLOCK_4)/4) stored,
MOTIVATION int default 0,
BOOK_READING INT default 0,
REVIEW INT default 0,
TASK varchar(150) default '----------',
HOURS decimal(3,1) default 0,
OFFICE_OTHER int default 0,
Overall_Percentage DECIMAL(5,2) generated always as (round((0.5*MEDITATION+2*GYM_WORKOUT+2*PYTHON_MYSQL+8*DEVOPS+0.5*MOTIVATION+0.5*BOOK_READING+0.5*REVIEW+HOURS*OFFICE_OTHER)/(CASE WHEN DAILY_DAY IN ('Sat', 'Sun') THEN 10 ELSE 13 END),2)) stored
);

