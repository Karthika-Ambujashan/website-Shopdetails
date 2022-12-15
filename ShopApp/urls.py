from django.urls import path
from .import views
urlpatterns = [
    path('shopdetails/',views.shopdetails,name='shopdetails'),
    path('viewshopdetails/',views.viewshopdetails,name='viewshopdetails'),
    path('getData/',views.getData,name='getData'),
    path('delete/<int:sid>/',views.delete,name='delete'),
    path('edit/<int:sid>/',views.edit,name='edit'),
    path('update/<int:sid>/',views.update,name='update')
]

