# Generated by Django 2.2.4 on 2019-10-10 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='intro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('email', models.TextField()),
                ('contatc_num', models.IntegerField()),
                ('additional_info', models.TextField()),
                ('address', models.TextField()),
            ],
        ),
    ]
