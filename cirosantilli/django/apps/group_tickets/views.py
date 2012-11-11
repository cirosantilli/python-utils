from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import user_passes_test

from polls.models import Choice, Poll

##without generic templates:

#def index(request):
    #latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
        #t = loader.get_template('polls/index.html')
        #c = Context({
            #'latest_poll_list': latest_poll_list,
        #})
        #return HttpResponse(t.render(c))

#shortcut to the above
#def index(request):
    #latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    #return render_to_response('polls/index.html', {'latest_poll_list': latest_poll_list})

#def detail(request, poll_id):
    #p = get_object_or_404(Poll, pk=poll_id)
    #return render_to_response('polls/detail.html', {'poll': p})

#def results(request, poll_id):
    #p = get_object_or_404(Poll, pk=poll_id)
    #return render_to_response('polls/results.html', {'poll': p})

#@login_required #if not, go to login page
#@permission_required('polls.can_vote') #simplified user_passes_test for single db permission
#@user_passes_test(lambda u: u.has_perm('polls.can_vote', login_url=None)) #if not go to login_url page
def vote(request, poll_id):

    poll = get_object_or_404(Poll, pk=poll_id)

    try:

        selected_choice = poll.choice_set.get(pk=request.POST['choice'])
        #request.POST is the POST to python interface

    except (KeyError, Choice.DoesNotExist):

        return render_to_response('polls/detail.html', {
            'poll': poll,
            'error_message': "you didn't select a choice.",
        }, context_instance=RequestContext(request))
        #redisplay the poll voting form.

    else:

        if request.user.is_authenticated():

            if request.user.has_perm('polls.can_vote'):

                if not poll.has_user_voted(request.user):

                    selected_choice.votes += 1
                    selected_choice.save()
                    #saves the modified object to db

                    poll.set_user_has_voted(request.user)

                    return HttpResponseRedirect(reverse('poll_results', args=(poll.id,)))
                    #Always return an HttpResponseRedirect after successfully dealing
                    #with POST data. This prevents data from being posted twice if a
                    #user hits the Back button.

                return HttpResponse('you have already voted once, cheater!')

            else:

                return HttpResponse('you dont have permission to vote for polls')

        else:

            #return HttpResponse('you must be logged in to vote') #returns this exact response. test only.
            return render_to_response('polls/cant_vote.html') #renders and returns