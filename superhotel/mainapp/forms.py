from django import forms
from django_starfield import Stars
# forms for booking.html

class HeaderPhotoForm(forms.Form):
    photos = forms.FileField()

class NameOfHotelForm(forms.Form):
    name_of_hotel = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'El Balata, например'}))

class StarsForm(forms.Form):
    STARS_CHOICES = (
        (1, ("1-звездочный отель")),
        (2, ("2-звездочный отель")),
        (3, ("3-звездочный отель")),
        (4, ("4-звездочный отель")),
        (5, ("5-звездочный отель"))
    )
    stars = forms.ChoiceField(choices=STARS_CHOICES, label="", initial='', required=True)

class NameOfHotelInfoForm(forms.Form):
    info = forms.CharField(max_length=6000, widget=forms.Textarea(attrs={'placeholder': 'Добавьте небольшое описание','cols': 45, 'rows': 10}))

class TelephoneNumberForm(forms.Form):
    number = forms.IntegerField(required=True)

class AddressForm(forms.Form):
    address = forms.CharField(max_length=100)


class LocalityForm(forms.Form):
    locality = forms.CharField(max_length=200)

class RegionForm(forms.Form):
    region = forms.CharField(max_length=200)

class PostalCodeForm(forms.Form):
    postalCode = forms.IntegerField(required=True)

class MapLinkForm(forms.Form):
    link = forms.URLField()

class UploadPhotoInfoForm(forms.Form):
    # for x in range(6):
    #     photo+x = forms.FileField
    photo1 = forms.FileField()
    photo2 = forms.FileField()
    photo3 = forms.FileField()
    photo4 = forms.FileField()
    photo5 = forms.FileField()
    photo6 = forms.FileField()

class LongDescriptionOfHotel(forms.Form):
    longdescr = forms.CharField(max_length=10000, widget=forms.Textarea(attrs={'placeholder': 'Добавьте большое описание','cols': 45, 'rows': 10}))

class FeatureForm(forms.Form):
    feature1 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Добавьте преимущество'}))
    feature2 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Добавьте преимущество'}))
    feature3 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Добавьте преимущество'}))
    feature4 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Добавьте преимущество'}))
    feature5 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Добавьте преимущество'}))
    feature6 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Добавьте преимущество'}))
    feature7 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Добавьте преимущество'}))
    feature8 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Добавьте преимущество'}))

class TermsAndConditionsForm(forms.Form):
    terms = forms.CharField(max_length=3000)

# forms for book_a_room.html

class FirstStepDirections(forms.Form):
    directions = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Указания'}))

class RoomSelectionText(forms.Form):
    text = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Напишите что-нибудь'}))

class RoomBookingInstructions(forms.Form):
    instructions = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Какое-нибудь предупреждение'}))

class SecondStepDirections(forms.Form):
    directions = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Указания 2'}))




