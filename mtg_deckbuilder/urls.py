from django.urls import path
from . import views, views_decks,  views_cards, views_users, mtg_api

from django.contrib.auth import views as auth_views


urlpatterns = [

    path('', views.homepage, name='homepage'),

    # Decks
    path('', views_decks.deck_list, name='deck_list'),
    path('decks/detail/<int:deck_pk>/', views_decks.deck_detail, name='deck_detail'),
    path('decks/add/', views_decks.new_deck, name='new_deck'),
    path('decks/edit/<int:deck_pk>/', views_decks.edit_deck, name='edit_deck'),

    # Users
    path('user/profile/<int:user_pk>/', views_users.user_profile, name='user_profile'),
    path('user/profile/', views_users.my_user_profile, name='my_user_profile'),
    path('user/profile/edit/', views_users.edit_user_profile, name='edit_user_profile'),
    path('user/profile/password/', views_users.change_password, name='change_password'),

    # Account
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('register/', views_users.register, name='register'),

    # API
    path('flavor_text/', mtg_api.flava, name='get_flavor_text'),

    # Card List
    path('card_list/', views_cards.card_list, name='card_list'),
    path('save_card_list/', views_cards.save_user_card_list, name='save_card_list')
]