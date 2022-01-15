from django.urls import path

from departments import views

urlpatterns = [
    path('', views.DepartmentListView.as_view(), name='department-list'),
    path('<pk>/', views.DepartmentDetailView.as_view(), name='department-detail'),
]
