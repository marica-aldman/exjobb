# Generated by Django 2.2.6 on 2020-03-23 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_coupon_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='errormessages',
            old_name='info_type',
            new_name='view_section',
        ),
        migrations.RenameField(
            model_name='informationmessages',
            old_name='info_type',
            new_name='view_section',
        ),
        migrations.RenameField(
            model_name='text',
            old_name='info_type',
            new_name='view_section',
        ),
        migrations.RenameField(
            model_name='warningmessages',
            old_name='info_type',
            new_name='view_section',
        ),
    ]
