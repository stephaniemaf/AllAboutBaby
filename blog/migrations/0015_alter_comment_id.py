# Generated by Django 3.2.23 on 2024-04-02 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_comment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]