# Generated by Django 2.2.6 on 2020-04-23 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_remove_faq_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='ButtonText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placeholder', models.TextField(null=True)),
                ('buttonText', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ButtonType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buttonType', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='LanguageChoices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=150)),
                ('language_short', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='TextField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=1024, null=True)),
                ('view_section', models.CharField(max_length=20, null=True)),
                ('description', models.TextField(null=True)),
                ('text', models.TextField(null=True)),
                ('language', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.LanguageChoices')),
            ],
        ),
        migrations.DeleteModel(
            name='Text',
        ),
        migrations.RenameField(
            model_name='errormessages',
            old_name='swedish',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='faq',
            old_name='swedish_content',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='faq',
            old_name='swedish_subject',
            new_name='subject',
        ),
        migrations.RenameField(
            model_name='informationmessages',
            old_name='swedish',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='warningmessages',
            old_name='swedish',
            new_name='text',
        ),
        migrations.AddField(
            model_name='buttontext',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.LanguageChoices'),
        ),
        migrations.AddField(
            model_name='buttontext',
            name='theButtonType',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.ButtonType'),
        ),
        migrations.AddField(
            model_name='errormessages',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.LanguageChoices'),
        ),
        migrations.AddField(
            model_name='faq',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.LanguageChoices'),
        ),
        migrations.AddField(
            model_name='informationmessages',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.LanguageChoices'),
        ),
        migrations.AddField(
            model_name='warningmessages',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.LanguageChoices'),
        ),
    ]
