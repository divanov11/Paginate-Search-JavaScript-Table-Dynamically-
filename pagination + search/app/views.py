from django.shortcuts import render
from . models import *

def dynamicAPIcall(request):
	return render(request, 'app/dynamic_call.html')

