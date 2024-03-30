from django import forms

class TalabaForm(forms.Form):
    ism = forms.CharField(required=True, max_length=50)
    guruh = forms.CharField(max_length=255)
    kurs = forms.IntegerField(min_value=1, max_value=5)
    kitob_soni = forms.IntegerField(min_value=0, label="Kitob soni")

class MuallifForm(forms.ModelForm):
    class Meta:
        model = Muallif
        fields = '__all__'