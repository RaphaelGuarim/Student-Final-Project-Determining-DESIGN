# Generated by Django 4.2.1 on 2023-06-05 04:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_user_delete_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='major',
            field=models.CharField(default=django.utils.timezone.now, max_length=100), # type: ignore
            preserve_default=False,
        ),
    ]