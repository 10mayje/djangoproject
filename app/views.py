from django.shortcuts import render




def index(request):

    return render(request, 'app/home.html')

def theam(request,username):
    if username == 'theamone':

        return render(request, 'app/theamone.html')
    if username == 'theamtwo':
        return render(request, 'app/theamtwo.html')
    if username == 'theamthree':
        return render(request, 'app/theamthree.html')
    if username == 'theamfour':
        return render(request, 'app/theamfour.html')
    else:
        return render(request, 'app/error.html')