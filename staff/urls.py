from django.urls import path, include
from rest_framework import routers

from staff.views import StaffListView, StaffModelViewSet

router = routers.DefaultRouter()
router.register(r'staff', StaffModelViewSet)
urlpatterns = [
    path('', StaffListView.as_view(), name="staff"),
    path('', include(router.urls))
]
