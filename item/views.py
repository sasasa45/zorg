from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Items, Photos, ProductCode, Spy
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.core.mail import send_mail


# Create your views here.


class ZorgList(ListView):
    template_name = 'list.html'
    model = Items
    context_object_name = 'lists'


class ZorgDetail(DetailView):
    template_name = 'detail.html'
    model = Items
    context_object_name = 'item'

    # slug_field='slug'
    def get(self, request, *args, **kwargs):
        object, created = Spy.objects.get_or_create(ip=request.META['REMOTE_ADDR'], slug=kwargs['slug'])
        if created:
            object.attempts = 1
        else:
            object.attempts += 1
        object.save()
        return super().get(request, *args, **kwargs)

    def post(self, request, slug):
        return super().post(request, slug)


def email(request):
    if request.GET:
        curr_language = request.session.get('language', None)

        if send_mail(request.GET.get('name'), request.GET.get('text') + ' \n ' + request.GET.get('email'),
                     '3org.light@gmail.com', ['3org.light@gmail.com'], fail_silently=False):
            if curr_language == 'RU':
                message = 'Сообщение отправлено'
            elif curr_language == 'EN':
                message = 'Message was sent successfully'
            else:
                message = 'Повідомлення відправлено успішно'

            messages.success(request, message)
        else:
            if curr_language == 'RU':
                message = 'Сообщение не отправлено'
            elif curr_language == 'EN':
                message = 'Message wasn\'t sent'
            else:
                message = 'Повідомлення не відправлено'

            messages.warning(request, message)

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def contact(request):
    return render(request, 'contacts.html')


def info_code(request):
    code = 'Enter'
    if request.GET:
        try:
            code = ProductCode.objects.get(code=request.GET.get('code'))
        except:
            code = ProductCode.objects.none()
    context = {'prod_info': code}
    return render(request, 'info.html', context)


def language(request, slug):
    """change language"""
    if request.session.get('language', False) != slug:
        request.session['language'] = slug
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
