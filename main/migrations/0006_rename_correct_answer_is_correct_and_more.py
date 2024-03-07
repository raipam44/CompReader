# Generated by Django 5.0.2 on 2024-03-07 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_question_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='correct',
            new_name='is_correct',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='answers',
            field=models.ManyToManyField(related_name='questions', to='main.answer'),
        ),
    ]
