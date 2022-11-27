from django.db import  models
from django.contrib.auth.models import User



class Appointment(models.Model):
          user = models.ForeignKey(User, on_delete = models.CASCADE,null=True)
          name = models.CharField(max_length=200)
          number = models.CharField(max_length=200)
          service = models.CharField(max_length=200)
          doctor = models.CharField(max_length=200)
          time = models.CharField(max_length=200)
          date = models.CharField(max_length=200)
          
          
          def __self__(self):
                    return self.name