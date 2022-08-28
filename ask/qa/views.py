from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.decorators.http import require_GET
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth import login, logout
from qa.forms import *
from qa.models import *

#@require_GET


def paginate(request, qs):
    try: 
       page = int(request.GET.get('page', 1))
    except ValueError:
       raise Http404
    paginator = Paginator(qs, 10)
    try: 
       page = paginator.page(page)
    except EmptyPage:
       page = paginator.page(paginator.num_pages)
    return page, paginator


def new(request):
    qs = Question.objects.new()
    
    page, paginator = paginate(request, qs)
    paginator.baseurl = reverse('new') + '?page='
    
    return render(request, 'qa/new.html',  {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,    
    })
   
   
def popular(request):
    qs = Question.objects.popular()
    
    page, paginator = paginate(request, qs)
    paginator.baseurl = reverse('popular') + '?page='
 
    return render(request, 'qa/popular.html',  {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })
    

def question_details(request, id):
    question = get_object_or_404(Question, id=id)
    answers = question.answer_set.all()

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            form._user = request.user
            answer = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm(initial={'question': str(id)})

    return render(request, 'qa/question_details.html',  {
        'question': question,
        'answers': answers,
        'form': form,
        'id': id,    
    })


def ask_question(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            form._user = request.user
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()

    return render(request, 'qa/create_question.html', {
        'form': form,
    })


def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                url = reverse('new')
                return HttpResponseRedirect(url)
    else:
        form = SignUpForm()

    return render(request, 'qa/signup.html', {
        'form': form,
    })


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                url = reverse('new')
                return HttpResponseRedirect(url)
    else:
        form = LoginForm()

    return render(request, 'qa/login.html', {
        'form': form,
    })


def user_logout(request):
    logout(request)
    url = reverse('login')
    return HttpResponseRedirect(url)
