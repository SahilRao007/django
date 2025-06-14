from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('create/',views.create.as_view(),name='create'),
    path('list/',views.listing.as_view(),name='list'),
    path('detail/<int:id>/',views.detailed.as_view(),name='detailed'),
    path('<pk>/delete',views.deleting.as_view()),


]
