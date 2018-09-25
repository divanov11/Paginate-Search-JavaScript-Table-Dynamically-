from django.http import JsonResponse
from django.shortcuts import render
from . serializers import *
import math
from django.db.models import Q

def posts(request, page):
	search = request.GET.get('search')
	results = 5
	
	length = math.ceil(len(Post.objects.filter(Q(title__icontains=search))))
	numberOfPages = math.ceil((length -1 ) / results)

	indexStart = ((page - 1) * results);
	indexEnd = indexStart + results;
	posts = Post.objects.filter(Q(title__icontains=search))[indexStart:indexEnd]
	serializer = PostSerializer(posts, many=True)
	return JsonResponse({'posts':serializer.data, 'count':numberOfPages}, safe=False)
