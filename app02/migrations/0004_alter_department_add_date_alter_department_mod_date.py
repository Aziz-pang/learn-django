# Generated by Django 4.2.2 on 2023-06-13 02:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app02', '0003_remove_department_ct_department_add_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='add_date',
            field=models.DateTimeField(db_comment='部门创建时间', default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='department',
            name='mod_date',
            field=models.DateTimeField(auto_now=True, db_comment='部门修改时间', verbose_name='创建时间'),
        ),
    ]