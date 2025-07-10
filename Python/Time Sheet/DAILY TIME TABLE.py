from tabulate import tabulate
import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Susmitha@789",
    database="Daily_Time_Sheet_2025"
)
cursor=conn.cursor()
sql="""SELECT S_NO,
  DATE_FORMAT(START_TIME, "%l:%i %p"),
  DATE_FORMAT(END_TIME, "%l:%i %p"),
  TASK,
  (
    CASE
      WHEN HOUR(HOURS_MINUTES) = 0 THEN CONCAT(MINUTE(HOURS_MINUTES), "M")
      WHEN MINUTE(HOURS_MINUTES) = 0 THEN CONCAT(HOUR(HOURS_MINUTES), " HOUR", IF(HOUR(HOURS_MINUTES) > 1, "S", ""))
      ELSE CONCAT(HOUR(HOURS_MINUTES), " HOUR", IF(HOUR(HOURS_MINUTES) > 1, "S", ""), " ", MINUTE(HOURS_MINUTES), "M")
    END
  ),STATUS
FROM DailyTimeTable;
"""
cursor.execute(sql)
print(tabulate(cursor.fetchall(), headers=["S.NO", "START", "END", "TASK", "HOURS/MINUTES","STATUS"], tablefmt="fancy_grid"))

conn.close()
