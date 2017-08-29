from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse

from twilio.rest import Client

import random,os

class MyForm(forms.Form):
	mobile_no=forms.CharField(max_length=20)

class OTPForm(forms.Form):
	otp=forms.IntegerField()

def generate_otp(mobile_no):

	otp=random.randint(1000,9999)
	#account_sid = "AC07ab8e0938b8758dd2cc29336754c258"
	#auth_token = "e9a340fa42a1a11f2279e23e830221e8"
	#client = Client(account_sid, auth_token)
	#client.messages.create(
	#	to=mobile_no,
	#	from_="+18635765103",
	#	body='Your One Time Password is '+str(otp))

	print otp
	f=open('otp.txt','w')
	f.write(str(otp))
	f.close()	

def send_otp(request):

	form=MyForm(request.POST)
	otp_form=OTPForm(request.POST)
	
	otp=0

	if form.is_valid():
		cd=form.cleaned_data
		mobile_no=cd.get('mobile_no')
		if os.path.getsize('otp.txt')==0L:
		
			generate_otp(mobile_no)

	elif otp_form.is_valid():
		f=open('otp.txt','r')
		otp=int(f.read())
		f.close()
		open('otp.txt','w').close()
		cd2=otp_form.cleaned_data
		entered_otp=cd2.get('otp')
		print otp,entered_otp
		if otp==entered_otp:
			return HttpResponseRedirect(reverse('Success'))
		else:
			return HttpResponseRedirect(reverse('Failure'))
	
	return render(request,'send_otp\index.html',{'form':form,'otp_form':otp_form})

def success(request):
	return render(request,'send_otp\success.html')

def failure(request):
	return render(request,'send_otp\\failure.html')

