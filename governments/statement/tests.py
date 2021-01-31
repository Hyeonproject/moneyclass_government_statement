from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.core.exceptions import ImproperlyConfigured
import json,os

from .models import Homework

key_file = os.path.join()

with open('key.json') as f:
    key = json.loads(f.read())


def get_key(setting, key=key):
    try:
        return key[setting]
    except KeyError:
        error_msg = '{0}값을 불러오지 못했습니다.'.format(setting)
        raise ImproperlyConfigured(error_msg)

class HomeworkTests(APITestCase):
    def setUp(self) -> None:
        self.token_teacher = get_key('teacher_token')
        self.test_homework_1 = Homework.objects.create(
            name='4주차 일기 검사', end_time='2021-02-01'
        )
        self.test_homework_2 = Homework.objects.create(
            name='수학익힘책 풀어오기', end_time='2021-02-5'
        )

    def test_create_homework(self):
        """
        숙제를 등록하는 기능을 테스트합니다.
        """
        url = reverse('homework')
        data = {
            'homework': '자신의 꿈을 생각하기',
            'end_time': '2021-02-15'
        }
        self.client.session.headers.update(
            {'Authorization': 'Bearer {}'.format(self.token_teacher)}
        )
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Homework.objects.count(), 3)
        self.assertEqual(Homework.objects.get(name='자신의 꿈을 생각하기'), '자신의 꿈을 생각하기')

    def test_read_homeworks(self):
        """
        전체 숙제를 보여주는 기능을 테스트 합니다.
        """
        url = reverse('homework')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Homework.objects.count(), 2)

    def test_read_homework(self):
        url = reverse('homeowork') + '/{}'.format(self.test_homework_1.id)
        response = self.client.get(url)

    def test_update_homework(self):
        """
        숙제 데이터를 변경합니다.
        """
        url = reverse('homework')
        data = {
            'homework': '1주차 일기 검사',
            'end_time': '2021-02-10'
        }
        self.client.session.headers.update(
            {'Authorization': 'Bearer {}'.format(self.token_teacher)}
        )
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Homework.objects.count(), 2)
        self.assertEqual(Homework.objects.get(name='4주차 일기 검사'))

    def test_delete_homework(self):
        """
        과제를 삭제합니다.
        """
        url = reverse('homework')
        self.client.session.headers.update(
            {'Authorization': 'Bearer {}'.format(self.token_teacher)}
        )
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Homework.objects.count(), 2)