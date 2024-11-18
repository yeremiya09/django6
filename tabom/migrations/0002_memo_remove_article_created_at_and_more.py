# Generated by Django 5.1.3 on 2024-11-15 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tabom", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Memo",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="article",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="article",
            name="updated_at",
        ),
        migrations.RemoveField(
            model_name="like",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="like",
            name="updated_at",
        ),
        migrations.RemoveField(
            model_name="user",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="user",
            name="updated_at",
        ),
        migrations.AddConstraint(
            model_name="like",
            constraint=models.UniqueConstraint(fields=("user", "article"), name="UIX_user_id_article_id"),
        ),
    ]