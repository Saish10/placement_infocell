from django.views.generic import DetailView, ListView

from departments.models import Department


class DepartmentListView(ListView):
    model = Department


class DepartmentDetailView(DetailView):
    model = Department
