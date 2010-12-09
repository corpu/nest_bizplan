from django.core.validators import MaxLengthValidator
from django.db import models

# Create your models here.
class Entry(models.Model):
    """An entry for round 1 of the business plan competition"""
    first_name = models.CharField('Contact First Name', max_length=200)
    last_name = models.CharField('Contact Last Name', max_length=200)
    applicant = models.CharField('Formal Applicant', max_length=200)
    job_title = models.CharField(max_length=200, blank=True, null=True)
    organization = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField()
    city = models.CharField(max_length=200)
    state = models.CharField('State/Province', max_length=200)
    country = models.CharField(max_length=200)
    
    problem = models.TextField(validators=[MaxLengthValidator(1500)])
    solution = models.TextField(validators=[MaxLengthValidator(3000)])
    execution = models.TextField(validators=[MaxLengthValidator(2000)])
    
    # Startl Prize Fields
    is_startl_applicant = models.BooleanField(default=False)
    startl_fiscally_sustainable = models.TextField(blank=True, null=True)
    startl_enable_access = models.TextField(blank=True, null=True)
    startl_reduce_cost = models.TextField(blank=True, null=True)
    
    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name,)
    
    class Meta:
        verbose_name_plural = 'Entries'
    
