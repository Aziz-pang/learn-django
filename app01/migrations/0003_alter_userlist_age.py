# Generated by Django 4.2.1 on 2023-05-28 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_userlist_age_userlist_remark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlist',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
