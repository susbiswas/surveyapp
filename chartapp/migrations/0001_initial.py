# Generated by Django 3.1.7 on 2021-03-24 00:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthIssue',
            fields=[
                ('health_issue_id', models.AutoField(db_column='health_issue_id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='name', max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Vaccination_Status',
            fields=[
                ('vaccine_status_id', models.AutoField(db_column='vaccine_status_id', primary_key=True, serialize=False)),
                ('first_dose', models.CharField(choices=[('0', 'Yes'), ('1', 'No')], db_column='first_dose', max_length=1)),
                ('fully_vaccinated', models.CharField(choices=[('0', 'Yes'), ('1', 'No')], db_column='fully_vaccinated', max_length=1)),
                ('cid', models.ForeignKey(db_column='cid', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Prevaccine_Health_Issue',
            fields=[
                ('prevaccine_health_issue', models.AutoField(db_column='prevaccine_health_issue', primary_key=True, serialize=False)),
                ('cid', models.ForeignKey(db_column='cid', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('health_issue_id', models.ForeignKey(db_column='health_issue_id', on_delete=django.db.models.deletion.CASCADE, to='chartapp.healthissue')),
            ],
        ),
        migrations.CreateModel(
            name='Postvaccine_Health_Issue',
            fields=[
                ('postvaccine_health_issue', models.AutoField(db_column='postvaccine_health_issue', primary_key=True, serialize=False)),
                ('cid', models.ForeignKey(db_column='cid', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('health_issue_id', models.ForeignKey(db_column='health_issue_id', on_delete=django.db.models.deletion.CASCADE, to='chartapp.healthissue')),
            ],
        ),
    ]