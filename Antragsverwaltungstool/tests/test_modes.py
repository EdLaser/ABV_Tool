from ast import And
from django.test import TestCase
import django
from Antragsverwaltungstool.models import AdvisoryMember, Finance, Position, Universall, Conduct, NumberCount

# TODOS:
# __ str__ auf leerzeichen testen --> wie funktioniert das dann ?  --> tests dafür schreiben
# Kommentare + Blöcke entfernen
# Ideen wie kann man URL brechen ?
# date_string erzeugen + testen bei einsetzen auch wenn es egal sein sollte
# number bei absolute_url importieren ? 
# Meta- Unterklasse ????

class test_Model_AdvisoryMember(TestCase):

    def setup(self):
        self.MessageSuccess = AdvisoryMember.objects.create(
            flag = 0,
            number = "1",
            date = "now",
            title = "TestOne",
            office = "office",
            name = "test",
            mail = "test@htw-dresden.de",
            text = "test_example_insert_here",
            frg1 = "answer_frg1",
            frg2 = "answer_frg2",
            frg3 = "answer_frg3",
            frg4 = "answer_frg4",
            anlagen= "anlangen_text",
            aenderung = "changes",
            mehrheit = "existing_majority",
            beschluss = "result",
            beschlusstext = "long_text",
            beschlussgrund = "reason_for_this"
        )

        self.MessageFailure = AdvisoryMember.objects.create(
            flag = 0,
            number = "1234567890123456", # space overflow
            date = "now",
            title = "TestOne",
            office = "office",
            name = "test",
            mail = "test@htw-dresden.de",
            text = "test_example_insert_here",
            frg1 = "answer_frg1",
            frg2 = "answer_frg2",
            frg3 = "answer_frg3",
            frg4 = "answer_frg4",
            anlagen= "anlangen_text",
            aenderung = "changes",
            mehrheit = "existing_majority",
            beschluss = "result",
            beschlusstext = "long_text",
            beschlussgrund = "reason_for_this"
        )
        

    def test_advisorymember___str___success(self):
        # Block kann potenziell raus (for myself)
        self.assertEquals(str(self.MessageSuccess.flag), "0")
        self.assertEquals(str(self.MessageSuccess.number), "1")
        self.assertEquals(self.MessageSuccess.date, "now")
        self.assertEquals(str(self.MessageSuccess.title), "TestOne")
        self.assertEquals(str(self.MessageSuccess.office), "office")
        self.assertEquals(str(self.MessageSuccess.name), "test")
        self.assertEquals(str(self.MessageSuccess.mail), "test@htw-dresden.de")
        self.assertEquals(str(self.MessageSuccess.text), "test_example_insert_here")
        self.assertEquals(str(self.MessageSuccess.frg1), "answer_frg1")
        self.assertEquals(str(self.MessageSuccess.frg2), "answer_frg2")
        self.assertEquals(str(self.MessageSuccess.frg3), "answer_frg3")
        self.assertEquals(str(self.MessageSuccess.frg4), "answer_frg4")
        self.assertEquals(str(self.MessageSuccess.anlagen), "anlangen_text")
        self.assertEquals(str(self.MessageSuccess.aenderung), "changes")
        self.assertEquals(str(self.MessageSuccess.mehrheit), "existing_majority")
        self.assertEquals(str(self.MessageSuccess.beschluss), "result")
        self.assertEquals(str(self.MessageSuccess.beschlusstext), "long_text")
        self.assertEquals(str(self.MessageSuccess.beschlussgrund), "reason_for_this")

        self.assertEquals(str(self), "0 1 now TestOne office test test@htw-dresden.de test_example_insert_here answer_frg1 answer_frg2 answer_frg3 answer_frg4 anlangen_text changes existing_majority result long_text reason_for_this")

    def test_advisorymember___str___failure(self):
        # Block kann potenziell raus (for myself)
        self.assertEquals(int(self.MessageSuccess.flag), "0")
        self.assertNotEquals(int(self.MessageSuccess.number), "1234567890123456") # // self.assertEquals(int(self.MessageSuccess.number), "123456789012345")
        self.assertEquals(self.MessageSuccess.date, "now")
        self.assertEquals(str(self.MessageSuccess.title), "TestOne")
        self.assertEquals(str(self.MessageSuccess.office), "office")
        self.assertEquals(str(self.MessageSuccess.name), "test")
        self.assertEquals(str(self.MessageSuccess.mail), "test@htw-dresden.de")
        self.assertEquals(str(self.MessageSuccess.text), "test_example_insert_here")
        self.assertEquals(str(self.MessageSuccess.frg1), "answer_frg1")
        self.assertEquals(str(self.MessageSuccess.frg2), "answer_frg2")
        self.assertEquals(str(self.MessageSuccess.frg3), "answer_frg3")
        self.assertEquals(str(self.MessageSuccess.frg4), "answer_frg4")
        self.assertEquals(str(self.MessageSuccess.anlagen), "anlangen_text")
        self.assertEquals(str(self.MessageSuccess.aenderung), "keine")
        self.assertEquals(str(self.MessageSuccess.mehrheit), "existing_majority")
        self.assertEquals(str(self.MessageSuccess.beschluss), "result")
        self.assertEquals(str(self.MessageSuccess.beschlusstext), "long_text")
        self.assertEquals(str(self.MessageSuccess.beschlussgrund), "reason_for_this")

        self.assertNotEquals(str(self), "0 1234567890123456 now TestOne office test test@htw-dresden.de test_example_insert_here answer_frg1 answer_frg2 answer_frg3 answer_frg4 anlangen_text changes existing_majority result long_text reason_for_this")
    """
    def test_that___str___failure(self):
            # was wenn leerzeichen in textabschnitten ?
            assert 1 == 1 # Platzhalter sonst error
    """

    def test_advisorymember_get_absolute_url_setup_normal_success(self):
        number_url = "1234567890"
        custom_url =  AdvisoryMember.get_absolute_url(number_url)
        self.assertEquals(str(custom_url), str("/Antragsverwaltungstool/show_advisory/?antrag=1234%2F67890"))

    def test_advisorymember_get_absolute_url_setup_short_success(self):
        number_url = "1"
        custom_url =  AdvisoryMember.get_absolute_url(number_url)
        self.assertEquals(str(custom_url), str("/Antragsverwaltungstool/show_advisory/?antrag=1%2F"))

    def test_advisorymember_get_absolute_url_setup_(self):
        number_url = "abs123&75%"
        custom_url =  AdvisoryMember.get_absolute_url(number_url)
        self.assertEquals(str(custom_url), str("/Antragsverwaltungstool/show_advisory/?antrag=abs1%2F3&75%"))



class test_Model_Finance(TestCase):

    def setup(self):
        self.MessageSuccess = Finance.objects.create(
            flag = 0,
            number = "1",
            date = "now",
            title = "TestOne",
            office = "office",
            name = "test",
            mail = "test@htw-dresden.de",
            text = "test_example_insert_here",
            reason = "reason",
            butget = "10000",
            suggestion = "something_new_here",
            anlagen= "anlangen_text",
            aenderung = "changes",
            mehrheit = "existing_majority",
            beschluss = "result",
            beschlusstext = "long_text",
            beschlussgrund = "reason_for_this"
        )

    def test_finance___str___success(self):
        # Block kann potenziell raus (for myself)
        self.assertEquals(str(self.MessageSuccess.flag), "0")
        self.assertEquals(str(self.MessageSuccess.number), "1")
        self.assertEquals(self.MessageSuccess.date, "now")
        self.assertEquals(str(self.MessageSuccess.title), "TestOne")
        self.assertEquals(str(self.MessageSuccess.office), "office")
        self.assertEquals(str(self.MessageSuccess.name), "test")
        self.assertEquals(str(self.MessageSuccess.mail), "test@htw-dresden.de")
        self.assertEquals(str(self.MessageSuccess.text), "test_example_insert_here")
        self.assertEquals(str(self.MessageSuccess.reason), "reason")
        self.assertEquals(str(self.MessageSuccess.butget), "10000")
        self.assertEquals(str(self.MessageSuccess.suggestion), "something_new_here")
        self.assertEquals(str(self.MessageSuccess.anlagen), "anlangen_text")
        self.assertEquals(str(self.MessageSuccess.aenderung), "changes")
        self.assertEquals(str(self.MessageSuccess.mehrheit), "existing_majority")
        self.assertEquals(str(self.MessageSuccess.beschluss), "result")
        self.assertEquals(str(self.MessageSuccess.beschlusstext), "long_text")
        self.assertEquals(str(self.MessageSuccess.beschlussgrund), "reason_for_this")

        self.assertEquals(str(self), "0 1 now TestOne office test test@htw-dresden.de test_example_insert_here reason 10000 something_new_here anlangen_text changes existing_majority result long_text reason_for_this")

    def test_finance_get_absolute_url_setup_normal_success(self):
        number_url = "1234567890"
        custom_url =  Finance.get_absolute_url(number_url)
        self.assertEquals(str(custom_url), str("/Antragsverwaltungstool/show_advisory/?antrag=1234%2F67890"))

    def test_finance_get_absolute_url_setup_short_success(self):
        number_url = "1"
        custom_url =  Finance.get_absolute_url(number_url)
        self.assertEquals(str(custom_url), str("/Antragsverwaltungstool/show_advisory/?antrag=1%2F"))

    def test_finance_get_absolute_url_setup_(self):
        number_url = "abs123&75%"
        custom_url =  Finance.get_absolute_url(number_url)
        self.assertEquals(str(custom_url), str("/Antragsverwaltungstool/show_advisory/?antrag=abs1%2F3&75%"))

class test_Model_Position(TestCase):

    def setup(self):
        self.MessageFailure = Position.objects.create(
            flag = 0,
            number = "1",
            date = "now",
            title = "TestOne",
            office = "office",
            name = "test",
            mail = "test@htw-dresden.de",
            text = "test_example_insert_here",
            frg1 = "answer_frg1",
            frg2 = "answer_frg2",
            frg3 = "answer_frg3",
            frg4 = "answer_frg4",
            frg_spez_1 = "Inhalt",
            frg_spez_2 = "Inhalt",
            frg_spez_3 = "Inhalt",
            anlagen= "anlangen_text",
            mehrheit = "existing_majority",
            beschluss = "result",
            beschlusstext = "long_text",
            beschlussgrund = "reason_for_this"
        )

    def test_position___str___success(self):
        self.assertEquals(str(self), "0 1 now TestOne office test test@htw-dresden.de test_example_insert_here answer_frg1 answer_frg2 answer_frg3 answer_frg4 Inhalt Inhalt Inhalt anlangen_text existing_majority result long_text reason_for_this")

    def test_position_get_absolute_url_setup_normal_success(self):
        number_url = "1234567890"
        custom_url =  Position.get_absolute_url(number_url)
        self.assertEquals(str(custom_url), str("/Antragsverwaltungstool/show_advisory/?antrag=1234%2F67890"))

    def test_position_get_absolute_url_setup_short_success(self):
        number_url = "1"
        custom_url =  Position.get_absolute_url(number_url)
        self.assertEquals(str(custom_url), str("/Antragsverwaltungstool/show_advisory/?antrag=1%2F"))

    def test_position_get_absolute_url_setup_(self):
        number_url = "abs123&75%"
        custom_url =  Position.get_absolute_url(number_url)
        self.assertEquals(str(custom_url), str("/Antragsverwaltungstool/show_advisory/?antrag=abs1%2F3&75%"))

class test_Model_Universall(TestCase):

    def setup(self):
        self.MessageSuccess = Universall.objects.create(
            flag = 0,
            number = "1",
            date = "now",
            title = "TestOne",
            office = "office",
            name = "test",
            mail = "test@htw-dresden.de",
            text = "test_example_insert_here",
            reason = "reason",
            suggestion = "something_new_here",
            anlagen= "anlangen_text",
            aenderung = "changes",
            mehrheit = "existing_majority",
            beschluss = "result",
            beschlusstext = "long_text",
            beschlussgrund = "reason_for_this"
        )

    def test_universall___str___success(self):
        self.assertEquals(str(self), "0 1 now TestOne office test test@htw-dresden.de test_example_insert_here reason something_new_here anlangen_text changes existing_majority result long_text reason_for_this")

    def test_position_get_absolute_url_setup_normal_success(self):
        number_url = "1234567890"
        custom_url =  Universall.get_absolute_url(number_url)
        self.assertEquals(str(custom_url), str("/Antragsverwaltungstool/show_advisory/?antrag=1234%2F67890"))

    def test_position_get_absolute_url_setup_short_success(self):
        number_url = "1"
        custom_url =  Universall.get_absolute_url(number_url)
        self.assertEquals(str(custom_url), str("/Antragsverwaltungstool/show_advisory/?antrag=1%2F"))

    def test_position_get_absolute_url_setup_(self):
        number_url = "abs123&75%"
        custom_url =  Universall.get_absolute_url(number_url)
        self.assertEquals(str(custom_url), str("/Antragsverwaltungstool/show_advisory/?antrag=abs1%2F3&75%"))

class test_Model_Conduct(TestCase):

    def setup(self):
        self.MessageSuccess = Conduct.objects.create(
            flag = 0,
            number = "1",
            date = "now",
            title = "TestOne",
            office = "office",
            name = "test",
            mail = "test@htw-dresden.de",
            text = "test_example_insert_here",
            reason = "reason",
            suggestion = "something_new_here",
            anlagen= "anlangen_text",
            aenderung = "changes",
            mehrheit = "existing_majority",
            beschluss = "result",
            beschlusstext = "long_text",
            beschlussgrund = "reason_for_this"
        )

    def test_conduct___str___success(self):
        self.assertEquals(str(self), "0 1 now TestOne office test test@htw-dresden.de test_example_insert_here reason something_new_here anlangen_text changes existing_majority result long_text reason_for_this")

    def test_conduct_get_absolute_url_setup_normal_success(self):
        number_url = "1234567890"
        custom_url =  Conduct.get_absolute_url(number_url)
        self.assertEquals(str(custom_url), str("/Antragsverwaltungstool/show_advisory/?antrag=1234%2F67890"))

    def test_conduct_get_absolute_url_setup_short_success(self):
        number_url = "1"
        custom_url =  Conduct.get_absolute_url(number_url)
        self.assertEquals(str(custom_url), str("/Antragsverwaltungstool/show_advisory/?antrag=1%2F"))

    def test_conduct_get_absolute_url_setup_(self):
        number_url = "abs123&75%"
        custom_url =  Conduct.get_absolute_url(number_url)
        self.assertEquals(str(custom_url), str("/Antragsverwaltungstool/show_advisory/?antrag=abs1%2F3&75%"))

class test_Model_NumberCount(TestCase):

    def setup(self):
        self.MessageSuccess = NumberCount.objects.create(
            number = "1",
            legislature = "insert",
            session = 12,
            ongoing_number = 6
        )

    def test_numbercount___str___success(self):
        self.assertEquals(str(self), "1 insert 12 6")