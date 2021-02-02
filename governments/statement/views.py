from django.conf import settings
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import jwt

from .models import Homework
from .serializers import HomeworkDataSerializer, HomeworkSerializer, HomeworkPutSerializer,\
    HomeworkDeleteSerializer

def token_testing(self, request):
    token = request.META.get('Authorization').split()[1]
    payload = jwt.decode(token, settings.JWT_PASSWORD, algorithms=[settings.JWT_ALGORITHMS])
    if (payload['authorities'][0] != 'ROLE_TEACHER') and (payload['authorities'][0] != 'ROLE_ADMIN'):
        raise Response({'detail': '권한이 없습니다'}, status=status.HTTP_401_UNAUTHORIZED)

class HomeworkView(APIView):
    """
    숙제 데이터베이스의 CRUD를 담당합니다.
    Read는 전체를 만듭니다.
    """
    def get(self, request):
        token_testing(request)
        homework = Homework.objects.all()
        serializer = HomeworkSerializer(homework, many=True)
        return Response(serializer.data)

    def post(self, request):
        token_testing(request)
        homework_serializer = HomeworkDataSerializer(data=request.data)
        if homework_serializer.is_valid():
            homework_serializer.save()
            return Response(homework_serializer.data, status=status.HTTP_201_CREATED)
        return Response(homework_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request): # Serializer에 무조건 데이터를 다 넣어야하나?
        token_testing(request)
        request_data = HomeworkPutSerializer(data=request.data)
        if request_data.is_valid():
            homework_data = Homework.objects.get(name=request_data.homework)

            if request_data.modified_homework == None:
                homework_data.objects.update(
                    end_time=request_data.modified_end_time
                )
            elif request_data.modified_end_time == None:
                homework_data.objects.update(
                    name=request_data.modified_homework
                )
            else:
                homework_data.objects.update(
                    name=request_data.modified_homework,
                    end_time=request_data.modified_end_time
                )
            homework_serializer = HomeworkSerializer(data=homework_data)
            return Response(homework_serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        token_testing(request)
        homework_serializer = HomeworkDeleteSerializer(request.data)
        if homework_serializer.is_valid():
            Homework.objects.get(name=homework_serializer.homework).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class HomeworkDetailView(APIView):
    """
    숙제 디테일 view : 일부 기능이 겹치지만 사용법이 다릅니다.
    """
    def get_object(self, id):
        try:
            return Homework.objects.get(id=id)
        except Homework.DoesNotExist:
            raise Http404

    def get(self, request, id):
        token_testing(request)
        homework = self.get_object(id)
        homework_serializer = HomeworkSerializer(homework)
        return Response(homework_serializer.data)

    def put(self, request, id):
        token_testing(request)
        homework = self.get_object(id)
        homework_serializer = HomeworkSerializer(homework, data=request.data)
        if homework_serializer.is_valid():
            homework_serializer.save()
            return Response(homework_serializer.data)
        return Response(homework_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        token_testing(request)
        homework = self.get_object(id)
        homework.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






