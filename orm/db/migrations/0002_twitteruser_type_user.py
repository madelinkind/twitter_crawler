# Generated by Django 3.1.2 on 2021-02-22 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitteruser',
            name='type_user',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
