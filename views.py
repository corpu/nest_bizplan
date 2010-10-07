from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from recaptcha.client import captcha

from nest_bizplan.forms import EntryForm

def entry_form(request):
    captcha_error = None
    html_captcha = captcha.displayhtml(settings.RECAPTCHA_PUB_KEY)
    
    if request.method == 'POST':
        captcha_response = captcha.submit(request.POST.get("recaptcha_challenge_field", None),  
                  request.POST.get("recaptcha_response_field", None),  
                  settings.RECAPTCHA_PRIVATE_KEY,  
                  request.META.get("REMOTE_ADDR", None))
        form = EntryForm(request.POST)
        if form.is_valid():
            if not captcha_response.is_valid:
                captcha_error = True
                html_captcha = captcha.displayhtml(settings.RECAPTCHA_PUB_KEY)
                return render_to_response('nest_bizplan/entry_form.html', {'form': form, 'captcha_error': captcha_error, 'html_captcha': html_captcha}, context_instance=RequestContext(request))
            form.save()
            return HttpResponseRedirect('/business-plan-competition-thanks/')
    else:
        form = EntryForm()
    
    return render_to_response('nest_bizplan/entry_form.html', {'form': form, 'html_captcha': html_captcha}, context_instance=RequestContext(request))

            