from django.views.generic import ListView
from staff.models import Staff
from rest_framework import viewsets

from staff.serializers import StaffSerializer


class StaffListView(ListView):
    queryset = Staff.objects.all()
    template_name = 'staff.html'
    context_object_name = 'staffs'


class StaffModelViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    filterset_fields = ['id']

    def get_queryset(self):
        return self.queryset.filter(parent=None)