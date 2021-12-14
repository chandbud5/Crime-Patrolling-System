from django.http import response
from django.shortcuts import render, HttpResponse
from django.contrib import auth
from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import auth
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Police_DB, Complaint, User
# Create your views here.
def index(request):
    return HttpResponse("You are in police panel")

@api_view(["POST"])
def register(request):
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    police_id = request.POST.get("police_id")
    email_id = request.POST.get("email_id")
    contact_number = request.POST.get("contact_number")
    password = request.POST.get("password")
    confirm_password = request.POST.get("c_password")
    response = {}
    already_exist = User.objects.filter(username = police_id).exists()

    if already_exist:
        response["message"] = str(police_id) + " is already registered try to sign in"
        return Response(response, status = status.HTTP_200_OK)

    if password == confirm_password:
        user = User.objects.create_user(username=police_id, email = email_id, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
    
        police_obj = Police_DB.objects.create(user = user, contact_number = contact_number, email_id = email_id, police_id = police_id)
        police_obj.first_name = first_name
        police_obj.last_name = last_name
        police_obj.save()
        
        response["message"] = "Police Registered to the system"
        return Response(response, status = status.HTTP_201_CREATED)
    else:
        response["message"] = "Passwords do not match"
        return Response(response, status = status.HTTP_406_NOT_ACCEPTABLE)

@api_view(["GET"])
def view_reports(request):
    response = {}
    registered_police = Police_DB.objects.filter(police_id = request.user.username).exists()
    if request.user.is_authenticated and registered_police:
        complaints = list(Complaint.objects.values())
        response["data"] = complaints
        return Response(response)
    else:
        response["message"] = "Please login to continue or you might not have access to this details"
        return Response(response)