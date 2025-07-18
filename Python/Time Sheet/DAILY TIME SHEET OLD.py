from tabulate import tabulate
import mysql.connector
from datetime import date,datetime,timedelta
import sys

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
        action=[("EXIT PORTAL"),("TODAY INSERT"),("PAST INSERT"),("WEEKLY VIEW"),("MONTHLY VIEW"),("FINAL VIEW")]
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
    sql=f"select {column} from DailyTimeSheet where DAILY_DATE=%s"
    cursor.execute(sql,[x])
    output=cursor.fetchone()
    if output:
        output=[list(output)]
        column=column.split(",")
        print(tabulate(output,headers=column,tablefmt="fancy_grid"))
    return output
def Record(task,output,hours=0,column=None):
    percent=int(input(f"Please enter your {task} completion percentage: "))
    execute=[percent,x]
    if hours!=0: execute[:0]=[task,hours]
    else: column=task
    if output:
        column=",".join([i+"=%s" for i in column.split(",")])
        sql=f"update DailyTimeSheet set {column} where DAILY_DATE=%s"
    else:
        column=column+",DAILY_DATE"
        sql=f"INSERT INTO DailyTimeSheet({column})VALUES({','.join(['%s'] * len(column.split(',')))})"
    cursor.execute(sql,execute)
    conn.commit()
    print(f"{task} percentage {percent}% saved successfully!")
def Block(task):
    block=list(enumerate([("BACK"),("BLOCK_1"),("BLOCK_2"),("BLOCK_3")]))
    app.Table(block,task)
    python=app.Choice()
    if python==0: return "0"
    elif python in range(1,4): return block[python][1]
    else: app.End(); Block(task)

def AllTaskMenu():
    global control
    if "control" not in globals():
        sql="select TASK from DailyTimeTable where LEVEL BETWEEN 1 AND 4"
        cursor.execute(sql)
        task=cursor.fetchall()
        task.insert(0,["BACK"])
        task.append(["ADDITIONAL"])
        task=[[i,task[i][0]] for i in range(len(task))]
        print(tabulate(task,headers=["S.NO","TASK"],tablefmt="fancy_grid"))
    else: del control
    temp=app.Choice()
    if temp==0: EntryMenu()
    elif temp in range(1,10):
        if temp==6:
            task[temp][1]=Block(task[temp][1])
            if task[temp][1]=="0": AllTaskMenu()
        elif temp==9:
            column="TASK,HOURS,OFFICE_OTHER"
            output=Check(column)
            task=input("Please enter your task details : ")
            task=task.title()
            hours=float(input("Please enter the number of hours you worked : "))
            Record(task,output,hours,column)
        if temp!=9: output=Check(task[temp][1]); Record(task[temp][1],output)
        AllTaskMenu()
    else: app.End(); control=1; AllTaskMenu()
        
def TaskMenu(choice):
    sql="select TASK from DailyTimeTable where LEVEL=%s"
    cursor.execute(sql,[choice])
    task=cursor.fetchall()
    task.insert(0,["BACK"])
    task=[[i,task[i][0]] for i in range(len(task))]
    print(tabulate(task,headers=["S.NO","TASK"],tablefmt="fancy_grid"))
    temp=app.Choice()
    if temp==0:
        LevelMenu()
    elif temp in [1,2]:
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
    task=task.title()
    hours=float(input("Please enter the number of hours you worked : "))
    Record(task,output,hours,column)
    LevelMenu()
    
def TodayView():
    cursor.execute("SHOW COLUMNS FROM DailyTimeSheet")
    column=[i[0] for i in cursor.fetchall()]
    cursor.execute("select * from DailyTimeSheet where DAILY_DATE=%s",[x])
    value=cursor.fetchone()
    if value: print(tabulate(list(zip(column,value)),tablefmt="fancy_grid"))
    else: print("Record Not Found.")
    read=input("Press Enter key to go back :")
    EntryMenu()

def MainView(choice,check):
    start=datetime.strptime("2025-05-12","%Y-%m-%d").date()
    try: display=int(input("Do you want to display the records? Enter 1 : ")) if check==0 and choice!=5 else 1; display=(display==1)
    except ValueError: display=False
    if display:
        if choice in [3,4]:
            days,name=(7,"WEEK") if choice==3 else (28,"MONTH")
            total=((date.today()-start).days+days)//days
            num = int(input(f"Enter a {name} number (0-{total}) : "))
            if num==0: MainMenu()
            first=1
        else:
            first,num,name="","","FINAL"
    else:
        first,num,value=1,1,[]
        days,name=(7,"WEEK") if choice==3 else (28,"MONTH")
    while start<=date.today():
        end=min(start+timedelta(days=(days-1)),date.today()) if choice!=5 else date.today()
        if first==num:
            if display:
                qry="select * from DailyTimeSheet where DAILY_DATE between %s and %s"
                cursor.execute(qry,[start,end])
                value = [list(i) for i in cursor.fetchall()]
                for i in value:
                    if len(i[13])>35:
                        i[13]=i[13][:30]+"..."
            cursor.execute("SHOW COLUMNS FROM DailyTimeSheet")
            column=[i[0] for i in cursor.fetchall()]
            average=",".join([f"ROUND(AVG({column[i]}),0)" for i in range(2,17) if i not in (13,14)])
            sql=f"select {average} from DailyTimeSheet where DAILY_DATE between %s and %s"
            cursor.execute(sql,[start,end])
            final=[f"{name} {first}","---"]+[i for i in cursor.fetchone()]
            final[13:13]=["----------","---"]
            [value.insert(i,[""]) for i in range(len(value),0,-1) if i%7==0]
            value=value+[""]+[final] if display else value+[final]
        if choice==5: break
        start=start+timedelta(days=days)
        first=first+1
        num+=not display
    headers=["DATE","DAY","MED","GYM","COM","API","MYSQL","B1","B2","B3","PYTHON","TODO","BOOK","TASK","HOURS","OFFICE","OVERALL"]
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
    if "control" not in globals(): app.Table(app.level,"LEVEL")
    else: del control
    choice=app.Choice()
    if choice==0: EntryMenu()
    elif choice in range(1,5): TaskMenu(choice)
    elif choice==5: Additional()
    else: app.End(); control=1; LevelMenu()

def MainMenu():
    global x,control
    if "control" not in globals(): app.Table(app.action,"ACTION")
    else: del control
    choice=app.Choice()
    if choice==0: print("🙏 THANK YOU FOR USING THE DAILY TIME SHEET - PLEASE COME AGAIN! 🙏"); sys.exit()
    elif choice in range(1,3):
        if choice==2:
            while True:
                if "y" not in locals():
                    try: y=(int(input("Do you want to update yesterday’s record? Enter 1 :"))==1)
                    except ValueError: y=False
                    if y: x=date.today()-timedelta(days=1); break
                try: x=datetime.strptime(input("Enter the past date in this format (MM/DD/YYYY): "),"%m/%d/%Y").date()
                except ValueError: print("❌ Invalid date. ❌"); continue  
                days=date.today()-timedelta(days=10)
                if x<=date.today() and x>=days: break
                print("❌ Invalid date. Future dates and dates older than 10 days are not allowed.")
        else: x=date.today()
        EntryMenu()
    elif choice in range(3,6): MainView(choice,0)
    else: app.End(); control=1; MainMenu()
MainMenu()

cursor.close()
conn.close()
      

