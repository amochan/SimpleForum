from django import forms
from django.contrib.auth.models import User
from django.core.validators import EmailValidator, RegexValidator
from django.utils.translation import ugettext as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout, Submit
from crispy_forms.bootstrap import FormActions

from .models import UserProfile


class LoginForm(forms.Form):
  v = {}
  v['username'] = [
    RegexValidator('^\w+$', message=_('Username must contain only alphabets numbers and/or underscore letters'))
  ]
  v['password'] = [
    RegexValidator('^[\x21-\x7e]+$', message=_('Password must be Ascii charators'))
  ]
  w = {}
  w['username'] = forms.TextInput
  w['password'] = forms.PasswordInput

  username = forms.CharField(label='Username', validators=v['username'], widget=w['username'],
                             required=True)
  password = forms.CharField(label='Password', validators=v['password'], widget=w['password'],
                             required=True, min_length=8)

  helper = FormHelper()
  helper.form_method = 'POST'
  helper.form_class = 'col-md-offset-1 form-horizontal'
  helper.label_class = 'col-md-2'
  helper.field_class = 'col-md-5'
  helper.layout = Layout(
    Field('username'),
    Field('password'),
    FormActions(Submit('Login', 'Login')),
  )

  def clean_username(self):
    username = self.cleaned_data['username']

    if username and not User.objects.filter(username=username).exists():
      raise forms.ValidationError('Username is wrong')
    return username

  def clean_password(self):
    password = self.cleaned_data['password']

    if 'username' not in self.cleaned_data:
      return password
    username = self.cleaned_data['username']
    if not password:
      raise forms.ValidationError('Password is wrong')
    user = User.objects.filter(username=username).first()
    if not user.check_password(password):
      raise forms.ValidationError('Password is wrong')
    return password


class SignupForm(forms.Form):
  v = {}
  v['username'] = [
    RegexValidator('^\w+$', message=_('Username must contain only alphabets numbers and/or underscore letters'))
  ]
  v['password'] = [
    RegexValidator('^[\x21-\x7e]+$', message=_('Password must be Ascii charators'))
  ]
  v['email'] = [
    EmailValidator()
  ]
  w = {}
  w['username'] = forms.TextInput
  w['password'] = forms.PasswordInput
  w['email'] = forms.EmailInput

  username = forms.CharField(label='Username', validators=v['username'], widget=w['username'],
                             required=True)
  password = forms.CharField(label='Password', validators=v['password'], widget=w['password'],
                             required=True, min_length=8)
  password_confirm = forms.CharField(label='Password Confirm', validators=v['password'],
                                     widget=w['password'], required=True, min_length=8) 
  email = forms.EmailField(label='Email', validators=v['email'], widget=w['email'],
                           required=True)

  helper = FormHelper()
  helper.form_method = 'POST'
  helper.form_class = 'col-md-offset-1 form-horizontal'
  helper.label_class = 'col-md-2'
  helper.field_class = 'col-md-5'
  helper.layout = Layout(
    Field('username'),
    Field('password'),
    Field('password_confirm'),
    Field('email'),
    FormActions(Submit('Signup', 'Signup')),
  )

  def clean_username(self):
    username = self.cleaned_data['username']

    if username and User.objects.filter(username=username).exists():
      raise forms.ValidationError('Username already exist')
    return username

  def clean_password_confirm(self):
    password_confirm = self.cleaned_data['password_confirm']

    if 'password' not in self.cleaned_data:
      return password_confirm
    password = self.cleaned_data['password']

    if password and password_confirm and password != password_confirm:
      raise forms.ValidationError('Passwords do not match')
    return password_confirm
      
  def clean_email(self):
    email = self.cleaned_data['email']
    if email and User.objects.filter(email=email).exists():
      raise forms.ValidationError('Email already exist')
    return email
