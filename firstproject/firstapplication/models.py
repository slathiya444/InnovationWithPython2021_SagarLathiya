from django.db import models

# Create your models here.
class firstmodel(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length=30)
    ids = models.CharField(max_length = 5)
    contact = models.CharField(max_length = 10)

    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name, )
        # return self.first_name

