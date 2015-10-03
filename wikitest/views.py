# -*- coding: utf-8 -*- 
from django.shortcuts import render, redirect
from wikitest.models import Files
import markdown2

# default url 
DEF_URL = "README"

def index(request, url):

	# find all files for menu
	files = Files.objects.all().values("name", "url")

	# set default url README
	if url == "":
		url = DEF_URL

	# get content
	document = Files()
	try:
		document = Files.objects.get(url=url)
		html_data = markdown2.markdown(document.data)
		document.data = html_data
		document.status = "ok"
	except:
		document.status = "none"

	context = {
		"files": files,
		"document": document,
	}
	return render(request, 'index.html', context)

def edit(request, url):

	# find all files for menu
	files = Files.objects.all()

	# get content
	document = Files()
	try:
		document = Files.objects.get(url=url)
		html_data = markdown2.markdown(document.data)
		document.data = html_data
		document.status = "ok"
	except:
		document.status = "none"

	context = {
		"files": files,
		"document": document,
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

	# find all files for menu
	files = Files.objects.all()

	# empty document without url
	document = Files()
	document.url = "none"

	context = {
		"files": files,
		"text": document,
	}
	return render(request, 'edit.html', context)