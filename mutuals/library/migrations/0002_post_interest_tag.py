# Generated by Django 4.1.3 on 2022-11-21 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='interest_tag',
            field=models.ManyToManyField(related_name='post_interest', to='library.interest'),
        ),
    ]
