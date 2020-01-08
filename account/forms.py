from django import forms
from .models import Profile


messages = {
	'required':'این فیلد اجباری است',
	'invalid':'لطفا یک ایمیل معتبر وارد کنید',
	'max_length':'تعداد کاراکترها بیشتر از حد مجاز است'
}

class UserLoginForm(forms.Form):
	username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
	password = forms.CharField(max_length=40, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))


class UserRegistrationForm(forms.Form):
	username = forms.CharField(error_messages=messages, max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
	email = forms.EmailField(error_messages=messages, max_length=50, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}))
	password = forms.CharField(error_messages=messages, max_length=40, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


class EditProfileForm(forms.ModelForm):
	email = forms.EmailField()
	class Meta:
		model = Profile
		fields = ('bio', 'age')


class PhoneLoginForm(forms.Form):
	phone = forms.IntegerField()

	def clean_phone(self):
		phone = Profile.objects.filter(phone=self.cleaned_data['phone'])
		if not phone.exists():
			raise forms.ValidationError('This phone number does not exists')
		return self.cleaned_data['phone']


class VerifyCodeForm(forms.Form):
	code = forms.IntegerField()











