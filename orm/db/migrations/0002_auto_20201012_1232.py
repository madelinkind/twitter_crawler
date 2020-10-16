# Generated by Django 3.1.2 on 2020-10-12 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='twitter_users',
            new_name='twitter_user',
        ),
        migrations.AlterField(
            model_name='tweet',
            name='tweet_id',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='twitteruser',
            name='twitter_user_id',
            field=models.CharField(max_length=20, null=True),
        ),
    ]