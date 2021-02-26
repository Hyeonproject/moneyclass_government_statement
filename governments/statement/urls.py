from django.urls import path

from .views import HomeworkView, HomeworkDetailView

urlpatterns = [
    path('', HomeworkView.as_view(), name='homework'),
    path('<uuid:pk>', HomeworkDetailView.as_view(), name='homework_detail'),
]