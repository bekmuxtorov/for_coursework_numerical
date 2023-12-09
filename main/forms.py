from django import forms


class MatrisItemInputForm(forms.Form):
    item_00 = forms.IntegerField(label='A00 kiriting:', required=True,
                                 widget=forms.NumberInput(attrs={'placeholder': 'A11'}))
    item_01 = forms.IntegerField(label='A01 kiriting:', required=True,
                                 widget=forms.NumberInput(attrs={'placeholder': 'A12'}))
    item_02 = forms.IntegerField(label='A02 kiriting:', required=True,
                                 widget=forms.NumberInput(attrs={'placeholder': 'A13'}))
    item_03 = forms.IntegerField(label='A03 kiriting:', required=True,
                                 widget=forms.NumberInput(attrs={'placeholder': 'A14'}))

    item_10 = forms.IntegerField(label='A10 kiriting:', required=True,
                                 widget=forms.NumberInput(attrs={'placeholder': 'A21'}))
    item_11 = forms.IntegerField(label='A11 kiriting:', required=True,
                                 widget=forms.NumberInput(attrs={'placeholder': 'A22'}))
    item_12 = forms.IntegerField(label='A12 kiriting:', required=True,
                                 widget=forms.NumberInput(attrs={'placeholder': 'A23'}))
    item_13 = forms.IntegerField(label='A13 kiriting:', required=True,
                                 widget=forms.NumberInput(attrs={'placeholder': 'A24'}))

    item_20 = forms.IntegerField(label='A20 kiriting:', required=True,
                                 widget=forms.NumberInput(attrs={'placeholder': 'A31'}))
    item_21 = forms.IntegerField(label='A21 kiriting:', required=True,
                                 widget=forms.NumberInput(attrs={'placeholder': 'A32'}))
    item_22 = forms.IntegerField(label='A22 kiriting:', required=True,
                                 widget=forms.NumberInput(attrs={'placeholder': 'A33'}))
    item_23 = forms.IntegerField(label='A23 kiriting:', required=True,
                                 widget=forms.NumberInput(attrs={'placeholder': 'A34'}))

    item_30 = forms.IntegerField(label='A30 kiriting:', required=True,
                                 widget=forms.NumberInput(attrs={'placeholder': 'A41'}))
    item_31 = forms.IntegerField(label='A31 kiriting:', required=True,
                                 widget=forms.NumberInput(attrs={'placeholder': 'A42'}))
    item_32 = forms.IntegerField(label='A32 kiriting:', required=True,
                                 widget=forms.NumberInput(attrs={'placeholder': 'A43'}))
    item_33 = forms.IntegerField(label='A33 kiriting:', required=True,
                                 widget=forms.NumberInput(attrs={'placeholder': 'A44'}))
