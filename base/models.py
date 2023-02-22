from contextlib import nullcontext
from statistics import mode
from django.db import models

# Create your models here.
Deptartments = (
    ('computer science','COMPUTER SCIENCE'),
    ('information system', 'INFORMATION SYSTEM'),
    ('information technology','INFORMATION TECHNOLOGY'),
    ('artificial intelligence','ARTIFICIAL INTELLIGENCE'),
    ('decision support system','DECISION SUPPORT SYSTEM'),
    ('null','NULL')
)
Gender = (
    ('male','MALE'),
    ('female','FEMALE')
)
Status = (
    ('active','ACTIVE'),
    ('inactive','INACTIVE')
)
'name','ID','GPA','dob','level','gender','email','status','department','phone_Num'
class Student(models.Model):
    name = models.CharField(max_length= 124)
    ID = models.CharField(primary_key=True, max_length= 10)
    GPA = models.CharField(max_length=10, blank=True,null=True)
    dob = models.DateField()
    level = models.IntegerField()
    gender = models.CharField(max_length= 32,choices=Gender,default='male')
    email = models.EmailField(max_length=240)
    status = models.CharField(max_length= 32, choices=Status,default='ACTIVE')
    department = models.CharField(max_length= 32, null =True, blank=True , choices=Deptartments,default=nullcontext)
    phone_Num = models.CharField(max_length= 124, blank=True,null=True)
    
    def __str__(self):
        return f"Name: {self.name} {self.status} {self.department}"
