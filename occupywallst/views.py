r"""

    occupywallst.views
    ~~~~~~~~~~~~~~~~~~

    Dynamic web page functions.

"""

from django.contrib import auth
from django.contrib.auth import views as authviews
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.gis.utils import GeoIP
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import Http404, HttpResponseRedirect

from occupywallst.forms import SignupForm
from occupywallst import models as db


def index(request):
    articles = db.Article.objects.order_by('-published')[:25]
    return render_to_response(
        'occupywallst/index.html', {'articles': articles},
        context_instance=RequestContext(request))


def article(request, slug):
    try:
        article = db.Article.objects.get(slug=slug)
    except db.Event.DoesNotExist:
        raise Http404()
    recent = db.Article.objects.order_by('-published')[:5]
    return render_to_response(
        'occupywallst/article.html', {'article': article,
                                      'recent': recent},
        context_instance=RequestContext(request))


def attendees(request):
    response = render_to_response(
        'occupywallst/attendees.html', {},
        context_instance=RequestContext(request))
    return response


def rides(request):
    return render_to_response(
        'occupywallst/rides.html', {},
        context_instance=RequestContext(request))


def housing(request):
    return render_to_response(
        'occupywallst/housing.html', {},
        context_instance=RequestContext(request))


def about(request):
    return render_to_response(
        'occupywallst/about.html', {},
        context_instance=RequestContext(request))


def user_page(request, username):
    try:
        user = db.User.objects.get(username=username)
    except db.User.DoesNotExist:
        raise Http404()
    return render_to_response(
        'occupywallst/user.html', {'user': user},
        context_instance=RequestContext(request))


def login(request):
    return authviews.login(
        request, template_name="occupywallst/login.html")


def logout(request):
    return authviews.logout(
        request, template_name="occupywallst/logged_out.html")


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(user)
            return HttpResponseRedirect(user.get_absolute_url())
    else:
        form = SignupForm()
    return render_to_response(
        'occupywallst/signup.html', {'form': form},
        context_instance=RequestContext(request))
