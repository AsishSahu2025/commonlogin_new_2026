from django.contrib import admin
from django.urls import path
from myapp import views as myapp
from myapp.views import *
from myapp import views as myapp



urlpatterns = [
    path('admin/', admin.site.urls),
    path('user_create/',myapp.user_create,name='user_create'),
    path('login/',myapp.login,name='login'),
    path('token_verification/',myapp.token_verification,name='token_verification'),
    path('user_regd/',myapp.user_registration,name='user_regd'),
    path('manager_regd/',ManagerRegisterview.as_view(),name='manager_regd'),
    path('master_regd/',myapp.master_registration,name='master_regd'),
    path('register_view/',myapp.register_view),
    path('forgotpassword/',myapp.forgotpassword),
    path('myhtml/<token>',myapp.myhtml)
    #***********************************************************************8
    # path('', myapp.index, name='index'),
    # path('admincreate/',myapp.admincreate),
    # path('admin_delete/',myapp.admin_delete),
    # path('admin_view/',myapp.admin_view),
]
