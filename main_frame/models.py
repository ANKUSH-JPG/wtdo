from django.db import models

class add_task(models.Model):
    id=models.IntegerField(primary_key=True)
    task=models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    dateTime=models.DateTimeField()

    def __str__(self):
        return self.task