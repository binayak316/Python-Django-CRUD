from django.db import models

# Create your models here.

class Employee(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    emp_name = models.CharField(max_length=100)
    emp_email = models.EmailField()
    emp_contact = models.CharField(max_length=20)
    emp_role = models.CharField(max_length=200)
    emp_salary = models.IntegerField()

    def __str__(self):
        return f"{self.id}:{self.emp_name}"
        # return self.emp_name

