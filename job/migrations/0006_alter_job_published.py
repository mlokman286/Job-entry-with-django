# Generated by Django 5.0 on 2024-01-04 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_alter_job_company_alter_job_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='published',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
