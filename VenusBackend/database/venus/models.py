from django.db import models

class tbl_project(models.Model):
    name = models.CharField(max_length=100)
    client_name = models.CharField(max_length=50)
    country = models.CharField(max_length=20)
    contact = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    status = models.IntegerField()


class tbl_payment(models.Model):
    project_id = models.IntegerField()
    amount = models.FloatField()
    date = models.DateField()
    for_plan = models.IntegerField()
    is_directly = models.IntegerField()
    note = models.TextField(blank=True, null=True)