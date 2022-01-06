from django.urls import path
from AppTwo import views

urlpatterns = [
    path('',views.test_map,name='test_map'),
]
