from django.shortcuts import render
from django.shortcuts import get_object_or_404, HttpResponseRedirect
from mainapp.forms import HeaderPhotoForm, NameOfHotelForm, StarsForm, NameOfHotelInfoForm
from mainapp.forms import TelephoneNumberForm, AddressForm, LocalityForm, RegionForm, PostalCodeForm
from mainapp.forms import MapLinkForm, UploadPhotoInfoForm, LongDescriptionOfHotel, FeatureForm, TermsAndConditionsForm
from mainapp.forms import FirstStepDirections, RoomSelectionText, RoomBookingInstructions, SecondStepDirections
# Create your views here.
def dataFromInputBooking(request):
    headerPhoto = HeaderPhotoForm(request.POST)
    nameOfHotel_form = NameOfHotelForm(request.POST)
    starsForm = StarsForm(request.POST)
    nameOfHotelInfo = NameOfHotelInfoForm(request.POST)
    telephoneNumberForm = TelephoneNumberForm(request.POST)
    addressForm = AddressForm(request.POST)
    localityForm = LocalityForm(request.POST)
    regionForm = RegionForm(request.POST)
    postal_codeForm = PostalCodeForm(request.POST)
    mapLinkForm = MapLinkForm(request.POST)
    uploadPhotoInfoForm = UploadPhotoInfoForm(request.POST)
    longDescriptionOfHotel = LongDescriptionOfHotel(request.POST)
    featureForm = FeatureForm(request.POST)
    termsAndConditions = TermsAndConditionsForm(request.POST)

    

    context = {'headerPhoto':headerPhoto, 'nameOfHotel_form':nameOfHotel_form,
               'starsForm':starsForm, 'nameOfHotelInfo':nameOfHotelInfo,
               'telephoneNumberForm':telephoneNumberForm, 'addressForm':addressForm,
               'localityForm':localityForm, 'regionForm':regionForm,
               'postal_codeForm':postal_codeForm, 'mapLinkForm':mapLinkForm,
               'uploadPhotoInfoForm':uploadPhotoInfoForm, 'longDescriptionOfHotel':longDescriptionOfHotel,
               'featureForm':featureForm, 'termsAndConditions':termsAndConditions}

    return render(request, 'mainapp/booking.html', context)

# из cleaned_data достаем данные и помещаем в файлы

def dataFromInputBookARoom(request):
    firstStepDirections = FirstStepDirections(request.POST)
    roomSelectionText = RoomSelectionText(request.POST)
    roomBookingInstructions = RoomBookingInstructions(request.POST)
    secondStepDirections = SecondStepDirections(request.POST)


    context = {'firstStepDirections':firstStepDirections,
               'roomSelectionText':roomSelectionText,
               'roomBookingInstructions':roomBookingInstructions,
               'secondStepDirections':secondStepDirections}

    return render(request, 'mainapp/book_a_room.html', context)