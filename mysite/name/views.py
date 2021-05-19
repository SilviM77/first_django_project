from django.http import JsonResponse

name = {'Name': 'SilviM', 'Track': 'Backend Python',
        'Message': 'Thank you all for helping me move forward in the program.'}

# Create your views here.

def index(request):
    return JsonResponse(name)
