# Generated by Django 2.2 on 2020-06-15 14:35

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='Message')),
                ('date_comment', models.DateField(default=datetime.date.today)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Blog')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.User')),
            ],
        ),
    ]
