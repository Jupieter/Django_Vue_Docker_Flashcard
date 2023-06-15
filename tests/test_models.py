# from django.test import TestCase
import django
django.setup()
from unittest import TestCase
from cards.models import CardSets, Card

class CardSetsTestCase(TestCase):
    def setUp(self):
        self.card_set = CardSets.objects.create(
            set_name="Test Set",
            set_description="Test Description",
            checked=True
        )

    def test_card_set_creation(self):
        self.assertEqual(self.card_set.set_name, "Test Set")
        self.assertEqual(self.card_set.set_description, "Test Description")
        self.assertTrue(self.card_set.checked)

    def test_card_set_str_representation(self):
        self.assertEqual(str(self.card_set), "Test Set")


class CardTestCase(TestCase):
    def setUp(self):
        self.card_set = CardSets.objects.create(
            set_name="Test Set",
            set_description="Test Description",
            checked=True
        )
        self.card = Card.objects.create(
            card_set=self.card_set,
            question="Test Question",
            answer="Test Answer",
            box=1
        )

    def test_card_creation(self):
        self.assertEqual(self.card.card_set, self.card_set)
        self.assertEqual(self.card.question, "Test Question")
        self.assertEqual(self.card.answer, "Test Answer")
        self.assertEqual(self.card.box, 1)

    def test_card_move_method(self):
        self.card.move(solved=True)
        self.assertEqual(self.card.box, 2)

        self.card.move(solved=False)
        self.assertEqual(self.card.box, 1)

    def test_card_str_representation(self):
        self.assertEqual(str(self.card), "Test Question")

