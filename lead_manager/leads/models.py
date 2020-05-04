from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Lead(models.Model):
    creation_time = models.DateTimeField('date published', blank=True)
    source = models.CharField(max_length=200)
    contact_person = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    address = models.CharField(max_length=350)
    current_stage = models.CharField(max_length=30)

    def __str__ (self):
        return self.name

class FollowUp(models.Model):
    medium_used = (
        ('call','CALL'),
        ('whatsapp','WHATSAPP'),
        ('email','EMAIL')
    )
    lead_name = models.ForeignKey(Lead, on_delete='DO_NOTHING')
    comment = models.CharField(max_length=500)
    medium_used = models.CharField(max_length=10, choices=medium_used, default='call')
    date_followed = models.DateTimeField('date followed')

    def __str__(self):
        return self.comment
    