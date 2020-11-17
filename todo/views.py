from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import A
from mysql import connector
# Create your views here.
def fun(request):
    return render(request,'ind.html',{"obj":A.objects.all()})
def sql_safe_update(cur):
    cur.execute("set sql_safe_updates=0")
def add(request):
    obj=A(details=request.POST["task"])
    obj.save()
    db=connector.connect(user="root",password="akshay",host="localhost",database="todo",auth_plugin="mysql_native_password")
    cur=db.cursor()
    cur.execute("SELECT id from todo_a where details="+repr(request.POST["task"]))
    l=cur.fetchall()[0][0]
    db.commit()
    db.close()
    return HttpResponse(str(l))
def dell(request):
    db=connector.connect(user="root",password="akshay",host="localhost",database="todo",auth_plugin="mysql_native_password")
    cur=db.cursor()
    cur.execute("set sql_safe_updates=0")
    cur.execute("delete from todo_a where id="+repr(request.POST["task"]))
    db.commit()
    db.close()
    return HttpResponse("delete from todo_a where id="+repr(request.POST["task"]))
def edit(request):
    db=connector.connect(user="root",password="akshay",host="localhost",database="todo",auth_plugin="mysql_native_password")
    cur=db.cursor()
    cur.execute("set sql_safe_updates=0")
    cur.execute("update todo_a set details="+repr(request.POST["ed"])+" where id="+request.POST["task"])
    db.commit()
    db.close()
    return HttpResponse(request.POST["ed"])