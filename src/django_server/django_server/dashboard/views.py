from django.shortcuts import render

def index(request):
    context_dict = {'context_key' : 'context_val'}
    return render(request, 'index.html', context=context_dict)
