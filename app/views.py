from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse
from app.models import Department,UserInfo


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
    return HttpResponse("https://www.baidu.com")

def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    username = request.POST.get("username")
    password = request.POST.get("password")
    if username == "root" and password == "123":
        return HttpResponse("http://www.chinaunicom.com.cn/")

    return render(request, "login.html", {"error": "用户名或密码错误"})
def orm(request):
    """
    Department.objects.create(title="销售部")
    Department.objects.create(title="IT部")
    Department.objects.create(title="运营部")
    UserInfo.objects.create(name="武沛齐",password="123",age=19)
    UserInfo.objects.create(name="张三",password="666",age=29)
    UserInfo.objects.create(name="李四",password="666")
    """
    #UserInfo.objects.filter(id=3).delete()
    #Department.objects.all().delete()

    data_list=UserInfo.objects.all()
    print(data_list)
    for obj in data_list:
        print(obj.id,obj.name,obj.password,obj.age)

    data_list = UserInfo.objects.filter(id=1)
    print(data_list)

    row_obj = UserInfo.objects.filter(id=1).first()
    print(row_obj.id,row_obj.name,row_obj.password,row_obj.age)
    return HttpResponse("成功")