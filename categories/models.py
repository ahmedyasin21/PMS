from django.db import models
from django.urls import reverse
from source.utils import category_unique_slug_generator
from django.db.models.signals import pre_save
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class ShopCategory(models.Model):

    
    name = models.CharField(("Pharmacy catagories"), max_length=150)
    slug = models.SlugField(blank =True,unique = True)

    class Meta:
        verbose_name = _("Pharmacy Category")
        verbose_name_plural = _("Pharmacy Categories")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("categories:categories_detail", kwargs={"slug": self.slug})


def shopcategory_pre_save_reciever(sender,instance,*args, **kwargs):
    if not instance.slug:
        instance.slug = category_unique_slug_generator(instance)
pre_save.connect(shopcategory_pre_save_reciever,ShopCategory)