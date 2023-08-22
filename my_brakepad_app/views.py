from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
# request -> response
# request handler

def say_hello(request):
    return render(request, 'index.html')


@csrf_exempt
def submit_data_quickrun(request):
    print('submit_data_quickrun called')
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            speed = data.get('speed[km/h]', '')
            brakePower = data.get('brakepower[PSI]', '')
            brakeTime = data.get('braketime[s]', '')
            restTime = data.get('resttime[s]', '')
            repeat = data.get('repeat', '')
            
            # You can perform additional processing/validation here
            
            #if
            
            # Store the data in some way (e.g., database)
            # For now, we'll just store the data in a list
            data_store.append({'speed': speed, 'brakePower': brakePower, 'brakeTime': brakeTime, 'restTime': restTime, 'repeat':repeat})
            
            return JsonResponse({'message': 'Data submitted successfully'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

# Store the submitted data
data_store = []