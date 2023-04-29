from django.contrib import admin

from .models import Card, CardSets

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('id', "card_set", 'question')

@admin.register(CardSets)
class CardSetsAdmin(admin.ModelAdmin):
    list_display = ('id',  'set_name')