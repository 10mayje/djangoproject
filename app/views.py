from django.shortcuts import render

import requests


def index(request):

    return render(request, 'app/home.html')

def theam(request,username):

    print("https://us-central1-instacooll.cloudfunctions.net/webdata/"+username)
    response = requests.get("https://us-central1-instacooll.cloudfunctions.net/webdata/"+username)
    print(response)
    if response.status_code==200:
        print(response.json())
        data=response.json()
        selectedteam=data['theme']
        print(selectedteam)
        Data={
            'name':data['name'],
            'dp':data['dp'],
            'bio':data['bio'],
            'fb':data['fb'],
            'ista':data['insta'],
            'youtube':data['youtube'],
            'linkedin':data['linkedin'],
            'twitter':data['twitter'],
            'phone':data['phone'],
            'whatsapp':data['whatsapp'],
            'links':data['links'],
            'count':len(data['links'])
        }
        print(len(data['links']))
        if selectedteam == 0:

            return render(request, 'app/theamone.html',Data)
        if selectedteam == 1:
            return render(request, 'app/theamtwo.html',Data)
        if selectedteam == 2:
            return render(request, 'app/theamthree.html',Data)
        if selectedteam == 3:
            return render(request, 'app/theamfour.html',Data)
        else:
            return render(request, 'app/error.html', Data)

    return render(request, 'app/er.html')