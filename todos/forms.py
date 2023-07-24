from django import forms
from .models import Todo
from django.core.exceptions import ValidationError


class TodoForm(forms.ModelForm):
    completed = forms.IntegerField(required=False, initial=bool, widget=forms.Textarea)

    class Meta:
        model = Todo
        fields = ['title', 'description', 'user', 'completed']


    def clean_title(self):
        if len(self.changed_data.get('title')) < 2:
            raise ValidationError('Value mast be more than 1 character')
        self.changed_data.get('title')


class TodoUpdateForm(forms.ModelForm):
    title = forms.CharField(required=False)
    description = forms.CharField(required=False)
    user = forms.CharField(required=False)
    completed = forms.BooleanField(required=False)


    class Meta:
        model = Todo
        fields = '__all__'


    def clean(self):
        cleaned_date = super().clean()
        cleaned_date['title'] = cleaned_date.get('title') or self.instance.title
        cleaned_date['description'] = cleaned_date.get('description') or self.instance.description
        cleaned_date['user'] = cleaned_date.get('user') or self.instance.user
        cleaned_date['completed'] = cleaned_date.get('completed') or self.instance.completed


    def clean_description(self):
        return self.cleaned_data.get('description').replace('/', '').strip()

    class TodoFilterForm(forms.Form):
        title = forms.CharField(required=False)