from django.db import models


class CardSets(models.Model):
    set_name = models.CharField(max_length=100)
    set_description = models.CharField(max_length=200, default="")
    checked = models.BooleanField(default=0)
    def __str__(self):
        return  self.set_name

NUM_BOXES = 5
BOXES = range(1, NUM_BOXES + 1)

class Card(models.Model):
    card_set = models.ForeignKey(CardSets, on_delete=models.CASCADE)
    question = models.CharField(max_length=100, default="")
    answer = models.CharField(max_length=100, default="")
    box = models.IntegerField(
        choices=zip(BOXES, BOXES),
        default=BOXES[0],
    )
    date_created = models.DateTimeField(auto_now_add=True)

    def move(self, solved):
        new_box = self.box + 1 if solved else BOXES[0]
        if new_box in BOXES:
            self.box = new_box
            self.save()
        return self

    def __str__(self):
        return self.question
