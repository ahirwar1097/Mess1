from django.db import models

# Create your models here.


class Mess(models.Model):
    mess_id = models.CharField(max_length=20, primary_key=True)
    mess_name = models.CharField(max_length=30, null=False)
    mess_capacity = models.IntegerField()
    mess_type = models.CharField(max_length=50, null=False)
    mess_boys = models.BooleanField()
    mess_img = models.ImageField()
    mess_address = models.TextField()


class Student(models.Model):
    stu_reg_no = models.CharField(max_length=15, primary_key=True)
    stu_name = models.CharField(max_length=50, null=False)
    stu_gender = models.CharField(max_length=2, null=False)
    stu_degree = models.CharField(max_length=50, null=False)
    stu_dept = models.CharField(max_length=50, null=False)
    stu_hostel_block = models.CharField(max_length=20, null=False)
    stu_room_no = models.IntegerField(null=False)
    stu_email = models.EmailField(max_length=50, null=False, unique=True)
    stu_contact = models.IntegerField(null=False, unique=True)
    stu_mess_roll_no = models.CharField(max_length=10, unique=True)
    stu_img = models.ImageField(upload_to='images')
    stu_sign = models.ImageField(upload_to='images')
    stu_password = models.CharField(max_length=16)


class MessAllot(models.Model):
    allot_reg_no = models.ForeignKey(Student, on_delete=models.CASCADE)
    allot_mess_id = models.ForeignKey(Mess, on_delete=models.CASCADE)
    allot_mess = models.BooleanField(default=False)
    allot_date = models.DateField(auto_now=False, auto_now_add=False)
    allot_card_no = models.CharField(max_length=20)


class FeeDetails(models.Model):
    stu_reg_no = models.ForeignKey(Student, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=100)
    fee_status = models.BooleanField(default=False)