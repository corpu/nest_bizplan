from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from recaptcha.client import captcha

from nest_bizplan.forms import EntryForm
from nest_bizplan.models import Entry

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
            new_entry = form.save()
            
            # Send e-mail to applicant
            subject = 'Education Business Plan Competition - Application Received '
            body = 'Thank you for entering the Milken-PennGSE Education Business Plan Competition! We have received your application. All applications will be reviewed by a panel of judges. Some applicants will then be invited to continue to the next round of the competition, as semi-finalists. We expect that semi-finalists will be announced by January 25, 2011. We will be in touch then - thank you, and best of luck!'
            send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [new_entry.email])
            
            return HttpResponseRedirect('/business-plan-competition-thanks/')
    else:
        form = EntryForm()
    
    return render_to_response('nest_bizplan/entry_form.html', {'form': form, 'html_captcha': html_captcha}, context_instance=RequestContext(request))

def judge_listing(request):
    entries = Entry.objects.all().order_by('id',)
    
    return render_to_response('nest_bizplan/judge_listing.html', {'entries': entries}, context_instance=RequestContext(request))

def judge_entry(request, entry_id = None):
    entry = get_object_or_404(Entry, id=entry_id)
    
    return render_to_response('nest_bizplan/judge_entry.html', {'entry': entry}, context_instance=RequestContext(request))
