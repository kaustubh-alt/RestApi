# Generated by Django 4.2.3 on 2023-08-10 11:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('onecult', '0002_alter_todo_created_on_alter_todo_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('13ecef28-0e87-43da-89b7-7a10c191103f'), editable=False, primary_key=True, serialize=False),
        ),
    ]
