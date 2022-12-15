from django.urls import path
from . import views
urlpatterns = [
    path('registration/',views.registration,name='registration'),
    path('getDetails/',views.getDetails,name='getDetails'),
    path('login/',views.login,name='login'),
    path('getValue/',views.getValue,name='getValue'),

]