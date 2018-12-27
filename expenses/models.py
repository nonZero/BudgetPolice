from django.db import models


# ORM: Object-Relational-Mapper

class Expense(models.Model):
    date = models.DateField()
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
