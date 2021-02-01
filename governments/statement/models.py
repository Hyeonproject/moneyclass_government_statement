from django.db import models
import uuid

HOMEWORK_CHECKED = [
    ('SUBMIT', 'Submit'),
    ('NOT_SUBMIT', 'Not_Submit'),
    ('LATE_SUBMIT', 'Late_Submit'),
]

class TimeStamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Homework(TimeStamp):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=True)
    name = models.CharField(max_length=50)
    end_time = models.DateTimeField()

    def __str__(self):
        return '{}'.format(self.name)


class Checked(TimeStamp):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    student_email = models.EmailField(max_length=75, unique=True)
    homework_name = models.ForeignKey('Homework', on_delete=models.CASCADE,
                                      related_name='homework_name', db_column='name')
    state = models.CharField(max_length=20, choices=HOMEWORK_CHECKED, default='NOT_SUBMIT')

    def __str__(self):
        return '{}님의 {}과제'.format(self.student_email, self.homework_name)