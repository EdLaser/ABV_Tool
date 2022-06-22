
from ast import And
from django.test import TestCase
import django
from Antragsverwaltungstool.models import AdvisoryMember, Finance, Position, Universall, Conduct, NumberCount


###   ADVISORYMEMBER   ###
class TestModel_AdvisoryMember(TestCase):

    def test_advisorymember___str___success(self):
        self.assertEquals(str(
         AdvisoryMember.objects.create(
            flag = 0,
            number = '1234567890',
            date = '2022-06-12',
            title = '2',
            office = '3',
            name = '4',
            mail = '5',
            text = '6',
            frg1 = '7',
            frg2 = '8',
            frg3 = '9',
            frg4 = '1',
            anlagen= '2',
            aenderung = '3',
            mehrheit = '4',
            beschluss = '5',
            beschlusstext = '6',
            beschlussgrund = '7'
        )    
        ), '0 1234567890 2022-06-12 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7')

    def test_advisorymember___str___failure(self):
        self.assertNotEquals(str(
         AdvisoryMember.objects.create(
            flag = 0,
            number = '1234567890',
            date = '2022-06-12',
            title = '2',
            office = '3',
            name = '4',
            mail = '5',
            text = '6',
            frg1 = '7',
            frg2 = '8',
            frg3 = '9',
            frg4 = '1',
            anlagen= '2',
            aenderung = '3',
            mehrheit = '4',
            beschluss = '5',
            beschlusstext = '6',
            beschlussgrund = '7'
        )    
        ), '0 123456789 2022-06-12 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7')

    def test_advisorymember_get_absolute_url_setup_normal_success(self):
        custom_url =  AdvisoryMember.get_absolute_url(AdvisoryMember.objects.create(
            flag = 0,
            number = '1234567890',
            date = '2022-06-12',
            title = '2',
            office = '3',
            name = '4',
            mail = '5',
            text = '6',
            frg1 = '7',
            frg2 = '8',
            frg3 = '9',
            frg4 = '1',
            anlagen= '2',
            aenderung = '3',
            mehrheit = '4',
            beschluss = '5',
            beschlusstext = '6',
            beschlussgrund = '7'
        ))
        self.assertEquals(str(custom_url), '/Antragsverwaltungstool/show_advisory/?antrag=1234%2F67890')


    def test_advisorymember_get_absolute_url_setup_short_success(self):
        custom_url =  AdvisoryMember.get_absolute_url(AdvisoryMember.objects.create(
            flag = 0,
            number = '1',
            date = '2022-06-12',
            title = '2',
            office = '3',
            name = '4',
            mail = '5',
            text = '6',
            frg1 = '7',
            frg2 = '8',
            frg3 = '9',
            frg4 = '1',
            anlagen= '2',
            aenderung = '3',
            mehrheit = '4',
            beschluss = '5',
            beschlusstext = '6',
            beschlussgrund = '7'
        ))
        self.assertEquals(str(custom_url), '/Antragsverwaltungstool/show_advisory/?antrag=1%2F')

    def test_advisorymember_get_absolute_url_setup_normal_fail(self):
        custom_url =  AdvisoryMember.get_absolute_url(AdvisoryMember.objects.create(
            flag = 0,
            number = '1234567890',
            date = '2022-06-12',
            title = '2',
            office = '3',
            name = '4',
            mail = '5',
            text = '6',
            frg1 = '7',
            frg2 = '8',
            frg3 = '9',
            frg4 = '1',
            anlagen= '2',
            aenderung = '3',
            mehrheit = '4',
            beschluss = '5',
            beschlusstext = '6',
            beschlussgrund = '7'
        ))
        self.assertNotEquals(str(custom_url), '/Antragsverwaltungstool/show_advisory/?antrag=1234%2F6789')

###   FINANCE   ###
class TestModel_Finance(TestCase):

    def test_finance___str___success(self):
        self.assertEquals(str(
            Finance.objects.create(
                flag = 0,
                number = '1234567890',
                date = '2022-06-12',
                title = 'TestOne',
                office = 'office',
                name = 'test',
                mail = 'test@htw-dresden.de',
                text = 'test_example_insert_here',
                reason = 'reason',
                budget = '10000',
                suggestion = 'something_new_here',
                anlagen= 'anlangen_text',
                aenderung = 'changes',
                mehrheit = 'existing_majority',
                beschluss = 'result',
                beschlusstext = 'long_text',
                beschlussgrund = 'reason_for_this'
            )   
        ), '0 1234567890 2022-06-12 TestOne office test test@htw-dresden.de test_example_insert_here reason 10000 something_new_here anlangen_text changes existing_majority result long_text reason_for_this')

    def test_finance___str___failure(self):
        self.assertNotEquals(str(
            Finance.objects.create(
                flag = 0,
                number = '1234567890',
                date = '2022-06-12',
                title = 'TestOne',
                office = 'office',
                name = 'test',
                mail = 'test@htw-dresden.de',
                text = 'test_example_insert_here',
                reason = 'reason',
                budget = '10000',
                suggestion = 'something_new_here',
                anlagen= 'anlangen_text',
                aenderung = 'changes',
                mehrheit = 'existing_majority',
                beschluss = 'result',
                beschlusstext = 'long_text',
                beschlussgrund = 'reason_for_this'
            )     
        ), '0 123456789 2022-06-12 TestOne office test test@htw-dresden.de test_example_insert_here reason 10000 something_new_here anlangen_text changes existing_majority result long_text reason_for_this')

    def test_finance_get_absolute_url_setup_normal_success(self):
        custom_url =  Finance.get_absolute_url(Finance.objects.create(
            flag = 0,
            number = '1234567890',
            date = '2022-06-12',
            title = 'TestOne',
            office = 'office',
            name = 'test',
            mail = 'test@htw-dresden.de',
            text = 'test_example_insert_here',
            reason = 'reason',
            budget = '10000',
            suggestion = 'something_new_here',
            anlagen= 'anlangen_text',
            aenderung = 'changes',
            mehrheit = 'existing_majority',
            beschluss = 'result',
            beschlusstext = 'long_text',
            beschlussgrund = 'reason_for_this'
        ))
        self.assertEquals(str(custom_url), '/Antragsverwaltungstool/show_finance/?antrag=1234%2F67890')

    def test_finance_get_absolute_url_setup_short_success(self):
        custom_url =  Finance.get_absolute_url(Finance.objects.create(
            flag = 0,
            number = '1',
            date = '2022-06-12',
            title = 'TestOne',
            office = 'office',
            name = 'test',
            mail = 'test@htw-dresden.de',
            text = 'test_example_insert_here',
            reason = 'reason',
            budget = '10000',
            suggestion = 'something_new_here',
            anlagen= 'anlangen_text',
            aenderung = 'changes',
            mehrheit = 'existing_majority',
            beschluss = 'result',
            beschlusstext = 'long_text',
            beschlussgrund = 'reason_for_this'
        ))
        self.assertEquals(str(custom_url), '/Antragsverwaltungstool/show_finance/?antrag=1%2F')

    def test_finance_get_absolute_url_setup_normal_fail(self):
        custom_url =  Finance.get_absolute_url(Finance.objects.create(
            flag = 0,
            number = '1234567890',
            date = '2022-06-12',
            title = 'TestOne',
            office = 'office',
            name = 'test',
            mail = 'test@htw-dresden.de',
            text = 'test_example_insert_here',
            reason = 'reason',
            budget = '10000',
            suggestion = 'something_new_here',
            anlagen= 'anlangen_text',
            aenderung = 'changes',
            mehrheit = 'existing_majority',
            beschluss = 'result',
            beschlusstext = 'long_text',
            beschlussgrund = 'reason_for_this'
        ))
        self.assertNotEquals(str(custom_url), '/Antragsverwaltungstool/show_finance/?antrag=1234%2F6789')

###   POSITION   ###
class TestModel_Position(TestCase):

    def test_position___str___success(self):
        self.assertEquals(str(
            Position.objects.create(
            flag = 0,
            number = '1234567890',
            date = '2022-06-12',
            title = 'TestOne',
            office = 'office',
            name = 'test',
            mail = 'test@htw-dresden.de',
            text = 'test_example_insert_here',
            frg1 = 'answer_frg1',
            frg2 = 'answer_frg2',
            frg3 = 'answer_frg3',
            frg4 = 'answer_frg4',
            frg_spez_1 = 'Inhalt',
            frg_spez_2 = 'Inhalt',
            frg_spez_3 = 'Inhalt',
            anlagen= 'anlangen_text',
            aenderung = 'change',
            mehrheit = 'existing_majority',
            beschluss = 'result',
            beschlusstext = 'long_text',
            beschlussgrund = 'reason_for_this'
            )   
        ), '0 1234567890 2022-06-12 TestOne office test test@htw-dresden.de test_example_insert_here answer_frg1 answer_frg2 answer_frg3 answer_frg4 Inhalt Inhalt Inhalt anlangen_text change existing_majority result long_text reason_for_this')

    def test_position___str___failure(self):
        self.assertNotEquals(str(
            Position.objects.create(
            flag = 0,
            number = '1234567890',
            date = '2022-06-12',
            title = 'TestOne',
            office = 'office',
            name = 'test',
            mail = 'test@htw-dresden.de',
            text = 'test_example_insert_here',
            frg1 = 'answer_frg1',
            frg2 = 'answer_frg2',
            frg3 = 'answer_frg3',
            frg4 = 'answer_frg4',
            frg_spez_1 = 'Inhalt',
            frg_spez_2 = 'Inhalt',
            frg_spez_3 = 'Inhalt',
            anlagen= 'anlangen_text',
            aenderung = 'change',
            mehrheit = 'existing_majority',
            beschluss = 'result',
            beschlusstext = 'long_text',
            beschlussgrund = 'reason_for_this'
            )     
        ), '0 1 2022-06-12 TestOne office test test@htw-dresden.de test_example_insert_here answer_frg1 answer_frg2 answer_frg3 answer_frg4 Inhalt Inhalt Inhalt anlangen_text change existing_majority result long_text reason_for_this')

    def test_position_get_absolute_url_setup_normal_success(self):
        custom_url =  Position.get_absolute_url(Position.objects.create(
            flag = 0,
            number = '1234567890',
            date = '2022-06-12',
            title = 'TestOne',
            office = 'office',
            name = 'test',
            mail = 'test@htw-dresden.de',
            text = 'test_example_insert_here',
            frg1 = 'answer_frg1',
            frg2 = 'answer_frg2',
            frg3 = 'answer_frg3',
            frg4 = 'answer_frg4',
            frg_spez_1 = 'Inhalt',
            frg_spez_2 = 'Inhalt',
            frg_spez_3 = 'Inhalt',
            anlagen= 'anlangen_text',
            aenderung = 'change',
            mehrheit = 'existing_majority',
            beschluss = 'result',
            beschlusstext = 'long_text',
            beschlussgrund = 'reason_for_this'
        ))
        self.assertEquals(str(custom_url), '/Antragsverwaltungstool/show_position/?antrag=1234%2F67890')

    def test_position_get_absolute_url_setup_short_success(self):
        custom_url =  Position.get_absolute_url(Position.objects.create(
            flag = 0,
            number = '1',
            date = '2022-06-12',
            title = 'TestOne',
            office = 'office',
            name = 'test',
            mail = 'test@htw-dresden.de',
            text = 'test_example_insert_here',
            frg1 = 'answer_frg1',
            frg2 = 'answer_frg2',
            frg3 = 'answer_frg3',
            frg4 = 'answer_frg4',
            frg_spez_1 = 'Inhalt',
            frg_spez_2 = 'Inhalt',
            frg_spez_3 = 'Inhalt',
            anlagen= 'anlangen_text',
            aenderung = 'change',
            mehrheit = 'existing_majority',
            beschluss = 'result',
            beschlusstext = 'long_text',
            beschlussgrund = 'reason_for_this'
        ))
        self.assertEquals(str(custom_url), '/Antragsverwaltungstool/show_position/?antrag=1%2F')

    def test_position_get_absolute_url_setup_normal_fail(self):
        custom_url =  Position.get_absolute_url(Position.objects.create(
            flag = 0,
            number = '1234567890',
            date = '2022-06-12',
            title = 'TestOne',
            office = 'office',
            name = 'test',
            mail = 'test@htw-dresden.de',
            text = 'test_example_insert_here',
            frg1 = 'answer_frg1',
            frg2 = 'answer_frg2',
            frg3 = 'answer_frg3',
            frg4 = 'answer_frg4',
            frg_spez_1 = 'Inhalt',
            frg_spez_2 = 'Inhalt',
            frg_spez_3 = 'Inhalt',
            anlagen= 'anlangen_text',
            aenderung = 'change',
            mehrheit = 'existing_majority',
            beschluss = 'result',
            beschlusstext = 'long_text',
            beschlussgrund = 'reason_for_this'
        ))
        self.assertNotEquals(str(custom_url), '/Antragsverwaltungstool/show_position/?antrag=1234%2F6789')

###   Universall   ###
class TestModel_Position(TestCase):

    def test_universall___str___success(self):
        self.assertEquals(str(
            Universall.objects.create(
            flag = 0,
            number = '1234567890',
            date = '2022-06-12',
            title = 'TestOne',
            office = 'office',
            name = 'test',
            mail = 'test@htw-dresden.de',
            text = 'test_example_insert_here',
            reason = 'reason',
            suggestion = 'something_new_here',
            anlagen= 'anlangen_text',
            aenderung = 'changes',
            mehrheit = 'existing_majority',
            beschluss = 'result',
            beschlusstext = 'long_text',
            beschlussgrund = 'reason_for_this'
            )   
        ), '0 1234567890 2022-06-12 TestOne office test test@htw-dresden.de test_example_insert_here reason something_new_here anlangen_text changes existing_majority result long_text reason_for_this')

    def test_universall___str___failure(self):
        self.assertNotEquals(str(
            Universall.objects.create(
            flag = 0,
            number = '1234567890',
            date = '2022-06-12',
            title = 'TestOne',
            office = 'office',
            name = 'test',
            mail = 'test@htw-dresden.de',
            text = 'test_example_insert_here',
            reason = 'reason',
            suggestion = 'something_new_here',
            anlagen= 'anlangen_text',
            aenderung = 'changes',
            mehrheit = 'existing_majority',
            beschluss = 'result',
            beschlusstext = 'long_text',
            beschlussgrund = 'reason_for_this'
            )     
        ), '0 1 2022-06-12 TestOne office test test@htw-dresden.de test_example_insert_here reason something_new_here anlangen_text changes existing_majority result long_text reason_for_this')

    def test_universall_get_absolute_url_setup_normal_success(self):
        custom_url =  Universall.get_absolute_url(Universall.objects.create(
            flag = 0,
            number = '1234567890',
            date = '2022-06-12',
            title = 'TestOne',
            office = 'office',
            name = 'test',
            mail = 'test@htw-dresden.de',
            text = 'test_example_insert_here',
            reason = 'reason',
            suggestion = 'something_new_here',
            anlagen= 'anlangen_text',
            aenderung = 'changes',
            mehrheit = 'existing_majority',
            beschluss = 'result',
            beschlusstext = 'long_text',
            beschlussgrund = 'reason_for_this'
        ))
        self.assertEquals(str(custom_url), '/Antragsverwaltungstool/show_universall/?antrag=1234%2F67890')

    def test_universall_get_absolute_url_setup_short_success(self):
        custom_url =  Universall.get_absolute_url(Universall.objects.create(
            flag = 0,
            number = '1',
            date = '2022-06-12',
            title = 'TestOne',
            office = 'office',
            name = 'test',
            mail = 'test@htw-dresden.de',
            text = 'test_example_insert_here',
            reason = 'reason',
            suggestion = 'something_new_here',
            anlagen= 'anlangen_text',
            aenderung = 'changes',
            mehrheit = 'existing_majority',
            beschluss = 'result',
            beschlusstext = 'long_text',
            beschlussgrund = 'reason_for_this'
        ))
        self.assertEquals(str(custom_url), '/Antragsverwaltungstool/show_universall/?antrag=1%2F')

    def test_universall_get_absolute_url_setup_normal_fail(self):
        custom_url =  Universall.get_absolute_url(Universall.objects.create(
            flag = 0,
            number = '1234567890',
            date = '2022-06-12',
            title = 'TestOne',
            office = 'office',
            name = 'test',
            mail = 'test@htw-dresden.de',
            text = 'test_example_insert_here',
            reason = 'reason',
            suggestion = 'something_new_here',
            anlagen= 'anlangen_text',
            aenderung = 'changes',
            mehrheit = 'existing_majority',
            beschluss = 'result',
            beschlusstext = 'long_text',
            beschlussgrund = 'reason_for_this'
        ))
        self.assertNotEquals(str(custom_url), '/Antragsverwaltungstool/show_universall/?antrag=1234%2F6789')

###   CONDUCT   ###
class TestModel_Conduct(TestCase):

    def test_conduct___str___success(self):
        self.assertEquals(str(
            Conduct.objects.create(
            flag = 0,
            number = '1234567890',
            date = '2022-06-12',
            title = 'TestOne',
            office = 'office',
            name = 'test',
            mail = 'test@htw-dresden.de',
            text = 'test_example_insert_here',
            reason = 'reason',
            suggestion = 'something_new_here',
            anlagen= 'anlangen_text',
            aenderung = 'changes',
            mehrheit = 'existing_majority',
            beschluss = 'result',
            beschlusstext = 'long_text',
            beschlussgrund = 'reason_for_this'
            )   
        ), '0 1234567890 2022-06-12 TestOne office test test@htw-dresden.de test_example_insert_here reason something_new_here anlangen_text changes existing_majority result long_text reason_for_this')

    def test_conduct___str___failure(self):
        self.assertNotEquals(str(
            Conduct.objects.create(
            flag = 0,
            number = '1234567890',
            date = '2022-06-12',
            title = 'TestOne',
            office = 'office',
            name = 'test',
            mail = 'test@htw-dresden.de',
            text = 'test_example_insert_here',
            reason = 'reason',
            suggestion = 'something_new_here',
            anlagen= 'anlangen_text',
            aenderung = 'changes',
            mehrheit = 'existing_majority',
            beschluss = 'result',
            beschlusstext = 'long_text',
            beschlussgrund = 'reason_for_this'
            )     
        ), '0 1 2022-06-12 TestOne office test test@htw-dresden.de test_example_insert_here reason something_new_here anlangen_text changes existing_majority result long_text reason_for_this')

    def test_conduct_get_absolute_url_setup_normal_success(self):
        custom_url =  Conduct.get_absolute_url(Conduct.objects.create(
            flag = 0,
            number = '1234567890',
            date = '2022-06-12',
            title = 'TestOne',
            office = 'office',
            name = 'test',
            mail = 'test@htw-dresden.de',
            text = 'test_example_insert_here',
            reason = 'reason',
            suggestion = 'something_new_here',
            anlagen= 'anlangen_text',
            aenderung = 'changes',
            mehrheit = 'existing_majority',
            beschluss = 'result',
            beschlusstext = 'long_text',
            beschlussgrund = 'reason_for_this'
        ))
        self.assertEquals(str(custom_url), '/Antragsverwaltungstool/show_conduct/?antrag=1234%2F67890')

    def test_conduct_get_absolute_url_setup_short_success(self):
        custom_url =  Conduct.get_absolute_url(Conduct.objects.create(
            flag = 0,
            number = '1',
            date = '2022-06-12',
            title = 'TestOne',
            office = 'office',
            name = 'test',
            mail = 'test@htw-dresden.de',
            text = 'test_example_insert_here',
            reason = 'reason',
            suggestion = 'something_new_here',
            anlagen= 'anlangen_text',
            aenderung = 'changes',
            mehrheit = 'existing_majority',
            beschluss = 'result',
            beschlusstext = 'long_text',
            beschlussgrund = 'reason_for_this'
        ))
        self.assertEquals(str(custom_url), '/Antragsverwaltungstool/show_conduct/?antrag=1%2F')

    def test_conduct_get_absolute_url_setup_normal_fail(self):
        custom_url =  Conduct.get_absolute_url(Conduct.objects.create(
            flag = 0,
            number = '1234567890',
            date = '2022-06-12',
            title = 'TestOne',
            office = 'office',
            name = 'test',
            mail = 'test@htw-dresden.de',
            text = 'test_example_insert_here',
            reason = 'reason',
            suggestion = 'something_new_here',
            anlagen= 'anlangen_text',
            aenderung = 'changes',
            mehrheit = 'existing_majority',
            beschluss = 'result',
            beschlusstext = 'long_text',
            beschlussgrund = 'reason_for_this'
        ))
        self.assertNotEquals(str(custom_url), '/Antragsverwaltungstool/show_conduct/?antrag=1234%2F6789')

###   NUMBERCOUNT   ###
class TestModel_NumberCount(TestCase):

    def test_numbercount___str___success(self):
        self.assertEquals(str(
            NumberCount.objects.create(
            number = '1',
            legislature = 'insert',
            session = 12,
            ongoing_number = 6
            )   
        ), 'insert 12 6')

    def test_numbercount___str___failure(self):
        self.assertNotEquals(str(
            NumberCount.objects.create(
            number = '1',
            legislature = 'insert',
            session = 12,
            ongoing_number = 6
            )     
        ), 'insert 12 7')
