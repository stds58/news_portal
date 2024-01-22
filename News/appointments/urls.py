from django.urls import path
from .views import AppointmentView

app_name = "appointments"
urlpatterns = [
   path('appointments/', AppointmentView.as_view(), name='make_appointment'),
]