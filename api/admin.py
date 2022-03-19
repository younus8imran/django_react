from django.contrib import admin

from .models import Lead 

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
	model = Lead 

	list_display = (
		'id',
		'name',
		'age', 
		'email', 
		'get_image',
		'message',
		'created_at',
		)
	list_filter = (
		"created_at",
		)
	list_editable = (
		'name',
		'age',
		'email',
		'message',
		)
	search_fields = (
		"name",
		)
	date_hierarchy = "created_at"
