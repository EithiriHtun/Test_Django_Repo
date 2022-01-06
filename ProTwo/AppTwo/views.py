from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def index(request):
#     return HttpResponse("My Second App")

def index(request):
 my_redir = {'redirect_page' : "Hello!.Testing from view for template challenge!"}
 return render(request,"index.html",context=my_redir)
