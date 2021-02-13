""" apps/accounts/forms.py """

from django import forms
from django.contrib.auth.forms import AuthenticationForm


class EditorLoginForm(AuthenticationForm):
    """ Login form of Editor. """
    username = forms.CharField(
        label='Utilisateur :',
        initial='editeur',
        error_messages={
            'required': 'Ce champ est obligatoire',
        }
    )
    password = forms.CharField(
        label='Entrez votre mot de passe :',
        error_messages={
            'required': 'Ce champ est obligatoire',
        },
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password', 'autofocus': True}),
    )

    error_messages = {
        'invalid_login': 'Données non valides',
    }
