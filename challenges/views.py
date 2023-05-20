from django.http import HttpResponseNotFound, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

challenges = {
    'january': 'run',
    'february': 'swim',
    'march': 'sing',
    'april': 'learn python',
    'may': 'learn django',
    'june': 'learn databases',
    'july': 'learn docker',
    'august': 'learn AWS',
    'september': 'learn PostrgreSQL',
    'october': 'learn API',
    'november': 'find a job',
    'december': None,
}


def index(request):
    context = {
        'months': challenges.keys(),
    }
    return render(request, 'challenges/index.html', context)


def monthly_challenges(request, month):
    try:
        challenge_text = challenges[month]
        context = {
            'month': month,
            'text': challenge_text
        }
        return render(request, 'challenges/challenge.html', context)

    except:
        raise Http404


def num_redirect(request, month):
    months = list(challenges.keys())
    if not 0 < month <= len(months):
        return HttpResponseNotFound('No such month')

    redirect_month = months[month - 1]
    redirect_url = reverse('monthly-challenge', args=[redirect_month])

    return HttpResponseRedirect(redirect_url)
