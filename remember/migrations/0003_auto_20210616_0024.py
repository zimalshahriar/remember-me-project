# Generated by Django 3.2.4 on 2021-06-15 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remember', '0002_alter_remember_datecompleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remember',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='remember',
            name='datecompleted',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
