from unittest import TestCase

from django.contrib.auth.models import User
from django.test import TestCase

from staff.models import Staff, Comment


class TestStaff(TestCase):

    # def test_score(self):
    # staff = Staff()
    # Comment1 = Comment(score=3, staff=staff)
    # Comment2 = Comment(score=4, staff=staff)
    # self.assertEqual(staff.score, 3.5)

    def test_name(self):
        staff = Staff(firstname='l', secondname='b')
        self.assertEqual(staff.firstname, 'l')
        self.assertEqual(staff.secondname, 'b')
        self.assertEqual(staff.name(), 'l b')
        self.assertEqual(str(staff), 'l b')

    def test_link(self):
        staff = Staff(
            link='https://stackoverflow.com/questions/56820/round-in-python-doesnt-seem-to-be-rounding-properly')
        self.assertEqual(staff.link,
                         'https://stackoverflow.com/questions/56820/round-in-python-doesnt-seem-to-be-rounding-properly')


class TestComment(TestCase):
    def test_user_goot(self):
        user = User()
        user1 = User()
        comment = Comment(owner=user)
        self.assertEqual(comment.owner, user)
        self.assertNotEqual(comment.owner, user1)

    def test_staff_goot(self):
        staff = Staff()
        staff1 = Staff()
        comment = Comment(staff=staff)
        self.assertEqual(comment.staff, staff)
        self.assertNotEqual(comment.staff, staff1)

    def test_score_good(self):
        comment = Comment(score=3)
        self.assertEqual(comment.score, 3)
