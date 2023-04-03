from unicodedata import name
from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import views as auth_views 


from.views import TaskList,TaskDetail,Taskcreate,DeleteTask,EditTask,CustomLoginView,Registerpage,Passwordchange,PasswordDone


urlpatterns = [
    path('',TaskList.as_view(),name='index'),
    path('detail/<int:pk>/',TaskDetail.as_view(),name='detail'),
    path('taskcreate/',Taskcreate.as_view(),name='create'),
    path('delete/<int:pk>/',DeleteTask.as_view(),name='delete'),
    path('edittask/<int:pk>/',EditTask.as_view(),name='edittask'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
    path('loginview/',CustomLoginView.as_view(),name='login'),
    path('registerpage/',Registerpage.as_view(),name='usersignup'),
    
    path('passwordchange/',Passwordchange.as_view(),name='passwordchange'),
    path('passwordchangedone/',PasswordDone.as_view(),name='passworddone'),
    
    
    # path('reset_password/',auth_views.PasswordResetView.as_view(),name='reset_password'),
    # path('reset_password_send/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    # path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    # path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='newtodo/reset_password.html'),name='reset_password'),
    path('reset_password_send/',auth_views.PasswordResetDoneView.as_view(template_name='newtodo/password_reset_send.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='newtodo/password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='newtodo/password_reset_complete.html'),name='password_reset_complete'),
]