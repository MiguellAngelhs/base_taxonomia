# Generated by Django 4.0.2 on 2022-02-14 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Taxonomia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.CharField(blank=True, max_length=50, null=True)),
                ('level', models.IntegerField()),
                ('levelfather', models.IntegerField(blank=True, null=True)),
                ('typefile', models.CharField(blank=True, max_length=50, null=True)),
                ('directory', models.CharField(blank=True, max_length=500, null=True)),
                ('numpages', models.IntegerField(blank=True, null=True)),
                ('transcription', models.TextField(blank=True, null=True)),
                ('numwords', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UploadZip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.FileField(blank=True, null=True, upload_to='FileZip/')),
            ],
        ),
    ]