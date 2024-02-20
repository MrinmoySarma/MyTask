from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('task/', views.task, name='task'),
    path('create_task/', views.create_task, name='create_task'),
    path('mark_complete/', views.view_task, name="mark_complete"),
    path('set_mark/', views.mark_complete, name='set_mark'),
    path('delete_update/', views.delete_update, name="delete_update"),
    path('delete/<int:id>', views.delete_task, name='delete_task'),
    path('update/<int:id>', views.update_task, name='update_task'),
    path('updated/<int:id>', views.save_updated_task, name='updated'),

]
