from unittest import TestCase

from django.contrib.auth.models import User

from forum.forms import TopicForm, CommentForm
from forum.models import Topic, Comment


class TestTopic(TestCase):

    def test_topic_text_more_then_can(self):
        text_for_topic = 'eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee' \
                         'eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee' \
                         'eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee' \
                         'eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee' \
                         'eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee' \
                         'eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee'

        topic = Topic(text=text_for_topic, owner=None)

        self.assertEqual(topic.text, text_for_topic)

    def test_topic_text(self):
        text = 'Hey boob'
        topic = Topic(text=text)
        self.assertEqual(topic.text, text)

    def test_owner(self):
        user = User.objects.create(username='alfred')
        topic = Topic(owner=user, text='la', subject='ta')
        self.assertEqual(topic.owner.username, 'alfred')
        self.assertEqual(topic.__str__(), 'ta la')


class TestComment(TestCase):
    def test_comment_text_more_then_can(self):
        text_for_commen = 'eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee' \
                         'eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee' \
                         'eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee' \
                         'eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee' \
                         'eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee' \
                         'eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee'

        comment = Comment(text=text_for_commen, topic=Topic(text='t'))

        self.assertEqual(comment.__str__(), text_for_commen[:50] + '...')

    def test_return(self):
        comment = Comment(text='ddd', topic=Topic(text='t'))

        self.assertEqual(comment.__str__(), 'ddd')

    def test_topic(self):
        topic = Topic(text='dd', id=1)
        comment = Comment(topic=topic, text='fd')
        self.assertEqual(comment.topic, topic)
        topic.delete()
        self.assertNotEqual(comment, None)

class TestTopicForm(TestCase):

    def test_topic_form_valdi(self):
        form = TopicForm(data={
            'text': 'hej',
            'subject': 'cos',
        })

        self.assertTrue(form.is_valid())

    def test_topic_form_is_not_valid(self):
        form = TopicForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)

class TestCommentForm(TestCase):

    def test_comment_form_valid(self):
        form = CommentForm(data={
            'text': 'hej'
        })

        self.assertTrue(form.is_valid())

    def test_comment_form_is_not_valid(self):
        form = CommentForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)
