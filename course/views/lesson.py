from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView

from course.models import Lesson
from course.paginators.course import LessonPaginator
from course.serializers.lesson import LessonSerializer


class LessonListAPIView(ListAPIView):
    """
        Представление для получения списка всех уроков.

        Attributes:
            serializer_class (LessonSerializer): Сериализатор, используемый для преобразования объектов уроков в JSON.
            queryset (QuerySet): Набор объектов уроков, используемых для построения списка.
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]


class LessonCreateAPIView(CreateAPIView):
    """
        Представление для создания нового урока.

        Attributes:
            serializer_class (LessonSerializer): Сериализатор, используемый для преобразования JSON в объект урока.
    """
    serializer_class = LessonSerializer
    permission_classes = {IsAdminUser}


class LessonDestroyAPIView(DestroyAPIView):
    """
        Представление для удаления урока.

        Attributes:
            queryset (QuerySet): Набор объектов уроков, используемых для поиска урока, который нужно удалить.
    """
    queryset = Lesson.objects.all()
    permission_classes = {IsOwner | IsAdminUser}


class LessonUpdateAPIView(UpdateAPIView):
    """
        Представление для обновления урока.

        Attributes:
            serializer_class (LessonSerializer): Сериализатор, используемый для преобразования JSON в объект урока.
            queryset (QuerySet): Набор объектов уроков, используемых для поиска урока, который нужно обновить.
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = {IsOwner | IsModerator | IsAdminUser}


class LessonRetrieveAPIView(RetrieveAPIView):
    """
        Представление для получения деталей урока.

        Attributes:
            serializer_class (LessonSerializer): Сериализатор, используемый для преобразования объекта урока в JSON.
            queryset (QuerySet): Набор объектов уроков, используемых для поиска урока, детали которого нужно получить.
            pagination_class (LessonPaginator): Пагинатор, для отображения уроков на странице.
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = {IsOwner | IsModerator | IsAdminUser}
    pagination_class = LessonPaginator