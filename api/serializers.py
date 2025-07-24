from rest_framework import serializers

# Main Data-Models
from InspectionData.models import Wheel_Specification_Form, Bogie_Check_Sheet_Form

# Foregin Data-Models
from InspectionData.models import Wheel_Specification_Data
from InspectionData.models import Bogie_Details_Data,Bogie_Check_Sheet_Data,BMBC_Check_Sheet_Data


#--------------------------------------------------For Wheel Data--------------------------------------------------------------------
class WheelDataFieldsSeralizers(serializers.ModelSerializer):
    
    class Meta:
        model = Wheel_Specification_Data
        fields = '__all__'
        

class WheelSpecificationsFormSerializers(serializers.ModelSerializer):
    
    class Meta:
        
        model = Wheel_Specification_Form
        fields = '__all__'
        


#-----------------------------------------------For Bogie Data-----------------------------------------------------------------------
class GET_WheelDataFieldsSeralizers(serializers.ModelSerializer):
    
    class Meta:
        model = Wheel_Specification_Data
        fields = ["treadDiameterNew", "lastShopIssueSize", "condemningDia", "wheelGauge"]


class GET_WheelSpecificationsFormSerializers(serializers.ModelSerializer):
    
    fields = GET_WheelDataFieldsSeralizers()
    class Meta:
        model = Wheel_Specification_Form
        fields= ["formNumber", "submittedBy", "submittedDate","fields"]


class POST_WheelResponceSerializers(serializers.ModelSerializer):
    
    status = serializers.SerializerMethodField()
    
    class Meta:
        model = Wheel_Specification_Form
        fields = ["formNumber", "submittedBy", "submittedDate", "status"]

    def get_status(self,obj):
        return "saved"

#-----------------------------------------------For Bogie Data-----------------------------------------------------------------------
class BogieDetailsSerializers(serializers.ModelSerializer):
    
    class Meta:
        
        model = Bogie_Details_Data
        fields = '__all__'
        
        
class BogieChecksheetSerializers(serializers.ModelSerializer):
    
    class Meta:
        
        model = Bogie_Check_Sheet_Data
        fields = '__all__'
        
        
class bmbcChecksheetSerializers(serializers.ModelSerializer):
    
    class Meta:
        
        model = BMBC_Check_Sheet_Data
        fields = '__all__'


class BogieCheckSheetFormSerializers(serializers.ModelSerializer):
    
    class Meta:
        
        model = Bogie_Check_Sheet_Form
        fields = '__all__'

#-----------------------------------------------For Bogie Data-----------------------------------------------------------------------

# set depth for foreign table data
class GET_BogieCheckSheetFormSerializers(serializers.ModelSerializer):
    
    class Meta:
        
        model = Bogie_Check_Sheet_Form
        fields = '__all__'
        depth = 1


class POST_BogieResponceSerializers(serializers.ModelSerializer):
    
    status = serializers.SerializerMethodField()
    
    class Meta:
        model = Bogie_Check_Sheet_Form
        fields = ["formNumber", "inspectionBy" ,"inspectionDate","status"]

    def get_status(self,obj):
        return "saved"