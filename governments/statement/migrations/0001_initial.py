# Generated by Django 3.1.5 on 2021-01-31 15:16

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.UUID('447eed79-3593-4933-8a1d-3fce95918e72'), primary_key=True, serialize=False)),
                ('name', models.TextField(help_text='숙제명')),
                ('end_time', models.DateTimeField(help_text='마감시간')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Checked',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.UUID('32542a26-109a-4c6f-85d0-30326a247e13'), primary_key=True, serialize=False)),
                ('student_email', models.EmailField(max_length=254, unique=True)),
                ('state', models.CharField(choices=[('SUBMIT', 'Submit'), ('NOT_SUBMIT', 'Not_Submit'), ('LATE_SUBMIT', 'Late_Submit')], default='NOT_SUBMIT', max_length=15)),
                ('homework', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='statement.homework')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
