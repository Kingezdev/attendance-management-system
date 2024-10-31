from django.db import models

class Attendance(models.Model):
    STATUS_CHOICES = [
        ('present', 'present'),
        ('absent', 'absent'),
    ]

    student_name = models.CharField(max_length=100)
    matric_number = models.CharField(max_length=100, default="2655")

    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.student_name} - {self.status} - {self.date}"
