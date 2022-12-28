from django import forms
from dashboard.models import Protein

class seqForm(forms.ModelForm):
    MAX_LENGTH = 1200
    sequence = forms.CharField(max_length=MAX_LENGTH, 
                            help_text="Please enter the protein sequence."
    )
    # Initial is an empty string - meaning no label currently. Must have required as False for empty initial
    label = forms.CharField(widget=forms.HiddenInput(), 
                            required=False, 
                            initial=""
    )

    class Meta:
        model = Protein
        fields = ('sequence', )

    def clean(self):
        cleaned_data = self.cleaned_data
        entered_seq = cleaned_data.get('sequence')
        clean_seq = []
        for let in entered_seq:
            # Amino acids must be capital letters.
            # Further cleaning necessary for protein sequence constraints.
            if let.isalpha() and let.isupper():
                clean_seq.append(let)

        new_seq = ''.join(clean_seq)
        cleaned_data['sequence'] = new_seq
        return cleaned_data
