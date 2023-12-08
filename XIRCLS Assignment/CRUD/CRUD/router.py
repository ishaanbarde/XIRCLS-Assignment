from Task.viewset import EmployeeViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('employee', EmployeeViewSet)