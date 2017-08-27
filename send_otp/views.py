from django.http import HttpResponse
from django.shortcuts import render

from twilio.rest import Client

import random

def generate_otp():
	otp=random.randint(1000,9999)
	print otp
	account_sid = "AC07ab8e0938b8758dd2cc29336754c258"
	auth_token = "e9a340fa42a1a11f2279e23e830221e8"
	client = Client(account_sid, auth_token)
	client.messages.create(
		to="+918179432609",
		from_="+18635765103",
		body=otp)

def send_otp(request):
	generate_otp()
	return render(request,'send_otp\index.html')

