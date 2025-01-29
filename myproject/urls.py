from django.contrib import admin
from django.urls import path
from myapp import views as myapp
from myapp.views import *
from myapp import views as myapp



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', myapp.index, name='index'),
    path('user_create/',myapp.user_create,name='user_create'),
    path('login/',myapp.login,name='login'),
    path('token_verification/',myapp.token_verification,name='token_verification'),
    path('regd/',myapp.registration,name='regd'),
    path('master_regd/',myapp.master_registration,name='master_regd'),
    path('register_view/',myapp.register_view),
    path('admincreate/',myapp.admincreate),
    path('admin_delete/',myapp.admin_delete),
    path('admin_view/',myapp.admin_view),
    path('forgotpassword/',myapp.forgotpassword),
    path('myhtml/<token>',myapp.myhtml)
    
]
