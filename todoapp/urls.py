
from django.urls import path
from .import views

app_name='todoapp'
urlpatterns = [

    path('', views.add, name='add'),
    path('addtask', views.addtask, name='addtask'),
    path('detail', views.detail, name='detail'),
    path('delete/<int:taskid>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('cbvhometask', views.Tasklistview.as_view(), name='cbvhometask'),
    path('cbvdetail/<int:pk>/', views.Taskdetailview.as_view(), name='cbvdetail'),
    path('cbvupdate/<int:pk>/', views.Taskupdateview.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.Taskdeleteview.as_view(), name='cbvdelete'),
]
