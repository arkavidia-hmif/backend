from arkav.arkavauth.models import User
from arkav.competition.models import Competition
from arkav.competition.models import Team
from arkav.competition.models import TeamMember
from arkav.competition.models import Task
from arkav.competition.models import TaskCategory
from arkav.competition.models import TaskWidget
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class SubmitTaskTestCase(APITestCase):
    def setUp(self):
        self.competition_ctf = Competition.objects.create(
            name='Capture the Flag', max_team_members=3)
        self.ctf_stage_registration = self.competition_ctf.stages.create(
            name='CTF Registration', order=1)

        self.user1 = User.objects.create_user(email='user1')
        self.user2 = User.objects.create_user(email='user2')

        self.ctf_team1 = Team.objects.create(
            name='ctf1', competition=self.competition_ctf, team_leader=self.user1)
        TeamMember.objects.create(team=self.ctf_team1, user=self.user1)

        self.ctf_team2 = Team.objects.create(
            name='ctf2', competition=self.competition_ctf, team_leader=self.user2)
        TeamMember.objects.create(team=self.ctf_team2, user=self.user2)

        self.category_documents = TaskCategory.objects.create(name='Documents')
        self.widget_file = TaskWidget.objects.create(name='File')

        self.ctf_upload_ktm_task = Task.objects.create(
            name='Upload KTM',
            stage=self.ctf_stage_registration,
            category=self.category_documents,
            widget=self.widget_file,
            requires_validation=True,
        )

    def test_submit_at_others_task(self):
        '''
        Submitting at other task
        '''
        url = reverse(
            'competition-team-task-detail',
            kwargs={'team_id': self.ctf_team1.pk, 'task_id': self.ctf_upload_ktm_task.pk})
        self.client.force_authenticate(self.user2)
        data = {
            'response': 'Upload KTM'
        }
        res = self.client.post(url, data=data, format='json')
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)