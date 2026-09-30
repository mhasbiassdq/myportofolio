import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_project_starred_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('institution', models.CharField(max_length=255)),
                ('degree', models.CharField(max_length=255)),
                ('start_year', models.CharField(max_length=4)),
                ('end_year', models.CharField(default='Present', max_length=20)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
