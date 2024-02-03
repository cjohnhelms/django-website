from django.contrib import admin

from .models import Experience, Education, Certification, Skill
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Certification)
admin.site.register(Skill)
