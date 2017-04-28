from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone
from datetime import timedelta
# Create your models here.
class Course(models.Model):
    is_active = models.BooleanField(default=True)
    title = models.CharField(max_length=50)
    created = models.DateTimeField(default=timezone.now())
    start_date = models.DateTimeField(default=timezone.now())
    end_date = models.DateTimeField(null=True, blank=True)
    abbreviation = models.CharField(
        max_length=10,
        default=self.set_abbr(),
        null=True,
        blank=True,
    )

    def set_abbr(self):
        if self.title is not None:
            return self.title[:9]
        else:
            return None
            
    
    

class CourseItem(models.Model):
    pass

class Contact(models.Model):
    short_name = models.CharField(max_length=40)
    full_name = models.CharField(max_length=40)
    descriptor = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(regex='^\d{10}$', message='Must be 10 numbers, no spaces', code='nomatch')
        ],
        blank=True,
        null=True
    )
    email_address = model.CharField(max_length=100, blank=True, null=True)

    def set_name(self, name):
        self.full_name = name.title()
        name_list = name.split()
        self.short_name = name_list[0].title()

    class Meta:
        abstract = True

class Professor(Contact):
    title = models.CharField(max_length=30, default='Professor')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
class Person(Contact):
    pass

class Event(models.Model):
    pass

class Reminder(models.Model):
    ONE_DAY = timedelta(days=1).total_seconds()
    TWO_DAYS = timedelta(days=2).total_seconds()
    ONE_HOUR = timedelta(hours=1).total_seconds()
    TWO_HOURS = timedelta(hours=2).total_seconds()
    ONE_WEEK = timedelta(days=7).total_seconds()
    REMINDER_CHOICES = (
        (ONE_DAY, 'One day before event'),
        (TWO_DAYS, 'Two days before event'),
        (ONE_HOUR, 'One hour before event'),
        (TWO_HOURS, 'Two hours before event'),
        (ONE_WEEK, 'A week before the event')
    )
    related_event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
    )
    rule = models.FloatField(verbose_name='seconds_before_occurence', choices=REMINDER_CHOICES)
    