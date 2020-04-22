from rest_framework import serializers
from .models import *


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = '__all__'


class SprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sprint
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class TeamSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = (
            'name', 'teamLead', 'projectManager', 'costPerHour', 'programers', 'technologyStack', 'participantsNumber')


class ProgSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('fullName', 'salary', 'employmentStatus', 'direction', 'position')

class TaskSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sprint
        fields = ('nameTask', 'priority', 'startDate', 'hoursNumber', 'completionStatus')

class SprintSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sprint
        fields = ('title', 'taskSprint', 'startDateSprint', 'responsible', 'score')
