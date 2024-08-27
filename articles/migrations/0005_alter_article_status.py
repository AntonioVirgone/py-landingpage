# Generated by Django 4.2.11 on 2024-08-26 14:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("articles", "0004_article_status_alter_article_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="status",
            field=models.CharField(
                choices=[("DRAFT", "Draft"), ("PUBLISHED", "Published")],
                default="PUBLISHED",
                max_length=10,
            ),
        ),
    ]
