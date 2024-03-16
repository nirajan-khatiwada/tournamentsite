from django.urls import path
from .views import *
urlpatterns = [
    path("register/",register,name="register"),
    path("login/",Logins,name="login"),
    path("logout/",Logouts,name="logot"),
    path("forgot/",Fpass,name="forgot"),
    path("activate/",activate,name="Activate")
]
