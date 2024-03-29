# Generated by Django 3.1.2 on 2021-09-16 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scrapper', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CnetModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('link', models.TextField()),
                ('description', models.TextField()),
                ('creator', models.TextField()),
                ('publication_date', models.CharField(max_length=255)),
                ('media_url', models.TextField()),
                ('media_description', models.TextField()),
                ('media_credit', models.TextField()),
                ('categories', models.TextField()),
                ('source_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scrapper.mastermodel')),
            ],
        ),
        migrations.CreateModel(
            name='FoxNewsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('link', models.TextField()),
                ('description', models.TextField()),
                ('creator', models.TextField()),
                ('publication_date', models.CharField(max_length=255)),
                ('media_url', models.TextField()),
                ('media_description', models.TextField()),
                ('media_credit', models.TextField()),
                ('categories', models.TextField()),
                ('source_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scrapper.mastermodel')),
            ],
        ),
        migrations.CreateModel(
            name='NyTimesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('link', models.TextField()),
                ('description', models.TextField()),
                ('creator', models.TextField()),
                ('publication_date', models.CharField(max_length=255)),
                ('media_url', models.TextField()),
                ('media_description', models.TextField()),
                ('media_credit', models.TextField()),
                ('categories', models.TextField()),
                ('source_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scrapper.mastermodel')),
            ],
        ),
        migrations.CreateModel(
            name='PcMagModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('link', models.TextField()),
                ('description', models.TextField()),
                ('creator', models.TextField()),
                ('publication_date', models.CharField(max_length=255)),
                ('media_url', models.TextField()),
                ('media_description', models.TextField()),
                ('media_credit', models.TextField()),
                ('categories', models.TextField()),
                ('source_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scrapper.mastermodel')),
            ],
        ),
        migrations.DeleteModel(
            name='ContentModel',
        ),
    ]
