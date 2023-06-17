from django.db import models


class tasks(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    time = models.TimeField(auto_now=True)
    status = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tasks'
