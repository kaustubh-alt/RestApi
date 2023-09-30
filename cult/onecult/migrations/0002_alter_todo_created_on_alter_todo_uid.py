# Generated by Django 4.2.3 on 2023-08-10 11:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('onecult', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_on',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('a7825787-30af-47b0-a0eb-d45b2e180db1'), editable=False, primary_key=True, serialize=False),
        ),
    ]
