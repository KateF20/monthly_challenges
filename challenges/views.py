from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
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
    'december': 'get on vacation',
}


def index(request):
    list_items = ''
    months = list(challenges.keys())

    for month in months:
        month_url = reverse('monthly-challenge-str', args=[month])
        list_items += f'<li><a href=\'{month_url}\'>{month.capitalize()}</a></li>'

    response_data = f'<ul>{list_items}</ul>'
    return HttpResponse(response_data)


def monthly_challenges(request, month):
    try:
        message = challenges[month]
        return HttpResponse(str(month).title() + ' challenge: ' + message)

    except KeyError:
        return HttpResponseNotFound('No such month')


def monthly_challenges_by_num(request, month):
    months = list(challenges.keys())
    if not 0 < month <= len(months):
        return HttpResponseNotFound('No such month')

    redirect_month = months[month - 1]
    redirect_url = reverse('monthly-challenge-str', args=[redirect_month])

    return HttpResponseRedirect(redirect_url)
