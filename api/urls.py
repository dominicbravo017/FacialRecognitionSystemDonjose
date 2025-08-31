from django.urls import path
from .views import PersonAttendanceListAPIView, PersonListCreateAPIView, FaceMatchAPIView, UpdatePersonAPIView, DeletePersonAPIView
from api import views

urlpatterns = [
    path('persons/', PersonListCreateAPIView.as_view(), name='person-list-create'),
    path('face-match/', FaceMatchAPIView.as_view(), name='face-match'),
    path('getUserAttendance/', PersonAttendanceListAPIView.as_view(), name='person-attendance'),
    path('updatePerson/<int:id>/', UpdatePersonAPIView.as_view(), name='update-person'),
    path('deletePerson/<int:id>/', views.DeletePersonAPIView.as_view(), name='delete-person'),
    path('getAttendanceById/<int:id>/', views.PersonAttendanceByIdAPIView.as_view(), name='attendance'),


    # testing purposes
    # path('excuse/submit/', ExcuseCreateView.as_view(), name='excuse-submit'),
    # path('excuse/admin/', ExcuseAdminListUpdateView.as_view(), name='excuse-admin'),
]