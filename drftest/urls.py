from django.contrib import admin
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from apps.listings.views import ListingViewSet

router = DefaultRouter()
router.register(r'listings', ListingViewSet)
urlpatterns = router.urls

urlpatterns += [
    url('admin/', admin.site.urls),
]
