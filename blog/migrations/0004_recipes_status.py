# Generated by Django 3.2.23 on 2023-12-13 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_description_recipes_instructions'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0),
        ),
    ]
