from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(Wheel_Specification_Form)
admin.site.register(Wheel_Specification_Data)


admin.site.register(Bogie_Check_Sheet_Form)
admin.site.register(Bogie_Details_Data)
admin.site.register(Bogie_Check_Sheet_Data)
admin.site.register(BMBC_Check_Sheet_Data)

