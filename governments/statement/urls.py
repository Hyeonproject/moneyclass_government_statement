from django.urls import path, include

from .views import HomeworkView, HomeworkDetailView

urlpatterns = [
    path('', HomeworkView.as_view(), name='homework'),
    path('<uuid:id>', HomeworkDetailView.as_view(), name='homework_detail'),
]