# Generated by Django 3.2.23 on 2024-04-02 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_alter_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0),
        ),
    ]
