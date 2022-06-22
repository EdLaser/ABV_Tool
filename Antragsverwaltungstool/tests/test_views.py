from cgi import test
from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_GET(self):
        response = self.client.get(reverse('index'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'stat_html/index.html')

    def test_finance_GET(self):
        response = self.client.get(reverse('finance'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'stat_html/finance.html')

    def test_universally_GET(self):
        response = self.client.get(reverse('universall'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'stat_html/universally.html')

    def test_election_GET(self):
        response = self.client.get(reverse('election_report'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'stat_html/election_report.html')

    def test_advisory_GET(self):
        response = self.client.get(reverse('advisory_member'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'stat_html/advisory_member.html')

    def test_new_universall_POST(self):
        response = self.client.post(reverse('universall'), {
            'flag': 0,
            'number': 5,
            'date_today': '13.06.2022',
            'title': 'Test',
            'office': 'Kultur',
            'name': 'Hans Meier',
            'mail': 'MaxMustermann@gmx.com',
            'text': 'Ich liebe das Wochenende.',
            'reason': 'blub',
            'suggestion': 'blub',
            'anlagen': 'blub',
        })

        self.assertEquals(response.status_code, 200)

    def test_new_finance_POST(self):
        response = self.client.post(reverse('finance'), {
            'flag': 0,
            'number': 5,
            'date_today': '13.06.2022',
            'title': 'Test',
            'office': 'Kultur',
            'name': 'Hans Meier',
            'mail': 'MaxMustermann@gmx.com',
            'text': 'Ich liebe das Wochenende.',
            'reason': 'blub',
            'budget': '10000',
            'suggestion': 'blub',
            'anlagen': 'blub',
        })

        self.assertEquals(response.status_code, 200)

    def test_new_advisory_POST(self):
        response = self.client.post(reverse('advisory_member'), {
            'flag': 0,
            'number': 5,
            'date_today': '13.06.2022',
            'title': 'Test',
            'office': 'Kultur',
            'name': 'Hans Meier',
            'mail': 'MaxMustermann@gmx.com',
            'text': 'Ich liebe das Wochenende.',
            'frg1': 'Was?',
            'frg2': 'Wie?',
            'frg3': 'Wer?',
            'frg4': 'Wo?',
            'anlagen': 'blub',
        })

        self.assertEquals(response.status_code, 200)

    def test_new_Position_POST(self):
        response = self.client.post(reverse('election_report'), {
            'flag': 0,
            'number': 5,
            'date_today': '13.06.2022',
            'title': 'Test',
            'office': 'Kultur',
            'name': 'Hans Meier',
            'mail': 'MaxMustermann@gmx.com',
            'text': 'Ich liebe das Wochenende.',
            'frg1': 'Was?',
            'frg2': 'Wie?',
            'frg3': 'Wer?',
            'frg4': 'Wo?',
            'frg_spez_1': 'Woher?',
            'frg_spez_2': 'Warum?',
            'frg_spez_3': 'Wieso?',
            'anlagen': 'blub',
        })

        self.assertEquals(response.status_code, 200)

    def test_new_conduct_POST(self):
        response = self.client.post(reverse('conduct'), {
            'flag': 0,
            'number': 5,
            'date_today': '13.06.2022',
            'title': 'Test',
            'office': 'Kultur',
            'name': 'Hans Meier',
            'mail': 'MaxMustermann@gmx.com',
            'text': 'Ich liebe das Wochenende.',
            'reason': 'blub',
            'suggestion': 'blub',
            'anlagen': 'blub',
        })

        self.assertEquals(response.status_code, 200)
        
    def test_intern_GET(self):
        response = self.client.get(reverse('intern'))

        self.assertEquals(response.status_code, 302)

    def test_login_required(self):
        response = self.client.get(reverse('login'))

        self.assertEquals(response.status_code, 200)

    def test_change_universall_GET(self):
        response = self.client.get(reverse('change_uni'))

        self.assertEquals(response.status_code, 200)

    def test_change_advisory_GET(self):
        response = self.client.get(reverse('change_advi'))

        self.assertEquals(response.status_code, 200)

    def test_change_position_GET(self):
        response = self.client.get(reverse('change_posi'))

        self.assertEquals(response.status_code, 200)

    def test_change_finance_GET(self):
        response = self.client.get(reverse('change_fin'))

        self.assertEquals(response.status_code, 200)

    def test_change_conduct_GET(self):
        response = self.client.get(reverse('change_con'))

        self.assertEquals(response.status_code, 200)