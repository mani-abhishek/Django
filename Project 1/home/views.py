from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.htm')
    #  HttpResponse("this is home page")

def temple(request):
    return render(request,'temple.htm')

def arts(request):
    return render(request,'arts.htm')

def books(request):
    return render(request,'books.htm')