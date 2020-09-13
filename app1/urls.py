
from django.contrib import admin
from django.urls import path

from app1 import views

urlpatterns = [
    path("user/",views.user),
    path("user2/",views.UserView.as_view()),
    path("emp/<str:id>/",views.EmployeeView.as_view()),
    path("emp/",views.EmployeeView.as_view()),
    path("api_user/",views.UserAPIView.as_view())

]
