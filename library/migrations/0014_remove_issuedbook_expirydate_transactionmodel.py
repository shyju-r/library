# Generated by Django 5.1 on 2024-09-13 04:47

import django.db.models.deletion
import library.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0013_addusermodel_memberid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issuedbook',
            name='expirydate',
        ),
        migrations.CreateModel(
            name='Transactionmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issuedate', models.DateField(auto_now=True)),
                ('duedate', models.DateField(default=library.models.get_expiry)),
                ('returndate', models.DateField()),
                ('bookname', models.TextField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.addusermodel')),
            ],
        ),
    ]
