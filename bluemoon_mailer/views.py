from django.shortcuts import render

# Create your views here.
from django.core.mail import send_mail
from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import ensure_csrf_cookie
import json


@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({'detail': 'CSRF cookie set'})


# @csrf_exempt
@csrf_protect
def send_email(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            subject = data.get("subject")
            message = data.get("message")
            recipient = data.get("recipient")

            send_mail(
                subject,
                message,
                "no-reply@example.com",  # From email
                [recipient],
                fail_silently=False,
            )


            return JsonResponse({"success": True, "message": "Email sent successfully"})

        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)}, status=400)

    return JsonResponse({"error": "POST only"}, status=405)

# curl --location 'http://127.0.0.1:8000/api/send-email/' \
# --header 'Content-Type: application/json' \
# --data-raw '{
#   "subject": "Test Email",
#   "message": "Hello!",
#   "recipient": "test@example.com"
# }'