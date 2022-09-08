from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label="نام کاربری", widget=forms
                               .TextInput(attrs={'class': 'form-group py-3 form-control', 'id': 'email'}),
                               error_messages={'invalid': '', })

    email = forms.EmailField(required=True, label="ایمیل", widget=forms
                             .TextInput(attrs={'class': 'form-group py-3 form-control', 'id': 'email'}),
                             error_messages={'invalid': 'لطفا ایمیل را به درستی وارد کنید', })
    error_messages = {
        'password_mismatch': "پسوردهای وارد شده مطابقت ندارند",
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = 'رمز عبور'
        self.fields['password2'].label = 'تکرار رمز عبور'
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-group py-3 form-control', 'id': 'pass'})
        self.fields['password2'].widget.attrs.update({'class': 'form-group py-3 form-control', 'id': 'pass'})

        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        self.fields['password1'].error_list = None
        self.fields['password2'].error_list = None

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', ]


class LoginForm(forms.Form):
    user_name = forms.EmailField(label="ایمیل", widget=forms
                                 .TextInput(attrs={'class': 'form-group py-3 form-control',
                                                   'id': 'email'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-group py-3 form-control', 'id': 'pass'}), label="رمز عبور")
