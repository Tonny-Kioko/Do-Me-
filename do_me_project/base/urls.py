from django.urls import path
from .views import taskDelete, taskList, taskUpdate, userLoginView
from .views import taskDetail
from .views import taskCreate
from django.contrib.auth.views import LogoutView

urlpatterns = [
    #Home
    path('', taskList.as_view(), name='tasks'), 

    #Login URL 
    path('login/', userLoginView.as_view(), name='login'),
    #Logout URL
    path('logout/', LogoutView.as_view(next_page = 'login'), name='logout'),

    #CRUD Functionality
    path('task/<int:pk>/', taskDetail.as_view(), name='task'),
    path('create-task/', taskCreate.as_view(), name='task-create'),
    path('update-task/<int:pk>/', taskUpdate.as_view(), name='task-update'),
    path('delete-task/<int:pk>/', taskDelete.as_view(), name='task-delete'),


]