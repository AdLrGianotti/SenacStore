from django import forms 

class ContatoForm(forms.form):

    nome = forms.charfil()
    email = forms.EmailField()
    telefone = forms.CharField()
    assunto = forms.CharField()
    mensagem = forms.CharField(widget=forms.Textarea)

