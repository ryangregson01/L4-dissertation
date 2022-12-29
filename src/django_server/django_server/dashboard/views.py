from django.shortcuts import render
from dashboard.models import Protein
from dashboard.forms import seqForm
from dashboard.views_helper import *
import torch

def index(request):
    context_dict = {}

    if request.method == 'POST':
        form = seqForm(request.POST)
        if form.is_valid():
            user_seq = form.save(commit=False)
            context_dict['input_seq'] = str(user_seq)
            
            # user_seq is a string, so convert it to Tensor
            full_seq = make_image(str(user_seq))

            loaded_model = model_class()
            with torch.no_grad():
                predicted_label = loaded_model(full_seq)
            predicted_label = torch.squeeze(predicted_label)
            pred_lab_list = ['1' if (float(val) > 0.5) else '0' for val in predicted_label]
            pred_lab_list = ''.join(pred_lab_list)
            context_dict['generated_label'] = pred_lab_list

            return render(request, 'index.html', context=context_dict)
        else:
            print(form.errors)
    
    form = seqForm()
    context_dict['form'] = form
    return render(request, 'index.html', context=context_dict)
