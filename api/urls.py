from django.urls import path
from .views import PersonListCreateAPIView, FaceMatchAPIView

urlpatterns = [
    path('persons/', PersonListCreateAPIView.as_view(), name='person-list-create'),
    path('face-match/', FaceMatchAPIView.as_view(), name='face-match'),
]
