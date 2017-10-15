from django.contrib import admin

from .models import SearchQuery

# Register your models here.

class SearchQueryAdmin(admin.ModelAdmin):
	list_display = ('query', 'search_time', 'formatted_name')
	list_filter = ['search_time']
	search_fields = ['query']


admin.site.register(SearchQuery, SearchQueryAdmin)