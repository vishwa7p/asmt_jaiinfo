from django.shortcuts import render

# Create your views here.

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import EmployeeSerializer
from .models import Employee


class EmployeeCreateApi(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeListApi(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDeleteApi(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


# '''I have also done in alternate method do please check if possible'''


# class EmployeeCreate(APIView):
#     def post(self, request):
#         try:
#             json_data = request.data
#             self.emp_id = json_data['employee_id']
#             self.emp_name = json_data['employee_name']
#             self.emp_email = json_data['employee_email']
#             self.emp_mobile = json_data['employee_mobile']
#             self.emp_address = json_data['employee_address']
#         except Exception as e:
#             print(e)
#             return Response('json_key_error', status=status.HTTP_406_NOT_ACCEPTABLE)
#         employee = Employee(employee_id=self.emp_id, employee_name=self.emp_name, employee_email=self.emp_email,
#                             employee_mobile=self.emp_mobile, employee_address=self.emp_address)
#         employee.save()
#         response_data = {"Status": "Success",
#                          "message": "employee created successfully"}
#         return Response(response_data, status=status.HTTP_200_OK)
#
#
# class EmployeeUpdate(APIView):
#     def post(self, request, pk):
#         try:
#             json_data = request.data
#             self.emp_id = json_data['employee_id']
#             self.emp_name = json_data['employee_name']
#             self.emp_email = json_data['employee_email']
#             self.emp_mobile = json_data['employee_mobile']
#             self.emp_address = json_data['employee_address']
#         except Exception as e:
#             print(e)
#             return Response('json_key_error', status=status.HTTP_406_NOT_ACCEPTABLE)
#         try:
#             emp = Employee.objects.get(pk=pk)
#             emp.employee_name = self.emp_name
#             emp.employee_email = self.emp_email
#             emp.employee_mobile = self.emp_mobile
#             emp.employee_address = self.emp_address
#             emp.save()
#             response_data = {"Status": "Success",
#                              "message": "updated successfully",
#                              "data": {}}
#             return Response(response_data, status=status.HTTP_200_OK)
#
#         except Exception as e:
#             print(e)
#         response_data = {"Status": "Failure",
#                          "message": "Invalid",
#                          "data": {}}
#         return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
#
#
# class EmployeeDelete(APIView):
#     def post(self, request, pk):
#         json_data = request.data
#         self.group = json_data['group']
#         if self.group == "admin":
#             try:
#                 emp = Employee.objects.get(pk=pk)
#                 emp.delete()
#                 response_data = {"Status": "Success",
#                                  "message": "deleted successfully",
#                                  "data": {}}
#                 return Response(response_data, status=status.HTTP_200_OK)
#             except Exception as e:
#                 print(e)
#                 response_data = {"Status": "Failure",
#                                  "message": "Invalid",
#                                  "data": {}}
#                 return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
#
#
# class EmployeeList(APIView):
#     def get(self, request):
#         employee = Employee.objects.all()
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data)
