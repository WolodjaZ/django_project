from django.forms import ModelForm, Textarea

from forum.models import Topic, Comment


class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ['subject', 'text']
        labels = {'subject': 'Wprowadz temat dyskusji', 'text': ''}
        widgets = {'text': Textarea(attrs={'cols': 80})}

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {'text': 'comment'}
