 
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('logout/',views.logout_user,name='logout'),
    path('add_task/',views.add_task,name='add_task'),
    path('done_task/<int:pk>',views.done_task,name='done'),
    path('undo_task/<int:pk>',views.undo_task,name='undo'),
    path('task_done/',views.task_done,name='task_done'),
    path('task_not_done/',views.task_not_done,name='task_not_done'),
    path('task_remove/<int:pk>',views.remove_task,name='remove'),
    path('task_edit/<int:pk>',views.edit_task,name='edit'),

]  
 