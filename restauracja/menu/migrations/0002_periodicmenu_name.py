# Generated by Django 2.1.3 on 2018-12-19 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='periodicmenu',
            name='name',
            field=models.CharField(default='Menu przykładowe', max_length=200),
        ),
    ]