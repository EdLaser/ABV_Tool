from django.test import SimpleTestCase
from django.urls import reverse, resolve
from Antragsverwaltungstool.views import index, new_universall, new_finance, new_position, new_advisory, new_conduct, get_all_by_electioninput, change_universall, change_advisory, change_position, change_finance, change_conduct

"""Die Reverse-Funktion ermöglicht es, URL-Details aus der Datei url's.py über den dort angegebenen Namenswert abzurufen."""
"""Die Resolve-Funktion ermöglicht es, URL-Pfade zu den entsprechenden View-Funktionen aufzulösen."""

class TestUrls(SimpleTestCase):

    def test_index_url_is_resolves(self):
        url = reverse('index')
        print(resolve(url))
        self.assertEquals(resolve(url).func, index)

    def test_universal_url_is_resolves(self):
        url = reverse('universall')
        print(resolve(url))
        self.assertEquals(resolve(url).func, new_universall)

    def test_finance_url_is_resolves(self):
        url = reverse('finance')
        print(resolve(url))
        self.assertEquals(resolve(url).func, new_finance)

    def test_election_report_url_is_resolves(self):
        url = reverse('election_report')
        print(resolve(url))
        self.assertEquals(resolve(url).func, new_position)

    def test_advisory_member_url_is_resolves(self):
        url = reverse('advisory_member')
        print(resolve(url))
        self.assertEquals(resolve(url).func, new_advisory)

    def test_conduct_url_is_resolves(self):
        url = reverse('conduct')
        print(resolve(url))
        self.assertEquals(resolve(url).func, new_conduct)

    def test_intern_url_is_resolves(self):
        url = reverse('intern')
        print(resolve(url))
        self.assertEquals(resolve(url).func, get_all_by_electioninput)

    def test_change_uni_url_is_resolves(self):
        url = reverse('change_uni')
        print(resolve(url))
        self.assertEquals(resolve(url).func, change_universall)

    def test_change_advi_url_is_resolves(self):
        url = reverse('change_advi')
        print(resolve(url))
        self.assertEquals(resolve(url).func, change_advisory)

    def test_change_posi_url_is_resolves(self):
        url = reverse('change_posi')
        print(resolve(url))
        self.assertEquals(resolve(url).func, change_position)

    def test_change_fin_url_is_resolves(self):
        url = reverse('change_fin')
        print(resolve(url))
        self.assertEquals(resolve(url).func, change_finance)

    def test_change_con_url_is_resolves(self):
        url = reverse('change_con')
        print(resolve(url))
        self.assertEquals(resolve(url).func, change_conduct)