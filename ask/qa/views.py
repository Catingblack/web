from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.views.decorators.http import require_GET
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator
from qa.models import *


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
        
        
        

@require_GET
def new(request):
    qs = Question.objects.new()
    
    page, paginator = paginate(request, qs)
    paginator.baseurl = reverse('new') + '?page='
    
    return render(request, 'qa/new.html',  {
        
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,    
    })
   
   
@require_GET
def popular(request):
    qs = Question.objects.popular()
    
    page, paginator = paginate(request, qs)
    paginator.baseurl = reverse('popular') + '?page='
 
    return render(request, 'qa/popular.html',  {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })
    

@require_GET
def question_details(request, id):
    question = get_object_or_404(Question, id=id)

    return render(request, 'qa/question_details.html',  {
        'question': question,
        'id': id,    
    })

