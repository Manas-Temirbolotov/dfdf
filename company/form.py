from django import forms

from .models import Block, Flat


class BlockForm(forms.ModelForm):
    class Meta:
        model = Block
        fields = '__all__'


class FlatForm(forms.ModelForm):
    class Meta:
        model = Flat
        fields = '__all__'
