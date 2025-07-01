from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

VERIFY_TOKEN = "Nishanth@_instadm18"

@csrf_exempt
def webhook(request):
    if request.method == "GET":
        verify_token = request.GET.get("hub.verify_token")
        challenge = request.GET.get("hub.challenge")
        mode = request.GET.get("hub.mode")

        if mode == "subscribe" and verify_token == VERIFY_TOKEN:
            return HttpResponse(challenge)
        else:
            return HttpResponse("Invalid verification token", status=403)

    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            print("Webhook Received:", json.dumps(data, indent=2))
        except Exception as e:
            print("Webhook Error:", str(e))
            print("Raw Body:", request.body)
        return JsonResponse({'status': 'ok'})


    return JsonResponse({'error': 'Invalid method'}, status=405)
