"""
this code will only run on a secure https server 

"""
from django.http import *
import json
from django.views.decorators.csrf import csrf_exempt, csrf_protect


# example endpoint and token to verify by face book
EndPoint= 'http://localhost:1998/ca9e9764-9e0d-4318-9d6d-9b6180d195f4/'
verify_token ="cd4ff259-f8e8-4d9e-8d69-410d1e2aed56"

@csrf_exempt
def WebHookSetUp(request):
    
    if request.method == "GET":
        mode = request.GET['hob.mode']
        token = request.GET['hub.verify_token']
        challenge = request.GET['hub.challenge']
        if mode =="subscribe" and token == verify_token:
            print("Verified webhook")
            return HttpResponse(challenge,status=200)
        else:
            return HttpResponse('Invalid verification token',status=403)
    if request.method == "POST":
        data = json.loads(request.body)
        print("Received webhook data: {} ".format(data))
        return HttpResponse("please subscribe field object on your dasboard")


   



