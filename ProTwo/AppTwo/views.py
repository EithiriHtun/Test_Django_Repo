from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import Users
# Create your views here.

# def index(request):
#     return HttpResponse("My Second App")

def index(request):
 my_redir = {'redirect_page' : "Hello!.Testing from view for template challenge!"}
 return render(request,"index.html",context=my_redir)

def test_map(request):
    return HttpResponse("Testing for Mapping!.")

def add_user(request):
    user_list = Users.objects.order_by('first_name')
    user_dct = {'users':user_list}
    return render(request,"ProApp/index.html",context=user_dct)
