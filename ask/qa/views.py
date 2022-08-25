from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator


def paginate(request, qs):
     try: 
        page = int(requests.GET.get('page', 1))
     except ValueError:
        raise Http404
    paginator = Paginator(qs, limit=10)
    paginator.baseurl = '/?page='
    try: 
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page
        
        

@require_GET
def home(request, *args, **kwargs):
    return HttpResponse('OK')

@require_GET
def new(request):
    qs = Question.objects.new()
    paginator = Paginator(qs, limit=10)
    page = paginate(request, qs)
    
    return render(request, 'new.html',  {
        
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,    
    })
   
   
@require_GET
def popular(request):
    qs = Question.objects.popular()
    paginator = Paginator(qs, limit=10) 
    page = paginate(request, qs)
    
    return render(request, 'popular.html',  {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })
    

@require_GET
def question_details(request, id):
    question = get_object_or_404(Question, id=id)

    return render(request, 'question_details.html',  {
        'question': question,
        'id': id,    
    })

