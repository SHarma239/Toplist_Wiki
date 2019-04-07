from django.shortcuts import render
from django.http import HttpResponse
import requests


def index(request):
	S = requests.Session()
	URL = "https://en.wikipedia.org/w/api.php"

	PARAMS = {
	"format": "json",
	"rcprop": "ids|title|ids|sizes|flags|parsedcomment|comment|user|timestamp",
	"list": "recentchanges",
	"action": "query",
	"rcstart": "2019-04-06T14:43:00Z",
	"rclimit": "100",
	"rctype":"edit",
	"rcdir":"newer",

	}
	R = S.get(url=URL, params=PARAMS)
	DATA = R.json()
	print(DATA)
#	return HttpResponse("Hello. "+str(DATA))
	return render(request, 'index.html', DATA)