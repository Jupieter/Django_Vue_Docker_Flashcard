import django
django.setup()
from unittest import TestCase
from django.urls import resolve
from cards.views import CardListView, SetListView, set_change, CardCreateView, CardUpdateView, BoxView

class CardsURLsTestCase(TestCase):
    def test_card_list_url_resolves_to_view(self):
        url = "/"
        resolved_view = resolve(url).func.view_class
        self.assertEqual(resolved_view, CardListView)

    def test_set_list_url_resolves_to_view(self):
        url = "/1"
        resolved_view = resolve(url).func.view_class
        self.assertEqual(resolved_view, SetListView)

    def test_set_change_url_resolves_to_view(self):
        url = "/set_change"
        resolved_view = resolve(url).func
        self.assertEqual(resolved_view, set_change)

    def test_card_create_url_resolves_to_view(self):
        url = "/new"
        resolved_view = resolve(url).func.view_class
        self.assertEqual(resolved_view, CardCreateView)

    def test_card_update_url_resolves_to_view(self):
        url = "/edit/1"
        resolved_view = resolve(url).func.view_class
        self.assertEqual(resolved_view, CardUpdateView)

    def test_box_url_resolves_to_view(self):
        url = "/box/1"
        resolved_view = resolve(url).func.view_class
        self.assertEqual(resolved_view, BoxView)
