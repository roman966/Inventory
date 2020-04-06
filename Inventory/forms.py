from django import forms
from .models import Transaction
from .models import Date
class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['Product_name','Price','Sale_able','Bounce']


class DateForm(forms.ModelForm):
    class Meta:
        model = Date
        fields = ['Root']