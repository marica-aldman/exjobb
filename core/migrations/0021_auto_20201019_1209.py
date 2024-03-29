# Generated by Django 2.2.6 on 2020-10-19 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_teamstaff_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='paid',
        ),
        migrations.RemoveField(
            model_name='order',
            name='received',
        ),
        migrations.RemoveField(
            model_name='order',
            name='sub_out_date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='subscription_order',
        ),
        migrations.AddField(
            model_name='order',
            name='cancel_handled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='canceled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='return_handled',
            field=models.BooleanField(default=False),
        ),
    ]
