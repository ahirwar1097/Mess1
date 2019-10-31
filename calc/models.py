from django.db import models
from datetime import datetime
# Create your models here.


class Mess(models.Model):
    mess_id = models.CharField(max_length=20, primary_key=True)
    mess_name = models.CharField(max_length=30, null=False)
    mess_capacity = models.CharField(max_length=4)
    mess_type = models.CharField(max_length=50, null=False)
    mess_boys = models.CharField(max_length=2)
    mess_count = models.CharField(max_length=4, null=True)

    def __str__(self):
        return self.mess_id


class Student(models.Model):
    stu_reg_no = models.CharField(max_length=15, primary_key=True)
    stu_name = models.CharField(max_length=50, null=False)
    stu_gender = models.CharField(max_length=2, null=False)
    stu_degree = models.CharField(max_length=50, null=False)
    stu_dept = models.CharField(max_length=50, null=False)
    stu_hostel_block = models.CharField(max_length=20, null=False)
    stu_room_no = models.CharField(max_length=10, null=False)
    stu_email = models.EmailField(max_length=50, null=False, unique=True)
    stu_contact = models.CharField(max_length=15, null=False)
    stu_mess_roll_no = models.CharField(max_length=10, unique=True)
    stu_img = models.ImageField(upload_to='images')
    stu_sign = models.ImageField(upload_to='images')

    def __str__(self):
        return self.stu_reg_no


class MessAllot(models.Model):
    allot_reg_no = models.ForeignKey(Student, on_delete=models.CASCADE)
    allot_mess_id = models.ForeignKey(Mess, on_delete=models.CASCADE)
    allot_mess = models.BooleanField(default=False)
    allot_date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.allot_reg_no.stu_reg_no


class FeeDetails(models.Model):
    stu_reg_no = models.ForeignKey(Student, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=100)
    fee_status = models.BooleanField(default=False)

    def __str__(self):
        return self.stu_reg_no.stu_reg_no
