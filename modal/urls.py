from django.urls import path

from . import views

app_name = 'modal'

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.createModal, name='createModal'),
    path('edit/', views.editModal, name='editModal'),
    path('delete/', views.deleteModal, name='deleteModal'),
]
