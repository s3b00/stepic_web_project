from django.views.decorators.http import require_GET

from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render, get_object_or_404, Http404

from .forms import AskForm, AnswerForm
from .models import Question, Answer


@require_GET
def test(request, *args, **kwargs):
    return HttpResponse('OK')


@require_GET
def get_new(request, *args, **kwargs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 10:
        limit = 10

    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        page = 1

    paginator = Paginator(Question.objects.new(), limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return render(request, 'news.html', {
        'paginator': paginator,
        'page': page,
        'questions': page.object_list
    })


@require_GET
def populars(request):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 10:
        limit = 10

    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        page = 1

    paginator = Paginator(Question.objects.popular(), limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return render(request, 'populars.html', {
        'paginator': paginator,
        'page': page,
        'questions': page.object_list
    })


def get_question(request, pk):
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save()
            answer.save()
    else:
        form = AnswerForm()
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'question_details.html', {
        'question': question,
        'form': form,
    })


def ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'add_question.html', {
        'form': form,
    })
