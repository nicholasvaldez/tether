# Generated by Django 4.2.5 on 2023-09-26 16:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
                ('contact_type', models.CharField(choices=[('acquaintance', 'Acquaintance'), ('warm', 'Warm'), ('close_friend', 'Close Friend'), ('personal', 'Personal'), ('professional', 'Professional')], default='acquaintance', max_length=20)),
                ('notes', models.TextField(blank=True, null=True)),
                ('connection_strength', models.CharField(choices=[('weak', 'Weak'), ('moderate', 'Moderate'), ('strong', 'Strong'), ('very_strong', 'Very Strong')], default='weak', max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TouchType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=155)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TouchPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
                ('touch_date', models.DateField()),
                ('notes', models.TextField(blank=True, null=True)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tetherapi.contact')),
                ('touch_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tetherapi.touchtype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InteractionLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interaction_type', models.CharField(choices=[('text_message', 'Text Message'), ('phone_call', 'Phone Call'), ('meetup', 'Meetup'), ('email', 'Email'), ('other', 'Other')], default='text_message', max_length=20)),
                ('date', models.DateField()),
                ('notes', models.TextField(blank=True, null=True)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interactions', to='tetherapi.contact')),
            ],
        ),
    ]