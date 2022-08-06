from datetime import timedelta
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import *


class QuestionModelTest(TestCase):
    def test_old__published_recently(self):
        time = timezone.now() - timedelta(days=2)
        old_q = Question(pub_date=time)
        self.assertFalse(old_q.was_published_recently())

    def test_future_published_recently(self):
        time = timezone.now() + timedelta(days=2)
        f_q = Question(pub_date=time)
        self.assertFalse(f_q.was_published_recently())

    def test_now_published_recently(self):
        time = timezone.now()
        n_q = Question(pub_date=time)
        self.assertTrue(n_q.was_published_recently())

    def test_client1(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++2")
        Question.objects.create(text="uuu")
        Question.objects.create(text="uy")
        Question.objects.create(text="uu")
        myq = Question.objects.all().order_by('pub_date')[:2]
        res = self.client.get(reverse('indexxx'))
        self.assertEqual(res.status_code, 200)
        self.assertQuerysetEqual(res.context["questions"], myq)

    def test_client2(self):
        Question.objects.create(text="uuu")
        Question.objects.create(text="uy")
        Question.objects.create(text="uu")
        res = self.client.get(reverse('indexx', args=[6]))
        self.assertEqual(res.status_code,404)
    # Create your tests here.
