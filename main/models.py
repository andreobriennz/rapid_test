from django.db import models

# Create your models here.
class PerformanceData(models.Model):
    page_name = models.CharField(max_length=200)
    data = models.TextField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return str(self.pub_date) + ' (' + self.page_name + ')'