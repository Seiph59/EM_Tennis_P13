# Generated by Django 2.2.3 on 2019-08-15 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20190815_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='payment_date_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
