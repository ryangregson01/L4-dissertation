from django import forms
from dashboard.models import Protein

class seqForm(forms.ModelForm):
    MAX_LENGTH = 5000
    example_protein_sequence = ">sp|P01308|INS_HUMAN Insulin OS=Homo sapiens OX=9606 GN=INS PE=1 SV=1\nMALWMRLLPLLALLALWGPDPAAAFVNQHLCGSHLVEALYLVCGERGFFYTPKTRREAED\nLQVGQVELGGGPGAGSLQPLALEGSLQKRGIVEQCCTSICSLYQLENYCN"
    sequence = forms.CharField(max_length=MAX_LENGTH, 
                            help_text="\n",
                            widget=forms.Textarea(attrs={'class': 'resizeForm form-control', 'placeholder': example_protein_sequence})
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
        entered_seq = entered_seq.strip()
        if not entered_seq.startswith('>'):
            raise forms.ValidationError('Invalid FASTA format: The input must start with ">"')
        
        entered_seq = entered_seq.split('\n')[1:]
        entered_seq = ''.join(entered_seq)
        clean_seq = []
        for let in entered_seq:
            # Amino acids must be capital letters.
            # Further cleaning necessary for protein sequence constraints.
            if let.isalpha() and let.isupper():
                # Amino acids must be recognised as one of the 20 valid amino acids.
                if let not in "ACDEFGHIKLMNPQRSTVWY":
                    raise forms.ValidationError('Invalid protein sequence: The input must use the recognised 20 amino acid letter codes.')
                
                clean_seq.append(let)

        new_seq = ''.join(clean_seq)
        cleaned_data['sequence'] = new_seq
        return cleaned_data
