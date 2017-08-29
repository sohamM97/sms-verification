from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.send_otp,name='Send OTP'),
    url(r'^success/',views.success,name='Success'),
    url(r'^failure/',views.failure,name='Failure'),
]