# Generated by Django 4.2.1 on 2023-06-12 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_user_major'),
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentId', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('major', models.CharField(max_length=100)),
                ('iq', models.CharField(max_length=100)),
                ('interestOutsideInformatic', models.CharField(max_length=100)),
                ('interestOutsideInformatic_2', models.CharField(max_length=100)),
                ('interestOutsideInformatic_3', models.CharField(max_length=100)),
                ('interestOutsideInformatic_4', models.CharField(max_length=100)),
                ('interestInsideInformatic', models.CharField(max_length=100)),
                ('interestInsideInformatic_2', models.CharField(max_length=100)),
                ('interestInsideInformatic_3', models.CharField(max_length=100)),
                ('interestInsideInformatic_4', models.CharField(max_length=100)),
                ('hobby', models.CharField(max_length=100)),
                ('hobby_2', models.CharField(max_length=100)),
                ('hobby_3', models.CharField(max_length=100)),
                ('hobby_4', models.CharField(max_length=100)),
                ('hobby_5', models.CharField(max_length=100)),
                ('hobby_6', models.CharField(max_length=100)),
                ('hobby_7', models.CharField(max_length=100)),
                ('hobby_8', models.CharField(max_length=100)),
                ('hobby_9', models.CharField(max_length=100)),
                ('juniorNetworkAdministrator', models.CharField(max_length=100)),
                ('juniorWebProgramer', models.CharField(max_length=100)),
                ('juniorProgramer', models.CharField(max_length=100)),
            ],
        ),
    ]
