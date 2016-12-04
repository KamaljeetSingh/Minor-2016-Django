from django.contrib.auth.models import User
from django.shortcuts import render,  redirect
from django.views.generic import View
from .forms import UserForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, StreamingHttpResponse
from .models import *
from rest_framework.views import APIView
import json
from Home.serializers import UsersinfoSerializers
from rest_framework.response import Response
from Cards.models import *
from django.http import Http404
from rest_framework import status
import logging
import os
import urllib.request
from Minor2k16.settings import BASE_DIR,MEDIA_ROOT

from django.core import files
from django.core.files import File
# Create your views here.
'''
json loads -> returns an object from a string representing a json object.
json dumps -> returns a string representing a json object from an object.
'''

class LoginFormView(View):
    form_class = LoginForm
    template_name = 'Home/index.html'

    def get(self, request):
        if request.user.is_authenticated():
            return redirect('cards:CardsProjects_All')
        form = self.form_class(None)
        return render(request, self.template_name,{})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:

            if user.is_active:
                login(request, user)
                return redirect('cards:CardsProjects_All')
        return HttpResponse('<p>Sorry ! Your Username and Password dont match.</p>')


class UserFormView(View):
    form_class = UserForm
    template_name = 'Home/registrationform.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            u = Usersinfo()
            us = User.objects.get(pk=user.pk)
            u.no = us
            u.save()
            st = Status()
            st.save()
            st.username = username
            c_id = Card_id.objects.get(key="manobhav")
            st.card_id.add(c_id)
            st.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('cards:CardsProjects_All')
        return render(request, self.template_name, {'form': form})

def logout_view(request):
    logout(request)
    return redirect('Home:welcome')


def board(request):
    return render(request, 'Home/base.html', {})


'''JSON'''
class Usersinfolist(APIView):

    def get(self, request, user):
        u = User.objects.get(username=user)
        user = Usersinfo.objects.get(no=u.pk)
        b = user.boards.all()
        serializer = UsersinfoSerializers(b, many=True)
        return Response(serializer.data)

    def post(self, request, user):
        username = request.POST['name']
        '''received_data = json.dumps(request.data)
        json_data = json.loads(received_data)
        return HttpResponse(json.dumps(json_data['uuid']))
        '''
        logging.warning(username)
        return HttpResponse("okay manobhav.")


class requests(APIView):
    def get(self, request):
        return HttpResponse("mai sab kaam phle karta hu")

    def post(self, request):
        usern = request.POST['username']
        json_data = request.POST['insertstatus']
        json_data_del = request.POST['deletestatus']
        json_cards = request.POST['insertcards']
        json_d_cards = request.POST['deletecards']

        if json_data is not '':                               #insert
            json_data_new = json.loads(json_data)
            logging.warning("insert mujme")
            for x in json_data_new:
                logging.warning(x['key'])
                card_id = Card_id.objects.get(key=x['key'])
                st = Status.objects.get(username=usern)
                st.card_id.add(card_id)
                st.save()

        if json_data_del is not '':                            #delete
            json_data_new_del = json.loads(json_data_del)
            logging.warning("delete mujme")
            for x in json_data_new_del:
                if x['key'] != 'manobhav':
                    st = Status.objects.get(username=usern)
                    card = Card_id.objects.get(key=x['key'])
                    st.card_id.remove(card)
                    st.save()

        if json_d_cards is not '':  # delete cards from admin
            json_cards_delete = json.loads(json_d_cards)
            logging.warning(json_cards_delete)
            logging.warning("deleteee")
            for x in json_cards_delete:
                if x['key'] != 'manobhav':
                    st = Status.objects.get(username=usern)
                    card = Card_id.objects.get(key=x['key'])
                    st.card_id.remove(card)
                    st.save()
                    card = Cards.objects.get(key=x['key'])
                    card.delete()

        if json_cards is not '':                                 #make new cards from admin
            json_cards_insert = json.loads(json_cards)
            logging.warning("insert")
            logging.warning(json_cards_insert)
            for x in json_cards_insert:
                cardnew = Cards()
                u = User.objects.get(username=usern)
                uinfo = Usersinfo.objects.get(no=u)
                cardnew.save()
                cardnew.key = x['key']
                cardnew.change = int(x['change'])
                cardnew.save()
                logging.warning(x['key'])
                logging.warning(x['change'])
                uinfo.cards.add(cardnew)
                uinfo.save()
                ob = Card_id()
                ob.key = cardnew.key
                ob.save()
                card_id = Card_id.objects.get(key=x['key'])
                st = Status.objects.get(username=usern)
                st.card_id.add(card_id)
                st.save()
                for y in x['database']:
                    logging.warning(y['type'])

                    if int(y['type']) == 0:                 #title
                        datanew = Data()
                        datanew.type = 0
                        datanew.data = y['data']
                        datanew.save()
                        cardnew.database.add(datanew)
                        cardnew.save()

                    elif int(y['type']) == 1:                 #description
                        datanew = Data()
                        datanew.type = 1
                        datanew.data = y['data']
                        datanew.save()
                        cardnew.database.add(datanew)
                        cardnew.save()

                    elif int(y['type']) == 2:                  #image
                        datanew = Data()
                        datanew.type = 2
                        datanew.data = "./" + y['data']
                        datanew.save()
                        cardnew.database.add(datanew)
                        cardnew.save()

                    elif int(y['type']) == 3:                  #checklist
                        json_check = json.loads(y['data'])
                        logging.warning(json_check)
                        c = Checklist()
                        c.title = "Default"
                        c.save()
                        data = Data()
                        data.type = 3
                        data.save()
                        for xc in json_check:
                            ci = ChecklistItems()
                            ci.Check_title = c
                            ci.item = xc['item']
                            ci.done = bool(xc['done'])
                            ci.save()
                            data.checklist.add(ci)
                            data.save()
                            cardnew.database.add(data)
                            cardnew.save()

        return HttpResponse("okay manobhav.")


class Photo(APIView):
    def post(self, request):
        card_attach = CardsAttach()
        card_attach.photo = request.FILES['upload_photo']
        card_attach.save()
        return HttpResponse("yes file done")

