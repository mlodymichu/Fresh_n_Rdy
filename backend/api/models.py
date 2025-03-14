from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    class Role(models.TextChoices):
        Admin = "ADMIN", "Admin"
        Building_manager = "MANAGER", "Manager"
        Janitor = "JANITOR", "Janitor"
        Cleaning_staff = "CLEANING", "Cleaning_staff" #TODO: ZMIENIC NAZWE
        Employee = "EMPLOYEE", "Employee"

    base_role = Role.Admin

    role = models.CharField(
        max_length=50,
        choices=Role.choices,
        )
    
    def save(self,*args,**kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args,**kwargs)

class Building(models.Model):
    name = models.CharField(max_length=250)
    is_private = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
class Toilet(models.Model):
    building_id = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='toilets')
    
    def __str__(self):
        return self.pk
    
class Cabin(models.Model):
    toilet_id = models.ForeignKey(Toilet, on_delete=models.CASCADE, related_name='cabins')
    
    def __str__(self):
        return self.pk

class MalfunctionStatus(models.TextChoices):
    WAITING = 'WAI', 'Waiting'
    RESOLVED = 'RES', 'Resolved'
    REJECTED = 'REJ', 'Rejected'

class MalfunctionType(models.TextChoices):
    HYGENIC = 'H', 'Hygenic'
    TECHNICAL = 'T', 'Technical'

class Malfunction(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField()
    cabin_id = models.ForeignKey(Cabin, on_delete=models.CASCADE, related_name='malfunctions')
    toilet_id = models.ForeignKey(Toilet, on_delete=models.CASCADE, related_name='malfunctions')
    status = models.CharField(
        max_length=3,
        choices=MalfunctionStatus.choices,
        default=MalfunctionStatus.WAITING,
        )
    malfunction_type = models.CharField(
        max_length=1,
        choices=MalfunctionType.choices,
        default=MalfunctionType.HYGENIC,
        )
    issue = models.TextField(max_length=200)
    