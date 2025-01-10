from django.shortcuts import render
from .models import *
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.middleware import csrf
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import psycopg2
from django.middleware.csrf import get_token
import datetime
import re
from django.conf import settings
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework import status

from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def index(request):
    return render(request,"index.html")

@csrf_exempt
def user_create(request):
    if request.method == 'POST':
        jsondata = JSONParser().parse(request)
        username = jsondata.get('username')
        password = jsondata.get('password')
        category = jsondata.get('category')

        try:
            token = csrf.get_token(request)
            data = User(username=username,password=password,token = token,category=category)

            data.save()

            return JsonResponse({'message': 'Login successfully.',"token":token})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

# @csrf_exempt
# # @permission_classes([IsAuthenticated])

# def login(request):
#     if request.method == 'POST':
#         jsondata = JSONParser().parse(request)
#         phone = jsondata.get('username')
#         password = jsondata.get('password')

#         phone_pattern = re.compile(r'^\d{10}$')  # Regex for a 10-digit phone number
#         email_pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')  # Regex for a valid email

#         if phone_pattern.match(phone):
#             if User.objects.filter(Mobno=phone).exists():
#                 users = User.objects.get(Mobno=phone)
#                 if phone == str(users.Mobno) and str(users.user_category) == "3d" and password == users.password:
#                     return JsonResponse({'message':"Login Successful For 3D User",'username':users.Name,'mobno':users.Mobno,'token':users.token,'cat':users.user_category})
#                 elif phone == str(users.Mobno) and str(users.user_category) == "water" and password == users.password:
#                     return JsonResponse({'message':"Login Successful For waterbody User",'username':users.Name,'mobno':users.Mobno,'token':users.token,'cat':users.user_category})
#                 elif phone == str(users.Mobno) and str(users.user_category) == "aqua" and password == users.password:
#                     return JsonResponse({'message':"Login Successful For aqua User",'username':users.Name,'mobno':users.Mobno,'token':users.token,'cat':users.user_category})
#                 elif phone == str(users.Mobno) and str(users.user_category) == "analytics" and password == users.password:
#                     return JsonResponse({'message':"Login Successful For analytics User",'username':users.Name,'mobno':users.Mobno,'token':users.token,'cat':users.user_category})
#                 else:  
#                     return JsonResponse({'error':"Invalid credential for General user"}, status=status.HTTP_404_NOT_FOUND)
#             elif AdminUser.objects.filter(Mobno=phone).exists():
#                 admin = AdminUser.objects.get(Mobno=phone)
#                 if phone == str(admin.Mobno) and str(admin.user_category) == "3d" and password == admin.password:
#                     return JsonResponse({'message':"Login Successful For 3D Admin",'username':admin.Name,'mobno':admin.Mobno,'token':admin.token,'cat':admin.user_category})
#                 elif phone == str(admin.Mobno) and str(admin.user_category) == "water" and password == admin.password:
#                     return JsonResponse({'message':"Login Successful For waterbody Admin",'username':admin.Name,'mobno':admin.Mobno,'token':admin.token,'cat':admin.user_category})
#                 elif phone == str(admin.Mobno) and str(admin.user_category) == "aqua" and password == admin.password:
#                     return JsonResponse({'message':"Login Successful For aqua Admin",'username':admin.Name,'mobno':admin.Mobno,'token':admin.token,'cat':admin.user_category})
#                 elif phone == str(admin.Mobno) and str(admin.user_category) == "analytics" and password == admin.password:
#                     return JsonResponse({'message':"Login Successful For analytics Admin",'username':admin.Name,'mobno':admin.Mobno,'token':admin.token,'cat':admin.user_category})
#                 else:  
#                     return JsonResponse({'error':"Invalid credential for Admin user"}, status=status.HTTP_404_NOT_FOUND)
#             else:
#                 return JsonResponse({'error':"Invalid credential"}, status=status.HTTP_404_NOT_FOUND)
#         elif email_pattern.match(phone):
#             if User.objects.filter(Email=phone).exists():
#                 users = User.objects.get(Email=phone)
#                 if phone == users.Email and str(users.user_category) == "3d" and password == users.password:
#                     return JsonResponse({'message':"Login Successful For 3D User",'username':users.Name,'mobno':users.Mobno,'token':users.token,'cat':users.user_category})
#                 elif phone == users.Email and str(users.user_category) == "water" and password == users.password:
#                     return JsonResponse({'message':"Login Successful For waterbody User",'username':users.Name,'mobno':users.Mobno,'token':users.token,'cat':users.user_category})
#                 elif phone == users.Email and str(users.user_category) == "aqua" and password == users.password:
#                     return JsonResponse({'message':"Login Successful For aqua User",'username':users.Name,'mobno':users.Mobno,'token':users.token,'cat':users.user_category})
#                 elif phone == users.Email and str(users.user_category) == "analytics" and password == users.password:
#                     return JsonResponse({'message':"Login Successful For analytics User",'username':users.Name,'mobno':users.Mobno,'token':users.token,'cat':users.user_category})
#                 else:  
#                     return JsonResponse({'error':"Invalid credential for general user"}, status=status.HTTP_404_NOT_FOUND)
#             elif SuperAdmin.objects.filter(Username=phone).exists():
#                 admin = SuperAdmin.objects.get(Username=phone)
#                 if phone == admin.Username and password == admin.Password:
#                     return JsonResponse({'message':"Login Successful For SuperAdmin",'username':admin.Username,'password':admin.Password})
#                 else:  
#                     return JsonResponse({'error':"Invalid credential for se:
                    #     response_data = {
                    #         'message': 'You are not an owner.',
                    #         'Mob': user.Mob,
                    #         'name': user.Company_name,
                    #         'email': user.Email,
                    #         'csrf_token': csrf_token,
                    #         'user_category': user.user_category,
                    #         'category': "not_owner"
                    #     }
                    #     return SuperAdmin user"}, status=status.HTTP_404_NOT_FOUND)
#             elif AdminUser.objects.filter(Email=phone).exists():
#                 admin = AdminUser.objects.get(Email=phone)
#                 if phone == admin.Email and str(admin.user_category) == "3d" and password == admin.password:
#                     return JsonResponse({'message':"Login Successful For 3D Admin",'username':admin.Name,'mobno':admin.Mobno,'token':admin.token,'cat':admin.user_category})
#                 elif phone == admin.Email and str(admin.user_category) == "water" and password == admin.password:
#                     return JsonResponse({'message':"Login Successful For waterbody Admin",'username':admin.Name,'mobno':admin.Mobno,'token':admin.token,'cat':admin.user_category})
#                 elif phone == admin.Email and str(admin.user_category) == "aqua" and password == admin.password:
#                     return JsonResponse({'message':"Login Successful For aqua Admin",'username':admin.Name,'mobno':admin.Mobno,'token':admin.token,'cat':admin.user_category})
#                 elif phone == admin.Email and str(admin.user_category) == "analytics" and password == admin.password:
#                     return JsonResponse({'message':"Login Successful For analytics Admin",'username':admin.Name,'mobno':admin.Mobno,'token':admin.token,'cat':admin.user_category})
#                 else:  
#                     return JsonResponse({'error':"Invalid credential for Admin user"}, status=status.HTTP_404_NOT_FOUND)
#             else:  
#                 return JsonResponse({'error':"Invalid credential"}, status=status.HTTP_404_NOT_FOUND)
#         else:
#             return JsonResponse({'error':"Invalid phone number or email format"}, status=status.HTTP_404_NOT_FOUND)



import time

# Define a dictionary to keep track of login attempts
login_attempts = {}

@csrf_exempt
def login(request):
    if request.method == 'POST':
        userdata = JSONParser().parse(request)
        identifier = userdata.get('identifier')
        password = userdata.get('password')
        
        
        def is_valid_email(identifier):
            return "@" in identifier

        try:
            if is_valid_email(identifier):
                users = User.objects.filter(Email=identifier, password=password)
                managers = Manager.objects.filter(Email=identifier, password=password)
            else:
                users = User.objects.filter(Mob=identifier, password=password)
                managers = Manager.objects.filter(Mob=identifier, password=password)


            if users.exists():
                user = users.first()

                # Ensure the User is in the "Water Body" or "Aqua Farming" category
                if user.user_category in ['WaterBody', 'Aquafarming']:
                    csrf_token = get_token(request)
                    # Check if customer_category is 'owner'
                    if user.customer_category == 'owner':
                        response_data = {
                            'message': 'You have successfully logged in to the owner page...',
                            'Mob': user.Mob,
                            'name': user.Company_name,
                            'email': user.Email,
                            'csrf_token': csrf_token,
                            'user_category': user.user_category,
                            'category': "master"
                        }
                        return JsonResponse(response_data, status=200)
                    # return JsonResponse ()
                
            
            if managers.exists():
                manager = managers.first()
                user = manager.user  # Get the associated User for the Manager
                
                # Check the user_category of the associated user
                if user.user_category in ['WaterBody', 'Aquafarming']:
                    csrf_token = get_token(request)
                    response_data = {
                        'message': 'You have successfully logged in as a manager...',
                        'Mob': manager.Mob,
                        'name': manager.username,
                        'email': manager.email,
                        'csrf_token': csrf_token,
                        'user_category': user.user_category,
                        'category': "manager"
                    }
                    return JsonResponse(response_data, status=200)

            
            # else:
                return JsonResponse({'message': 'user does not exist.'}, status=403)

        except ObjectDoesNotExist:
            pass

        # If no valid user is found
        return JsonResponse({'message': 'Invalid credentials'}, status=400)

    return JsonResponse({'message': 'Invalid request method'}, status=400)
    




@csrf_exempt
def token_verification(request):
    
    if request.method == 'POST':
        jsondata = JSONParser().parse(request)
        token = jsondata.get('token')

        try:
            data = User.objects.get(token=token)
            return JsonResponse({'message': 'Authenticated successfully.',"token":data.token,"mobile_no":data.Mobno,"username":data.password})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
# @permission_classes([IsAuthenticated])
def registration(request):
    if request.method == 'POST':
        regd_instance=JSONParser().parse(request)
        firstname=regd_instance.get('firstname')
        lastname=regd_instance.get('lastname')
        Email=regd_instance.get('email')
        Mobno=regd_instance.get('mobno')
        Adhaar=regd_instance.get('adhaar')
        user_cat=regd_instance.get('user_cat')
        params = regd_instance.get('params')
        fullname=firstname+" "+lastname
        try:
            import json
            name = f'{fullname}'
            email = f'{Email}'
            mobno = f'{Mobno}'
            adhaar = f'{Adhaar}'
            user_category = f'{user_cat}'
            
            
            if user_cat == '3d':
                params = f'{params}'
                param = {
                    'host':settings.THREED_DB_HOST,
                    'database':settings.THREED_DB_NAME,
                    'user':settings.THREED_DB_USER,
                    'password':settings.THREED_DB_PASS
                    }
                conn = psycopg2.connect(**param)
                print("connected")
                cur = conn.cursor() 
                cur.execute('INSERT INTO public.myapp_registration("Name", "Email", "Mobno", "Adhaar", "user_category", "params") VALUES (%s, %s, %s, %s, %s, %s);', (name, email, mobno, adhaar, user_category, params))
                conn.commit()
                return JsonResponse({'message': 'Registration successfully as 3d-Dashboard user'})
            
            
            elif user_cat == 'analytics':
                params = f'{json.dumps(params)}'
                param = {
                    'host':settings.ADMIN_DASH_DB_HOST,
                    'database':settings.ADMIN_DASH_DB_NAME,
                    'user':settings.ADMIN_DASH_DB_USER,
                    'password':settings.ADMIN_DASH_DB_PASS
                    }
                conn = psycopg2.connect(**param)
                print("connected")
                cur = conn.cursor() 
                cur.execute('INSERT INTO public.app1_registration("Name", "Email", "Mobno", "Adhaar", "user_category", "params") VALUES (%s, %s, %s, %s, %s, %s);', (name, email, mobno, adhaar, user_category, params))
                conn.commit()
                return JsonResponse({'message': 'Registration successfully as Analytics-Dashboard user'})
            
            
            
            elif user_cat == 'aqua':
                local_user = User(
                    Name=fullname,
                    Email=Email,
                    Mobno=Mobno,
                    Adhaar=Adhaar,
                    user_category=user_category,
                    password=params
                )
                local_user.save()
                
                
                params = f'{params}'
                param = {
                    'host':settings.AQUA_FARM_DB_HOST,
                    'database':settings.AQUA_FARM_DB_NAME,
                    'user':settings.AQUA_FARM_DB_USER,
                    'password':settings.AQUA_FARM_DB_PASS
                    }
                conn = psycopg2.connect(**param)
                print("connected")
                cur = conn.cursor() 
                cur.execute('INSERT INTO public.myapp_user("Name", "Email", "Mob", "adhaar", "user_category", "password") VALUES (%s, %s, %s, %s, %s, %s);', (name,email, mobno, adhaar, user_category, params)) and ('INSERT INTO public.myapp_user("Name", "Email", "Mobno", "adhaar", "user_category", "password") VALUES (%s, %s, %s, %s, %s, %s);', (name, email, mobno, adhaar, user_category, params))
                conn.commit()
                return JsonResponse({'message': 'Registration successfully as Aqua-Farming user'})
            
            elif user_cat == 'water':
                water_user = User(
                    Name=fullname,
                    Email=Email,
                    Mobno=Mobno,
                    Adhaar=Adhaar,
                    user_category=user_category,
                    password=params
                )
                water_user.save()
                params = f'{params}'
                param = {
                    'host':settings.WATERBODY_DB_HOST,
                    'database':settings.WATERBODY_DB_NAME,
                    'user':settings.WATERBODY_DB_USER,
                    'password':settings.WATERBODY_DB_PASS
                    }
                conn = psycopg2.connect(**param)
                print("connected")
                cur = conn.cursor() 
                cur.execute('INSERT INTO public.myapp_user("Name", "Email", "Mob", "adhaar", "user_category", "password") VALUES (%s, %s, %s, %s, %s, %s);', (name,email, mobno, adhaar, user_category, params)) and ('INSERT INTO public.myapp_user("Name", "Email", "Mob", "adhaar", "user_category", "password") VALUES (%s, %s, %s, %s, %s, %s);', (name, email, mobno, adhaar, user_category, params))
                conn.commit()
                return JsonResponse({'message': 'Registration successfully as Water-Body user'})
            else:
                return JsonResponse({'error': 'Error occured!'})
        except Exception as e:
            return JsonResponse({'error': str(e)})
import random  
@csrf_exempt
def master_registration(request):
    if request.method == 'POST':
        regd_instance=JSONParser().parse(request)
        firstname=regd_instance.get('firstname')
        lastname=regd_instance.get('lastname')
        Email=regd_instance.get('email')
        Mobno=regd_instance.get('mobno')
        address=regd_instance.get('address')
        user_cat=regd_instance.get('user_cat')
        params = regd_instance.get('params')
        fullname=firstname+" "+lastname
        try:
            import json
            name = f'{fullname}'
            email = f'{Email}'
            mobno = f'{Mobno}'
            address = f'{address}'
            user_category = f'{user_cat}'
            
            
            if user_cat == '3d':
                params = f'{params}'
                param = {
                    'host':settings.THREED_DB_HOST,
                    'database':settings.THREED_DB_NAME,
                    'user':settings.THREED_DB_USER,
                    'password':settings.THREED_DB_PASS
                    }
                conn = psycopg2.connect(**param)
                print("connected")
                cur = conn.cursor() 
                cur.execute('INSERT INTO public.myapp_Master("Name", "Email", "Mobno", "address", "user_category", "params") VALUES (%s, %s, %s, %s, %s, %s);', (name, email, mobno, address , user_category, params))
                conn.commit()
                return JsonResponse({'message': 'Registration successfully as 3d-Dashboard user'})
            
            
            elif user_cat == 'analytics':
                if user_cat:
                    first_word_of_name = fullname.split()[0].lower()  
                    random_number = random.randrange(100000000,99999999999) 
        
                    customer_id = f"{first_word_of_name}{random_number}"
                    current_time = datetime.datetime.now()
                    token = get_token(request)
                    iot_user = Master(
                        Name=fullname,
                        Email=Email,
                        Mobno=Mobno,
                        # created_at=created_at,
                        customer_id=customer_id,
                        address=address,
                        user_category=user_category,
                        password=params
                    )
                    iot_user.save()
                    # params = f'{json.dumps(params)}'
                    params = f'{params}'
                    param = {
                        'host':settings.ADMIN_DASH_DB_HOST,
                        'database':settings.ADMIN_DASH_DB_NAME,
                        'user':settings.ADMIN_DASH_DB_USER,
                        'password':settings.ADMIN_DASH_DB_PASS
                        }
                    conn = psycopg2.connect(**param)
                    print("connected")
                    cur = conn.cursor() 
                    cur.execute('INSERT INTO public.app1_Master("Name", "Email", "Mobno","address","customer_id","created_at","token", "user_category", "password") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);', (name,email, mobno, address,customer_id,current_time,token, user_category, params)) and ('INSERT INTO public.myapp_master("Name", "Email", "Mobno","address","customer_id","created_at","token","user_category", "password") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);', (name, email, mobno, address, customer_id, current_time, user_category,token, params))
                    conn.commit()
                    return JsonResponse({'message': 'Registration successfully as Analytics-Dashboard user'})
                else:
                    return JsonResponse({'error': 'Error occured!'})
                
            
            elif user_cat == 'aqua':
                if user_cat:
                    first_word_of_name = fullname.split()[0].lower()  
                    random_number = random.randrange(100000000,99999999999) 
        
                    customer_id = f"{first_word_of_name}{random_number}"
                    current_time = datetime.datetime.now()
                    # token = get_token(request)
                    token = csrf.get_token(request)
                    local_user = Master(
                        Name=fullname,
                        Email=Email,
                        Mobno=Mobno,
                        address=address,
                        customer_id=customer_id,
                        # created_at=created_at,
                        created_at=current_time,
                        user_category=user_category,
                        password=params
                    )
                    local_user.save()  
                    print("User saved successfully")
                    
                    params = f'{params}'
                    print(params)
                    param = {
                        'host':settings.AQUA_FARM_DB_HOST,
                        'database':settings.AQUA_FARM_DB_NAME,
                        'user':settings.AQUA_FARM_DB_USER,
                        'password':settings.AQUA_FARM_DB_PASS
                        }
                    conn = psycopg2.connect(**param)
                    print("connected")
                    cur = conn.cursor() 
                    
                    cur.execute('INSERT INTO public.myapp_master("Name", "Email", "Mobno","address","customer_id","created_at","token", "user_category", "password") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);', (name,email, mobno, address,customer_id,current_time,token, user_category, params)) and ('INSERT INTO public.myapp_master("Name", "Email", "Mobno","address","customer_id","created_at","token","user_category", "password") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);', (name, email, mobno, address, customer_id, current_time, user_category,token, params))
                    conn.commit()
                    return JsonResponse({'message': 'Registration successfully as Aqua-Farming user'})
                else:
                    return JsonResponse({'error': 'Error occured!'})
            
            elif user_cat == 'water':
                if user_cat:
                    first_word_of_name = fullname.split()[0].lower()  
                    random_number = random.randrange(100000000,99999999999) 
        
                    customer_id = f"{first_word_of_name}{random_number}"
                    current_time = datetime.datetime.now()
                    token = get_token(request)
                    water_user = User(
                        Name=fullname,
                        Email=Email,
                        Mobno=Mobno,
                        # created_at=created_at,
                        customer_id=customer_id,
                        address=address,
                        user_category=user_category,
                        password=params
                    )
                    water_user.save()
                    params = f'{params}'
                    param = {
                        'host':settings.WATERBODY_DB_HOST,
                        'database':settings.WATERBODY_DB_NAME,
                        'user':settings.WATERBODY_DB_USER,
                        'password':settings.WATERBODY_DB_PASS
                        }
                    conn = psycopg2.connect(**param)
                    print("connected")
                    cur = conn.cursor() 
                    cur.execute('INSERT INTO public.myapp_Master("Name", "Email", "Mobno","address","customer_id","created_at","token", "user_category", "password") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);', (name,email, mobno, address,customer_id,current_time,token, user_category, params)) and ('INSERT INTO public.myapp_master("Name", "Email", "Mobno","address","customer_id","created_at","token","user_category", "password") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);', (name, email, mobno, address, customer_id, current_time, user_category,token, params))
                    conn.commit()
                    return JsonResponse({'message': 'Registration successfully as Water-Body user'})
                else:
                    return JsonResponse({'error': 'choose correct category!'})
            else:
                return JsonResponse({'error': 'Error occured!'})
        except Exception as e:
            return JsonResponse({'error': str(e)})
            

@csrf_exempt
def register_view(request):
    try:
        if request.method == 'GET':
            data = Master.objects.all()
            final_list = [(data.Name,data.Mobno,data.Email,data.password,data.created_at,data.customer_id,data.token,data.address,data.user_category) for data in data]
            return JsonResponse({"items":final_list})
        else:
            pass
    except Exception as e:  
            return JsonResponse({'error': str(e)}, status=500)
@api_view(['POST'])
@csrf_exempt        
def admincreate(request):
    if request.method == 'POST':
        userimg=request.data['userimg']
        print(userimg)
        firstname=request.data['firstname']
        lastname=request.data['lastname']
        email=request.data['email']
        mobno=request.data['mobno']
        password=request.data['password']
        usertype=request.data['user_cat']
        fullname=firstname+" "+lastname
        a = AdminUser.objects.filter(Mobno=mobno)
        b = User.objects.filter(Mobno=mobno)
        # try:
        if b.exists():
            return JsonResponse({"message":"Mobile no already used as General User"})
        if not a.exists():
            token = get_token(request)
            datas = AdminUser(Name=fullname,Email=email,Mobno=mobno,password=password,user_category=usertype,token=token)
            datas.save()
            param = {
                    'host':settings.ADMIN_DASH_DB_HOST,
                    'database':settings.ADMIN_DASH_DB_NAME,
                    'user':settings.ADMIN_DASH_DB_USER,
                    'password':settings.ADMIN_DASH_DB_PASS
                    }
            conn = psycopg2.connect(**param)
            print("connected")
            cur = conn.cursor() 
            cur.execute('INSERT INTO public.app1_adminuser("Name", "Email", "Mobno", "password", "token", "user_category", "user_img") VALUES (%s, %s, %s, %s, %s, %s, %s);', (f'{fullname}', f'{email}', f'{mobno}', f'{password}', f'{token}', f'{usertype}', f'{userimg}'))
            conn.commit()
            return JsonResponse({"message":"Admin user created"})
        else:
            return JsonResponse({"message":"Mobile no. already exists"})
            # else:
            #     return JsonResponse({"message":"Mobile no. already exists"})
        # except Exception as e:
        #     return JsonResponse({"error":str(e)})

@csrf_exempt        
def admin_delete(request):
    if request.method == 'POST':
        admininstance = JSONParser().parse(request)
        mobno=admininstance.get('mobno')
        param = {
                    'host':settings.ADMIN_DASH_DB_HOST,
                    'database':settings.ADMIN_DASH_DB_NAME,
                    'user':settings.ADMIN_DASH_DB_USER,
                    'password':settings.ADMIN_DASH_DB_PASS
                    }
        conn = psycopg2.connect(**param)
        print("connected")
        cur = conn.cursor() 
        cur.execute(f'DELETE FROM public.app1_adminuser WHERE "Mobno"={mobno};')
        conn.commit()
        a = AdminUser.objects.get(Mobno=mobno)
        a.delete()
        return JsonResponse({"message":"Admin deleted"})
    
@csrf_exempt        
def admin_view(request):
    if request.method == 'GET':
        a = AdminUser.objects.all()
        data = [(i.Name,i.Email,i.Mobno,i.user_category,i.password) for i in a]

            
@csrf_exempt
def forgetpasswords(request):
    if request.method == 'POST':
        admininstance = JSONParser().parse(request)
        email=admininstance.get('email')
        a = User.objects.filter(Email=email)
        if a.exists():
            admin = a.first()
            admin.password = get_random_password(length=10, allowed_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
            admin.save()
            send_mail(
                'Password Reset',
                f'Your password has been reset to {admin.password}. Please login to your account and change it.',
                'your-email@example.com',
                [admin.Email],
                fail_silently=False,
            )
            return JsonResponse({"message":"Password reset email sent successfully"})
        else:
            return JsonResponse({"message":"No admin account found with this email"})