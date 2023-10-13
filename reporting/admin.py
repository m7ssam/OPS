from django.contrib import admin
from .models import StatusDefinition, Project
# Register your models here.

admin.site.register(StatusDefinition)
admin.site.register(Project)


# admin change

admin.site.site_header = "Operation Planning System"
admin.site.site_title = "OPS"
admin.site.index_title = "OPS Admin Control panal"