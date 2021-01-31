# Generated by Django 3.1.5 on 2021-01-31 15:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('statement', '0003_auto_20210201_0024'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checked',
            old_name='homework',
            new_name='homework_name',
        ),
        migrations.AlterField(
            model_name='checked',
            name='id',
            field=models.UUIDField(default=uuid.UUID('6e5bca6a-fc9e-4fb2-a067-34d21d0df274'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='checked',
            name='state',
            field=models.CharField(choices=[('SUBMIT', 'Submit'), ('NOT_SUBMIT', 'Not_Submit'), ('LATE_SUBMIT', 'Late_Submit')], default='NOT_SUBMIT', help_text='과제상태', max_length=11),
        ),
        migrations.AlterField(
            model_name='homework',
            name='id',
            field=models.UUIDField(default=uuid.UUID('f5ee71e8-b245-48e9-8e8d-6dfebc70aae4'), primary_key=True, serialize=False),
        ),
    ]
