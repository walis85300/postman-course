from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from courses.filters import FilterByDate
from courses.models import Course, Material, Comment
from courses.pagination import LargeResultsSetPagination
from courses.serializers import (
    CourseSerializer,
    MaterialSerializer,
    CommentSerializer,
)


class CoursesViewSet(viewsets.ModelViewSet):
    model = Course
    queryset = Course.objects.all()
    pagination_class = LargeResultsSetPagination
    serializer_class = CourseSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
        FilterByDate,
    ]
    ordering_fields = ['created_at', 'ranking']
    ordering = ['created_at']


class PrivateCoursesViewSet(CoursesViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class MaterialViewSet(viewsets.ModelViewSet):
    model = Material
    queryset = Material.objects.filter(is_active=True)
    serializer_class = MaterialSerializer

    def get_serializer_class(self):
        serializers = {'comments': CommentSerializer}

        return serializers.get(self.action, self.serializer_class)

    def list(self, request, *args, **kwargs):
        return Response(
            {'Error': 'Action not allowed'},
            status=status.HTTP_405_METHOD_NOT_ALLOWED,
        )

    @action(methods=['get'], detail=True)
    def comments(self, request, pk=None, *args, **kwargs):
        material = self.get_object()
        queryset = Comment.objects.filter(material=material)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CommentViewSet(viewsets.ModelViewSet):
    model = Comment
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def list(self, request, *args, **kwargs):
        return Response(
            {'Error': 'Action not allowed'},
            status=status.HTTP_405_METHOD_NOT_ALLOWED,
        )
