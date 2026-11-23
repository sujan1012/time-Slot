from django.db import models

# Create your models here.
class TimeSlot(models.Model):
    DAYS = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
    ]
    day = models.CharField(max_length=15,choices=DAYS)
    start_time= models.TimeField()
    end_time=models.TimeField()
    subject_name =models.CharField(max_length=100)
    faculty_name=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.day} - {self.subject_name}"

    