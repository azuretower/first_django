from django.shortcuts import render
from django.http import HttpResponse
from django.utils.html import escape
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.utils.decorators import method_decorator

from main.models import State, StateCapital, City
# Create your views here.


def first_view(request, starts_with=None):

    states = State.objects.all()

    text_string = ''

    for state in states:
        cities = state.city_set.filter(name__startswith="%s" % starts_with)
        for city in cities:
            text_string += "States: %s , City: %s <br>" % (state, city.name)

    return HttpResponse(text_string)


@csrf_exempt
def get_post(request):

    if request.method == "GET":

        # print request

        city_state_string = """
        <form action="/get_post/" method="POST">

            State:
            </br>
            <input type="text" name="state" />
            </br>

            </br>

            City:
            </br>
            <input type="text" name="city" />
            </br>
            <input type="submit" value="Submit" />

        </form>
        """
        return HttpResponse(city_state_string)

    if request.method == "POST":

        # print request

        city_state_string = """
        <form action="/get_post/" method="POST">

            State:
            </br>
            <input type="text" name="state" />
            </br>

            </br>

            City:
            </br>
            <input type="text" name="city" />
            </br>
            <input type="submit" value="Submit" />

        </form>
        """

        get_state = request.POST.get('state', None)
        get_city = request.POST.get('city', None)

        states = State.objects.filter(name__startswith="%s" % get_state)

        for state in states:
            cities = state.city_set.filter(name__startswith="%s" % get_city)
            for city in cities:
                city_state_string += "<b>%s</b> %s </br>" % (state, city.name)

        response = city_state_string

        return HttpResponse(response)


class GetPost(View):

    form = """
        <form action="/GetPost/" method="POST">

            State:
            </br>
            <input type="text" name="state" />
            </br>

            </br>

            City:
            </br>
            <input type="text" name="city" />
            </br>
            <input type="submit" value="Submit" />

        </form>
        """

    def get(self, request, *args, **kwargs):
        return HttpResponse(self.form)

    def post(self, request, *args, **kwargs):
        get_state = request.POST.get('state', None)
        get_city = request.POST.get('city', None)

        states = State.objects.filter(name__startswith="%s" % get_state)

        for state in states:
            cities = state.city_set.filter(name__startswith="%s" % get_city)
            for city in cities:
                self.form += "<b>%s</b> %s </br>" % (state, city.name)

        response = self.form

        return HttpResponse(response)
