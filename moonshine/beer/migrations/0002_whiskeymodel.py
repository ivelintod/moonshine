# Generated by Django 2.2.6 on 2019-10-13 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhiskeyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('whiskey_type', models.CharField(choices=[('BR', 'Bourbon'), ('CN', 'Corn'), ('GR', 'Grain')], default='BR', max_length=2)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
