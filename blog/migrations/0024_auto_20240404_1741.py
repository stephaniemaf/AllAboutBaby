# Generated by Django 3.2.23 on 2024-04-04 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('blog', '0023_auto_20240404_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='content_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='comment',
            name='object_id',
            field=models.PositiveIntegerField(null=True),
        ),
    ]