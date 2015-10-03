# -*- coding: utf-8 -*- 
from django.shortcuts import render, redirect
from wikitest.models import Files
import markdown2

# Create your views here.

DEF_URL = "README"
ERROR = "Извините, данного документа не существует"

def index(request, url):

	files = Files.objects.all()
	
	if url == "":
		url = DEF_URL

	doc = Files()
	try:
		doc = Files.objects.get(url=url)
		html_data = markdown2.markdown(doc.data)
		doc.data = html_data
	except:
		doc.name = ERROR
		doc.data = "none"

	context = {
		"files": files,
		"text": doc,
	}
	return render(request, 'index.html', context)

def edit(request, url):

	files = Files.objects.all()

	doc = Files()
	try:
		doc = Files.objects.get(url=url)
	except:
		doc.name = ERROR
		doc.data = "none"

	context = {
		"files": files,
		"text": doc,
	}
	return render(request, 'edit.html', context)

def save(request):

	url = request.POST.get('doc_url')
	name = request.POST.get('doc_name')
	data = request.POST.get('doc_data')

	if url != "none":
		doc = Files.objects.get(url=url)
		doc.name = name
		doc.data = data
	else:
		doc = Files.objects.create(name=name, data=data, url=name.replace (" ", "_"))


	doc.save()

	return redirect('index', doc.url)

def add(request):

	files = Files.objects.all()

	text = Files()
	text.url = "none"

	context = {
		"files": files,
		"text": text,
	}
	return render(request, 'edit.html', context)