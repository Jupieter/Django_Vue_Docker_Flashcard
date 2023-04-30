from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
import random
from django.views.generic import ListView, CreateView, UpdateView
from .forms import CardCheckForm, ChangeSetForm

from .models import Card, CardSets

def set_change(request):   
    if request.method == "POST":
        form = ChangeSetForm(request.POST)
        if form.is_valid():
            choice = form.save(commit=False)
            pk = choice.card_set.id
            print(type(pk), pk)
            a_dress = 'cards/' + str(pk)
            context = {'pk': pk, 'choice': choice.card_set}
            return redirect('cards:set-list', pk=pk  )
        else:
            context = {'choice': "Fault"}
            return render(request, 'cards:set-list', context )
        print(context)
    else:
        form = ChangeSetForm()
    return render(request, 'cards/card_set_form.html', {'form': form})

class CardListView(ListView):
    model = Card
    queryset = Card.objects.all().order_by("box", "-date_created")


class SetListView(ListView):
    model = Card
    
    def get_queryset(self):
        card_set = get_object_or_404(CardSets, pk=self.kwargs["pk"])
        return Card.objects.filter(card_set=self.kwargs["pk"]).order_by("box", "-date_created")


class CardCreateView(CreateView):
    model = Card
    fields = ["card_set", "question", "answer", "box"]
    success_url = reverse_lazy("card-create")


class CardUpdateView(CardCreateView, UpdateView):
    success_url = reverse_lazy("card-list")


class BoxView(CardListView):
    template_name = "cards/box.html"
    form_class = CardCheckForm

    def get_queryset(self):
        return Card.objects.filter(box=self.kwargs["box_num"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["box_number"] = self.kwargs["box_num"]
        if self.object_list:
            context["check_card"] = random.choice(self.object_list)
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            card = get_object_or_404(Card, id=form.cleaned_data["card_id"])
            card.move(form.cleaned_data["solved"])

        return redirect(request.META.get("HTTP_REFERER"))