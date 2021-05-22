from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

app_name="main"
urlpatterns = [
    path('',views.index,name="home"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('form/<str:name>/',views.form,name="form"),
    
]
    # path("login/",LoginView.as_view(),name="login")