from rest_framework.routers import DefaultRouter
from courses.views import CategoryViewSet, CourseViewSet, LessonViewSet, AssignmentViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='categories')
router.register('courses', CourseViewSet, basename='courses')
router.register('lessons', LessonViewSet, basename='lessons')
router.register('assignments', AssignmentViewSet, basename='assignments')

urlpatterns = router.urls
