# Generated by Django 2.2.9 on 2021-10-14 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20211010_1203'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ('-title',)},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-pub_date',)},
        ),
        migrations.AlterField(
            model_name='post',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='posts.Group'),
        ),
    ]
