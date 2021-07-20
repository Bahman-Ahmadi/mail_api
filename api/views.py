from django.shortcuts import render

# Create your views here.
def index(request):
	appName = open("/data/data/com.termux/files/home/tools/djSocket/vars.txt").read().strip().split("|")[1]
	return render(request, f'{appName}/index.html')