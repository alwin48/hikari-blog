from django import forms

class AddPostForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField()
    #date_time = forms.DateTimeField()
    image_1 = forms.ImageField()
