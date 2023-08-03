# Generated by Django 4.1.7 on 2023-07-16 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('post', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='blog.post')),
            ],
        ),
    ]
