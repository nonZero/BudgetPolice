# Generated by Django 2.1.4 on 2018-12-27 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
