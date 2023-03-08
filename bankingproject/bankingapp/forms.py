from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout, Div, Row
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from bankingapp.models import Register, Branch
from django.contrib.admin.widgets import AdminDateWidget
from datetime import date



class MemberCreationForm(forms.ModelForm):
    MATERIAL_CHOICES = (
        ('debitcard', 'Debit Card'),
        ('creditcard', 'Credit Card'),
        ('chequebook', 'Cheque Book')
    )
    material_choices = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=MATERIAL_CHOICES)
    birthdate = forms.DateField(
        # widget=forms.TextInput(
        #     attrs={'type': 'date'}
        # )
    )

    class Meta:
        model = Register
        fields = ['name', 'birthdate', 'age', 'gender', 'phone', 'email', 'address', 'district', 'branch', 'account',
                  'material_choices']
        labels = {'birthdate': 'Date of Birth',
                  'phone': 'Phone Number',
                  'account': 'Account Type',
                  'material_choices': 'Materials Provided'}


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div('birthdate', css_class='form-group col-4'),
                Div('age', css_class='form-group col-4'),

                css_class='form-row'
            ),
            Div(
                Div('district', css_class='form-group col-4'),
                Div('branch', css_class='form-group col-4'),

                css_class='form-row'
            ),
            Div(
                Div('debitcard', css_class='form-group col-4'),
                Div('creditcard', css_class='form-group col-4'),
                Div('chequebook', css_class='form-group col-4'),
                css_class='form-row'
            ),
        )

        self.fields['branch'].queryset = Branch.objects.none()
        self.fields['age'].widget.attrs['readonly'] = True

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['branch'].queryset = Branch.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Branch queryset
        elif self.instance.pk:
            self.fields['branch'].queryset = self.instance.district.branch_set.order_by('name')


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_no = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)

    class Meta:
        model = Register
        fields = ['name', 'email', 'password']
