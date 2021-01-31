# Generated by Django 3.1.5 on 2021-01-31 17:55

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('statement', '0002_auto_20210201_0254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='id',
            field=models.UUIDField(default=uuid.UUID('1045daf9-150b-45da-a51d-656435e20f00'), primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Checked',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.UUID('606af8c0-d7a7-4e5d-af2c-6d6c8f73071e'), primary_key=True, serialize=False)),
                ('student_email', models.EmailField(max_length=75, unique=True)),
                ('state', models.CharField(choices=[('SUBMIT', 'Submit'), ('NOT_SUBMIT', 'Not_Submit'), ('LATE_SUBMIT', 'Late_Submit')], default='NOT_SUBMIT', max_length=20)),
                ('homework_name', models.ForeignKey(db_column='name', on_delete=django.db.models.deletion.CASCADE, related_name='homework_name', to='statement.homework')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
