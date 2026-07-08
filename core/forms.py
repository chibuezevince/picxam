from django import forms

class CustomSignupForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    agree = forms.BooleanField(required=True)

    def signup(self, request, user):
        user.name = self.cleaned_data["name"]
        user.save()
