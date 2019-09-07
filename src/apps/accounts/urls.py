from rest_framework import routers
from . import views

accounts_urls = routers.SimpleRouter()
accounts_urls.register(r'accounts', views.UserViewSet)
accounts_urls = accounts_urls.urls