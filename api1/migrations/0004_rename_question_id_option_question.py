# Generated by Django 4.1.5 on 2023-02-04 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api1', '0003_rename_question_option_question_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='option',
            old_name='question_id',
            new_name='question',
        ),
    ]
