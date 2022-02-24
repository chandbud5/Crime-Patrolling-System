from django.contrib import auth
from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import auth
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import User_DB, User
from police_panel.models import Complaint
# Create your views here.
def index(request):
    return HttpResponse("You are in User panel")

@csrf_exempt
@api_view(['POST'])
def registerUser(request):
    response = {}
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    email_id = request.POST.get("email_id")
    contact_number = request.POST.get("contact_number")
    aadhar_number = request.POST.get("aadhar_number")
    address = request.POST.get("address")
    password = request.POST.get("password")
    confirm_password = request.POST.get("c_password")

    already_exist = User.objects.filter(username = contact_number).exists()

    if already_exist:
        response["message"] = str(contact_number) + " is already registered try to sign in"
        return Response(response, status = status.HTTP_200_OK)

    if password == confirm_password:
        user = User.objects.create_user(username=contact_number, email = email_id, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user_db_obj = User_DB.objects.create(contact_number = contact_number, aadhar_number = aadhar_number, user = user)
        user_db_obj.first_name = first_name
        user_db_obj.last_name = last_name
        user_db_obj.email_id = email_id
        user_db_obj.address = address
        user_db_obj.save()
        user.save()

        response["message"] = "User Registered to the system"
        return Response(response, status = status.HTTP_201_CREATED)
    else:
        response["message"] = "Passwords do not match"
        return Response(response, status = status.HTTP_406_NOT_ACCEPTABLE)

@csrf_exempt
@api_view(['POST'])
def logout(request):
    auth.logout(request)
    return Response({"message": "User Log out"}, status = status.HTTP_200_OK)

@csrf_exempt
@api_view(["POST"])
def login(request):
    response = {}
    if request.method =='POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            response["message"] = "Login Successful"
            return Response(response, status=status.HTTP_202_ACCEPTED)
        else:
            response["message"] = "Invalid Credentials Login Failed Please try again"
            return Response(response, status=status.HTTP_401_UNAUTHORIZED)

@csrf_exempt
@api_view(["POST"])
def create_complaint(request):
    response = {}
    if request.method == "POST" and request.user.is_authenticated:
        response["method"] = "POST"
        crime_title = request.POST.get("crime_title")
        threat = request.POST.get("threat")
        crime_description = request.POST.get("crime_description")
        longitude = request.POST.get("longitude")
        latitude = request.POST.get("latitude")
        user = request.user

        complain_obj = Complaint.objects.create(complainee = request.user, longitude = longitude, latitude = latitude)
        complain_obj.complainee = user
        complain_obj.crime_title = crime_title
        complain_obj.threat = threat
        complain_obj.crime_description = crime_description
        complain_obj.latitude = latitude
        complain_obj.longitude = longitude
        complain_obj.save()
        response["message"] = crime_title + " Complaint Registered"

    elif request.method != "POST":
        response["method"] = "GET"
        response["message"] = "Invalid Request"
    elif request.user.is_authenticated != True:
        response["message"] = "Unauthorized User"
    return Response(response)