from django.shortcuts import redirect
from django.http import JsonResponse, HttpResponseNotFound
from resume.models import Experience, Education, Certification, Skill

def api(request):
    return HttpResponseNotFound("API is only for JSON responses. Please specify endpoint")

def resume(request):
    data = {'content': [
        {'experience': list(Experience.objects.values())}, 
        {'certifications': list(Certification.objects.values())},
        {'education':list(Education.objects.values())},
        {'skills': list(Skill.objects.values())}
        ]}
    def remove_id_keys(d):
        if isinstance(d, dict):
            for key in list(d.keys()):
                if key == 'id':
                    del d[key]
                else:
                    remove_id_keys(d[key])
        elif isinstance(d, list):
            for item in d:
                remove_id_keys(item)
    remove_id_keys(data)
    if request.accepts("application/json"):
        return JsonResponse(data)

def experience(request):
    data = list(Experience.objects.values())
    for item in data:
        item.pop('id')
    if request.accepts("application/json"):
        return JsonResponse({'content': {'experience': data}})

def certification(request):
    data = list(Certification.objects.values())
    for item in data:
        item.pop('id')
    if request.accepts("application/json"):
        return JsonResponse({'content': {'certification': data}})

def education(request):
    data = list(Education.objects.values())
    for item in data:
        item.pop('id')
    if request.accepts("application/json"):
        return JsonResponse({'content': {'education': data}})
    
def skill(request):
    data = list(Skill.objects.values())
    for item in data:
        item.pop('id')
    if request.accepts("application/json"):
        return JsonResponse({'content': {'skills': data}})