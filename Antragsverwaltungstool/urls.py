""" Sets the url mappings for the requests. """
from django.urls import path, re_path, include
from . import views



urlpatterns = [
    path('', views.index, name='index'),

    path('new_universall/', views.new_universall, name="universall"),
    path('new_finance/', views.new_finance, name="finance"),
    path('new_election_report/', views.new_position, name="election_report"),
    path('new_advisory_member/', views.new_advisory, name="advisory_member"),
    path('new_conduct/', views.new_conduct, name="conduct"),
    path('intern/', views.get_all_by_electioninput, name="intern"),
    path('published_applications/', views.published_applications, name="published_applications"),

    path('show_universall/', views.change_universall, name="change_uni"),
    path('show_advisory/', views.change_advisory, name="change_advi"),
    path('show_position/', views.change_position, name="change_posi"),
    path('show_finance/', views.change_finance, name="change_fin"),
    path('show_conduct/', views.change_conduct, name="change_con"),

    path('show_universall_public/', views.show_universall, name="show_uni"),
    path('show_advisory_public/', views.show_advisory, name="show_advi"),
    path('show_position_public/', views.show_position, name="show_posi"),
    path('show_finance_public/', views.show_finance, name="show_fin"),
    path('show_conduct_public/', views.show_conduct, name="show_con"),

    path('', include('django.contrib.auth.urls')),
]
""" All the url patterns and the according view to the mappings """
