from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Seu Nome', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Seu E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    message = forms.CharField(
        label='Sua Mensagem',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5})
    )
