from django import forms

from .models import Note, Todo

class NoteForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    text = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Your note",
                "class": "new-class-name two",
                "id": "my-id-for-textarea",
                "rows": 20,
                "cols": 120,
            }
        )
    )
    favorited = forms.BooleanField()

    class Meta:
        model = Note
        fields = [ 
            'title',
            'text',
            'favorited',
        ]

class TodoForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    task = forms.CharField(
        required = False,
        widget = forms.Textarea(
            attrs = {
                "rows": 20,
                "cols": 120,
            }
        )
    )
    favorited = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    deadline = forms.DateTimeField(required=False, label='Due Date', widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Todo
        fields = [ 
            'title',
            'task',
            'favorited',
            'deadline',
        ]