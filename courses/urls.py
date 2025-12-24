from rest_framework.routers import DefaultRouter
from courses.views import CategoryViewSet, CourseViewSet, LessonViewSet, AssignmentViewSet, AssignmentSubmissionViewSet, LessonProgressViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='categories')
router.register('courses', CourseViewSet, basename='courses')
router.register('lessons', LessonViewSet, basename='lessons')
router.register('assignments', AssignmentViewSet, basename='assignments')
router.register('submissions', AssignmentSubmissionViewSet, basename='submissions'),
router.register('lesson-progress', LessonProgressViewSet, basename='lesson-progress')

urlpatterns = router.urls
