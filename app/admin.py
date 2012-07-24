from django.contrib import admin
from django_si.app.models import RoTable

class RoTableAdmin(admin.ModelAdmin):
    list_display = ("name", "number",)
    list_filter = ("number",)

admin.site.register(RoTable, RoTableAdmin)
