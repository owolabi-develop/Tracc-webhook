"""
this code will only run on a secure https server 

"""
from django.http import *
import json
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from mysite.settings import VERIFY_TOKEN


# example endpoint and token to verify by face book
EndPoint= 'https://tracc-busines.herokuapp.com/ca9e9764-9e0d-4318-9d6d-9b6180d195f4/'


@csrf_exempt
def WebHookSetUp(request):
    verify_token = VERIFY_TOKEN
    if request.method == "GET":
        mode = request.GET.get('hob.mode',None)
        token = request.GET.get('hub.verify_token',None)
        challenge = request.GET.get('hub.challenge',None)
        if mode =="subscribe" and token == verify_token:
            print("Verified webhook")
            return HttpResponse(challenge,status=200)
        else:
            return HttpResponse('Invalid verification token',status=403)
    if request.method == "POST":
        data = json.loads(request.body)
        print("Received webhook data: {} ".format(data))
        return HttpResponse("please subscribe field object on your dasboard")


   



