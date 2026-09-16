from django.shortcuts import render
from .models import *
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.middleware import csrf
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .helper import send_forget_password_mail
import psycopg2
from django.middleware.csrf import get_token
import datetime
import re
from django.conf import settings
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework import status
from .serializers import MasterDetailsSerializer,ManagerRegisterSerializer
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
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
@csrf_exempt
def login(request):
    if request.method == 'POST':
        userdata = JSONParser().parse(request)
        identifier = userdata.get('identifier')
        password = userdata.get('password')

        def is_valid_email(identifier):
            return "@" in identifier

        try:
            # Check by email or mobile
            if is_valid_email(identifier):
                masters = Master.objects.filter(Email=identifier, password=password)
                users = User.objects.filter(Email=identifier, password=password)
                managers = Manager.objects.filter(email=identifier, password=password)
            else:
                masters = Master.objects.filter(Mobno=identifier, password=password)
                users = User.objects.filter(Mob=identifier, password=password)
                print(users)
                managers = Manager.objects.filter(Mob=identifier, password=password)
            # token=get_token(request)
            # MASTER LOGIN
            if masters.exists():
                master = masters.first()
                response_data = {
                    'message': "you have successfully logged in as master....",
                    'Mob': master.Mobno,
                    'name': master.Name,
                    'email': master.Email,
                    # 'csrf_token':token,
                    'category': 'master'
                }
                return JsonResponse(response_data, status=200)

            # USER LOGIN (OWNER)
            if users.exists():
                user = users.first()
                if user.user_category in ['WaterBody', 'Aquafarming']:
                    response_data = {
                        'message': 'You have successfully logged in to the owner page...',
                        'Mob': user.Mob,
                        'name': user.Company_name,
                        'email': user.Email,
                        'user_category':user.user_category,
                        # 'csrf_token': token,
                        'category': "owner"
                    }
                    return JsonResponse(response_data, status=200)

            # MANAGER LOGIN
            if managers.exists():
                manager = managers.first()
                user = manager.user
                if user.user_category in ['WaterBody', 'Aquafarming']:
                    response_data = {
                        'message': 'You have successfully logged in as a manager...',
                        'Mob': manager.Mob,
                        'name': manager.username,
                        'email': manager.email,
                        # 'csrf_token': token,
                        'user_category': manager.user_category,
                        'category': "manager"
                    }
                    return JsonResponse(response_data, status=200)

        except ObjectDoesNotExist:
            pass

        return JsonResponse({'message': 'Invalid credentials'}, status=400)

    return JsonResponse({'message': 'Invalid request method'}, status=400)

    




#***********Token Varification**********#
########################################
@csrf_exempt
def token_verification(request):
    if request.method == 'POST':
        jsondata = JSONParser().parse(request)
        token = jsondata.get('token')

        # Check in Master Table
        try:
            master = Master.objects.get(token=token)
            return JsonResponse({
                'message': 'Authenticated successfully.',
                'model': 'Master',
                'token': master.token,
                'mobile_no': master.Mobno,
                'username': master.Name,
            })
        except Master.DoesNotExist:
            pass

        # Check in User Table
        try:
            user = User.objects.get(token=token)
            return JsonResponse({
                'message': 'Authenticated successfully.',
                'model': 'User',
                'token': user.token,
                'mobile_no': user.Mob,
                'username': user.Company_name,
            })
        except User.DoesNotExist:
            pass

        # Check in Manager Table
        try:
            manager = Manager.objects.get(token=token)
            return JsonResponse({
                'message': 'Authenticated successfully.',
                'model': 'Manager',
                'token': manager.token,
                'mobile_no': manager.Mob,
                'username': manager.username,
                'user_category': manager.user_category,
                'connected_user': manager.user.Mob  # Fk to User model
            })
        except Manager.DoesNotExist:
            pass

        # Token not matched in any table
        return JsonResponse({'error': 'Invalid token or user not found.'}, status=400)




#***********User Registration********#
########################################
@api_view(['POST'])
@csrf_exempt        
def user_registration(request):
    if request.method == 'POST':
        try:
            print(request.data)
            # Incoming request data
            # firstname = request.data.get('firstname')
            # lastname = request.data.get('lastname')
            # email = request.data.get('email')

            mob = request.data.get('mobno')
            password = request.data.get('password')

            # Additional required fields
            # company_name = request.data.get('company_name')
            # address = request.data.get('address')
            # pan_no = request.data.get('pan_no')
            # gst_no = request.data.get('gst_no')
            # customer_id = request.data.get('customer_id')
            user_category= request.data.get('user_category')
            full_name = request.data.get('name')
            print(user_category)
            if user_category==None or user_category=='':
                print('*****')
                user_category="Aquafarming"

            ########################################################
            #********Function to Create table if not exists********#
            ########################################################
            
            # Create authentication token
            token = get_token(request)

            # Save to Django database
            user_obj = User(
                Name=full_name,
                # Company_name=company_name,
                Mob=mob,
                # Email=email,
                # Customer_id=customer_id,
                user_category=user_category,
                password=password,
                # address=address,
                # Pan_no=pan_no,
                # GST_no=gst_no,
                token=token,
            )
            user_obj.save()

            # Save to external PostgreSQL DB
            # param = {
            #     'host': settings.ADMIN_DASH_DB_HOST,
            #     'database': settings.ADMIN_DASH_DB_NAME,
            #     'user': settings.ADMIN_DASH_DB_USER,
            #     'password': settings.ADMIN_DASH_DB_PASS
            # }

            # conn = psycopg2.connect(**param)
            # cur = conn.cursor()
            # cur.execute("""
            #     INSERT INTO public.myapp_user
            #     ("Name","Email", "Mob", "password",
            #      "Customer_id", "Company_name","user_category",
            #      "address", "Pan_no", "GST_no", "token")
            #     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)
            # """, (full_name,email,mob,password,customer_id,company_name,user_category,address,pan_no,gst_no,token))
            # conn.commit()
            # conn.close()

            return JsonResponse({"message": "User successfully registered"}, status=201)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)



#***********Master Registration********#
########################################
import random  
@csrf_exempt
def master_registration(request):
    if request.method == 'POST':
        regd = JSONParser().parse(request)
        firstname = regd.get('firstname')
        lastname = regd.get('lastname')
        email = regd.get('email')
        mobno = regd.get('mobno')
        address = regd.get('address')
        user_cat = regd.get('user_cat')
        params = regd.get('params')

        fullname = f"{firstname} {lastname}"

        try:
            # ---------------- COMMON FUNCTIONS ----------------

            def generate_customer_id(fullname):
                first = fullname.split()[0].lower()
                number = random.randrange(10**7, 10**10)
                return f"{first}{number}"

            def ensure_table_exists(connection, table_name):
                """Creates table if it doesn't exist."""
                ddl = f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                    id SERIAL PRIMARY KEY,
                    "Name" VARCHAR(255),
                    "Email" VARCHAR(255),
                    "Mobno" VARCHAR(50),
                    "address" TEXT,
                    "customer_id" VARCHAR(255),
                    "created_at" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    "token" TEXT,
                    "user_category" VARCHAR(100),
                    "password" TEXT
                )
                """
                cur = connection.cursor()
                try:
                    cur.execute(ddl)
                    connection.commit()
                finally:
                    cur.close()

            def insert_into_db(settings_obj, query, values, table_name):
                """Ensures table exists before inserting data."""
                param = {
                    'host': settings_obj['HOST'],
                    'database': settings_obj['NAME'],
                    'user': settings_obj['USER'],
                    'password': settings_obj['PASS']
                }
                conn = psycopg2.connect(**param)

                # Ensure table exists
                ensure_table_exists(conn, table_name)

                # Insert data
                cur = conn.cursor()
                cur.execute(query, values)
                conn.commit()
                cur.close()
                conn.close()

            # ---------------- CATEGORY HANDLING ----------------

            # 3D USER
            if user_cat == '3d':
                customer_id = generate_customer_id(fullname)
                current_time = datetime.datetime.now()
                token = get_token(request)

                Master.objects.create(
                    Name=fullname,
                    Email=email,
                    Mobno=mobno,
                    customer_id=customer_id,
                    created_at=current_time,
                    token=token,
                    address=address,
                    user_category=user_cat,
                    password=params
                )

                query = """
                    INSERT INTO public.myapp_master
                    ("Name","Email","Mobno","address","customer_id","created_at","token","user_category","password")
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """

                insert_into_db(
                    {
                        "HOST": settings.ADMIN_DASH_DB_HOST,
                        "NAME": settings.ADMIN_DASH_DB_NAME,
                        "USER": settings.ADMIN_DASH_DB_USER,
                        "PASS": settings.ADMIN_DASH_DB_PASS
                    },
                    query,
                    (fullname, email, mobno, address, customer_id, current_time, token, user_cat, params),
                    "public.myapp_master"
                )

                return JsonResponse({'message': 'Registration successful as 3D Dashboard user'})

            # ANALYTICS USER
            elif user_cat == 'analytics':
                customer_id = generate_customer_id(fullname)
                current_time = datetime.datetime.now()
                token = get_token(request)

                Master.objects.create(
                    Name=fullname,
                    Email=email,
                    Mobno=mobno,
                    customer_id=customer_id,
                    created_at=current_time,
                    token=token,
                    address=address,
                    user_category=user_cat,
                    password=params
                )

                query = """
                    INSERT INTO public.myapp_master
                    ("Name","Email","Mobno","address","customer_id","created_at","token","user_category","password")
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """

                insert_into_db(
                    {
                        "HOST": settings.ADMIN_DASH_DB_HOST,
                        "NAME": settings.ADMIN_DASH_DB_NAME,
                        "USER": settings.ADMIN_DASH_DB_USER,
                        "PASS": settings.ADMIN_DASH_DB_PASS
                    },
                    query,
                    (fullname, email, mobno, address, customer_id, current_time, token, user_cat, params),
                    "public.myapp_master"
                )

                return JsonResponse({'message': 'Registration successful as Analytics Dashboard user'})

            # AQUA USER
            elif user_cat == 'aqua':
                customer_id = generate_customer_id(fullname)
                current_time = datetime.datetime.now()
                token = csrf.get_token(request)

                Master.objects.create(
                    Name=fullname,
                    Email=email,
                    Mobno=mobno,
                    customer_id=customer_id,
                    token=token,
                    address=address,
                    created_at=current_time,
                    user_category=user_cat,
                    password=params
                )

                query = """
                    INSERT INTO public.myapp_master
                    ("Name","Email","Mobno","address","customer_id","created_at","token","user_category","password")
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """

                insert_into_db(
                    {
                        "HOST": settings.ADMIN_DASH_DB_HOST,
                        "NAME": settings.ADMIN_DASH_DB_NAME,
                        "USER": settings.ADMIN_DASH_DB_USER,
                        "PASS": settings.ADMIN_DASH_DB_PASS
                    },
                    query,
                    (fullname, email, mobno, address, customer_id, current_time, token, user_cat, params),
                    "public.myapp_master"
                )

                return JsonResponse({'message': 'Registration successful as Aqua Farming user'})

            # WATERBODY USER
            elif user_cat == 'water':
                customer_id = generate_customer_id(fullname)
                current_time = datetime.datetime.now()
                token = get_token(request)

                Master.objects.create(
                    Name=fullname,
                    Email=email,
                    Mobno=mobno,
                    customer_id=customer_id,
                    created_at=current_time,
                    token=token,
                    address=address,
                    user_category=user_cat,
                    password=params
                )

                query = """
                    INSERT INTO public.myapp_master
                    ("Name","Email","Mobno","address","customer_id","created_at","token","user_category","password")
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """

                insert_into_db(
                    {
                        "HOST": settings.ADMIN_DASH_DB_HOST,
                        "NAME": settings.ADMIN_DASH_DB_NAME,
                        "USER": settings.ADMIN_DASH_DB_USER,
                        "PASS": settings.ADMIN_DASH_DB_PASS
                    },
                    query,
                    (fullname, email, mobno, address, customer_id, current_time, token, user_cat, params),
                    "public.myapp_master"
                )

                return JsonResponse({'message': 'Registration successful as Water Body user'})

            else:
                return JsonResponse({'error': 'Invalid user category!'})

        except Exception as e:
            return JsonResponse({'error': str(e)})



#***********Manager Helper FunctionRegistration********#
########################################################
def ensure_table_exists(connection, table_name):
    ddl = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        "user_id" INTEGER,
        "username" VARCHAR(255),
        "email" VARCHAR(255),
        "Mob" VARCHAR(50),
        "created_at" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        "token" TEXT,
        "user_category" VARCHAR(100),
        "password" TEXT
    )
    """
    cur = connection.cursor()
    try:
        cur.execute(ddl)
        connection.commit()
    finally:
        cur.close()


#***********Manager Registration********#
########################################################
class ManagerRegisterview(APIView):
    def post(self, request):
        token = get_token(request)

        serializer = ManagerRegisterSerializer(
            data=request.data,
            context={'token': token}
        )
        serializer.is_valid(raise_exception=True)
        manager = serializer.save()

        # ================= External DB Insert =================
        try:
            connection = psycopg2.connect(
                host=settings.ADMIN_DASH_DB_HOST,
                dbname=settings.ADMIN_DASH_DB_NAME,
                user=settings.ADMIN_DASH_DB_USER,
                password=settings.ADMIN_DASH_DB_PASS
            )

            table_name = "myapp_manager"
            ensure_table_exists(connection, table_name)

            cur = connection.cursor()
            insert_query = f"""
                INSERT INTO {table_name}
                ("user_id", "username", "email", "Mob",
                 "token", "user_category", "password")
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """

            cur.execute(
                insert_query,
                (
                    manager.user_id,        # FK user id
                    manager.username,
                    manager.email,
                    manager.Mob,
                    manager.token,
                    manager.user_category,
                    manager.password
                )
            )

            connection.commit()
            cur.close()
            connection.close()

        except Exception as e:
            return Response(
                {"error": f"External DB insert failed: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        return Response(
            {"sms": "Manager registered successfully"},
            status=status.HTTP_201_CREATED
        )




       

@csrf_exempt
def register_view(request):
    if request.method == 'GET':
        data = Master.objects.all()
        serializer=MasterDetailsSerializer(data)
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
    else:
        return Response({"sms":"NotFound"},status=status.HTTP_404_NOT_FOUND)

    

# @api_view(['POST'])
# @csrf_exempt        
# def admincreate(request):
#     if request.method == 'POST':
#         userimg=request.data['userimg']
#         print(userimg)
#         firstname=request.data['firstname']
#         lastname=request.data['lastname']
#         email=request.data['email']
#         mobno=request.data['mobno']
#         password=request.data['password']
#         usertype=request.data['user_cat']
#         fullname=firstname+" "+lastname
#         a = AdminUser.objects.filter(Mobno=mobno)
#         b = User.objects.filter(Mobno=mobno)
#         # try:
#         if b.exists():
#             return JsonResponse({"message":"Mobile no already used as General User"})
#         if not a.exists():
#             token = get_token(request)
#             datas = AdminUser(Name=fullname,Email=email,Mobno=mobno,password=password,user_category=usertype,token=token)
#             datas.save()
#             param = {
#                     'host':settings.ADMIN_DASH_DB_HOST,
#                     'database':settings.ADMIN_DASH_DB_NAME,
#                     'user':settings.ADMIN_DASH_DB_USER,
#                     'password':settings.ADMIN_DASH_DB_PASS
#                     }
#             conn = psycopg2.connect(**param)
#             print("connected")
#             cur = conn.cursor() 
#             cur.execute('INSERT INTO public.app1_adminuser("Name", "Email", "Mobno", "password", "token", "user_category", "user_img") VALUES (%s, %s, %s, %s, %s, %s, %s);', (f'{fullname}', f'{email}', f'{mobno}', f'{password}', f'{token}', f'{usertype}', f'{userimg}'))
#             conn.commit()
#             return JsonResponse({"message":"Admin user created"})
#         else:
#             return JsonResponse({"message":"Mobile no. already exists"})
#             # else:
            #     return JsonResponse({"message":"Mobile no. already exists"})
        # except Exception as e:
        #     return JsonResponse({"error":str(e)})

# @csrf_exempt        
# def admin_delete(request):
#     if request.method == 'POST':
#         admininstance = JSONParser().parse(request)
#         mobno=admininstance.get('mobno')
#         param = {
#                     'host':settings.ADMIN_DASH_DB_HOST,
#                     'database':settings.ADMIN_DASH_DB_NAME,
#                     'user':settings.ADMIN_DASH_DB_USER,
#                     'password':settings.ADMIN_DASH_DB_PASS
#                     }
#         conn = psycopg2.connect(**param)
#         print("connected")
#         cur = conn.cursor() 
#         cur.execute(f'DELETE FROM public.app1_adminuser WHERE "Mobno"={mobno};')
#         conn.commit()
#         a = AdminUser.objects.get(Mobno=mobno)
#         a.delete()
#         return JsonResponse({"message":"Admin deleted"})
    
# @csrf_exempt        
# def admin_view(request):
#     if request.method == 'GET':
#         a = AdminUser.objects.all()
#         data = [(i.Name,i.Email,i.Mobno,i.user_category,i.password) for i in a]

            
# @csrf_exempt
# def forgetpasswords(request):
#     if request.method == 'POST':
#         admininstance = JSONParser().parse(request)
#         email=admininstance.get('email')
#         a = User.objects.filter(Email=email)
#         if a.exists():
#             admin = a.first()
#             admin.password = get_random_password(length=10, allowed_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
#             admin.save()
#             send_mail(
#                 'Password Reset',
#                 f'Your password has been reset to {admin.password}. Please login to your account and change it.',
#                 'your-email@example.com',
#                 [admin.Email],
#                 fail_silently=False,
#             )
#             return JsonResponse({"message":"Password reset email sent successfully"})
#         else:
#             return JsonResponse({"message":"No admin account found with this email"})
        


# ############################################################################


@csrf_exempt
def myhtml(request,token):
    if request.method == "POST":
        password = request.POST.get('password')

        try:
            submit = User.objects.get(token=token)
        
            submit.password = password
            submit.save()
            
            param = {
                'host': settings.AQUA_FARM_DB_HOST,
                'database': settings.AQUA_FARM_DB_NAME,
                'user': settings.AQUA_FARM_DB_USER,
                'password': settings.AQUA_FARM_DB_PASS
            }
            conn = psycopg2.connect(**param)
            cur = conn.cursor()
            
            email = submit.Email  
            
            cur.execute('UPDATE public.myapp_user SET password = %s WHERE "Email" = %s;', (password, email))
            conn.commit()
            return JsonResponse({'message': 'Password successfully changed'}, status=200)

        
        except User.DoesNotExist:
            return JsonResponse({'message': 'Invalid token'}, status=404)
        except Exception as e:
            # Log the exception for debugging
            print(f'Error occurred: {e}')
            return JsonResponse({'message': 'An error occurred'}, status=500)

        finally:
            # Ensure proper resource cleanup
            if cur:
                cur.close()
            if conn:
                conn.close()
    
    return render(request,'home.html')


import uuid
@csrf_exempt
def forgotpassword(request):
    if request.method == 'POST':
        jsondata = JSONParser().parse(request)
        email = jsondata.get('Email')
        try:
            user = User.objects.get(Email=email)
            reset_token = user.token
            send_forget_password_mail(email, reset_token)
            return JsonResponse({'message': 'We send a change password link to your registered email id .Please click the link to reset password'}, status=200)
        except ObjectDoesNotExist:
            return JsonResponse({'message': 'Email does not exist'}, status=404)
