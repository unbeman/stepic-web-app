from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_GET, require_POST

from .models import Question, Answer
from .utils import paginate
from .forms import AskForm, AnswerForm


def test(request, *args, **kwargs):
    return HttpResponse("OK")


@require_GET
def home(request):
    paginator, page = paginate(request, Question.objects.order_by('-added_at'))
    return render(request, 'qa/home.html', {
        'page': page,
        'paginator': paginator,
    })


def question(request, id):
    question = get_object_or_404(Question, id=id)
    answers = question.answer_set.all()
    answer_form = AnswerForm({"question": question.id})
    return render(request, 'qa/question.html', {
        'question': question,
        'answers': answers,
        'form': answer_form
    })

@require_POST
def answer(request):
    form = AnswerForm(request.POST)
    if form.is_valid():
        answer = form.save()
        question = answer.question
        return HttpResponseRedirect(question.get_absolute_url())


@require_GET
def popular(request):
    paginator, page = paginate(request, Question.objects.order_by('-rating'))
    return render(request, 'qa/index.html', {
        'page': page,
        'paginator': paginator
    })


def ask(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            return redirect(question)
    else:
        form = AskForm()
    return render(request, 'qa/ask.html', {'form': form})
