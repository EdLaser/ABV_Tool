""" Defines all the models the application is working with. """
import django
from django.db import models
import os
#from formatChecker import ContentTypeRestrictedFileField
from django.core.exceptions import ValidationError

def file_size(value): # add this to some file where you can import it from
    limit = 5 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 5 MiB.')



def upload_attachment(instance, filename):
        print(os.getcwd() + filename)
        #return f"" + os.getcwd() + "/" + filename + ""
        return f"{filename}"


class AdvisoryMember(models.Model):
    """
    Represents an application for an advisory members with variables containing all application data.
    All variables are of type model.field with max lengths and the possibility to be null in the database.

    Arguments: models.Model: Django uses models to represent classes to work with in the application, which are
    representing database tables.
    """
    flag = models.IntegerField(default=0)
    """ The current status of the application. """
    number = models.CharField(max_length=15, primary_key=True, unique=True)
    """ Number of the application in the database (primary_key). """
    date = models.DateField(default=django.utils.timezone.now)
    """ Date when the application is made. """
    title = models.CharField(max_length=50, null=True)
    """ Title of the application. """
    office = models.CharField(max_length=75, null=True)
    """ Office the application is pointed to. """
    name = models.CharField(max_length=25, null=True)
    """ Name of the applicant. """
    mail = models.EmailField(max_length=30, null=True)
    """ Email of the applicant. """
    text = models.CharField(max_length=260, null=True)
    """ Text of the application. """
    frg1 = models.CharField(max_length=260, null=True)
    """ Question wether the applicant is in other organisation. """
    frg2 = models.CharField(max_length=260, null=True)
    """ Question about the time investment of the applicant. """
    frg3 = models.CharField(max_length=260, null=True)
    """ Is the applicant willing to put work outside his position. """
    frg4 = models.CharField(max_length=260, null=True)
    """ How can the applicant support during a zombie apocalypose. """
    anlagen = models.FileField(upload_to=upload_attachment, null=True)
    """ Attachments to the entry. """
    aenderung = models.CharField(max_length=260, null=True)
    """ Possible changes of the application. """
    mehrheit = models.CharField(max_length=25, null=True)
    """ The majority needed to pass the application. """
    beschluss = models.CharField(max_length=250, null=True)
    """ Decision done in the application. """
    beschlusstext = models.CharField(max_length=250, null=True)
    """ Text of the deciosion. """
    beschlussgrund = models.CharField(max_length=250, null=True)
    """ Reason for the deciosion. """
    status = models.IntegerField(default=0)
    """ Application WIP status """

    class Meta:
        """ Sets the ordering for the model. """
        ordering = ['number']

    def __str__(self):
        """
         Displays a string representation of the model AdvisoryMember for the admin class to call.

         Retuns a string representation of the model with all the variables in it to display on the admin page.
        """
        return '%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s' % (
            self.flag, self.number, self.date, self.title, self.office, self.name, self.mail, self.text,
            self.frg1, self.frg2, self.frg3, self.frg4, self.anlagen, self.aenderung, self.mehrheit, self.beschluss,
            self.beschlusstext, self.beschlussgrund)

    def get_absolute_url(self):
        return f"/Antragsverwaltungstool/show_advisory/?antrag={self.number[:4]+'%2F'+self.number[5:]}"

    def get_absolute_url_public(self):
        return f"/Antragsverwaltungstool/show_advisory_public/?antrag={self.number[:4]+'%2F'+self.number[5:]}"

class Finance(models.Model):
    """
    Represents an application with financial support with variables containing all application data.
    All variables are of type model.field with max lengths and the possibility to be null in the database.

    Arguments: models.Model: Django uses models to represent classes to work with in the application, which are
    representing database tables.
    """
    flag = models.IntegerField(default=0)
    """ The current status of the application. """
    number = models.CharField(max_length=15, primary_key=True, unique=True)
    """ Number of the application in the database (primary_key). """
    date = models.DateField(default=django.utils.timezone.now)
    """ Date when the application is made. """
    title = models.CharField(max_length=50, null=True)
    """ Title of the application. """
    office = models.CharField(max_length=75, null=True)
    """ Office the application is pointed to. """
    name = models.CharField(max_length=25, null=True)
    """ Name of the applicant. """
    mail = models.EmailField(max_length=30, null=True)
    """ Email of the applicant. """
    text = models.CharField(max_length=260, null=True)
    """ Text of the application. """
    reason = models.CharField(max_length=260, null=True)
    """ Reason why the application has been made. """
    budget = models.CharField(max_length=260, null=True)
    """ Budget needed for the application. """
    suggestion = models.CharField(max_length=260, null=True)
    """ Suggestion what should be done after the applications is processed. """
    anlagen = models.FileField(upload_to=upload_attachment, null=True)
    """ Attachments to the entry. """
    aenderung = models.CharField(max_length=260, null=True)
    """ Possible changes of the application. """
    mehrheit = models.CharField(max_length=25, null=True)
    """ The majority needed to pass the application. """
    beschluss = models.CharField(max_length=250, null=True)
    """ Decision done in the application. """
    beschlusstext = models.CharField(max_length=250, null=True)
    """ Text of the deciosion. """
    beschlussgrund = models.CharField(max_length=250, null=True)
    """ Reason for the deciosion. """
    status = models.IntegerField(default=0)
    """ Application WIP status """

    class Meta:
        """ Sets the ordering for the model. """
        ordering = ['number']

    def __str__(self):
        """
         Displays a string representation of the model Finance for the admin class to call.

         Retuns a string representation of the model with all the variables in it to display on the admin page.
        """
        return '%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s' % (
            self.flag, self.number, self.date, self.title, self.office, self.name, self.mail, self.text,
            self.reason, self.budget, self.suggestion, self.anlagen, self.aenderung, self.mehrheit, self.beschluss,
            self.beschlusstext, self.beschlussgrund)

    def get_absolute_url(self):
        return f"/Antragsverwaltungstool/show_finance/?antrag={self.number[:4]+'%2F'+self.number[5:]}"
    def get_absolute_url_public(self):
        return f"/Antragsverwaltungstool/show_finance_public/?antrag={self.number[:4]+'%2F'+self.number[5:]}"
    



class Position(models.Model):
    """
    Represents an application for a special position with variables containing all application data. This application
    is very similar to the advisory member but with three extra questions.
    All variables are of type model.field with max lengths and the possibility to be null in the database.

    Arguments: models.Model: Django uses models to represent classes to work with in the application, which are
    representing database tables.
    """
    flag = models.IntegerField(default=0)
    """ The current status of the application. """
    number = models.CharField(max_length=15, primary_key=True, unique=True)
    """ Number of the application in the database (primary_key). """
    date = models.DateField(default=django.utils.timezone.now)
    """ Date when the application is made. """
    title = models.CharField(max_length=50, null=True)
    """ Title of the application. """
    office = models.CharField(max_length=75, null=True)
    """ Office the application is pointed to. """
    name = models.CharField(max_length=25, null=True)
    """ Name of the applicant. """
    mail = models.EmailField(max_length=30, null=True)
    """ Email of the applicant. """
    text = models.CharField(max_length=260, null=True)
    """ Text of the application. """
    frg1 = models.CharField(max_length=260, null=True)
    """ Question wether the applicant is in other organisation. """
    frg2 = models.CharField(max_length=260, null=True)
    """ Question about the time investment of the applicant. """
    frg3 = models.CharField(max_length=260, null=True)
    """ Is the applicant willing to put work outside his position. """
    frg4 = models.CharField(max_length=260, null=True)
    """ How can the applicant support during a zombie apocalypose. """
    frg_spez_1 = models.CharField(max_length=260, null=True)
    """ Evaluation of the announcement of the position. """
    frg_spez_2 = models.CharField(max_length=260, null=True)
    """ Evaluation of the previous work done by predecessors. """
    frg_spez_3 = models.CharField(max_length=260, null=True)
    """ What topics does the applicant plan to  put in the foreground in his term of office. """
    anlagen = models.FileField(upload_to=upload_attachment, null=True)
    """ Attachments to the entry. """
    aenderung = models.CharField(max_length=260, null=True)
    """ Possible changes of the application. """
    mehrheit = models.CharField(max_length=25, null=True)
    """ The majority needed to pass the application. """
    beschluss = models.CharField(max_length=250, null=True)
    """ Decision done in the application. """
    beschlusstext = models.CharField(max_length=250, null=True)
    """ Text of the deciosion. """
    beschlussgrund = models.CharField(max_length=250, null=True)
    """ Reason for the deciosion. """
    status = models.IntegerField(default=0)
    """ Application WIP status """

    class Meta:
        """ Sets the ordering for the model. """
        ordering = ['number']

    def __str__(self):
        """
         Displays a string representation of the model Position for the admin class to call.

         Retuns a string representation of the model with all the variables in it to display on the admin page.
        """
        return '%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s' % (
            self.flag, self.number, self.date, self.title, self.office, self.name, self.mail, self.text, self.frg1,
            self.frg2, self.frg3, self.frg4, self.frg_spez_1, self.frg_spez_2, self.frg_spez_3, self.anlagen,
            self.aenderung, self.mehrheit, self.beschluss, self.beschlusstext, self.beschlussgrund)

    def get_absolute_url(self):
        return f"/Antragsverwaltungstool/show_position/?antrag={self.number[:4]+'%2F'+self.number[5:]}"
    def get_absolute_url_public(self):
        return f"/Antragsverwaltungstool/show_position_public/?antrag={self.number[:4]+'%2F'+self.number[5:]}"


class Universall(models.Model):
    """
    Represents an universall application with variables containing all application data. This application is similar
    to the application with financial support but without the budegt variable.
    All variables are of type model.field with max lengths and the possibility to be null in the database.

    Arguments: models.Model: Django uses models to represent classes to work with in the application, which are
    representing database tables.
    """
    flag = models.IntegerField(default=0)
    """ The current status of the application. """
    number = models.CharField(max_length=15, primary_key=True, unique=True)
    """ Number of the application in the database (primary_key). """
    date = models.DateField(default=django.utils.timezone.now)
    """ Date when the application is made. """
    title = models.CharField(max_length=50, null=True)
    """ Title of the application. """
    office = models.CharField(max_length=75, null=True)
    """ Office the application is pointed to. """
    name = models.CharField(max_length=25, null=True)
    """ Name of the applicant. """
    mail = models.EmailField(max_length=30, null=True)
    """ Email of the applicant. """
    text = models.CharField(max_length=260, null=True)
    """ Text of the application. """
    reason = models.CharField(max_length=260, null=True)
    """ Reason why the application has been made. """
    suggestion = models.CharField(max_length=260, null=True)
    """ Suggestion what should be done after the applications is processed. """
    anlagen = models.FileField(upload_to=upload_attachment, null=True)
    """ Attachments to the entry. """
    aenderung = models.CharField(max_length=260, null=True)
    """ Possible changes of the application. """
    mehrheit = models.CharField(max_length=25, null=True)
    """ The majority needed to pass the application. """
    beschluss = models.CharField(max_length=250, null=True)
    """ Decision done in the application. """
    beschlusstext = models.CharField(max_length=250, null=True)
    """ Text of the deciosion. """
    beschlussgrund = models.CharField(max_length=250, null=True)
    """ Reason for the deciosion. """
    status = models.IntegerField(default=0)
    """ Application WIP status """

    class Meta:
        """ Sets the ordering for the model. """
        ordering = ['number']

    def __str__(self):
        """
         Displays a string representation of the model Universall for the admin class to call.

         Retuns a string representation of the model with all the variables in it to display on the admin page.
        """
        return '%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s' % (
            self.flag, self.number, self.date, self.title, self.office, self.name, self.mail, self.text, self.reason,
            self.suggestion, self.anlagen, self.aenderung, self.mehrheit, self.beschluss, self.beschlusstext,
            self.beschlussgrund)

    def get_absolute_url(self):
        return f"/Antragsverwaltungstool/show_universall/?antrag={self.number[:4]+'%2F'+self.number[5:]}"
    def get_absolute_url_public(self):
        return f"/Antragsverwaltungstool/show_universall_public/?antrag={self.number[:4]+'%2F'+self.number[5:]}"


class Conduct(models.Model):
    """
    Represents an application to establishe conduct with for special proceedures with variables containing all
    application data. This application may look like the universall one but must be seperated by the universall one.
    All variables are of type model.field with max lengths and the possibility to be null in the database.

    Arguments: models.Model: Django uses models to represent classes to work with in the application, which are
    representing database tables.
    """
    flag = models.IntegerField(default=0)
    """ The current status of the application. """
    number = models.CharField(max_length=15, primary_key=True, unique=True)
    """ Number of the application in the database (primary_key). """
    date = models.DateField(default=django.utils.timezone.now)
    """ Date when the application is made. """
    title = models.CharField(max_length=50, null=True)
    """ Title of the application. """
    office = models.CharField(max_length=75, null=True)
    """ Office the application is pointed to. """
    name = models.CharField(max_length=25, null=True)
    """ Name of the applicant. """
    mail = models.EmailField(max_length=30, null=True)
    """ Email of the applicant. """
    text = models.CharField(max_length=260, null=True)
    """ Text of the application. """
    reason = models.CharField(max_length=260, null=True)
    """ Reason why the application has been made. """
    suggestion = models.CharField(max_length=260, null=True)
    """ Suggestion what should be done after the applications is processed. """
    anlagen = models.FileField(upload_to=upload_attachment, null=True)
    """ Attachments to the entry. """
    aenderung = models.CharField(max_length=260, null=True)
    """ Possible changes of the application. """
    mehrheit = models.CharField(max_length=25, null=True)
    """ The majority needed to pass the application. """
    beschluss = models.CharField(max_length=250, null=True)
    """ Decision done in the application. """
    beschlusstext = models.CharField(max_length=250, null=True)
    """ Text of the deciosion. """
    beschlussgrund = models.CharField(max_length=250, null=True)
    """ Reason for the deciosion. """
    status = models.IntegerField(default=0)
    """ Application WIP status """

    class Meta:
        """ Sets the ordering for the model. """
        ordering = ['number']

    def __str__(self):
        """
         Displays a string representation of the model Conduct for the admin class to call.

         Retuns a string representation of the model with all the variables in it to display on the admin page.
        """
        return '%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s' % (
            self.flag, self.number, self.date, self.title, self.office, self.name, self.mail, self.text, self.reason,
            self.suggestion, self.anlagen, self.aenderung, self.mehrheit, self.beschluss, self.beschlusstext,
            self.beschlussgrund)

    def get_absolute_url(self):
        return f"/Antragsverwaltungstool/show_conduct/?antrag={self.number[:4]+'%2F'+self.number[5:]}"
    def get_absolute_url_public(self):
        return f"/Antragsverwaltungstool/show_conduct_public/?antrag={self.number[:4]+'%2F'+self.number[5:]}"


class NumberCount(models.Model):
    """
    Represents the ongoing number of the application.
    """
    number = models.CharField(max_length=15, primary_key=True)
    legislature = models.CharField(max_length=7)
    session = models.IntegerField()
    ongoing_number = models.IntegerField()

    class Meta:
        """ Sets the ordering for the model. """
        ordering = ['ongoing_number']

    def __str__(self):
        return '%s %s %s' % (self.legislature, self.session, self.ongoing_number)
