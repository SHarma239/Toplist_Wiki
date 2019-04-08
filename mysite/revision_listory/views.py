#from django.shortcuts import render
#from django.http import HttpResponse
import requests
import pandas as pd
import json
from collections import Counter
'''
def index(request):
	S = requests.Session()
	URL = "https://en.wikipedia.org/w/api.php"

	PARAMS = {
	"format": "json",
	"rcprop": "ids|title|ids|sizes|flags|parsedcomment|comment|user|timestamp",
	"list": "recentchanges",
	"action": "query",
	"rcstart": "2019-04-07T19:36:25Z",
	"rclimit": "10",
	"rctype":"edit",
	"rcdir":"newer",

	}
	R = S.get(url=URL, params=PARAMS)
	DATA = R.json()
	print(DATA)

	#df = pd.read_json("data.json");
	#print(df.head());

	return HttpResponse(""+str(DATA))
	return render(request, 'index.html', DATA)
'''
if __name__ == "__main__":
		file = './data.json'
		with open(file) as json_file:
		    data = json.load(json_file)

		# converting json dataset from dictionary to dataframe
		df = pd.DataFrame.from_dict(data, orient='index')
		#users = df[['user']].values
		#user_dict = Counter(users)
		#sorted(user_dict, reverse = True)
		print(df.head())
