from rest_framework import routers
from django.urls import path
from course.views.course import CourseViewSet
from course.views.lesson import LessonListAPIView, LessonCreateAPIView, LessonDestroyAPIView, LessonUpdateAPIView, \
    LessonRetrieveAPIView

app_name = 'course'

router = routers.SimpleRouter()
router.register('course', CourseViewSet)
urlpatterns = [
                  path('lesson/', LessonListAPIView.as_view(), name='lesson-list'),
                  path('lesson/create', LessonCreateAPIView.as_view(), name='lesson-create'),
                  path('lesson/delete/<int:pk>', LessonDestroyAPIView.as_view(), name='lesson-delete'),
                  path('lesson/update/<int:pk>', LessonUpdateAPIView.as_view(), name='lesson-update'),
                  path('lesson/<int:pk>', LessonRetrieveAPIView.as_view(), name='lesson-detail'),
                  path('', include('payment.urls')),

              ] + router.urls