from rest_framework.response import Response
from .models import *
from .serializers import *
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework import viewsets, mixins, generics

""" Вивести інформацію про працівників (ПІБ, дата народження, номер телефону), які
    працюють за певною посадою та мають певну дату прийому, та мають досвід роботи більший певного досвіду роботи """

class EmployeeQueryset(mixins.UpdateModelMixin, generics.ListCreateAPIView):
    model = Employee

    def get_serializer_class(self):
        return EmployeeSerializer

    def get_queryset(self):
        if self.request.GET.get('position', 'workExperience'):
            return Employee.objects.all().filter(
                position=self.request.GET.get('position'), workExperience=self.request.GET.get('workExperience'))

""" Вивести інформацію про ІТ-компанії (назва, керівник, 
    капіталізація, спрямованість), що мають певний рік заснування та певний рейтинг."""

class CompanyQueryset(mixins.UpdateModelMixin, generics.ListCreateAPIView):
    model = Company

    def get_serializer_class(self):
        return CompanySerializer

    def get_queryset(self):
        if self.request.GET.get('foundationDate', 'rating'):
            return Company.objects.all().filter(foundationDate=self.request.GET.get('foundationDate'),
                                                rating=self.request.GET.get('rating'))

""" Вивести інформацію про офіси (адреса, рік покупки, кількість працівників, графік роботи), що мають певну площу та 
    кількість робочих місць, із них ті, що мають вартість оренди нижче певної вартості оренди. """

class OfficeQueryset(mixins.UpdateModelMixin, generics.ListCreateAPIView):
    model = Office

    def get_serializer_class(self):
        return OfficeSerializer

    def get_queryset(self):
        if self.request.GET.get('area','priceRent'):
            return Office.objects.all().filter(area=self.request.GET.get('area'),
                                               priceRent=self.request.GET.get('priceRent'),
                                               jobsNumber__lte=self.request.GET.get('jobsNumber'))

""" Вивести інформацію про проекти (назва, замовник, рівень альтернативності), 
    які мають певну сферу та певний бюджет, із них ті, 
    що мають тривалість коротшу від певної тривалості. """

class ProjectQueryset(mixins.UpdateModelMixin, generics.ListCreateAPIView):
    model = Project

    def get_serializer_class(self):
        return ProjectSerializer

    def get_queryset(self):
        if self.request.GET.get('scope', 'budget'):
            return Project.objects.all().filter(scope=self.request.GET.get('scope'),
                                                budget=self.request.GET.get('budget'),
                                                duration__lte=self.request.GET.get('duration'))

""" Вивести інформацію про команди (назва, тімлід, проджект-менеджер, вартість роботи за годину, програмісти), 
    що мають певний стек технологій та певну кількість учасників. """

class TeamQueryset(mixins.UpdateModelMixin, generics.ListCreateAPIView):
    model = Team

    def get_serializer_class(self):
        return TeamSetSerializer

    def get_queryset(self):
        if self.request.GET.get('technologyStack', 'participantsNumber'):
            return Team.objects.all().filter(technologyStack=self.request.GET.get('technologyStack'),
                                             participantsNumber=self.request.GET.get('participantsNumber'))

""" Вивести інформацію про програмістів (ПІБ, заробітна плата, статус зайнятості), 
    які працюють за певним напрямом та досягли певної позиції.
"""

class ProgQueryset(mixins.UpdateModelMixin, generics.ListCreateAPIView):
    model = Team

    def get_serializer_class(self):
        return ProgSetSerializer

    def get_queryset(self):
        if self.request.GET.get('direction', 'position'):
            return Team.objects.all().filter(direction=self.request.GET.get('direction'),
                                             position=self.request.GET.get('position'))

""" Вивести інформацію про задачі (назва, пріоритетність, дата початку), 
    що мають певну кількість годин та мають певний статус виконання."""

class TaskQueryset(mixins.UpdateModelMixin, generics.ListCreateAPIView):
    model = Sprint

    def get_serializer_class(self):
        return TaskSetSerializer

    def get_queryset(self):
        if self.request.GET.get('hoursNumber', 'completionStatus'):
            return Sprint.objects.only('nameTask', 'priority', 'startDate', 'hoursNumber', 'completionStatus')\
                .filter(hoursNumber=self.request.GET.get('hoursNumber'),
                                             completionStatus=self.request.GET.get('completionStatus'))

""" Вивести інформацію про спрінти (назва, задачі, дата початку), які належать 
    певному відповідальному та мають певну оцінку. """

class SprintQueryset(mixins.UpdateModelMixin, generics.ListCreateAPIView):
    model = Sprint

    def get_serializer_class(self):
        return SprintSetSerializer

    def get_queryset(self):
        if self.request.GET.get('responsible', 'score'):
            return Sprint.objects.all().filter(responsible=self.request.GET.get('responsible'),
                                             score=self.request.GET.get('score'))


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class OfficeViewSet(viewsets.ModelViewSet):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class SprintViewSet(viewsets.ModelViewSet):
    queryset = Sprint.objects.all()
    serializer_class = SprintSerializer
