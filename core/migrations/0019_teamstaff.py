# Generated by Django 2.2.6 on 2020-10-13 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20201005_1231'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamStaff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('position', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='media_root/')),
            ],
        ),
    ]
