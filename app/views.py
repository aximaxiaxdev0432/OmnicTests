import requests
import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from dateutil import rrule
from datetime import datetime
from django.contrib.auth import authenticate, login


def get_days(from_date, to_date):
	days = []
	for dt in rrule.rrule(rrule.DAILY, dtstart=datetime.strptime(from_date, '%Y%m%d'), until=datetime.strptime(to_date, '%Y%m%d')):
		days.append(dt.strftime('%Y%m%d'))
	return days


@csrf_exempt
def exchange(request):
	username = request.POST.get('username')
	password = request.POST.get('password')

	result = 'Нужен Ваш логин и пароль в теле'

	user = authenticate(username=username, password=password)

	if user is not None:
		result = requests.get('https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json')
		return HttpResponse(str(result)) 	
	else:
		return HttpResponse('Error') 	


@csrf_exempt
def exchange_period(request):
	if request.method == 'GET':
		username = request.GET.get('username')
		password = request.GET.get('password')
		from_date = request.GET.get('from')
		to_date = request.GET.get('to')


	if request.method == 'POST':

		username = request.POST.get('username')
		password = request.POST.get('password')

		from_date = request.POST.get('from')
		to_date = request.POST.get('to')

	print(username)


	print(password)
	all_dates = {}


	if from_date != None and to_date != None:

		result = 'Нужен Ваш логин и пароль в теле'

		user = authenticate(username=username, password=password)

		json_obj = {}

		if user is not None:
			days = get_days(from_date, to_date)
			print(len(days))

			for d in days:
				result = requests.get(f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json&date={d}')
				all_dates[d] = result.text

			print(all_dates)
			print(len(all_dates))
			# all_dates =json.dumps(all_dates)

		return HttpResponse(str(all_dates)) 	
	else:
		return HttpResponse('Error') 	

