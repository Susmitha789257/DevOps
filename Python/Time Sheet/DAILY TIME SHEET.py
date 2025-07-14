from tabulate import tabulate
import mysql.connector
from datetime import date,datetime,timedelta
import sys
import pandas as pd

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Susmitha@789",
    database="Daily_Time_Sheet_2025"
)
cursor=conn.cursor()
class Daily_Time_Sheet:
    def __init__(self):
        print("WELCOME TO DAILY TIME SHEET PORTAL\n")
        old=[("EXIT PORTAL"),("OLD"),("NEW"),("SYNCED")]
        self.old=list(enumerate(old))
        action=[("BACK"),("TODAY INSERT"),("PAST INSERT"),("WEEKLY VIEW"),("MONTHLY VIEW"),("FINAL VIEW")]
        self.action=list(enumerate(action))
        level=[("BACK"),("BASIC"),("INTERMEDIATE"),("ADVANCED"),("EXPERT"),("ADDITIONAL")]
        self.level=list(enumerate(level))
        entry=[("BACK"),("LEVEL WISE"),("ALL IN ONE"),("VIEW RECORD")]
        self.entry=list(enumerate(entry))       
    def Table(self,values,column):
        print(tabulate(values,headers=["S.NO",column],tablefmt="fancy_grid"))
    def End(self):
        print("Oops! Invalid option. Please enter a valid option and try again!")    
    def Choice(self):
        try: choice=int(input("\nPlease enter your option : "))
        except ValueError: self.End(); return self.Choice()
        else: return choice
app=Daily_Time_Sheet()
def EntryMenu():
    global control
    if "control" not in globals(): app.Table(app.entry,"ENTRY")
    else: del control
    choice=app.Choice()
    if choice==0: MainMenu()
    elif choice==1: LevelMenu()
    elif choice==2: AllTaskMenu()
    elif choice==3: TodayView()
    else: app.End(); control=1; EntryMenu()
def Check(column):
    sql=f"select {column} from DailyTimeSheet{main} where DAILY_DATE=%s"
    cursor.execute(sql,[x])
    output=cursor.fetchone()
    if output:
        output=[list(output)]
        column=column.split(",")
        print(tabulate(output,headers=column,tablefmt="fancy_grid"))
    return output
def Record(task,output,hours=0,column=None):
    while True:
        try:
            percent=int(input(f"Please enter your {task} completion percentage: "))
            if percent<0 or percent>300: raise ValueError
        except ValueError: print("❌ Invalid input. Numeric between (0-300). ❌"); continue
        else: break
    execute=[percent,x]
    if hours!=0: execute[:0]=[task,hours]
    else: column=task
    if output:
        if hours!=0:
            if output[0][0]!="----------": execute[0]=output[0][0]+","+task
            current=(float(output[0][1])*(output[0][2]/100))+hours*(percent/100)
            execute[1]=float(output[0][1])+hours
            execute[-2]=(current/execute[1])*100
        else:
            execute[0]=output[0][0]+percent
        column=",".join([i+"=%s" for i in column.split(",")])
        sql=f"update DailyTimeSheet{main} set {column} where DAILY_DATE=%s"
    else:
        column=column+",DAILY_DATE"
        sql=f"INSERT INTO DailyTimeSheet{main}({column})VALUES({','.join(['%s'] * len(column.split(',')))})"
    cursor.execute(sql,execute)
    conn.commit()
    print(f"{task} percentage {percent}% saved successfully!")
def Block(task):
    block=list(enumerate([("BACK"),("BLOCK_1"),("BLOCK_2"),("BLOCK_3")]))
    if main=="1": block.append((4,'BLOCK_4'))
    app.Table(block,task)
    python=app.Choice()
    if python==0: return "0"
    if 1 <= python < len(block): return block[python][1]
    else: app.End(); Block(task)

def AllTaskMenu():
    global control
    sql=f"select TASK from DailyTimeTable{main} where LEVEL BETWEEN 1 AND 4"
    cursor.execute(sql)
    task=cursor.fetchall()
    task.insert(0,["BACK"])
    task.append(["ADDITIONAL"])
    task=[[i,task[i][0]] for i in range(len(task))]
    if "control" not in globals(): print(tabulate(task,headers=["S.NO","TASK"],tablefmt="fancy_grid"))
    else: del control
    temp=app.Choice()
    if temp==0: EntryMenu()
    elif 1<=temp<len(task):
        if (temp==6 and main=="") or (temp==4 and main=="1"):
            task[temp][1]=Block(task[temp][1])
            if task[temp][1]=="0": AllTaskMenu()
        elif (temp==9 and main=="") or (temp==8 and main=="1"):
            column="TASK,HOURS,OFFICE_OTHER"
            output=Check(column)
            task=input("Please enter your task details : ")
            if task=="": AllTaskMenu()
            task=task.title()
            while True:
                try:
                    hours=float(input("Please enter the number of hours you worked : "))
                    if hours<0 or hours>10: raise ValueError
                except ValueError: print("❌ Invalid input. Numeric between (0-10). ❌"); continue
                else: break
            Record(task,output,hours,column)
        if (temp!=9 and main=="") or (temp!=8 and main=="1"): output=Check(task[temp][1]); Record(task[temp][1],output)
        AllTaskMenu()
    else: app.End(); control=1; AllTaskMenu()
        
def TaskMenu(choice):
    sql=f"select TASK from DailyTimeTable{main} where LEVEL=%s"
    cursor.execute(sql,[choice])
    task=cursor.fetchall()
    task.insert(0,["BACK"])
    task=[[i,task[i][0]] for i in range(len(task))]
    print(tabulate(task,headers=["S.NO","TASK"],tablefmt="fancy_grid"))
    temp=app.Choice()
    if temp==0:
        LevelMenu()
    elif 1<=temp<len(task):
        if choice==4 and temp==2:
            task[temp][1]=Block(task[temp][1])
            if task[temp][1]=="0": TaskMenu(choice)
        output=Check(task[temp][1])
        Record(task[temp][1],output)
        TaskMenu(choice)
    else: app.End(); TaskMenu(choice)

def Additional():
    column="TASK,HOURS,OFFICE_OTHER"
    output=Check(column)
    task=input("Please enter your task details : ")
    if task=="": LevelMenu()
    task=task.title()
    while True:
        try:
            hours=float(input("Please enter the number of hours you worked : "))
            if hours<0 or hours>10: raise ValueError
        except ValueError: print("❌ Invalid input. Numeric between (0-10). ❌"); continue
        else: break
    Record(task,output,hours,column)
    LevelMenu()

def TodayView():
    cursor.execute(f"SHOW COLUMNS FROM DailyTimeSheet{main}")
    column=[i[0] for i in cursor.fetchall()]
    cursor.execute(f"select * from DailyTimeSheet{main} where DAILY_DATE=%s",[x])
    value=cursor.fetchone()
    if value: print(tabulate(list(zip(column,value)),tablefmt="fancy_grid"))
    else: print("Record Not Found.")
    read=input("Press Enter key to go back :")
    EntryMenu()
    
def MainView(choice,check):
    global main
    start=datetime.strptime("2025-05-12" if main=="" else "2025-07-07","%Y-%m-%d").date()
    last=datetime.strptime("2025-07-06","%Y-%m-%d").date() if main=="" else date.today()
    try: display=int(input("Do you want to display the records? Enter 1 : ")) if check==0 and choice!=5 else 1; display=(display==1)
    except ValueError: display=False
    if display:
        if choice in [3,4]:
            days,name=(7,"WEEK") if choice==3 else (28,"MONTH")
            total=((last-start).days+days)//days
            while True:
                try:
                    num = int(input(f"Enter a {name} number (0-{total}) : "))
                    if num<0 or num>total: raise ValueError
                except ValueError: print("❌ Invalid input. ❌"); continue
                else: break
            if num==0: MainMenu()
            first=1
        else:
            first,num,name="","","FINAL"
    else:
        first,num,value=1,1,[]
        days,name=(7,"WEEK") if choice==3 else (28,"MONTH")
    while start<=last:
        end=min(start+timedelta(days=(days-1)),last) if choice!=5 else last
        if first==num:
            if display:
                qry=f"select * from DailyTimeSheet{main} where DAILY_DATE between %s and %s"
                cursor.execute(qry,[start,end])
                value = [list(i) for i in cursor.fetchall()]
                for i in value:
                    if len(i[13])>35:
                        i[13]=i[13][:30]+"..."
            table_name=f"DailyTimeSheet{main}"
            cursor.execute(f"SHOW COLUMNS FROM {table_name}")
            column=[i[0] for i in cursor.fetchall()]
            average=",".join([f"ROUND(AVG({column[i]}),0)" for i in range(2,17) if i not in (13,14)])
            sql=f"select {average} from DailyTimeSheet{main} where DAILY_DATE between %s and %s"
            cursor.execute(sql,[start,end])
            final=[f"{name} {first}","---"]+[i for i in cursor.fetchone()]
            final[13:13]=["----------","---"]
            if (display and choice==4) or choice==5: [value.insert(i,[""]) for i in range(len(value),0,-1) if i%7==0]
            value=value+[""]+[final] if display else value+[final]
        if choice==5: break
        start=start+timedelta(days=days)
        first=first+1
        num+=not display
    headers=["DATE","DAY","MED","GYM","COM","API","MYSQL","B1","B2","B3","PYTHON","TODO","BOOK","TASK","HOURS","OFFICE","OVERALL"]
    if main=="1": headers=["DATE","DAY","MED","GYM","PYTHON/MYSQL","B1","B2","B3","B4","DEVOPS","MOTI","BOOK","REVEW","TASK","HOURS","OFFICE","OVERALL"]
    print(tabulate(value,headers=headers,tablefmt="pretty"))
    if choice==5 or not display:
        pro=True
        if not display:
            try: pro=int(input("Do you want to view the Progress? Enter 1 : ")); pro=(pro==1)
            except ValueError: pro=False
            if pro:
                main=[]
                for i in range(1,len(value)):
                    change=[]
                    for j in range(len(value[i])):
                        if j==0:
                            a="W" if choice==3 else "M"
                            result=f"W{i}-W{i+1}"
                        elif j==13: result="----------"
                        elif j in [1,14]: result="---"
                        else:
                            w1=value[i-1][j]
                            w2=value[i][j]
                            down=w1 if w1!=0 else 1
                            result=f"{round(((w2-w1)/down)*100)}%"
                        change.append(result)
                    main.append(change)
                print(tabulate(main,headers=headers,tablefmt="pretty"))
        if pro: read=input("Press Enter key to go back :")
        MainMenu()
    else:
        MainView(choice,1)
        
def LevelMenu():
    global control
    if "control" not in globals():
        if main=="1": level=list(enumerate([val for i,val in app.level if val not in ('INTERMEDIATE')]))
        else: level=app.level
        app.Table(level,"LEVEL")
    else: del control
    choice=app.Choice()
    if main=="1" and choice>=2: choice=choice+1
    if choice==0: EntryMenu()
    elif choice in range(1,5): TaskMenu(choice)
    elif choice==5: Additional()
    else: app.End(); control=1; LevelMenu()

##def Synced():
##    file_path = r"E:\SUSMITHA 2025\DevOps\Daily Time Sheet\Daily Time Sheet.xlsx"
##    df = pd.read_excel(file_path, sheet_name="8 Months", skiprows=3, header=None)
##    columns_to_use = [0, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 15]
##    cursor = conn.cursor()
##    cursor.execute("SHOW COLUMNS FROM DailyTimeSheet1")
##    db_columns = [i[0] for idx, i in enumerate(cursor.fetchall()) if idx not in [1,9,13,14,16]]
##    cursor.close()
##    cursor = conn.cursor(dictionary=True)
##    day=0
##    for i, row in df.iterrows():
##        row_number = i + 4
##        if (i + 1) % 8 == 0: continue
##        day=day+1
##        try:
##            selected = [row[col] for col in columns_to_use]
##            selected = [0 if pd.isna(val) else val for val in selected]
##            parsed_date = pd.to_datetime(str(selected[0]) + "-2025").date()
##            selected[0] = parsed_date
##            cursor.execute("SELECT * FROM DailyTimeSheet1 WHERE DAILY_DATE = %s", (parsed_date,))
##            existing = cursor.fetchone()
##            if not existing:
##                task = str(row[13]) if pd.notna(row[13]) else '----------'
##                hours = float(row[14]) if pd.notna(row[14]) else 0.0
##                cursor.execute(f"""INSERT INTO DailyTimeSheet1 ({", ".join(db_columns)},TASK, HOURS)
##                VALUES ({", ".join(['%s'] * len(db_columns))}, %s, %s)""", tuple(selected) + (task, hours))
##                print(f"🆕 Inserted ✅ DAY {day}: {parsed_date}")
##            else:
##                updates = {}
##                for j, col in enumerate(db_columns[1:]):  # Skip DAILY_DATE
##                    if int(existing[col]) != int(selected[j + 1]):
##                        updates[col] = int(selected[j + 1])
##                if updates:
##                    set_clause = ", ".join([f"{col} = %s" for col in updates])
##                    values = list(updates.values()) + [parsed_date]
##                    cursor.execute(f"UPDATE DailyTimeSheet1 SET {set_clause} WHERE DAILY_DATE = %s", values)
##                    print(f"🔁 Updated {len(updates)} field's ✅ DAY {day}: {parsed_date}")
##        except Exception as e:
##            print(f"❌ DAY {day} failed: {e}")
##    conn.commit()
##    print(f"✅ {day} days completed! 📅 You have only {224 - day} days left!")
##    read=input("Press Enter key to go back :")
##    MainMenu1()


def Synced():
    file_path = r"E:\SUSMITHA 2025\DevOps\Daily Time Sheet\Daily Time Sheet.xlsx"
    df = pd.read_excel(file_path, sheet_name="8 Months", skiprows=3, header=None)
    columns_to_use = [0, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 15]
    cursor = conn.cursor()
    cursor.execute("SHOW COLUMNS FROM DailyTimeSheet1")
    db_columns = [i[0] for idx, i in enumerate(cursor.fetchall()) if idx not in [1, 9, 13, 14, 16]]  # Exclude calculated columns
    cursor.close()
    cursor = conn.cursor(dictionary=True)
    day = 0
    for i, row in df.iterrows():
        row_number = i + 4
        if (i + 1) % 8 == 0:
            continue
        day += 1
        try:
            selected = [row[col] for col in columns_to_use]
            selected = [0 if pd.isna(val) else val for val in selected]
            parsed_date = pd.to_datetime(str(selected[0]) + "-2025").date()
            selected[0] = parsed_date
            task = str(row[13]) if pd.notna(row[13]) else '----------'
            hours = float(row[14]) if pd.notna(row[14]) else 0.0
            cursor.execute("SELECT * FROM DailyTimeSheet1 WHERE DAILY_DATE = %s", (parsed_date,))
            existing = cursor.fetchone()
            data_values = [row[col] for col in columns_to_use[1:]]
            if all(pd.isna(val) for val in data_values):
                if existing: cursor.execute("DELETE FROM DailyTimeSheet1 WHERE DAILY_DATE = %s", (parsed_date,)); print(f"🗑️ Deleted empty record: {parsed_date}")
                day=day-1
                continue
            if not existing:
                cursor.execute(f"""
                    INSERT INTO DailyTimeSheet1 ({", ".join(db_columns)}, TASK, HOURS)
                    VALUES ({", ".join(['%s'] * len(db_columns))}, %s, %s)
                """, tuple(selected) + (task, hours))
                print(f"🆕 Inserted ✅ DAY {day}: {parsed_date}")
            else:
                updates = {}
                for j, col in enumerate(db_columns[1:]):
                    if int(existing[col]) != int(selected[j + 1]):
                        updates[col] = int(selected[j + 1])
                if existing['TASK'] != task: updates['TASK'] = task
                if float(existing['HOURS']) != hours: updates['HOURS'] = hours
                if updates:
                    set_clause = ", ".join([f"{col} = %s" for col in updates])
                    values = list(updates.values()) + [parsed_date]
                    cursor.execute(f"UPDATE DailyTimeSheet1 SET {set_clause} WHERE DAILY_DATE = %s", values)
                    print(f"🔁 Updated {len(updates)} field(s) ✅ DAY {day}: {parsed_date}")
        except Exception as e:
            print(f"❌ Row {row_number} failed: {e}")
    conn.commit()
    cursor.close()
    print(f"✅ {day} days completed! 📅 You have only {224 - day} days left!")
    input("🔙 Press Enter key to go back: ")
    MainMenu1()


def MainMenu():
    global x,control
    if "control" not in globals():
        action=list(enumerate([val for i,val in app.action if val not in ('TODAY INSERT', 'PAST INSERT')]))if main=="" else app.action 
        app.Table(action,"ACTION")
    else: del control
    choice=app.Choice()
    if main=="" and choice>0 : choice=choice+2
    if choice==0: MainMenu1()
    elif choice in range(1,3):
        if choice==2:
            while True:
                if "y" not in locals():
                    try: y=(int(input("Do you want to update yesterday’s record? Enter 1 :"))==1)
                    except ValueError: y=False
                    if y: x=date.today()-timedelta(days=1); break
                try: x=datetime.strptime(input("Enter the past date in this format (MM/DD/YYYY): "),"%m/%d/%Y").date()
                except ValueError: print("❌ Invalid Date. ❌"); continue  
                days=date.today()-timedelta(days=10)
                if x<=date.today() and x>=days: break
                print("❌ Invalid date. Future dates and dates older than 10 days are not allowed.")
        else: x=date.today()
        EntryMenu()
    elif choice in range(3,6): MainView(choice,0)
    else: app.End(); control=1; MainMenu()
    
def MainMenu1():
    global control,main
    if "control" not in globals(): app.Table(app.old,"OLD/NEW")
    else: del control
    main=app.Choice()
    if main==0: print("🙏 THANK YOU FOR USING THE DAILY TIME SHEET - PLEASE COME AGAIN! 🙏"); sys.exit()
    elif main in (1,2):
        main="" if main==1 else "1"
        MainMenu()
    elif main==3:
        Synced()
    else: app.End(); control=1; MainMenu1()
MainMenu1()
cursor.close()
conn.close()
      

