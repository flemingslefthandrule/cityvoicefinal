# Generated by Django 5.0.3 on 2024-03-11 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_polloption_pollvote_poll'),
    ]

    operations = [
        migrations.AddField(
            model_name='polloption',
            name='vote_count',
            field=models.IntegerField(default=0),
        ),
    ]
