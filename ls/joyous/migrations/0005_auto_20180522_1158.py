# Generated by Django 2.0.3 on 2018-05-21 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('joyous', '0004_auto_20180425_2355'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cancellationpage',
            options={'default_manager_name': 'objects', 'verbose_name': 'Cancellation'},
        ),
        migrations.AlterModelOptions(
            name='extrainfopage',
            options={'default_manager_name': 'objects', 'verbose_name': 'Extra Event Information'},
        ),
        migrations.AlterModelOptions(
            name='multidayeventpage',
            options={'default_manager_name': 'objects', 'verbose_name': 'Multiday Event Page'},
        ),
        migrations.AlterModelOptions(
            name='postponementpage',
            options={'default_manager_name': 'objects', 'verbose_name': 'Postponement'},
        ),
        migrations.AlterModelOptions(
            name='recurringeventpage',
            options={'default_manager_name': 'objects', 'verbose_name': 'Recurring Event Page'},
        ),
        migrations.AlterModelOptions(
            name='simpleeventpage',
            options={'default_manager_name': 'objects', 'verbose_name': 'Event Page'},
        ),
        migrations.AlterField(
            model_name='multidayeventpage',
            name='group_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='joyous.GroupPage'),
        ),
        migrations.AlterField(
            model_name='postponementpage',
            name='group_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='joyous.GroupPage'),
        ),
        migrations.AlterField(
            model_name='recurringeventpage',
            name='group_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='joyous.GroupPage'),
        ),
        migrations.AlterField(
            model_name='simpleeventpage',
            name='group_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='joyous.GroupPage'),
        ),
    ]