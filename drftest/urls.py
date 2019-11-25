from django.contrib import admin
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from testmodel.views import TestModelViewSet

router = DefaultRouter()
router.register(r'test', TestModelViewSet)
urlpatterns = router.urls

urlpatterns += [
    url('admin/', admin.site.urls),
]
