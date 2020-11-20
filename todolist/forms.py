from django import forms

class TodoListForm(for,s.Form):
    text = forms.CharField(max-length=45,
        widget = forms.TextInput(
            attrs = {'class' : 'form-control', 'placeholder' : 'Enter todo e.g. Wash my car', 'aria-label' : 'Todo', 'aria-describedby' : 'dd-btn'}))
    