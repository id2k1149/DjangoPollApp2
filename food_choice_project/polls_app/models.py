from django.db import models


# Create your models here.
class Diner(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=32, unique=False)
    price = models.DecimalField(decimal_places=2, default=0, max_digits=5)

    def __str__(self):
        return self.name


class Menu(models.Model):
    created = models.DateField(auto_now_add=True)
    diner_id = models.ForeignKey(Diner, on_delete=models.CASCADE)
    dish_id = models.ForeignKey(Dish, on_delete=models.CASCADE)
    is_actual = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Menu'


class User(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class Vote(models.Model):
    vote_date = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    diner_id = models.ForeignKey(Diner, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)


class Result(models.Model):
    poll_date = models.DateField(auto_now_add=True)
    diner_id = models.ForeignKey(Diner, on_delete=models.CASCADE)
    votes = models.PositiveIntegerField(default=0)
