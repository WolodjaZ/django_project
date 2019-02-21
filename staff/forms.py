from django.forms import ModelForm, Textarea, forms

from staff.models import Staff, Comment

class StaffForm(ModelForm):

    link = forms.Field(required=False)

    class Meta:
        model = Staff
        fields = {'firstname', 'secondname', 'academic_rank', 'link'}
        labels = {'firstname': 'Imie', 'secondname': 'Nazwisko', 'academic_rank': 'tytuł',
                  'link': 'link do jego strony'}


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['subject', 'score', 'text']
        labels = {'subject': 'Przedmiot', 'score': 'Ocena', 'text': 'opis'}
        widgets = {'text': Textarea(attrs={'cols': 80, 'rows': 20})}