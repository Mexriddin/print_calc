from django.db import models
from django.urls import reverse
# from django.contrib.auth.models import User


# Create your models here.

# class Client(models.Model):
#     """Kliyentlar"""
#     # user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
#     name = models.CharField(max_length=200, null=True)
#     phone = models.CharField(max_length=100, null=True)
#     company = models.CharField(max_length=200, null=True)
#     # email = models.CharField(max_length=200, null=True)
#     # profile_pic = models.ImageField(default="profile.png", null=True, blank=True)
#     # date_created = models.DateTimeField(auto_now_add=True, null=True)
#
#     def __str__(self):
#         return self.company + " " + self.name
#
#     class Meta:
#         verbose_name = "Клиент"
#         verbose_name_plural = "Клиенты"

class Paper(models.Model):
    """Qog`ozlar"""
    name = models.CharField(max_length=100, null=True)
    # price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price = models.FloatField(max_length=20,)
    # category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    # description = models.CharField(max_length=200, null=True, blank=True)
    # date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Бумага"
        verbose_name_plural = "Бумаги"


class Format(models.Model):
    """Formatlar"""
    name = models.CharField(max_length=100, null=True)
    format_paper = models.IntegerField(default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Формат"
        verbose_name_plural = "Форматы"


class Print_paper(models.Model):
    """Printerga ketadigan xarajatlar"""
    name = models.CharField(max_length=200, null=True)
    # price_if_before_1000 = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # price_if_after_1000 = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # price_form_print = models.DecimalField( max_digits=10, decimal_places=2, default=0)
    price_if_before_1000 = models.FloatField(max_length=20)
    price_if_after_1000 = models.FloatField(max_length=20)
    price_form_print = models.FloatField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Печать бамагу"
        verbose_name_plural = "Печати бумаг"


class Order(models.Model):
    """Zakazlar"""
    # client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    client_name = models.CharField(max_length=200, null=True)
    client_phone = models.CharField(max_length=100, null=True)
    client_company = models.CharField(max_length=200, null=True)
    count = models.IntegerField(default=1)
    paper = models.ForeignKey(Paper, null=True, on_delete=models.SET_NULL)
    format_p = models.ForeignKey(Format, null=True,on_delete=models.CASCADE)
    print_paper = models.ForeignKey(Print_paper, null=True,on_delete=models.CASCADE)
    # total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.FloatField(max_length=20, blank=True, null=True, default=True)
    # price_for_one = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price_for_one = models.FloatField(max_length=20, blank=True, null=True, default=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.client_name + "-" + str(self.count)

    def get_absolute_url(self):
        return reverse('home')

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def save(self, *args, **kwargs):
        price_for_paper = ((self.paper.price) / self.format_p.format_paper) * self.count
        print("price_for_paper:{}".format(price_for_paper))
        price_for_print = self.print_paper.price_form_print
        print("price_for_paper1:{}".format(price_for_print))
        if self.count <= 1000:
            price_for_print += self.print_paper.price_if_before_1000
        elif self.count >= 1000:
            price_for_print += (self.print_paper.price_if_before_1000 + ((self.count - 1000)/1000)*self.print_paper.price_if_after_1000)
        print("price_for_paper2:{}".format(price_for_print))
        total_price = price_for_paper + price_for_print
        self.total_price = total_price
        self.price_for_one = total_price / self.count

        super(Order, self).save(*args, **kwargs)

