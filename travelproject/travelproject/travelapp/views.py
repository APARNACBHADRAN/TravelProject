from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# def demo(request):
#     return render(request,"index.html")
# def about(request):
#     return render(request,"about.html")
# def contact(request):
#     return HttpResponse("Iam in contact page")
#
def first(request):
    return render(request,"input.html")
def addition(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    z=x+y
    # print(x)
    # print(y)
    return render(request,"result.html",{'res':z})