from django.contrib import admin
from .models import Project, Review, Profile

admin.site.register(Project)
admin.site.register(Profile)
admin.site.register(Review)