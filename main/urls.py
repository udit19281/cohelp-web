from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

app_name="main"
urlpatterns = [
    path('',views.index,name="home"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('form/<str:name>/',views.form,name="form"),
    path('blog/',views.blog,name="blog"),
    path('mission/',views.mission,name="mission"),
    path('workshops/',views.workshop,name="workshop"),
    path('contact/',views.contact,name="contact"),
    path('founders/',views.founders,name="founders"),
    path('volunteer/',views.volunteer,name="volunteer"),
     path('resource/',views.showresource,name="showresource"),
     path('resource/',views.backToSchool,name="backToSchool"),
    path('resource/<int:id>/',views.resourcetable,name="resourcetable"),
]
    # path("login/",LoginView.as_view(),name="login")