from rest_framework import routers
from . import views

r = routers.SimpleRouter()
r.register(r'accounts', views.UserViewSet)