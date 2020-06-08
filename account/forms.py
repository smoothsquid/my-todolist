from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import ugettext_lazy as _

from .models import User

class UserCreationForm(forms.ModelForm):
    username = forms.CharField(label=_('Username'))
    name = forms.CharField(label=_('name'))
    emial = forms.EmailField(label=_('Email'))
    date_of_birth = forms.DateField(label=_('Birthday'))
    password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_('Password confirmation'), widget=forms.PasswordInput)

    class Meta():
        model = User
        fields = ('username', 'name', 'email', )
    
    # password2를 초기화 할 때 password1과 일치하는지 확인함
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField()
    date_of_birth = forms.DateField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'date_of_birth', 'is_active',)
        
    # 사용자 정보 수정 시 비밀번호가 변경되지 않도록 기존 비밀번호로 초기화함
    def clean_password(self):
        return self.initial["password"]
