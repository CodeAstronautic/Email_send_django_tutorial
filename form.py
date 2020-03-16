from django import forms
#from app import Register

'''
class RegisterForm(forms.ModelForm):
    class Meta:
        Model = Register
        fields = ('Name','email','phone_no','password','cpassword','study') 
'''
class SubscribeForm(forms.Form):
    Email = forms.EmailField()
    def __str__(self):
        return self.Email