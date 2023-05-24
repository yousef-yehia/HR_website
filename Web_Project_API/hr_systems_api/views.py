from ast import Try
import imp
import logging
from os import stat
from pickle import NONE

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Employee, Vacation
from .serializers import AddEmployeeSerializers, AddVacationSerializers, EmployeeSerializers, UpdateVacationSerializers, VacationSerializers
from django.db.models import Q
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import api_view
import json

# Create your views here.


@api_view(['GET'])
def employee_list_count(request):
    return HttpResponse(Employee.objects.all().count())


@api_view(['GET', 'POST'])
def employee_list(request, query=None):

    if request.method == 'GET':
        employees = Employee.objects.all()
        if query is not None:
            employees = employees.filter(
                Q(name__icontains=query) | Q(email__icontains=query) | Q(phoneNumber__icontains=query))
        serializer = EmployeeSerializers(employees, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AddEmployeeSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def employee_by_id(request, id):
    try:
        employee = Employee.objects.get(pk=id)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EmployeeSerializers(employee, many=False)

    elif request.method == 'PUT':
        serializer = AddEmployeeSerializers(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def vacations_list_count(request):
    all=Vacation.objects.all()
    accepted=Vacation.objects.filter(status='Accepted').count()
    rejected=Vacation.objects.filter(status='Rejected').count()
    submitted=Vacation.objects.filter(status='Submitted').count()
    return Response({"accepted":accepted,"rejected":rejected,"submitted":submitted})


@api_view(['GET', 'POST'])
def vacations_list(request, query=None):

    if request.method == 'GET':
        vacations = Vacation.objects.all()
        if query is not None:
            vacations = vacations.filter(
                Q(reason__icontains=query) | Q(date_from__icontains=query) | Q(date_to__icontains=query) | Q(status__icontains=query))
        serializer = VacationSerializers(vacations, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AddVacationSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def vacations_by_id(request, id):
    try:
        vacation = Vacation.objects.get(pk=id)
    except Vacation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VacationSerializers(vacation, many=False)

    elif request.method == 'PUT':
        serializer = UpdateVacationSerializers(vacation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        vacation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return JsonResponse(serializer.data, safe=False)
