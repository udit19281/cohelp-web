from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

app_name="main"
urlpatterns = [
    path('',views.index,name="index"),
    # path("login/",views.login_user,name="login"),
    # path("register/",views.register,name="register"),
    # path("logout/",views.logout_user,name="logout"),
    path("plasmaxchange/", views.plasmaxchange, name="plasmaxchange"),
]
    # path("login/",LoginView.as_view(),name="login")