# Generated by Django 4.2.6 on 2023-10-30 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_question_question_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(default='text', max_length=200),
        ),
    ]
