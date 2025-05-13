from django.shortcuts import render
 

import pymysql 

# Create your views here.
def home(request):
    return render(request,"home.html")
def Student(request):
    return render(request,"student.html")
def StudentRegister(request):
    return render(request,"studentregister.html")
  

def StudentLogAction(request):
    u=request.POST["username"]
    p=request.POST["password"]
    con=pymysql.connect(host="localhost",user="root",password="root",database="ordersapp")
    cur=con.cursor()
    i=cur.execute("select * from register where username='"+u+"'and password='"+p+"'")             
    if i>0:
        context={'data':'Login Successful....'}
        return render(request,"student.html",context)
    else:
        context={'data':'Login Failed....'}
        return render(request,"student.html",context)  


def StudentRegAction(request):
      n=request.POST["name"]
      g=request.POST["gender"]
      y=request.POST["year"]
      l=request.POST["lang"]
      u=request.POST["username"]
      p=request.POST["password"]
      con=pymysql.connect(host="localhost",user="root",password="root",database="ordersapp")
      cur=con.cursor()
      i=cur.execute("insert into register values('"+n+"','"+g+"','"+y+"','"+l+"','"+u+"','"+p+"')")
      con.commit()
      if i>0:
            context={'data':'Registration Successful....'}
            return render(request,"student.html",context)
      else:
            context={'data':'Registration Failed....'}
            return render(request,"studentregister.html",context)




def quiz(request):
    return render(request,"quiz.html")
