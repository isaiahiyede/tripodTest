from django.db import models
import datetime


# Create your models here.


'''
	generic model that can be abstracted by other models
'''

class GeneralInfo(models.Model):
	name = models.CharField(max_length=50, null=True, blank=True)
	email = models.CharField(max_length=50, null=True, blank=True)
	phone_number = models.CharField(max_length=50, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class EmployeeInfo(GeneralInfo):
    department = models.CharField(max_length=50, null=True, blank=True)
    employee_id = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return (f"{self.employee_id}")


