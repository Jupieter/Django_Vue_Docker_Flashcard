import django
django.setup()
from django.test import TestCase
from django.urls import reverse
from django.shortcuts import get_object_or_404
from cards.models import Card, CardSets
from cards.views import set_change, CardListView, SetListView, CardCreateView, CardUpdateView, BoxView

class SetChangeViewTest(TestCase):
    def test_set_change_post_valid_form(self):
        card_set = CardSets.objects.create(set_name="Test Set", set_description="Test Description")
        form_data = {"card_set": card_set.id}
        response = self.client.post(reverse("cards:set_change"), data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("cards:set-list", kwargs={"pk": card_set.id}))

    # def test_set_change_post_invalid_form(self):
    #     form_data = {"card_set": 0}
    #     response = self.client.post(reverse("cards:set_change"), data=form_data)
        # self.assertEqual(response.status_code, 200)
        # self.assertTemplateUsed(response, "cards/card_set_form.html")
        # self.assertContains(response, "Fault")

"""     def test_set_change_get(self):
        response = self.client.get(reverse("cards:set_change"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "cards/card_set_form.html") """

""" class CardListViewTest(TestCase):
    def test_card_list_view(self):
        response = self.client.get(reverse("cards:card-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "cards/card_list.html")
        self.assertQuerysetEqual(response.context["object_list"], Card.objects.all().order_by("box", "-date_created")) """

""" class SetListViewTest(TestCase):
    def test_set_list_view(self):
        card_set = CardSets.objects.create(set_name="Test Set", set_description="Test Description")
        response = self.client.get(reverse("cards:set-list", kwargs={"pk": card_set.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "cards/card_list.html")
        self.assertQuerysetEqual(response.context["object_list"], Card.objects.filter(card_set=card_set.id).order_by("box", "-date_created"))
 """
""" class CardCreateViewTest(TestCase):
    def test_card_create_view(self):
        response = self.client.get(reverse("cards:card-create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "cards/card_form.html")
 """
""" class CardUpdateViewTest(TestCase):
    def test_card_update_view(self):
        card = Card.objects.create(card_set=CardSets.objects.create(set_name="Test Set"), question="Test Question", answer="Test Answer", box=1)
        response = self.client.get(reverse("cards:card-update", kwargs={"pk": card.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "cards/card_form.html") """

class BoxViewTest(TestCase):
    def test_box_view(self):
        box_num = 1
        response = self.client.get(reverse("cards:box", kwargs={"box_num": box_num}))
        print(response)
        self.assertEqual(response.status_code, 200)
        # self.assertTemplateUsed(response, "cards/box.html")
        # self.assertQuerysetEqual(response.context["object_list"], Card.objects.filter(box=box_num))