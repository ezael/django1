from django.shortcuts import render
from django.conf import settings

# Create your views here.
def engine(request):
    if 'id' in request.GET:
        id = request.GET['id']
    else:
        id = ''

    ctx = {
        'id': id,
        'test': getattr(settings, "TH1"),
    }
    return render(request, 'engine.html', context=ctx)

