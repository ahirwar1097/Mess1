from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Student, Mess, MessAllot, FeeDetails

# Create your views here.\


def home(request):
    return render(request, 'home.html')


def mess(request):
    return render(request, 'mess.html')


def allot(request):
    return render(request, 'allot.html')


def apply(request):
    if request.method == 'POST':
        mess_type = request.POST['mess_type']
        stu_id = Student.objects.get(stu_reg_no=request.user)
        sobj = Mess.objects.filter(mess_type=mess_type, mess_boys=stu_id.stu_gender)
        return render(request, 'allot.html', {'sobj': sobj})
        # for i in sobj:
        #     print(i.mess_name)
        # return redirect('apply')
    else:
        return render(request, 'apply.html')


def allot_details(request):
    if request.method == 'POST':
        mess_id = request.POST['Messes']
        #print(mess_id)
        print(request.user)
        user_id = Student.objects.get(stu_reg_no=request.user)

        mes_obj = Mess.objects.get(mess_id=mess_id)

        fee_uid = FeeDetails.objects.get(stu_reg_no=user_id)

        #alloted_uid = MessAllot.objects.filter(allot_reg_no=user_id).exists()

        if MessAllot.objects.filter(allot_reg_no=user_id).exists():
            messages.info(request, 'Mess already alloted')
            print('user existing')
            return redirect('/')
        elif mes_obj.mess_count > mes_obj.mess_capacity:
            messages.info(request, 'Sorry ! All seats filled !')
            return redirect('allot.html')
        elif fee_uid.fee_status is True:
            if mes_obj.mess_count > mes_obj.mess_capacity:
                messages.info(request, 'Sorry ! All seats filled !')
                return redirect('allot.html')
            else:
                add_mess_obj = MessAllot(
                        allot_reg_no=user_id,
                        allot_mess_id=mes_obj,
                        allot_mess=True
                    )
                add_mess_obj.save()
                add_count = Mess(
                    mess_count=mes_obj.mess_count+1,
                )
                add_count.save()
                print('mess alloted successfully')
        else:
            return redirect('home.html')
            #return HttpResponse("welcome")
   # else:
        #return redirect('allot.html')


def register(request):
    if request.method == 'POST':
        reg_no = request.POST['reg_no']
        name = request.POST['name']
        gender = request.POST['gender']
        degree = request.POST['course']
        dept = request.POST['dept']
        hostel = request.POST['hostel']
        room_no = request.POST['room_no']
        email = request.POST['email']
        contact = request.POST['contact']
        mess_roll_no = request.POST['mess_roll_no']
        img = request.POST['img']
        sign = request.POST['sign']
        password = request.POST['password']
        password1 = request.POST['password1']

        #user_id = Student.objects.get(stu_reg_no=reg_no)
        if password == password1:
            if Student.objects.filter(stu_reg_no=reg_no).exists():
                messages.info(request, 'Already Registered')
                print('user existing')
                return redirect('/')
            else:
                add_stu = Student(
                    stu_reg_no=reg_no,
                    stu_name=name,
                    stu_gender=gender,
                    stu_degree=degree,
                    stu_dept=dept,
                    stu_hostel_block=hostel,
                    stu_room_no=room_no,
                    stu_email=email,
                    stu_contact=contact,
                    stu_mess_roll_no=mess_roll_no,
                    stu_img=img,
                    stu_sign=sign
                )
                add_stu.save()
                user = User.objects.create_user(username=reg_no, password=password)
                user.save()

                print('registered')
                messages.info(request, 'Registered')
                return redirect('register.html')
        else:
            messages.info(request, 'Password not matching')
            return redirect('register')
    else:
        return render(request, 'register.html')



        #if password == password1:
         #   if User.objects.filter(username=username).exists():
          #      messages.info(request, 'User already exist')
           #     return redirect('register')
            #else:

             #   user.save();
              #  messages.info(request, 'User created')
        #else:
         #   messages.info(request, 'Password not matching')
          #  return redirect('register')
        #return redirect('/')
    #else:
     #   return render(request, 'register.html')