# Generated by Django 3.1.7 on 2021-04-02 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follow', models.BooleanField(default=0)),
                ('comment', models.BooleanField(default=0)),
                ('like', models.BooleanField(default=0)),
                ('story', models.BooleanField(default=0)),
                ('account', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
            ],
        ),
    ]
