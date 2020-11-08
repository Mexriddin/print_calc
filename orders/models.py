from django.db import models
from django.urls import reverse
import math
# from django.contrib.auth.models import User


# Create your models here.


class Paper(models.Model):
    """ Papers """
    name = models.CharField(max_length=100, null=True)
    price = models.FloatField(max_length=20,)
    format_paper = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name + "("+self.format_paper+")"

    class Meta:
        verbose_name = "Бумага"
        verbose_name_plural = "Бумаги"


class Devision(models.Model):
    """ Forms """
    name = models.CharField(max_length=100, null=True)
    division = models.IntegerField(default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Деление"
        verbose_name_plural = "Деление"


class Print_paper(models.Model):
    """ Costs for print """
    name = models.CharField(max_length=200, null=True)
    price_form_print = models.DecimalField( max_digits=10, decimal_places=2, default=0)
    price_if_before_1000 = models.FloatField(max_length=20)
    price_if_after_1000 = models.FloatField(max_length=20)
    price_form_print = models.FloatField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Печать бамагу"
        verbose_name_plural = "Печати бумаг"


class Order(models.Model):
    """ Orders """
    client_name = models.CharField(max_length=200, null=True)
    client_phone = models.CharField(max_length=100, null=True)
    client_company = models.CharField(max_length=200, null=True)
    count = models.IntegerField(default=1)
    paper = models.ForeignKey(Paper, null=True, on_delete=models.SET_NULL)
    devision_paper = models.ForeignKey(Devision, null=True,on_delete=models.CASCADE)
    print_paper = models.ForeignKey(Print_paper, null=True,on_delete=models.CASCADE)
    total_price = models.FloatField(max_length=20, blank=True, null=True, default=True)
    price_for_one = models.FloatField(max_length=20, blank=True, null=True, default=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.client_name + "-" + str(self.count)

    def get_absolute_url(self):
        return reverse('home')

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    """ Calculate cost and save in orders """
    def save(self, *args, **kwargs):
        price_for_paper = ((self.paper.price) / self.devision_paper.division) * self.count
        # print("price_for_paper:{}".format(price_for_paper))
        price_for_print = self.print_paper.price_form_print
        # print("price_for_form:{}".format(price_for_print))
        if self.count <= 1000:
            price_for_print += self.print_paper.price_if_before_1000
        elif self.count >= 1000:
            price_for_print += (self.print_paper.price_if_before_1000 + (math.ceil((self.count - 1000)/1000))*self.print_paper.price_if_after_1000)
        # print("price_for_print:{}".format(price_for_print))
        total_price = price_for_paper + price_for_print
        self.total_price = total_price
        self.price_for_one = total_price / self.count

        super(Order, self).save(*args, **kwargs)

