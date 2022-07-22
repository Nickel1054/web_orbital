from django import forms
from .models import CelestialBody
from django.forms import CheckboxSelectMultiple
#
BODIES = [obj.name for obj in CelestialBody.objects.all().order_by('a')]
#
#
class CelestialBodiesChecked(forms.Form):
#     def __init__(self, *args, **kwargs):
#
#         super(CelestialBodiesChecked, self).__init__(*args, **kwargs)
#
#         self.fields["name"].widget = CheckboxSelectMultiple()
#         self.fields["name"].queryset = CelestialBody.objects.all().order_by('a')

    bodies = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=BODIES,
    )

    def show_checked(self):
        print(self.cleaned_data)
