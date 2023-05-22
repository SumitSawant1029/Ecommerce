from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.log,name="log"),
    path('/home',views.login,name="login"),
    path('/register',views.register,name="register")
]
