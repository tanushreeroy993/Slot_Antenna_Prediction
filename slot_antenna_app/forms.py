# slot_antenna_app/forms.py
from django import forms

class AntennaForm(forms.Form):
    number_of_loop = forms.ChoiceField(choices=[('2', '2'), ('4', '4')], initial='2')
    l1_outer = forms.FloatField()
    l1_inner = forms.FloatField()
    l2_outer = forms.FloatField()
    l2_inner = forms.FloatField()
    l3_outer = forms.FloatField(required=False)
    l3_inner = forms.FloatField(required=False)
    l4_outer = forms.FloatField(required=False)
    l4_inner = forms.FloatField(required=False)
    frequency = forms.FloatField()
    rl_depth = forms.FloatField()