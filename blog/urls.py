from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='MRS_Data_Analysis'),
]
