from django.shortcuts import render, redirect

from .models import Topic, Entry
from .forms import TopicForm, EntryForm
# Create your views here.

def index(request):
    """"Головна сторінка Журналу спостережень"""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """Відображає всі теми"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries':entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """Добавити нову тему"""
    if request.method != 'POST':
        # Жодних данних не відправленно; створити порожню форму
        form = TopicForm()
    else:
        # Відправлений POST; обробити данні
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')

    # Показати порожню або недійсну форму
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        # Жодних данних не відправленно; створити порожню форму
        form = EntryForm()
    else:
        # Відправлений POST; обробити данні
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    # Показати порожню або не дійсну форму
    context = {
        'topic': topic,
        'form': form
        }
    return render(request, 'learning_logs/new_entry.html', context)


def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {
        'entry': entry,
        'topic': topic,
        'form': form
    }
    return render(request, 'learning_logs/edit_entry.html', context)

