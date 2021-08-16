from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('<str:username>/',views.theam,name='theam'),
    path('raw/privecy-policy/',views.policy,name='policy')

]