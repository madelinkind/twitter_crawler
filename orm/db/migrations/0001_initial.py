# Generated by Django 3.1.2 on 2020-10-05 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TwitterUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screen_name', models.CharField(max_length=15)),
                ('twitter_user_id', models.IntegerField(null=True)),
                ('user_info', models.JSONField()),
            ],
            options={
                'db_table': 'twitter_users',
            },
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet_text', models.CharField(max_length=280)),
                ('tweet_date', models.DateTimeField()),
                ('tweet_id', models.IntegerField()),
                ('tweet_info', models.JSONField()),
                ('twitter_users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.twitteruser')),
            ],
            options={
                'db_table': 'tweets',
            },
        ),
    ]
