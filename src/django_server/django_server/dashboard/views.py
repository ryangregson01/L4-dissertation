from django.shortcuts import render
from dashboard.models import Protein
from dashboard.forms import seqForm

def index(request):
    context_dict = {}

    if request.method == 'POST':
        form = seqForm(request.POST)
        if form.is_valid():
            user_seq = form.save(commit=False)
            context_dict['input_seq'] = str(user_seq)
            return render(request, 'index.html', context=context_dict)
        else:
            print(form.errors)
    
    form = seqForm()
    context_dict['form'] = form
    return render(request, 'index.html', context=context_dict)
