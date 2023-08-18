import json
from django.shortcuts import render

def json_data(request):
    with open('data.json') as json_file:
        data = json.load(json_file)
    
    return render(request, 'json_template.html', {'data': data})