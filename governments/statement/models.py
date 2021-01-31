from django.db import models
import uuid

HOMEWORK_CHECKED = [
    ('SUBMIT', 'Submit'),
    ('NOT_SUBMIT', 'Not_Submit'),
    ('LATE_SUBMIT', 'Late_Submit'),
]


class TimeStampModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Homework(TimeStampModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    name = models.CharField(max_length=50)
    end_time = models.DateTimeField()

    def __str__(self):
        return '{}'.format(self.name)


class Checked(TimeStampModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    student_email = models.EmailField(max_length=100)
    homework_name = models.ForeignKey('Homework', related_name='checked_homework_name',on_delete=models.CASCADE,
                                      db_column='name')
    state = models.CharField()