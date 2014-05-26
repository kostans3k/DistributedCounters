from django.shortcuts import render, render_to_response, redirect
from counters.models import Counter
from django.template import RequestContext

# Create your views here.


def counters_list(request):
    if request.method == 'GET':
        counters = Counter.objects.all()
        return render_to_response("counters/counters_list.html", {"counters": counters})


def add_counter(request):
    if request.method == 'GET':
        return render_to_response('counters/add_counter.html', context_instance=RequestContext(request))
    if request.method == 'POST':
        counter = Counter()
        counter.name = request.POST["name"]
        counter.value = 0
        counter.save()
        return redirect('counters_list')


def counter_detail(request, counter_id):
    counter = Counter.objects.get(pk=counter_id)
    return render_to_response('counters/counter_detail.html', {"counter": counter}, context_instance=RequestContext(request))


def counter_increase(request, counter_id):
    counter = Counter.objects.get(pk=counter_id)
    counter.value += int(request.GET["increase"])
    counter.save()
    return redirect('counter_detail', counter_id)


def counter_reset(request, counter_id):
    counter = Counter.objects.get(pk=counter_id)
    counter.value = 0
    counter.save()
    return redirect('counter_detail', counter_id)


def home(request):
    return redirect('counters_list')
