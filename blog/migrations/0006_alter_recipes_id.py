# Generated by Django 3.2.23 on 2023-12-13 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20231213_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
