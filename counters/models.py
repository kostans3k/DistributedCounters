from django.db import models

# Create your models here.


class Counter(models.Model):
    name = models.CharField(max_length=32)
    value = models.IntegerField()
    #author = models.ForeignKey(User)
    #template_id = models.IntegerField()
    #text = HTMLField()
    #roles = models.ManyToManyField(Role, verbose_name="Who can see this section")
    #length = models.IntegerField(verbose_name="Section length in hours")
    #active = models.BooleanField(default=True, verbose_name="False when deleted")

    #def __unicode__(self):
    #    return 'Name: %s, Author: %s, Template_id: %s' % (self.name, self.author.username, self.template_id)
