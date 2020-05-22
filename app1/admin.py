from django.contrib import admin
from .models import registration,skill,education,project,language
# Register your models here.
admin.site.register(registration)
admin.site.register(skill)
admin.site.register(education)
admin.site.register(project)
admin.site.register(language)