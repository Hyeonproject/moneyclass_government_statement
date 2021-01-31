# Generated by Django 3.1.5 on 2021-01-31 17:54

from django.db import migrations, models
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
                ('id', models.UUIDField(default=uuid.UUID('0fe23380-f00f-40b5-8089-5fa75e3f9faf'), primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('end_time', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
