from rest_framework import routers
from .api import StudentViewSet, SubjectViewSet, StudentSubjectViewSet

router = routers.DefaultRouter()
router.register('api/students', StudentViewSet,'Students')
router.register('api/subjects', SubjectViewSet,'Subjects')
router.register('api/studentsubject', StudentSubjectViewSet,'StudentSubject')

urlpatterns = router.urls