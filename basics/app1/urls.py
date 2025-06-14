
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('create/',views.create_view,name='create_view'),
    path('list/',views.list_view,name='list'),
    path('detail/<int:id>/',views.detail_view,name='detail_view'),
    path('update/<int:id>/',views.update_view,name='update_view'),
    path('delete/<int:id>',views.delete_view,name='delete_view'),
    
]
