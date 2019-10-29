from django.contrib import admin
from .models import Student, Mess, MessAllot, FeeDetails

# Register your models here.


admin.site.register(Student)
admin.site.register(Mess)
admin.site.register(MessAllot)
admin.site.register(FeeDetails)
