from django.shortcuts import render

def home(request):
    html_response = render(request, 'personal-website/index.html')
    if request.accepts("text/html"):
        return html_response