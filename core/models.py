from django.db import models

# Create your models here.
class Course(models.Model):
    pass

class CourseItem(models.Model):
    pass

class Contact(models.Model):
    short_name = models.CharField(max_length=40)
    full_name = models.CharField(max_length=40)
    descriptor = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=10, min_length=10,  blank=True, null=True)
    email_address = model.CharField(max_length=100, blank=True, null=True)

    def set_name(self, name):
        self.full_name = name.title()
        name_list = name.split()
        self.short_name = name_list[0].title()




    