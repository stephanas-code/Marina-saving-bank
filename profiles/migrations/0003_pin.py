# Generated by Django 4.2.6 on 2023-10-20 14:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0002_alter_basicdetails_bvn_alter_basicdetails_id_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='pin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin', models.IntegerField(max_length=4)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='senderpin', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
