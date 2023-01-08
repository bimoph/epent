# Generated by Django 4.1 on 2023-01-07 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("landingpage", "0002_company_event_remove_user_eo_user_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="logo_image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
        migrations.AlterField(
            model_name="company",
            name="email",
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name="event",
            name="email",
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
