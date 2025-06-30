from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt  # ✅ CSRF disabled for this webhook view
def webhook(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user = data.get('user')
            comment = data.get('comment')
            return JsonResponse({'news': f"Received {comment} from {user}"})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Only POST Requests allowed in webhooks'}, status=405)
