from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from courses.models import Course, Material
from courses.serializers import CourseSerializer, MaterialSerializer


class CoursesViewSet(viewsets.ModelViewSet):
    model = Course
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class PrivateCoursesViewSet(CoursesViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class MaterialViewSet(viewsets.ModelViewSet):
    model = Material
    queryset = Material.objects.filter(is_active=True)
    serializer_class = MaterialSerializer

    def list(self, request, *args, **kwargs):
        return Response(
            {'Error': 'Action not allowed'},
            status=status.HTTP_405_METHOD_NOT_ALLOWED,
        )
