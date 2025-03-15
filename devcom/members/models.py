from django.db import models

# Create your models here.
class memberList(models.Model):
    firstName = models.CharField(default="",max_length=255)
    lastName = models.CharField(default="",max_length=255)
    mailId = models.EmailField(default="")
    dateOfJoin = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.firstName}"