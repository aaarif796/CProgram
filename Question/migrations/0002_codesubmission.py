# Generated by Django 4.2.13 on 2024-07-20 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("usermode", "0001_initial"),
        ("Question", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CodeSubmission",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.TextField()),
                ("test_case_pass", models.BooleanField(default=False)),
                ("no_of_attempt", models.IntegerField(default=0)),
                ("score", models.IntegerField(default=0)),
                ("submitted_at", models.DateTimeField(auto_now_add=True)),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Question.question",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="usermode.customuser",
                    ),
                ),
            ],
        ),
    ]
