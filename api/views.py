from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from InspectionData.models import *
# Create your views here



# Wheel Specifications API handling
class Wheel_Specifications(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    # it handle GET request to Wheel Specifications with parameters -> formNumber, submittedBy, submittedDate.
    def get(self, request):
        query_params = request.query_params
        print(request.user)
        query_set = Wheel_Specification_Form.objects.filter(formNumber = query_params['formNumber'], submittedBy= query_params['submittedBy'], submittedDate= query_params['submittedDate'])    # Update this line as per query parameters
        if not query_set.exists():
            return Response({
                'status' : 'No Data Found'
            },status=status.HTTP_204_NO_CONTENT)
        
        serialized_data = GET_WheelSpecificationsFormSerializers(query_set, many = True)    # Make JSON Formate using serializer
        
        content = {
            "success": True,
            "message" : "Filtered wheel specification forms fetched successfully.",
            "data" : serialized_data.data
        }
        
        return Response(content,status=status.HTTP_200_OK)     # Successfullly Return Data
    
    
    # it handle POST request to Wheel Specifications (I assumed that all data fields provided by front-end).
    def post(self, request):
        data = request.data
        
        if Wheel_Specification_Form.objects.filter(formNumber = data['formNumber']).exists():   # Handle if formNumber exist previously if same formNumber can be more than one
            return Response({
                    'status' : 'formNumber already Exist.'
                },status=status.HTTP_208_ALREADY_REPORTED)
            
        wheel_field = WheelDataFieldsSeralizers(data=data["fields"])    # Serialized the wheel specification data fields as obj structure.
        if (wheel_field.is_valid()) == False:       # if we get invalid data Return Error.
            return Response(wheel_field.errors)
        info = wheel_field.save()                   # First we save the wheel infos about wheel then we map the foregin key with main Form table
        
        data["fields"] = info.id                    # map the primary key of wheel info table
        wheel_data_form = WheelSpecificationsFormSerializers(data = data)       # 
        if wheel_data_form.is_valid() == False:     # if we get invalid data Return Error.
            return Response(wheel_data_form.errors)
        new_wheel = wheel_data_form.save()      # if valid then save
        
        responce_data = POST_WheelResponceSerializers(new_wheel)
        
        content = {
            "success" : True,
            "message" : "Wheel specification submitted successfully.",
            "data" : responce_data.data
        }
        return Response(content, status=status.HTTP_201_CREATED)       # Successfullly Return Data

#----------------------------------------------------------------------------------------------------------------------------


# Bogie Checksheet API handling
class Bogie_Checksheet(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    # it handle GET request to Wheel Specifications with parameters -> formNumber, inspectionBy, inspectionDate.
    def get(self, request):
        
        query_params = request.query_params
        query_set = Bogie_Check_Sheet_Form.objects.filter(formNumber = query_params['formNumber'], inspectionBy = query_params['inspectionBy'], inspectionDate = query_params['inspectionDate'])
        
        if not query_set.exists():
            return Response({
                'status' : 'No Data Found'
            },status=status.HTTP_204_NO_CONTENT)
        serialized_data = GET_BogieCheckSheetFormSerializers(query_set, many = True)        # Make JSON Formate using serializer
        
        content = {
            "success": True,
            "message" : "Filtered bogie checksheet forms fetched successfully.",
            "data" : serialized_data.data
        }
        return Response( content, status=status.HTTP_200_OK)     # Successfullly Return Data


    # it handle POST request to Bogie Checksheet.
    def post(self, request):
        data = request.data
        
        if Bogie_Check_Sheet_Form.objects.filter(formNumber = data['formNumber']).exists():         # Handle if formNumber already exist
            return Response({
                    'status' : 'formNumber already Exist.'
                },status=status.HTTP_208_ALREADY_REPORTED)      # If form Number Already exist.
        
        bogie_details = BogieDetailsSerializers(data=data['bogieDetails'])
        if bogie_details.is_valid() == False:
            return Response(bogie_details.errors)
        bogie_details = bogie_details.save()            # Create new bogie_details instance
        
        bogie_check_sheet = BogieChecksheetSerializers(data = data['bogieChecksheet'])
        if bogie_check_sheet.is_valid() == False:
            return Response(bogie_check_sheet.errors)
        bogie_check_sheet = bogie_check_sheet.save()    # Create new bogie_check_sheet instance
        
        bmbc_check_sheet = bmbcChecksheetSerializers(data = data['bmbcChecksheet'])
        if bmbc_check_sheet.is_valid() == False:
            return Response(bmbc_check_sheet.errors)
        bmbc_check_sheet = bmbc_check_sheet.save()      # Create new bmbc_check_sheet instance
        
        
        data['bogieDetails'] = bogie_details.id
        data['bogieChecksheet'] = bogie_check_sheet.id          # map ids of foreign tables with foreign key
        data['bmbcChecksheet'] = bmbc_check_sheet.id
        
        bogie_data_form = BogieCheckSheetFormSerializers(data = data)
        if bogie_data_form.is_valid() == False:
            return Response(bogie_data_form.errors)
        
        new_bogie_data = bogie_data_form.save()          # Create the Bogie_Checksheet form instance.
        
        responce_data = POST_BogieResponceSerializers(new_bogie_data)
        
        content = {
            "success" : True,
            'message' : "Bogie checksheet submitted successfully.",
            'resultResponce' : responce_data.data
        }
        
        return Response(content, status=status.HTTP_201_CREATED)       # Successfullly Return Data