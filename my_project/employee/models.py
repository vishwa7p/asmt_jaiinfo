from django.db import models

# Create your models here.


class Employee(models.Model):
    employee_id = models.CharField(max_length=200, unique=True)
    employee_name = models.CharField(max_length=200, null=True)
    employee_email = models.EmailField(null=True)
    employee_mobile = models.TextField(null=True)
    employee_address = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.employee_name)

