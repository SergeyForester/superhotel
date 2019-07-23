from django import forms
from django_starfield import Stars


# forms for booking.html

class HeaderPhotoForm(forms.Form):
    photos = forms.FileField(widget=forms.ClearableFileInput(attrs={'id': 'fileForm'}))


class NameOfHotelForm(forms.Form):
    name_of_hotel = forms.CharField(max_length=100,
                                    widget=forms.TextInput(attrs={'placeholder': 'THE FALCON AT HATTON HOTEL', 'class':'nameOfHotel'}))


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
    info = forms.CharField(max_length=6000, widget=forms.Textarea(
        attrs={'placeholder': 'Добавьте небольшое описание', 'cols': 45, 'rows': 10}))


class TelephoneNumberForm(forms.Form):
    number = forms.IntegerField(required=True, widget=forms.TextInput(
        attrs={'placeholder': '+30 123 123 12 12'}))


class AddressForm(forms.Form):
    address = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'г.Москва, Ленинградский проспект'}))


class LocalityForm(forms.Form):
    locality = forms.CharField(max_length=200)


class RegionForm(forms.Form):
    region = forms.CharField(max_length=200)


class PostalCodeForm(forms.Form):
    postalCode = forms.IntegerField(required=True, widget=forms.TextInput(
        attrs={'placeholder': '248880'}))


class MapLinkForm(forms.Form):
    mapCode = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Всавьте код карты', 'cols': 55, 'rows': 20}))


class UploadPhotoInfoForm(forms.Form):
    photo1 = forms.FileField(widget=forms.ClearableFileInput(attrs={'id': 'bookingPhotoForm1'}))
    photo2 = forms.FileField(widget=forms.ClearableFileInput(attrs={'id': 'bookingPhotoForm2'}))
    photo3 = forms.FileField(widget=forms.ClearableFileInput(attrs={'id': 'bookingPhotoForm3'}))


class LongDescriptionOfHotel(forms.Form):
    longdescr = forms.CharField(max_length=10000, widget=forms.Textarea(
        attrs={'placeholder': 'Our accommodation is situated in a separate building right next to the pub, perfect for a short stay whether it’s business or pleasure. Enjoy breakfast lunch or dinner with us at your leisure.',
               'cols': 45, 'rows': 10, 'class': 'headerDescription'}))


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


class JoinUsForm(forms.Form):
    text = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'JOIN US AT THE FALCON THIS SPRING!', 'class': 'joinUs'}))


class AdvantagesForm(forms.Form):
    advantages = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'placeholder': 'Gastro Restaurant, Country Pub and Hotel, The Falcon offers fine food, cosy corners and a real rustic feel.',
        'class': 'advantages'}))


class HeaderDescription(forms.Form):
    headerDescr = forms.CharField(max_length=400, widget=forms.Textarea(attrs={
        'placeholder': 'Enjoy our Autumn Menu – irresistibly innovative, with a choice of delightfully fresh flavours and familiar favourites. Toast our Sunday Roast, or simply savour a hand-pulled cask ale. Take a stroll straight off the car park down the public footpath and you’ll find stunning countryside. Amble past pretty St Mary’s Church, and down country lanes. Finish back at the Falcon for a well earned lunch.',
        'class': 'headerDescription', 'cols': 80, 'rows': 30}))


class ThreeWordsForm(forms.Form):
    threeWords = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'DINE . DRINK . STAY', 'class': 'threeWords'}))


class TextAfterThreeWords(forms.Form):
    textAfterThreeWords = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={
            'placeholder': 'View our latest menus, book one of our comfortable rooms for a short stay or feel special and indulge in our superb offers.',
            'class': 'afterThreeWords'}))

class PhotoDescriptions(forms.Form):
    photo1 = forms.FileField(widget=forms.ClearableFileInput(attrs={'id': 'photoDescription1'}))
    photo2 = forms.FileField(widget=forms.ClearableFileInput(attrs={'id': 'photoDescription2'}))
    photo3 = forms.FileField(widget=forms.ClearableFileInput(attrs={'id': 'photoDescription3'}))
    photo4 = forms.FileField(widget=forms.ClearableFileInput(attrs={'id': 'photoDescription4'}))

class BookAHotelRoom(forms.Form):
    text = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'BOOK A HOTEL ROOM', 'class': 'nameOfHotel'}))

# forms for book_a_room.html

class FirstStepDirections(forms.Form):
    directions = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Указания'}))


class RoomSelectionText(forms.Form):
    text = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Напишите что-нибудь'}))


class RoomBookingInstructions(forms.Form):
    instructions = forms.CharField(max_length=200,
                                   widget=forms.TextInput(attrs={'placeholder': 'Какое-нибудь предупреждение'}))


class SecondStepDirections(forms.Form):
    directions = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Указания 2'}))
