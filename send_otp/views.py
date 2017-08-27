from django.http import HttpResponse
from django.shortcuts import render
from django import forms

from twilio.rest import Client

import random

class MyForm(forms.Form):
	mobile_no=forms.CharField(max_length=20)

#def form_handle(request):
	
	

#def generate_otp():
#	otp=random.randint(1000,9999)
#	print otp
#	account_sid = "AC07ab8e0938b8758dd2cc29336754c258"
#	auth_token = "e9a340fa42a1a11f2279e23e830221e8"
#	client = Client(account_sid, auth_token)
#	client.messages.create(
#		to="+917095972533",
#		from_="+18635765103",
#		body='Your One Time Password is '+str(otp))

def send_otp(request):
	#generate_otp()
	form=MyForm(request.POST)
	if form.is_valid():
		cd=form.cleaned_data
		mobile_no=cd.get('mobile_no')
		print mobile_no
	return render(request,'send_otp\index.html',{'form':form})

