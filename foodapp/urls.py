from . import views
from django.urls import path
from users import views as user_reg
from django.contrib.auth import views as login

app_name = 'foodapp'

urlpatterns = [
    #food
    path('admins/',views.firstview,name='firstview'),
    #food/1
    path('<int:id>/',views.details,name='details'),
    
    path('items/',views.items,name='items'),
    
    #add food item
    path('add-item/',views.ctreateItem,name="ctreateItem"),
    path('',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('viewcontact/',views.contactview,name='contactview'),
    path('succssmes/',views.contactsu,name="contactsu"),
    path('update-item/<int:id>/',views.update_item,name='update_item'),
    path('delete-item/<int:id>/',views.delete_item,name='delete_item'),
    path('register/',user_reg.register,name='register'),
    path('userview/',views.userview,name='userview'),
    path('login/',login.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',login.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('adminLogIn/', views.AdminLogIn, name="Admin_LogIn"),
    path('userdesc/<int:id>/',views.userdesc,name="userdesc")
]