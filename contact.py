from django.db import  models



class Contact(models.Model):
          name = models.CharField(max_length=200)
          email = models.CharField(max_length=200)
          subject = models.CharField(max_length=200)
          message = models.TextField()
          
          
          def __self__(self):
                    return self.name