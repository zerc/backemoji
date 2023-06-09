# Generated by Django 4.1.7 on 2023-03-31 14:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("feedback", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="choice",
            name="emoji",
            field=models.IntegerField(
                choices=[(0, "😡"), (1, "😔"), (2, "😐"), (3, "🙂"), (4, "🥰")], default=0
            ),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name="choice",
            unique_together={("name", "rating", "emoji")},
        ),
    ]
