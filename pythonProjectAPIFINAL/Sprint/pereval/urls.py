from django.urls import path, include
from rest_framework import routers
from .views import *


router = routers.SimpleRouter()
router.register(r'submit-data', PerevalViewSet)

urlpatterns = [
   path('', include(router.urls)),
   path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
   path('api2/submit-data', CreateListView.as_view(), name='create_list'),
   path('api2/submit-data/<int:pk>/', GetRetrieveView.as_view(), name='get_retrieve'),

]