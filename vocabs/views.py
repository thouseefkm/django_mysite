from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Dictionary, Example
from .forms import DictionaryForm


def index(request):
    vocab = Dictionary.get_random()
    context = {
            'vocab': vocab,
        }
    return render(request, 'vocabs/index.html', context)


def detail(request, vocab_id):
    vocab = get_object_or_404(Dictionary, pk=vocab_id)
    return render(request, 'vocabs/detail.html', {'vocab': vocab})

def results(request, vocab_id):
    vocab = get_object_or_404(Dictionary, pk=vocab_id)
    return render(request, 'vocabs/results.html', {'vocab': vocab})

def results_update(request, vocab_id):
    print("In result update")
    context ={}

    # fetch the object related to passed id
    vocab = get_object_or_404(Dictionary, pk=vocab_id)

    # pass the object as instance in form
    form = DictionaryForm(request.POST or None, instance=vocab)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        print("In result update : It is saving")
        return HttpResponseRedirect(reverse('vocabs:results', args=(vocab_id,)))

    # add form dictionary to context
    context["form"] = form
    context["vocab"] = vocab

    print("In result update it is rendering")
    return render(request, "vocabs/results_update.html", context)


def update(request, vocab_id):
    vocab = get_object_or_404(Dictionary, pk=vocab_id)
    form = request.POST
    print("Printing from Update {}".format(form['example']))
    vocab.example_set.create(example_text=form['example'])

    return render(request, 'vocabs/results.html', {'vocab': vocab})

def vote(request, vocab_id):
    vocab = get_object_or_404(Dictionary, pk=vocab_id)
    vocab.update_total_attempts()

    if request.POST['answer'] == "Correct":
        vocab.increment_attempt()
        vocab.set_last_attempt(value='Right')
    else:
        vocab.update_total_false_attempts()
        vocab.set_last_attempt(value='Wrong')
        print("False attempts {}".format(vocab.total_false_attempts))
        if vocab.total_false_attempts > 1:
            vocab.decrement_attempts()
            if vocab.total_false_attempts > 2:
                context = {'vocab': vocab, }
                return render(request, 'vocabs/detail_example.html', context)


    vocab.save()
    return HttpResponseRedirect(reverse('vocabs:results', args=(vocab.id,)))


def dashboard(request):
    vocab = Dictionary.objects.all()
    context = {
            'vocab': vocab,
            'progress': Dictionary.progress(),
            'ratio': Dictionary.find_ratio(),
            'ratio_per_one': Dictionary.ratio_per_one()
        }
    return render(request, 'vocabs/dashboard.html', context)