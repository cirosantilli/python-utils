from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from polls.models import Choice, Poll

##without generic templates

#def index(request):
    #latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    #return render_to_response('polls/index.html', {'latest_poll_list': latest_poll_list})

#def detail(request, poll_id):
    #p = get_object_or_404(Poll, pk=poll_id)
    #return render_to_response('polls/detail.html', {'poll': p})

#def results(request, poll_id):
    #p = get_object_or_404(Poll, pk=poll_id)
    #return render_to_response('polls/results.html', {'poll': p})

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:

        selected_choice = p.choice_set.get(pk=request.POST['choice'])
        #request.POST is the POST to python interface

    except (KeyError, Choice.DoesNotExist):

        return render_to_response('polls/detail.html', {
            'poll': p,
            'error_message': "you didn't select a choice.",
        }, context_instance=requestcontext(request))
        #redisplay the poll voting form.

    else:

        selected_choice.votes += 1

        selected_choice.save()
        #saves the modified object to db

        return HttpResponseRedirect(reverse('poll_results', args=(p.id,)))
        #Always return an HttpResponseRedirect after successfully dealing
        #with POST data. This prevents data from being posted twice if a
        #user hits the Back button.
