from django.test import SimpleTestCase
from Antragsverwaltungstool.forms import NewUniversallForm


class TestForms(SimpleTestCase):

    def test_universal_form_valid(self):
        form = NewUniversallForm(data={
         'title' : 'TestOne',
         'office' : 'office',
         'name' : 'test',
         'mail' : 'test@htw-dresden.de',
         'text' : 'test_example_insert_here',
         'reason' : 'reason',
         'suggestion' : 'something_new_here',
         'anlagen' : 'anlangen_text',
         'aenderung' : 'changes',
         'mehrheit' : 'existing_majority',
         'beschluss' : 'result',
         'beschlusstext' : 'long_text',
         'beschlussgrund' : 'reason_for_this'
     })
        self.assertTrue(form.is_valid())

    def test_universal_form_no_data_invalid(self):
        form = NewUniversallForm(data={
        })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),13)