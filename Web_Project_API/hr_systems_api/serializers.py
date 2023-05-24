from rest_framework import serializers
from .models import Employee
from .models import Vacation


class EmployeeVacationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vacation
        fields = ['id', 'reason', 'date_from', 'date_to', 'status']


class EmployeeSerializers(serializers.ModelSerializer):
    vacations=EmployeeVacationSerializers(many=True)
    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', 'phoneNumber', 'dateOfBirth', 'dateOfBirth', 'gender', 'maritalStatus',
                  'address', 'availableVacations', 'salary','vacations']


class AddEmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', 'phoneNumber', 'dateOfBirth', 'dateOfBirth', 'gender', 'maritalStatus',
                  'address', 'availableVacations', 'salary']


class VacationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vacation
        fields = ['id', 'reason', 'date_from', 'date_to', 'status', 'employee']
        depth = 1


class AddVacationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vacation
        fields = ['id', 'reason', 'date_from', 'date_to', 'status', 'employee']


class UpdateVacationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vacation
        fields = ['status']
