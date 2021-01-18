# Generated by Django 2.2.6 on 2020-04-23 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20200423_1505'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormFields',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formFieldType', models.CharField(max_length=250)),
            ],
        ),
        migrations.RenameField(
            model_name='paymenttype',
            old_name='swedish',
            new_name='text',
        ),
        migrations.RemoveField(
            model_name='buttontext',
            name='placeholder',
        ),
        migrations.AddField(
            model_name='paymenttype',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.LanguageChoices'),
        ),
        migrations.CreateModel(
            name='FormText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formTextLabel', models.TextField(null=True)),
                ('formTextPlaceholder', models.TextField(null=True)),
                ('language', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.LanguageChoices')),
                ('theformFieldType', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.FormFields')),
            ],
        ),
    ]
