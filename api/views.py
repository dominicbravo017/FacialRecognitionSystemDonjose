from rest_framework import generics
from .models import Person
from .serializers import PersonSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Person
from .serializers import PersonSerializer
from deepface import DeepFace
import tempfile
import cv2
import numpy as np

class PersonListCreateAPIView(generics.ListCreateAPIView):
    queryset = Person.objects.all().order_by('-timestamp')
    serializer_class = PersonSerializer

class FaceMatchAPIView(APIView):
    def post(self, request):
        upload = request.FILES.get('image')
        if not upload:
            return Response({"error": "No image provided"}, status=status.HTTP_400_BAD_REQUEST)

        # Save uploaded image to a temp file
        with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp_img:
            for chunk in upload.chunks():
                temp_img.write(chunk)
            temp_img_path = temp_img.name

        # Compare to all saved persons
        for person in Person.objects.all():
            if not person.image:
                continue

            try:
                # Convert bytes to image
                np_arr = np.frombuffer(person.image, np.uint8)
                db_image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

                with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as db_img_file:
                    cv2.imwrite(db_img_file.name, db_image)

                    result = DeepFace.verify(img1_path=temp_img_path, img2_path=db_img_file.name, enforce_detection=False)
                    
                    if result["verified"]:
                        serializer = PersonSerializer(person)
                        return Response(serializer.data, status=status.HTTP_200_OK)

            except Exception as e:
                print(f"Skipping a person due to error: {e}")
                continue

        return Response({"detail": "No matching face found"}, status=status.HTTP_404_NOT_FOUND)