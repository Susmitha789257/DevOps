##print("Tuter Joes")   # alt 3 for comment, alt4 for uncomment
##a=25
##b=25
##c=a+b
##print("Total :",c)
##print(type(a))
##print(id(a))  

##import keyword
##print(keyword.kwlist)

##name=input("Enter Name : ")
##print(type(name))
##print(name)

##a=float(input("Enter the value of a : ")) #str,int,float
##b=float(input("Enter the value of b : "))
##c=a+b
##print(c)
##print(type(c))

##name1,name2,name3=input("Enter 3 names :").split(",")
##print("Name1 : ",name1)
##print("Name1 : ",name2)
##print("Name1 : ",name3)

##a="""
##Lorem Ipsum is simply dummy text of the printing and typesetting industry.
##Lorem Ipsum has been the industry's standard dummy text ever since the 1500s.
##"""
##print(type(a))

##para=["25","26","50"]
##print("|".join(para))
##
##para=[]
##print("Enter a para: ")
##
##while True:
##    line=input()
##    if line:
##        para.append(line)
##    else:
##        break
##print(para)
##output="\n".join(para)
##print(output) 
##
##a=10.0 #type casting
##print(a)
##print(type(a))
##b=int(a)
##print(type(b))
##
##a=int(input("Enter the value of A : "))
##b=int(input("Enter the value of B : "))
##c=a+b
##print("Total :"+str(c))
##
##S="tutor Joes" #String and String Functions  
##print(type(S))
##print("upper:",S.upper())
##print("lower:",S.lower())
##print("capitalize:",S.capitalize())
##print("title:",S.title())
##print("count:",S.count("t"))
##print("endswith:",S.endswith("es"))
##print("startswith:",S.startswith("tu"))
##print("find:",S.find("o"))
##print("find with position:",S.find("o",5))
##print("replace:",S.replace("o","0"))
##a="joes1234" #Boolen Function - True or False
##print("is upper:",a.isupper())
##print("is lower:",a.islower())
##print("is alpha numeric:",a.isalnum())
##print("is alpha:",a.isalpha())
##print("is numeric:",a.isnumeric())
##s="he\nis\ngood" 
##print(s)
##print(s.splitlines())
##print(s.splitlines(True))
##a="tuter joes computer education"
##print(a.split(" "))
##a="tuter,joes,computer,education"
##print(a.split(","))
##s="    susmitha   "
##print(len(s))
##print(len(s.strip()))
##print(len(s.lstrip()))
##print(len(s.rstrip()))
##s="12-12-2020"
##print(s.partition("-"))

##s="sample" #String Manipulation - string sliceing
##print(s[0:2])
##print(s[:5])
##print(s[1:])
##print(s[-1])
##print(s[-2:-1])
##print(s[:-1])
##print(s[::-1]) #reverse

##a=123 #Arithmetic Operation
##b=10  # assignment
##print(a+b) #addition
##print(a-b) #subtraction
##print(a*b) #multiplication
##print(a/b) #division
##print(a//b) #floor division
##print(a%b) #modulus
####print(2**3) #exponentiation
##
##a=123 #arithmetic assignment
##a+=5
##a=a+5
##print(a)
##a=a-10
##a-=10
##print(a)
##a/=10
##print(a)

##a=20  #comparison operators or relational operators 
##b=20
##print(a==b)
##print(a!=b)
##print(a>b)
##print(a<b)
##print(a>=b)
##print(a<=b)

##a=10  #Logical(and,or,not)
##print(a>=10 and a<=20)
##print(a>=10 or a<=20)
##print(not(a>=10 and a<=20))

##a=25  #bitwise operators(& and,| or,^ xor,~ not,<< zero fill left shift,>> signed right shift)
##b=45
##print(a&b)
##print(a|b)
##print(a^b)
##print(~a)
##print(a<<2)
##print(a>>2)

##X=0 #if statement (even no or not)
##n=int(input("Enter the number: "))
##if n%2==0:
##    print(n, "is a even number")
##else:
##    print(n, "is a odd number")

##name=input("Enter name: ")
##age=int(input("Enter age: "))
##if age>=18:
##    print(name," age is ",age," eligible for vote")
##else:
##     print(name," age is ",age," not eligible for vote")

##days=int(input("Enter the days :"))
##if days==0:
##    print("good no fine")
##elif (days>=1 and days<=5):
##    print("fine amount:",days*0.5)
##elif (days>5 and days<=10):
##    print("fine amount:",days*1)
##elif (days>10 and days<=30):
##    print("fine amount:",days*5)
##else:
####    print("Membership Cancel")
##    
##mark1=int(input("mark1:"))
##mark2=int(input("mark2:"))
##mark3=int(input("mark3:"))
##total=mark1+mark2+mark3
##print("total:",total)
##avg=total/3
##print("average:",avg)
##if (mark1>=35 and mark2>=35 and mark3>=35):
##    print("result: PASS")
##    if (avg<=100 and avg>=90):
##        print("grade: A")
##    elif (avg<=89 and avg>=80):
##        print("grade: B")
##    elif (avg<=79 and avg>=70):
##       print("grade: C")
##    else:
##        print("grade: D")
##else:
##    print("result: FAIL")
##
##i=1
##while i<=10:
##    print(i)
##    i=i+1
##print("----------------")
##print("Even Numbers")
##n=2
##while n<=20:
##    print(n)
##    n=n+2

##i=1
##while i<=19:
##    print(i)
####    i=i+2
##
##i=1   #continue
##while i<=20:
##    if i%2==0:
##        i=i+1
##        continue
##    print(i)
##    i=i+1
##
##i=1
##while i<=20:
##    if i==7:
##        break
##    print(i)
##    i=i+1

##print(list(range(5)))
##print(list(range(2,5))) #n-1
##print(list(range(0,21,2)))

##a=1 #for loop
##
##for i in range(20):
##    print(i)
##for i in range(0,21,2):
##    print(i)

##for i in range(5):
##    a=int(input("Enter number 1:"))
##    b=int(input("Enter number 2:"))
##    print("total:",a+b)

##for i in range(6):
##    for j in range(i):
##        print("*",end="")
##    print("")

##for i in range(5,0,-1):
##    for j in range(i):
##        print("*",end="")
##    print("")

##for i in range(65,70,1):
##    for j in range(65,70,1):
##        print(chr(j),end="")
##    print("")
##
##for i in range(97,102,1):
##    for j in range(97,102,1):
##        print(chr(j),end="")
##    print("")

##i=1
##while i<=10:
##    if i==3:
##        i=i+1
##        continue
##    if i>7:
##        break
##    print(i)
##    i=i+1
####else:
####    print("loop completed")
####
####for i in range(1,10):
####    if i==3:
####        continue
####    if i>7:
####        break
####    print(i)
####else:
####    print("loop completed")
####
####a=[1,2,3,4,5]
####print(a)
####print(type(a))
####a[0]=100
####print(a[::-1])
##
####a=[1,True,"susmitha",2.5,range(3),[1,2,3]]
####print(type(a[4]))
####print(a[5][2])
##
##a=[10,-22,22,45,22,22,22,33,33,44] #list methods
###a.clear()
##print(a)
##b=a.copy()
##print(b)
##print(a.count(25))
##print(a.index(22,2))
##print(len(a))
##print(max(a))
##print(min(a))
##print(a)
##a.pop(0)
##print(a)
##a.remove(22)
##print(a)
##print("---------------------------------------------")
##names=["ram"]
##print(names)
##names.append("sam")
##names.append("ravi")
##names.append("kumar")
####print(names)
####name2=["a","b"]
####names.extend(name2)
####print(names)
####names[1]="k"
####names.insert(2,"5")
####print(names)
####print(list(range(5)))
####print(list("susmitha"))
####a=[50,20,30,60,10,90,1,0,33]
####a.sort()
####print(a)
######a.sort(reverse=True)
######a.sort()
########print(a)
######
######a=["orange","apple","zebra"]
######a=["o","appledsgbe","zebra","gfhf"]
######a.sort(key=len)
######print(a)
####
##a=(1,4,5) #Tuple in python
##print(type(a))
##print(a)
##print(a[0])
##print(a[::-1])
##b=list(a)
##print(b)
##b.append("raja")
##print(b)
##a=tuple(b)
##print(a)
##for i in a:
##    print(i)
##if 'raja' in a:
##    print("found")
##else:
##    print("not found")
##print(len(a))
##a=(1,)
##print(type(a))
##del a
##a=(1,2,7,4)
##b=(5,6,7,8)
##c=a+b
##print(c)
##print(c.count(7))
##c=(a,b)
##print(c)
##x=("joes",)*10
##print(x)
##print(max(a))
####print(min(b))
##
##a={'ram','sam','vijay'} #set in python
##a.add("sara")
##print(a)
##print(type(a))
##for i in a:
##    print(i)
##b={"a","b","c","d"}
##a.update(b)
##print(a)
##a.remove("sara")
##print(a)
##a.discard("aa")
##print(a)
##a.pop()
##a.clear()
##print(a)
##del a
# set removes duplicate values automatically
##a={1,2,3,4}
##b={'a','b','c','d'}
##c=a.union(b)
##print(c)
####a.update(b)
####print(a)
##
##a={1,2,3,9,5}
##b={5,6,7,8,9}
####c=a.intersection(b)
####print(c)
####a.intersection_update(b)
####a.inetrsection_update(b)
####print(a)
##c=a.symmetric_difference(b)
##print(c)
##a.symmetric_difference_update(b)
####print(a) 
##user={"name":"susmitha","age":23,"isMarried":False}
##print(user["name"])
##print(type(user))
##print(user.keys())
##print(user.values())
##print(user.items())
##
##for i in user:
##    print(i," ",user[i])
##for i,y in user.items():
##    print(i,y)
##user.update({"gender":"male"})
##print(user)
##user.pop("age")
##print(user)

##def welcome():  #functions
##    print("welcome to tuterjoes")
##welcome()
##type1=1 # No return type without argument function in python
##def add():
##    a=int(input("Enter value of a:"))
##    b=int(input("Enter value of b:"))
##    c=a+b
##    print(c)
##add()
##type2=2 # No return type with argument function in python
##def sub(a,b):
##    c=a-b
##    print(c)
##a=int(input("Enter value of a:"))
##b=int(input("Enter value of b:"))
##sub(a,b)
##
##type3=3 # return type without argument function in python
##def mul():
##    a=int(input("Enter value of a:"))
##    b=int(input("Enter value of b:"))
##    c=a*b
##    return c
##x=mul()
##print(x)
##
##type4=4 # return type with argument function in python
##def div(a,b):
##    c=a/b
##    return c
##a=int(input("Enter value of a:"))
##b=int(input("Enter value of b:"))
##x=div(a,b)
##print(x)

##type5=5 # Arbitrary arguments function in python(*)
##def class_10(*students):
##    print(students)
##    for i in students:
##        print(i)
##class_10("susmitha","ok","hi")

##type6=6 # Keyword arguments function in python
##def message(name,age):
##    print(name,"age is",age)
##message(age=25,name="susmitha")

##type7=7 # Arbitrary Keyword arguments function in python(**)
##def biodata(**data):
##    print(data)
##biodata(age=25,name="susmitha",gender="female")

##type8=8 #default parameter function in python
##def user(name,city="salem"):
##    print(name,"is from ",city)
##user("Ram","Namakkal")
##user("Ram")
##
##type9=9 #passing a list as an argumet in function.
##def total(marks):
##    return sum(marks)
##print(total([2,4,5]))
##
##a=10 #recursive function
##b=10 #pass to bypass the function
##def factor(x):
##    if x==1:
##        return 1
##    else:
##        return x*(factor(x-1))
##print(factor(5))
##a=10 #lambda function
##a=lambda a:a
##print(a(1))
##
##import datetime as dt
####print(dt.date.today())
####print(dt.date(2021,10,26))
####print(dt.date(2021,10,26).year)
####print(dt.date(2021,10,26).month)
####print(dt.date(2021,10,26).day)
##print(dt.time(10,30,30,646))
##print(dt.time(10,30,30,646).hour)
##print(dt.time(10,30,30,646).minute)
##print(dt.time(10,30,30,646).second)
##print(dt.time(10,30,30,646).microsecond)
##print(dt.datetime.now())
##print(dt.datetime(2021,5,31,12,4,5,436753))
##print(dt.datetime(2021,5,31,12,4,5,436753).date())
##print(dt.datetime(2021,5,31,12,4,5,436753).time())
##current=dt.datetime.now()
##new=dt.datetime(2022,1,1)
##difference=current-new
##print(difference)
##print(dt.datetime.now()) 

##import math
##print(dir(math))

##try:
####    a=10/0
####except Exception as e:
####    print(e)
#print("--------------------------Class and Object--------------------------")
##class demo():
##    pass
##a=10
##print(type(demo))
##swift=demo()
##print(type(swift))
##print(isinstance(swift,demo))
##print(isinstance(a,int))
##a=9 # class attributes
##class Student():
##    name="ram kumar"
##    age=25
##print(getattr(Student,"name"))
##print(getattr(Student,"age"))
##print(getattr(Student,"gender","novalue"))
##print(Student.name)
##setattr(Student,"name","Tuter joes")
##setattr(Student,"gender","female")
##print(Student.gender)
##Student.city="Salem"
##print(Student.city)
##print(Student.__dict__)
##delattr(Student,"city")
##print(Student.__dict__)
####del Student.gender
####print(getattr(Student,"__dict__"))
##class user:
##    course='java'
##o=user()
##print(user.__dict__)
##print(user.course)
##print(o.__dict__)
##print(o.course)
##o.course="c++"
##print(o.__dict__)
##print(o.course)   #class method

##class student:
##    name="susmitha"
##    age=25
##
##    def printall():
##        print(student.name)
##        print(student.age)
##student.printall()
###print(student.__dict__)
##getattr(student,"printall")()
##getattr(student,"printall")()
##student.__dict__['printall']()
##
##class student:
##    name="susmitha" #instance method
##    age=25
##
##    def printall(self):
##        print(student.name)
##        print(student.age)
##o=student()
####o.printall()
####a=10 #constructer init method
##
####class user:
####    def __init__(self,name):
####        print("call when new instance created")
####        self.name=name
####
####    def printall(self):
####        print(self.name)
####p1=user("tuter joes")
####p1.printall()
####print(p1.__dict__)
####p2=user("susmitha")
####p2.printall()
####print(p2.__dict__)
####print(user.__dict__)
##class user:
##    def __init__(self,name,age):
##        self.name=name
##        self.age=age
##        # self.msg=self.name+" is " + str(self.age) + "years old"
##    @property
##    def msg(self):
##        return self.name+" is " + str(self.age) + "years old"
##
##p1=user("tuter joes",25)
##print(p1.name)
##print(p1.age)
##print(p1.msg)
##p1.age=45
##print(p1.msg)   # property decorators getter setter
##
##class student:
##    def __init__(self,total):
##        self.total=total
##    def average(self):
##        return self.total/5.0
##    @property
##    def total(self):
##        return self._total
##    @total.setter
##    def total(self,t):
##        if t<0 or t>500:
##            print("invalid total and can't Change")
##        else:
##            self._total=t
##o=student(450)
####print(o.total)
####print(o.average())
####o.total=550
####print(o.total)
####print(o.average())
##
##class student:     #property method
##    def __init__(self,total):
##        self.total=total
##    def average(self):
##        return self.total/5.0
##
##    def getter(self):
##        return self._total
##
##    def setter(self,t):
##        if t<0 or t>500:
##            print("invalid total and can't Change")
##        else:
##            self._total=t
##    total=property(getter,setter)
##o=student(450)
##print(o.total)
##print(o.average())
##o.total=350
####print(o.total)
####print(o.average()) 
##
##class student:
##    count=0
##    def __init__(self,name,age):
##        self.name=name
##        self.age=age
##        student.count+=1
##    def detail(self):
##        print(self.name," ",self.age)
##    @classmethod
##    def total(cls):
##        return cls.count
##o=student("susmitha",25)
##o.detail()
##a=student("raja",45)
##a.detail()
####print(student.total())
##class student:    #static method
##    def __init__(self,name,age):
##        self.name=name
##        self.age=age
##    def detail(self):
##        print(self.name," ",self.age)
##    @staticmethod 
##    def welcome():
##        print("Welcome to our institution")
##s1=student("susmitha",25)
####s1.detail()
####s1.welcome()
##a=10 # Data abstraction and encapsulation in python
##class Library:
##    def __init__(self,books):
##        self.books=books
##    def list_books(self):
##        print("Available books :")
##        for book in self.books:
##            print(book)
##            
##    def borrow(self,borrow):
##        if borrow in self.books:
##            print("Get your book now")
##            self.books.remove(borrow)
##        else:
##            print("Book not available")
##    def receive(self,receive):
##        print("you have returned the book")
##        self.books.append(receive)
##books=["c","python","java","c++","mysql"]
##obj=Library(books)
##msg="""
##1.Display Book
##2.Borrow Book
##3.return Book
##"""
##while True:
##    print(msg)
##    option=int(input("Enter a choice: "))
##    if option==1:
##        obj.list_books()
##    elif option==2:
##        borrow=input("Enter the borrow book: ")
##        obj.borrow(borrow)
##    elif option==3:
##        receive=input("Enter the receive book: ")
##        obj.receive(receive)
##    else:
##        print("Thank you come again")
##        quit()

##class Nokia(): # single inhetance
##    company="Nokia India"
##    website="www.nokia-india.com"
##    def contact(self):
##        print("Address : Cherry Road,Near Bus Stand,Salem")
##class Nokia2163(Nokia):
##    def __init__(self):
##        self.name="Nokia 2163"
##        self.year=1998
##    def product(self):
##        print(self.name)
##        print(self.year)
##        print(self.company)
##        print(self.website)
##mobile=Nokia2163()
##mobile.product()
##mobile.contact()

##class father:    #Multiple inheritance
##    def fishing(self):
##        print("Fishing in Rivers")
##    def chess(self):
##        print("playing chess from father")
##class mother:
##    def cooking(self):
##        print("cooking food")
##    def chess(self):
##        print("playing chess from mother")
##class son(father,mother):
##    def ride(self):
##        print("riding bicycle")
##o=son()
##o.ride()
##o.fishing()
##o.cooking()
####o.chess()
##
##a=10 #multilevel inheritance
##class grandfather:
##    def ownhouse(self):
##        print("Grandpa house")
##class father(grandfather):
##    def ownbike(self):
##        print("father's Bike")
##class son(father):
##    def ownbook(self):
##        print("son hav25e a book")
##o=son()
##o.ownhouse()
##o.ownbike()
##o.ownbook()

##a=10 #function overriding 6/13/2025-3:30 pm
##class employee:
##    def working(self):
##        self.hrs=50
##    def printhrs(self):
##        print("Total working hours : ",self.hrs)
##class trainee(employee):
##    def working(self):
##        self.hrs=60
##    def resethrs(self):
##        super().working()
##obj=employee()
##obj.working()
##obj.printhrs()
##obj=trainee()
##obj.working()
##obj.printhrs()
##obj.resethrs()
##obj.printhrs()
##a=10 #diamond problem 6/13/2025-4:07 pm
##class a:
##    def display(self):
##        print("class a")
##class b(a):
##    def display(self):
##        print("class b")
##class c(a):
##    def display(self):
##        print("class c")
##class d(b,c):
##    def display(self):
##        print("class d")
##
##o=d()
##o.display()

##a=10 #operator overloading 6/13/2025-4:17 pm
##b=20
##print(a+b)
##a="susmitha"
##b=" is a software developer"
##print(a+b)
##
##class calculation:
##    def __init__(self,a):
##        self.a=a
##    def __add__(o1,o2):
##        return o1.a+o2.a
##    def __sub__(o1,o2):
##        return o1.a-o2.a
##o1=calculation(10)
##o2=calculation(20)
##print(o1+o2)
##print(o1-o2)
##print(o1.a*o2.a)





































































