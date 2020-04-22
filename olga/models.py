from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from datetime import datetime, date, timedelta

""" User """
class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, name=None, full_name=None, is_active=True, is_staff=None,
                    is_admin=None):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        if not password:
            raise ValueError('The given password must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.staff = is_staff
        user.admin = is_admin
        user.is_active = is_active
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, name=None):
        user = self.create_user(email, name=name, password=password, is_staff=True, is_admin=True)
        return user

    def create_staffuser(self, email, password=None, name=None):
        user = self.create_user(email, name=name, password=password, is_staff=True, is_admin=False)
        return user

class User(AbstractBaseUser):

    email = models.EmailField(unique=True, max_length=250)
    name = models.CharField(max_length=250, blank=True, null=True)
    full_name = models.CharField(max_length=250, blank=True, null=True)
    staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    object = UserManager()

    def __str__(self):
        return self.email

    def get_short_name(self):
        if self.name:
            return self.name
        return self.email

    def get_full_name(self):
        if self.full_name:
            return self.full_name
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        if self.admin:
            return True
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    def save(self, *args, **kwargs):
        if not self.id and not self.staff and not self.admin:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)


""" Вивести інформацію про працівників (ПІБ, дата народження, номер телефону), які мають певний 
    працюють за певною посадою та мають певну дату прийому, та мають досвід роботи більший певного досвіду роботи """

class Employee(models.Model):
    fullName = models.CharField(default='Noname', max_length=100)
    birthDate = models.DateField(null=True)
    telephoneNumber = models.CharField(null=True, max_length=25)
    workExperience = models.IntegerField(default=0)
    position = models.CharField(max_length=100)
    employmentDate = models.DateField(default=date.today())

    def __str__(self):
        return self.fullName

""" Вивести інформацію про ІТ-компанії (назва, керівник, 
    капіталізація, спрямованість), що мають певний рік заснування та певний рейтинг."""

class Company(models.Model):
    name = models.CharField(max_length=200)
    manager = models.ManyToManyField(Employee)
    capitalization = models.FloatField(null=True)
    focus = models.CharField(max_length=200)
    foundationDate = models.DateField(null=True, default=date.today())
    rating = models.FloatField(null=True)

    def __str__(self):
        return self.name

""" Вивести інформацію про офіси (адреса, рік покупки, кількість працівників, графік роботи), що мають певну площу та 
    кількість робочих місць, із них ті, що мають вартість оренди нижче певної вартості оренди. """

class Office(models.Model):
    address = models.CharField(max_length=255)
    purchaseDate = models.DateField(null=True)
    employees = models.IntegerField()
    schedule = models.CharField(max_length=255, null=True)
    area = models.FloatField(null=True)
    jobsNumber = models.IntegerField(null=True)
    priceRent = models.IntegerField()

    def __str__(self):
        return self.address

""" Вивести інформацію про команди (назва, тімлід, проджект-менеджер, вартість роботи за годину, програмісти), 
    що мають певний стек технологій та певну кількість учасників. 

    Вивести інформацію про програмістів (ПІБ, заробітна плата, статус зайнятості), 
    які працюють за певним напрямом та досягли певної позиції.
"""

class Team(models.Model):
    name = models.CharField(max_length=200)
    teamLead = models.CharField(max_length=255)
    projectManager = models.CharField(max_length=255)
    costPerHour = models.FloatField(null=True)
    programers = models.CharField(max_length=255)
    technologyStack = models.CharField(max_length=255)
    participantsNumber = models.IntegerField(default=0)

    fullName = models.CharField(max_length=100, null=False)
    salary = models.FloatField(null=True)
    employmentStatus = models.CharField(max_length=255)
    direction = models.CharField(max_length=255)
    position = models.CharField(max_length=255)

    def __str__(self):
        return self.name

""" Вивести інформацію про проекти (назва, замовник, рівень альтернативності), які мають певну 
    сферу та певний бюджет, із них ті, що мають тривалість коротшу від певної тривалості. """

class Project(models.Model):
    name = models.CharField(max_length=300)
    customer = models.CharField(max_length=300, null=True)
    alternativeLevel = models.CharField(max_length=300, null=True)
    scope = models.CharField(max_length=1000, null=True)
    budget = models.FloatField(null=True)
    duration = models.IntegerField(null=True)

    def __str__(self):
        return self.name

""" Вивести інформацію про задачі (назва, пріоритетність, дата початку), 
    що мають певну кількість годин та мають певний статус виконання.
     
    Вивести інформацію про спрінти (назва, задачі, дата початку), які належать 
    певному відповідальному та мають певну оцінку. """

class Sprint(models.Model):
    title = models.CharField(max_length=500, null=False)
    taskSprint = models.CharField(max_length=255)
    startDateSprint = models.DateField(default=date.today())
    responsible = models.CharField(max_length=255)
    score = models.CharField(max_length=255)

    nameTask = models.CharField(max_length=200)
    priority = models.CharField(max_length=255)
    startDate = models.DateField(null=True, default=None)
    hoursNumber = models.FloatField(null=True)
    completionStatus = models.CharField(max_length=255)
    def __str__(self):
        return self.title
