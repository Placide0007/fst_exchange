from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'core/home.html')

def profile(request):
    return render(request,'core/profile.html')

def about(request):
    return render(request,'core/about.html')




