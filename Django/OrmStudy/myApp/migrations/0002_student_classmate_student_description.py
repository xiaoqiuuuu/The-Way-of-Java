# Generated by Django 5.0.1 on 2024-02-04 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='classmate',
            field=models.CharField(db_column='class', db_index=True, default='Weiqt', max_length=5, verbose_name='班级'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='description',
            field=models.TextField(default='', verbose_name='个性签名'),
        ),
    ]
