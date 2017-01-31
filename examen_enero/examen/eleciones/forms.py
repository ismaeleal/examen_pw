from django import forms 

class iniForm(forms.Form):
	
	usuario = forms.CharField(max_length=100)
	contraseña = forms.CharField(widget=forms.PasswordInput)


class CircuscricionesForm(forms.Form):
	
	nombre = forms.CharField(max_length=100)
	numero = forms.IntegerField()