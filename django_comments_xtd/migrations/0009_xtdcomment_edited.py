# Generated by Django 3.2.2 on 2021-05-10 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_comments_xtd', '0008_auto_20200920_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='xtdcomment',
            name='edited',
            field=models.BooleanField(blank=True, default=False, help_text='Has comment been edited?'),
        ),
    ]
