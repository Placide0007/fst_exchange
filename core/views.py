from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'core/home.html')

def profile(request):
    return render(request,'core/profile.html')

def math(request):
    return render(request,'core/academic_program/math_info/math.html')

def pc(request):
    return render(request,'core/academic_program/pc/pc.html')

