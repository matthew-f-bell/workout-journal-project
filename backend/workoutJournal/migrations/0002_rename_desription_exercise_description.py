# Generated by Django 4.0.4 on 2022-04-21 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workoutJournal', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercise',
            old_name='desription',
            new_name='description',
        ),
    ]
