from django.urls import path
from . import views
urlpatterns = [

    path('<int:pk>/',views.home,name='home'),
    path('register/',views.register_page,name='register'),
    path('',views.login_user,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('update/<int:pk>/<int:task_id>/',views.update_task,name='update'),
    path('delete/<int:pk>/<int:task_id>/',views.delete_task,name='delete_task'),
    path('delete_all/<int:pk>/',views.delete_all_tasks,name='delete_all_tasks'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('<int:pk>/delete_account/',views.delete_account,name='delete_account')


]
