from django import forms
from . import models



class AddAccount(forms.ModelForm):
    class Meta:
        model = models.Account
        fields = ['userid', 'password','status']

    def __init__(self, *args, **kwargs):
        super(AddAccount, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = ' form-control'
            visible.field.widget.attrs['style'] = 'height: 40px; width: 90%; resize:none'
            visible.field.widget.attrs['resize'] = 'none'
            visible.field.widget.attrs['max'] = '1'
            visible.field.widget.attrs['min'] = '0'



class AddComment(forms.ModelForm):
    class Meta:
        model = models.Comments
        fields = ['title']

    def __init__(self, *args, **kwargs):
        super(AddComment, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = ' form-control'
            visible.field.widget.attrs['style'] = 'height: 43px; width: width: 90%; resize:none'
            visible.field.widget.attrs['resize'] = 'none'

