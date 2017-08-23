from django.http import HttpResponse
from django.shortcuts import render

def send_otp(request):
	return render(request,'send_otp\index.html')

