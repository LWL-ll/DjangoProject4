from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse


def index(request):
    return HttpResponse("欢迎使用")

def user_list(request):
    return HttpResponse("用户列表")

def user_add(request):
    return HttpResponse("添加用户")

def something(request):
    print(request.method)
    print(request.GET)
    print(request.POST)
    return HttpResponse("httrs://www.baidu.com")

def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    username = request.POST.get("username")
    password = request.POST.get("password")
    if username == "root" and password == "123":
        return HttpResponse("http://www.chinaunicom.com.cn/")

    return render(request, "login.html", {"error": "用户名或密码错误"})