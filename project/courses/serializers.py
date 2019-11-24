from rest_framework import serializers

from courses import models


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = (
            'id',
            'name',
            'description',
            'current_job',
            'created_at',
            'updated_at',
        )


class CourseSerializer(serializers.ModelSerializer):
    teachers = TeacherSerializer(many=True)

    class Meta:
        model = models.Course
        fields = (
            'id',
            'name',
            'description',
            'teachers',
            'ranking',
            'created_at',
            'updated_at',
        )

    def create(self, validated_data):
        teachers = validated_data.pop('teachers')

        course = models.Course(**validated_data)
        course.save()

        for teacher in teachers:
            t = models.Teacher(**teacher)
            t.save()
            t.course_set.add(course)

        return course


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Video
        fields = ('id', 'provider', 'url')


class MaterialSerializer(serializers.ModelSerializer):
    videos = VideoSerializer(many=True)

    class Meta:
        model = models.Material
        fields = ('id', 'title', 'description', 'videos', 'is_active')

    def create(self, validated_data):
        videos = validated_data.pop('videos')
        validated_data['course'] = self.context.get('course')

        material = models.Material(**validated_data)
        material.save()

        for video in videos:
            v = models.Video(**video)
            v.material = material
            v.save()

        return material


class CourseDetailSerializer(serializers.ModelSerializer):
    materials = MaterialSerializer(many=True)

    class Meta:
        model = models.Course
        fields = (
            'id',
            'description',
            'badge',
            'teachers',
            'ranking',
            'materials',
            'created_at',
            'updated_at',
        )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = '__all__'
