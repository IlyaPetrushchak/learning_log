from django.shortcuts import render

from .models import Topic

# Create your views here.

def index(request):
    """"Головна сторінка Журналу спостережень"""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """Відображає всі теми"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


