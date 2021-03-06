# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-08 19:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('club_id', models.CharField(max_length=120, primary_key=True, serialize=False)),
                ('club_name', models.CharField(max_length=120, null=True)),
                ('contact_info', models.IntegerField(null=True)),
                ('objective', models.TextField(null=True)),
                ('description', models.TextField(null=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_id', models.CharField(max_length=120)),
                ('event_id', models.IntegerField()),
                ('event_name', models.CharField(max_length=120)),
                ('event_date', models.DateTimeField(default='')),
                ('venue', models.CharField(max_length=120, null=True)),
                ('no_part', models.IntegerField()),
                ('no_reg', models.IntegerField(blank=True, null=True)),
                ('contact_info', models.TextField(default='')),
                ('event_desc', models.TextField(null=True)),
                ('requirements', models.TextField(blank=True, null=True)),
                ('own_form', models.URLField(blank=True, null=True)),
                ('poster', models.ImageField(blank=True, null=True, upload_to='./tester/static')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(choices=[('Admin', 'Admin'), ('Cultural Secretary', 'Cultural Secretary'), ('Event Manager', 'Event Manager'), ('Other', 'Other')], max_length=50, null=True)),
                ('club_id', models.ForeignKey(db_column='club_id', on_delete=django.db.models.deletion.CASCADE, to='tester.Club')),
            ],
        ),
        migrations.CreateModel(
            name='Pending_transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_id', models.CharField(default='', max_length=120)),
                ('event_id', models.IntegerField()),
                ('usn', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=120, null=True)),
                ('email', models.EmailField(default='abc@xyz.com', max_length=254, null=True)),
                ('phone', models.BigIntegerField(null=True)),
                ('dept', models.CharField(max_length=50, null=True)),
                ('sem', models.CharField(max_length=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('usn', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('dept', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(default='abc@xyz.com', max_length=254, null=True)),
                ('dob', models.DateField(null=True)),
                ('phone', models.BigIntegerField(null=True)),
                ('sem', models.IntegerField(null=True)),
                ('club_id', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='seller',
            name='seller_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tester.Signup'),
        ),
        migrations.AlterUniqueTogether(
            name='register',
            unique_together=set([('event_id', 'usn', 'club_id')]),
        ),
        migrations.AddField(
            model_name='pending_transactions',
            name='buyer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tester.Signup'),
        ),
        migrations.AddField(
            model_name='pending_transactions',
            name='seller',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='tester.Seller'),
        ),
        migrations.AddField(
            model_name='member',
            name='usn',
            field=models.ForeignKey(db_column='usn', on_delete=django.db.models.deletion.CASCADE, to='tester.Signup'),
        ),
        migrations.AlterUniqueTogether(
            name='event',
            unique_together=set([('club_id', 'event_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='club',
            unique_together=set([('club_id',)]),
        ),
        migrations.AlterUniqueTogether(
            name='seller',
            unique_together=set([('book_name', 'seller_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='pending_transactions',
            unique_together=set([('buyer_id', 'seller')]),
        ),
        migrations.AlterUniqueTogether(
            name='member',
            unique_together=set([('club_id', 'usn')]),
        ),
    ]
