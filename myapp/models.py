from django.db import models

# Create your models here.
class Master(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.EmailField()
    Mobno=models.BigIntegerField(primary_key=True)
    password=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    # customer_id=models.CharField(max_length=100)                                #commented by tapas
    # token = models.CharField(max_length=100,blank=True, null=True)
    # address = models.CharField(max_length=100)
    # USER_TYPES = (
    #     ('3d', '3d'),
    #     ('analytics', 'analytics'),
    #     ('aqua', 'aqua'),
    #     ('water', 'water'),
    # )
    # user_category = models.CharField(max_length=30, choices=USER_TYPES,default=USER_TYPES)
    def __str__(self):
        return self.Name 
        


class User(models.Model):  
    # id = models.AutoField()                                       
    Company_name=models.CharField(max_length=30,null=False)
    Mob=models.BigIntegerField(primary_key=True,unique=True)
    Email=models.EmailField()
    Customer_id=models.CharField(max_length=100)
    password = models.CharField(max_length=50, blank=True, null=True)
    address=models.CharField(max_length=100, blank=True, null=True)
    Pan_no = models.CharField(max_length=50)
    GST_no = models.CharField(max_length=50)
    user_category = models.CharField(max_length=50, blank=True, null=True)                   #commentout by tapas
    customer_category = models.CharField(max_length=50, blank=True, null=True) 
    token = models.CharField(max_length=200,blank=True,null=True)                    #commented by soumya
    # telegram_username = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        return str(self.Company_name)
    

class Manager(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    Mob = models.BigIntegerField(primary_key=True)
    email = models.EmailField()
    # company_name = models.CharField(max_length=50,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.username)