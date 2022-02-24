from http.client import CannotSendRequest
import imp
from django.http import response
from django.shortcuts import render, HttpResponse
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import auth
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Police_DB, Complaint, User, Reports
# Create your views here.
def index(request):
    return HttpResponse("You are in police panel")

## POLICE WILL BE ADDED FROM ADMIN PANEL ONLY NO NEED TO REGISTER FROM USER SIDE
# @api_view(["POST"])
# def register(request):
#     first_name = request.POST.get("first_name")
#     last_name = request.POST.get("last_name")
#     police_id = request.POST.get("police_id")
#     email_id = request.POST.get("email_id")
#     contact_number = request.POST.get("contact_number")
#     password = request.POST.get("password")
#     confirm_password = request.POST.get("c_password")
#     response = {}
#     already_exist = User.objects.filter(username = police_id).exists()

#     if already_exist:
#         response["message"] = str(police_id) + " is already registered try to sign in"
#         return Response(response, status = status.HTTP_200_OK)

#     if password == confirm_password:
#         user = User.objects.create_user(username=police_id, email = email_id, password=password)
#         user.first_name = first_name
#         user.last_name = last_name
#         user.save()
    
#         police_obj = Police_DB.objects.create(user = user, contact_number = contact_number, email_id = email_id, police_id = police_id)
#         police_obj.first_name = first_name
#         police_obj.last_name = last_name
#         police_obj.save()
        
#         response["message"] = "Police Registered to the system"
#         return Response(response, status = status.HTTP_201_CREATED)
#     else:
#         response["message"] = "Passwords do not match"
#         return Response(response, status = status.HTTP_406_NOT_ACCEPTABLE)

@csrf_exempt
@api_view(["GET"])
def view_complaints(request):
    response = {}
    registered_police = Police_DB.objects.filter(user = request.user).exists()
    print(registered_police)
    if request.user.is_authenticated and registered_police:
        complaints = list(Complaint.objects.values())
        response["data"] = complaints
        return Response(response, status = status.HTTP_200_OK)
    else:
        response["message"] = "Please login to continue or you might not have access to this details"
        return Response(response, status = status.HTTP_401_UNAUTHORIZED)

@csrf_exempt
@api_view(['POST'])
def report(request, id):
    response = {}
    exits = Police_DB.objects.filter(user = request.user).exists()
    if request.user.is_authenticated and exits:
        description = request.POST.get("description")
        comments = request.POST.get("comments")
        police_officer = Police_DB.objects.get(user = request.user)
        complaint = Complaint.objects.get(id = id)
        report_obj = Reports.objects.create(complaint = complaint, officer_incharge = police_officer)
        report_obj.report_description = description
        report_obj.comment = comments
        report_obj.save()
        complaint.status = "Reported"
        complaint.save()
        response["message"] = "Report filed"
        return Response(response, status = status.HTTP_201_CREATED)
    else:
        response["message"] = "You are not authorized for this action"
        return Response(response, status = status.HTTP_401_UNAUTHORIZED)

# @csrf_exempt
@api_view(['POST'])
def complaint_accepted(request, id):
    response = {}
    exits = Police_DB.objects.filter(user = request.user.id).exists()
    if request.user.is_authenticated and exits:
        police_officer = Police_DB.objects.get(user = request.user)
        complaint = Complaint.objects.get(id = id)
        complaint.status = "In Progress"
        complaint.police_assigned = police_officer
        complaint.save()
        response["message"] = "Police taking action on complaint registered"
        return Response(response, status = status.HTTP_200_OK)
    else:
        response["message"] = "You are not authorized for this action"
        return Response(response, status = status.HTTP_401_UNAUTHORIZED)
