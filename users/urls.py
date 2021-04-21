from django.urls import path,include
from .views import *
from . import views
from rest_framework.routers import DefaultRouter

from django.views.generic import TemplateView
router=DefaultRouter()

router.register('Employee',views.EmployeemodelViewSet)

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    #path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    path('api',include(router.urls)),



]
