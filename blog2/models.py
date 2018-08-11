from django.db import models

class students(models.Model):
    student_id=models.CharField(max_length=32,default='True')
    student_name=models.TextField(null=True)
