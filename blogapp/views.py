from django.shortcuts import render
from blogapp.models import Summaries
import math, types

# Create your views here.
def index(request):
	summaries = Summaries.objects.all().order_by('-date')
	entry_count =  Summaries.objects.all().count()
	summaries_pages = math.ceil(float(entry_count / 4))
	page_numbers = list(range(1, summaries_pages + 1))
	snap_limits = [i * 4 for i in page_numbers]
	snap_starts = [i - 4 for i in snap_limits]
	print(type(summaries))
	smoothscroll = "smoothscroll"
	limits_list = []
	for i in page_numbers:
		print(i)
		limits_obj = {}
		limits_obj['start'] = snap_starts[i-1]
		limits_obj['end'] = snap_limits[i-1]
		limits_obj['pagenum'] = i
		limits_list.append(limits_obj)
	print(limits_list)
	return render(request, 'index.html', {
		'summaries': summaries,
		'summaries_pages': summaries_pages,
		'page_numbers': page_numbers,
		'snap_limits': snap_limits,
		'snap_starts': snap_starts,
		'limits_list': limits_list,
		'smoothscroll': smoothscroll
	})


def entry(request):
	entry = Summaries.objects.get(id=1)
	date = entry.date
	keywords = str(entry.keywords)
	keywords = keywords.split(",")
	print("KILUBEDBIEDBIEWBDIEWBD")
	print(len(keywords))
	return render(request, 'entries/soil-carbon-science.html', {
		'date': date,
		'keywords': keywords,
	})

def entry(request):
	entry = Summaries.objects.get(id=2)
	date = entry.date
	keywords = str(entry.keywords)
	keywords = keywords.split(",")
	print("KILUBEDBIEDBIEWBDIEWBD")
	print(len(keywords))
	return render(request, 'entries/about-the-page.html', {
		'date': date,
		'keywords': keywords,
	})

def about(request):
    return render(request, 'about.html')

def resume(request):
    return render(request, 'resume.html')

def projects(request):
	return render(request, 'projects.html')
