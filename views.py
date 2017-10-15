from django.shortcuts import render, redirect

from django.views.generic import TemplateView
from .weather import Weather
from .models import SearchQuery

import time
from django.utils import timezone

# Create your views here.
class IndexView(TemplateView):
	template_name = "weather/index.html"

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		context['latest_queries'] = SearchQuery.objects.all().order_by('-search_time')[:10]
		return context

def detail(request, location_name):
	start_time = time.time()
	weather = Weather(location_name)
	lat_lng = weather.get_lat_lng()

	# Log the query in database
	sq = SearchQuery()
	sq.query = location_name
	sq.formatted_name = weather.full_name
	sq.search_time = timezone.now()
	sq.save()

	if (weather.result == "__FAIL__"):
		error_message = "Requested '" + location_name + "' was not found on our server.\nSorry for that."
		return render(request, 'weather/detail.html', {'error_message': error_message})
	
	current_weather = weather.get_current_weather()

	elapsed_sec = time.time() - start_time

	context = {
		'location_name': weather.full_name,
		'lat_lng': lat_lng,
		'current_weather': weather.current_summary,
		'current_temp': weather.current_temperature,
		'current_humidity': weather.current_humidity,
		'photo_url': weather.photo_url,
		'll_runtime': weather.latlng_time,
		'fetch_runtime': weather.fetchweather_time,
		'total_runtime': elapsed_sec,
	}

	return render(request, 'weather/detail.html', context)

def search(request):
	search_text = request.GET.get("name")
	return redirect('weather:detail', search_text)