from rest_framework import routers
from .views import MoodViewSet

app_name = 'moods'
router = routers.SimpleRouter()
router.register(r'moods',MoodViewSet)

urlpatterns = router.urls