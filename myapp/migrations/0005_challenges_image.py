# Generated by Django 4.0.4 on 2022-06-07 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_workout_categories_workout'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenges',
            name='image',
            field=models.ImageField(default='challenges/default.jpg', upload_to='challenges'),
        ),
    ]
