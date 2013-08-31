from django.test import TestCase
from appA import Poll

class TestPoll(TestCase):
    def test_unicode_returns_blah(self):
        p = Poll(question="What's new?")
        self.assertEqual(str(p), "What's new?")
