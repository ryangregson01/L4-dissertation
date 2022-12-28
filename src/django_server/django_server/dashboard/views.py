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
            
            # Make a random label just for the label test
            import random
            lab_arr = []
            for i in range(len(str(user_seq))):
                rand_val = random.randint(0, 1)
                lab_arr.append(str(rand_val))

            test_lab = ''.join(lab_arr)
            context_dict['generated_label'] = test_lab

            return render(request, 'index.html', context=context_dict)
        else:
            print(form.errors)
    
    form = seqForm()
    context_dict['form'] = form
    return render(request, 'index.html', context=context_dict)
