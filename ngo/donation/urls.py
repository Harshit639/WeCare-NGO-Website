from django.urls import path
from . import views
app_name = 'donate'

urlpatterns=[
              path('',views.donation.as_view(),name='fg'),
]
