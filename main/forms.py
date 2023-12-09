from django import forms


class MatrisItemInputForm(forms.Form):
    item_00 = forms.FloatField(label='A00 kiriting:', required=True,
                                 widget=forms.NumberInput(attrs={'placeholder': 'A11'}))
    item_01 = forms.FloatField(label='A01 kiriting:', required=True,
                                 widget=forms.NumberInput(attrs={'placeholder': 'A12'}))
    item_02 = forms.FloatField(label='A02 kiriting:', required=True,
                                 widget=forms.NumberInput(attrs={'placeholder': 'A13'}))
    item_03 = forms.FloatField(label='A03 kiriting:', required=True,
                                 widget=forms.NumberInput(attrs={'placeholder': 'A14'}))

    item_10 = forms.FloatField(label='A10 kiriting:', required=True,
                                 widget=forms.NumberInput(attrs={'placeholder': 'A21'}))
    item_11 = forms.FloatField(label='A11 kiriting:', required=True,
                                 widget=forms.NumberInput(attrs={'placeholder': 'A22'}))
    item_12 = forms.FloatField(label='A12 kiriting:', required=True,
                                 widget=forms.NumberInput(attrs={'placeholder': 'A23'}))
    item_13 = forms.FloatField(label='A13 kiriting:', required=True,
                                 widget=forms.NumberInput(attrs={'placeholder': 'A24'}))

    item_20 = forms.FloatField(label='A20 kiriting:', required=True,
                                 widget=forms.NumberInput(attrs={'placeholder': 'A31'}))
    item_21 = forms.FloatField(label='A21 kiriting:', required=True,
                                 widget=forms.NumberInput(attrs={'placeholder': 'A32'}))
    item_22 = forms.FloatField(label='A22 kiriting:', required=True,
                                 widget=forms.NumberInput(attrs={'placeholder': 'A33'}))
    item_23 = forms.FloatField(label='A23 kiriting:', required=True,
                                 widget=forms.NumberInput(attrs={'placeholder': 'A34'}))

    item_30 = forms.FloatField(label='A30 kiriting:', required=True,
                                 widget=forms.NumberInput(attrs={'placeholder': 'A41'}))
    item_31 = forms.FloatField(label='A31 kiriting:', required=True,
                                 widget=forms.NumberInput(attrs={'placeholder': 'A42'}))
    item_32 = forms.FloatField(label='A32 kiriting:', required=True,
                                 widget=forms.NumberInput(attrs={'placeholder': 'A43'}))
    item_33 = forms.FloatField(label='A33 kiriting:', required=True,
                                 widget=forms.NumberInput(attrs={'placeholder': 'A44'}))
