from django.db import models

# Create your models here.
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
    