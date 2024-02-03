from django.urls import path
from . import views

urlpatterns = [
    path("", views.api, name="api"),
    path("resume/", views.resume, name="apiResume"),
    path("resume/experience/", views.experience, name="apiExperience"),
    path("resume/certifications/", views.certification, name="apiCertifications"),
    path("resume/education/", views.education, name="apiEducation"),
    path("resume/skills/", views.skill, name="apiSkills"),
]