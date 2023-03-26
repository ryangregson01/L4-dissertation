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
            # Returns an instance of the Protein model
            user_seq = form.save(commit=False)

            str_user_seq = user_seq.sequence
            str_user_seq_id = user_seq.sequence_id
            context_dict['input_seq'] = str(str_user_seq)
            context_dict['input_seq_id'] = str(str_user_seq_id)
            
            # user_seq is a string, so convert it to Tensor
            full_seq = get_vector(str(user_seq))
            # Mimics batch
            full_seq = full_seq.unsqueeze(0)

            loaded_model = get_model()
            loaded_model.eval()
            with torch.no_grad():
                full_seq = torch.einsum('ijk->ikj', full_seq)
                predicted_label, _ = loaded_model(full_seq)
            predicted_label = torch.squeeze(predicted_label)
            predicted_label = torch.sigmoid(predicted_label)
            predicted_label[predicted_label>=0.5] = 1
            predicted_label[predicted_label<0.5] = 0
            pred_lab_list = ['1' if (float(val) == 1) else '0' for val in predicted_label]
            pred_lab_list = ''.join(pred_lab_list)
            context_dict['generated_label'] = pred_lab_list

            return render(request, 'index.html', context=context_dict)
        else:
            print(form.errors)
    
    form = seqForm()
    context_dict['form'] = form
    return render(request, 'index.html', context=context_dict)
