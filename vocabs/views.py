from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Dictionary

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

def vote(request, vocab_id):
    vocab = get_object_or_404(Dictionary, pk=vocab_id)
    vocab.update_total_attempts()

    if request.POST['answer'] == "Correct":
        vocab.increment_attempt()
    else:
        vocab.update_total_false_attempts()
        print("False attempts {}".format(vocab.total_false_attempts))
        if vocab.total_false_attempts > 1:
            vocab.decrement_attempts()
            if vocab.total_false_attempts > 2:
                pass
                # TODO: add return logic
                return HttpResponseRedirect(reverse('vocabs:detail', args=(vocab.id, "example")))


    vocab.save()
    return HttpResponseRedirect(reverse('vocabs:results', args=(vocab.id,)))

