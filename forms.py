from django import forms


class FileForm(forms.Form):
    file = forms.FileField(max_length=20, label="Наименование файла")  # post


class ResultForm(forms.Form):
    result = forms.CharField(label="Результат")  # get










