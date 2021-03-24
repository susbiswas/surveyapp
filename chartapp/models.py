from django.db import models
from django.db.models.deletion import CASCADE

# NOTE: CustomUser is in ./users/models.py
from users.models import CustomUser

# Create your models here.
class Vaccination_Status(models.Model):
    vaccine_status_id = models.AutoField(primary_key=True, db_column='vaccine_status_id')
    cid = models.ForeignKey(CustomUser, 
                        db_column='cid',
                        on_delete=models.CASCADE)
    first_dose = models.CharField(
        max_length=1,
        choices=[
            ('0',"Yes"),
            ('1',"No")
        ],
        db_column='first_dose'
    )
    fully_vaccinated = models.CharField(
        max_length=1,
        choices=[
            ('0',"Yes"),
            ('1',"No")
        ],
        db_column='fully_vaccinated'
    )

class HealthIssue(models.Model):
    health_issue_id = models.AutoField(primary_key=True, db_column='health_issue_id')
    name = models.CharField(max_length=64,db_column='name')
    
    def __str__(self):
        return self.name

class Prevaccine_Health_Issue(models.Model):
    prevaccine_health_issue = models.AutoField(primary_key=True, db_column='prevaccine_health_issue')
    cid = models.ForeignKey(CustomUser, 
                        db_column='cid',
                        on_delete=CASCADE)
    health_issue_id = models.ForeignKey(HealthIssue, db_column='health_issue_id', on_delete=CASCADE)
    
class Postvaccine_Health_Issue(models.Model):
    postvaccine_health_issue = models.AutoField(primary_key=True, db_column='postvaccine_health_issue')
    cid = models.ForeignKey(CustomUser, 
                        db_column='cid',
                        on_delete=CASCADE)
    health_issue_id = models.ForeignKey(HealthIssue, db_column='health_issue_id', on_delete=CASCADE)
    


