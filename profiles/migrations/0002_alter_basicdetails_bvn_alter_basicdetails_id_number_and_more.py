# Generated by Django 4.2.6 on 2023-10-12 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicdetails',
            name='BVN',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='basicdetails',
            name='ID_number',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='basicdetails',
            name='National_ID',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='othertransfer',
            name='enter_the_amount_to_be_transferred',
            field=models.IntegerField(null=True),
        ),
    ]
