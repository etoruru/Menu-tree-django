from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=200)


class MenuItem(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    menu = models.ForeignKey("Menu", on_delete=models.CASCADE)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    level = models.IntegerField(default=0)

