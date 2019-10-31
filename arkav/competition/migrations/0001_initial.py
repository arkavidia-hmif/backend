# Generated by Django 2.2.5 on 2019-09-14 07:27

from django.conf import settings
from django.db import migrations
from django.db import models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('max_team_members', models.IntegerField(default=1)),
                ('min_team_members', models.IntegerField(default=1)),
                ('is_registration_open', models.BooleanField(default=True)),
                ('view_icon', models.URLField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('order', models.IntegerField(default=0)),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stages',
                                                  to='competition.Competition')),
            ],
            options={
                'ordering': ['competition', 'order'],
            },
        ),
        migrations.CreateModel(
            name='TaskCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name_plural': 'task categories',
            },
        ),
        migrations.CreateModel(
            name='TaskWidget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('institution', models.CharField(max_length=50)),
                ('is_participating', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('active_stage', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT,
                                                   related_name='active_teams', to='competition.Stage')),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='teams',
                                                  to='competition.Competition')),
            ],
            options={
                'get_latest_by': 'created_at',
            },
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('invitation_full_name', models.CharField(max_length=75)),
                ('invitation_email', models.EmailField(max_length=254)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_members',
                                           to='competition.Team')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
                                           related_name='team_members', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'created_at',
                'unique_together': {('team', 'user')},
            },
        ),
        migrations.AddField(
            model_name='team',
            name='members',
            field=models.ManyToManyField(related_name='teams', through='competition.TeamMember',
                                         to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='team',
            name='team_leader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='led_teams',
                                    to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('widget_parameters', models.TextField(default='')),
                ('requires_validation', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tasks',
                                               to='competition.TaskCategory')),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks',
                                            to='competition.Stage')),
                ('widget', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tasks',
                                             to='competition.TaskWidget')),
            ],
        ),
        migrations.CreateModel(
            name='TaskResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.TextField()),
                ('status', models.CharField(choices=[('awaiting_validation', 'Awaiting validation'),
                                                     ('completed', 'Completed'), ('rejected', 'Rejected')],
                                            max_length=20)),
                ('last_submitted_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='task_responses',
                                           to='competition.Task')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_responses',
                                           to='competition.Team')),
            ],
            options={
                'get_latest_by': 'created_at',
                'unique_together': {('task', 'team')},
            },
        ),
    ]
