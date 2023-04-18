# Generated by Django 3.1.13 on 2023-04-18 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.user')),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=1024)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=20)),
                ('profilepicture', models.ImageField(upload_to='uploads/% Y/% m/% d/')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.user')),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=1024)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=20)),
                ('profilepicture', models.ImageField(upload_to='uploads/% Y/% m/% d/')),
            ],
        ),
        migrations.RemoveField(
            model_name='employee',
            name='user',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_customer',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_employee',
        ),
        migrations.AddField(
            model_name='user',
            name='is_doctor',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_patient',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
