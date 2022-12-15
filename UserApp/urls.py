from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index,name='index'),
    path('view/<int:sid>/',views.view,name='view')
]    