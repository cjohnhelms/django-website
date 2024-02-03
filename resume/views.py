from django.shortcuts import render
from django.shortcuts import redirect
from django.http import JsonResponse
from .models import Experience, Education, Certification, Skill

def resume(request):
    queryset = {
        "experiences": Experience.objects.values().order_by('-start_date'),
        "education": Education.objects.values().order_by('-start_date'),
        "certifications": Certification.objects.values().order_by('-date_achieved'),
        "skills": Skill.objects.values(),
    }
    html_response = render(request, 'resume/resume.html', queryset)
    if request.accepts("text/html"):
        return html_response