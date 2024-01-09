from django.db import models


class Job(models.Model):
    job_title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    company_location = models.CharField(max_length=255)
    total_salary = models.FloatField()
    City = models.CharField(max_length=255)
    State = models.CharField(max_length=255)
    link = models.URLField()
    
    class Meta:
        db_table = 'pythondeveloper'

    def __str__(self):
        return self.job_title