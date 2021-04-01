""" apps/products/forms.py """

from django import forms

from .models import Collection, Interpreter, Product


class BookForm(forms.ModelForm):
    """ Form for Book. """
    category = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'book',
            }
        ),
    )
    ref_tm = forms.CharField(
        required=False,
        label='Réf. TM :',
        label_suffix='',
    )
    ean = forms.CharField(
        required=False,
        label='EAN :',
        label_suffix='',
    )
    title = forms.CharField(
        required=False,
        label='Titre :',
        label_suffix='',
    )
    sub_title = forms.CharField(
        required=False,
        label='Sous-titre :',
        label_suffix='',
    )
    author = forms.CharField(
        required=False,
        label='Auteur :',
        label_suffix='',
    )
    collection = forms.ModelChoiceField(
        required=False,
        queryset=Collection.objects.all().order_by('name'),
        label='Collection :',
        label_suffix='',
    )
    number_in_collection = forms.IntegerField(
        required=False,
        label='Numéro dans la collection :',
        label_suffix='',
        error_messages={
            'min_value': 'Veuillez entrer un nombre positif.',
        },
    )
    circulation = forms.IntegerField(
        required=False,
        label='Tirage :',
        label_suffix='',
        error_messages={
            'min_value': 'Veuillez entrer un nombre positif.',
        },
    )
    publication = forms.DateField(
        required=False,
        label='Date de parution :',
        label_suffix='',
    )
    width = forms.IntegerField(
        required=False,
        label='Largeur :',
        label_suffix='',
        error_messages={
            'min_value': 'Veuillez entrer un nombre positif.',
        },
    )
    height = forms.IntegerField(
        required=False,
        label='Hauteur :',
        label_suffix='',
        error_messages={
            'min_value': 'Veuillez entrer un nombre positif.',
        },
    )
    number_of_pages = forms.IntegerField(
        required=False,
        label='Nombre de pages :',
        label_suffix='',
        error_messages={
            'min_value': 'Veuillez entrer un nombre positif.',
        },
    )
    weight = forms.IntegerField(
        required=False,
        label='Poids :',
        label_suffix='',
        error_messages={
            'min_value': 'Veuillez entrer un nombre positif.',
        },
    )
    presentation_product = forms.CharField(
        required=False,
        widget=forms.Textarea(),
        label='Présentation produit :',
        label_suffix='',
    )
    presentation_author = forms.CharField(
        required=False,
        widget=forms.Textarea(),
        label='Présentation auteur :',
        label_suffix='',
    )
    strong_points = forms.CharField(
        required=False,
        widget=forms.Textarea(),
        label='Points forts :',
        label_suffix='',
    )
    target_audience = forms.CharField(
        required=False,
        widget=forms.Textarea(),
        label='Public visé :',
        label_suffix='',
    )
    coefficient = forms.FloatField(
        required=False,
        label='Coefficient :',
        label_suffix='',
        widget=forms.NumberInput(
            attrs={
                'placeholder': '6',
            }
        ),
        error_messages={
            'min_value': 'Veuillez entrer un nombre positif.',
        },
    )
    price = forms.FloatField(
        required=False,
        label='Prix public :',
        label_suffix='',
    )

    class Meta:
        model = Product
        fields = [
            'category',
            'ean',
            'ref_tm',
            'title',
            'sub_title',
            'author',
            'collection',
            'number_in_collection',
            'presentation_product',
            'presentation_author',
            'strong_points',
            'target_audience',
            'number_of_pages',
            'circulation',
            'publication',
            'width',
            'height',
            'weight',
            'coefficient',
            'price',
        ]


class DiskForm(forms.ModelForm):
    """ Form for CD. """
    category = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'disk',
            }
        ),
    )
    ref_tm = forms.CharField(
        required=False,
        label='Réf. TM :',
        label_suffix='',
    )
    ean = forms.CharField(
        required=False,
        label='EAN :',
        label_suffix='',
    )
    title = forms.CharField(
        required=False,
        label='Titre :',
        label_suffix='',
    )
    sub_title = forms.CharField(
        required=False,
        label='Sous-titre :',
        label_suffix='',
    )
    interpreter = forms.ModelChoiceField(
        required=False,
        queryset=Interpreter.objects.all().order_by('name'),
        label='Interprète :',
        label_suffix='',
    )
    circulation = forms.IntegerField(
        required=False,
        label='Diffusion :',
        label_suffix='',
    )
    publication = forms.DateField(
        required=False,
        label='Date de parution :',
        label_suffix='',
    )
    weight = forms.IntegerField(
        required=False,
        label='Poids :',
        label_suffix='',
    )
    coefficient = forms.FloatField(
        required=False,
        label='Coefficient :',
        label_suffix='',
    )
    pght = forms.FloatField(
        required=False,
        label='PGHT :',
        label_suffix='',
    )

    class Meta:
        model = Product
        fields = [
            'category',
            'ean',
            'ref_tm',
            'title',
            'sub_title',
            'interpreter',
            'circulation',
            'publication',
            'weight',
            'coefficient',
            'pght',
        ]


class ImageForm(forms.ModelForm):
    """ Form for Image. """
    category = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'image',
            }
        )
    )
    ref_tm = forms.CharField(
        required=False,
        label='Réf. TM :',
        label_suffix='',
    )
    ean = forms.CharField(
        required=False,
        label='EAN :',
        label_suffix='',
    )
    recto_img = forms.CharField(
        max_length=255,
        required=False,
        label='Recto :',
        label_suffix='',
    )
    verso_img = forms.CharField(
        required=False,
        max_length=255,
        label='Verso :',
        label_suffix='',
    )
    width = forms.IntegerField(
        required=False,
        label='Largeur :',
        label_suffix='',
    )
    height = forms.IntegerField(
        required=False,
        label='Hauteur :',
        label_suffix='',
    )
    price = forms.FloatField(
        required=False,
        label='Prix :',
        label_suffix='',
    )

    class Meta:
        model = Product
        fields = [
            'category',
            'ean',
            'ref_tm',
            'recto_img',
            'verso_img',
            'width',
            'height',
            'price',
        ]
