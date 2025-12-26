from django.shortcuts import render
from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request,'index.html')

# @csrf_exempt
def analyze(request):
    djtext=request.POST.get('text','default')
    removepune=request.POST.get('removepune','off')
    length=request.POST.get('length','off')
    
    if length == 'on' and removepune == 'on':
        puntutions ='''!()-{}[];:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in puntutions:
                analyzed = analyzed + char
        lent=len(analyzed)
        params={'purpose':'Removesd Punctuation','analyed':analyzed,'length':lent}
        return render(request,'analyze.html',params)

    elif removepune == 'on':
        puntutions ='''!()-{}[];:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in puntutions:
                analyzed = analyzed + char
        params={'purpose':'Removesd Punctuation','analyed':analyzed }
        return render(request,'analyze.html',params)
    
    elif length == 'on':
        lent=len(djtext)
        params={'purpose':'Count length','analyed':djtext,'length':lent}
        return render(request,'analyze.html',params)
    
    
    else:
        return HttpResponse('Error')