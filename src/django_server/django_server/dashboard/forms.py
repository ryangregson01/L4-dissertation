from django import forms
from dashboard.models import Protein

class seqForm(forms.ModelForm):
    MAX_LENGTH = 5000
    example_protein_sequence = ">sp|P01308|INS_HUMAN Insulin OS=Homo sapiens OX=9606 GN=INS PE=1 SV=1\nMALWMRLLPLLALLALWGPDPAAAFVNQHLCGSHLVEALYLVCGERGFFYTPKTRREAED\nLQVGQVELGGGPGAGSLQPLALEGSLQKRGIVEQCCTSICSLYQLENYCN"
    sequence_id = forms.CharField(max_length=100, widget=forms.HiddenInput(), required=False)
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
        fields = ('sequence', 'sequence_id')

    def clean(self):
        cleaned_data = self.cleaned_data
        # Gets everything from sequence as 1 input box. Splits this and takes out the first line for the identifier
        entered_seq = cleaned_data.get('sequence')
        entered_seq = entered_seq.strip()
        if not entered_seq.startswith('>'):
            raise forms.ValidationError('Invalid FASTA format: The input must start with ">"')
        
        entered_seq = entered_seq.split('\n')
        seq_identifier = entered_seq[0]
        # Gets the ID up to the first space - similar to DISOPRED truncates the ID
        seq_identifier = seq_identifier.split()[0]
        entered_seq = ''.join(entered_seq[1:])
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

        # Stripping here removes any \n or \r character
        cleaned_data['sequence_id'] = seq_identifier.strip()
        cleaned_data['sequence'] = new_seq
        return cleaned_data
