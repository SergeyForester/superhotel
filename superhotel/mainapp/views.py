from django.shortcuts import render
from timetable.models import Room
import datetime
from django.utils import timezone
from django.shortcuts import get_object_or_404, HttpResponseRedirect
from mainapp.forms import HeaderPhotoForm, NameOfHotelForm, StarsForm, NameOfHotelInfoForm
from mainapp.forms import TelephoneNumberForm, AddressForm, LocalityForm, RegionForm, PostalCodeForm
from mainapp.forms import MapLinkForm, UploadPhotoInfoForm, LongDescriptionOfHotel, FeatureForm, TermsAndConditionsForm
from mainapp.forms import FirstStepDirections, RoomSelectionText, RoomBookingInstructions, SecondStepDirections
# Create your views here.

from django.shortcuts import render, HttpResponse
from mainapp.models import constructNameHotel
from django.http import JsonResponse

def mainPage(request):
    return render(request, 'mainapp/index.html')


def saveColumns(request):
    if request.is_ajax():

        tempSave = request.GET
        id = tempSave['id']
        content = tempSave['content']
        newConstruct = constructNameHotel(tag_name=id, tag_text=content)
        if constructNameHotel.objects.filter(tag_name=id).first().tag_name == id:
            newConstruct = constructNameHotel.objects.get(tag_name=id)
            newConstruct.tag_text = content
            newConstruct.save()
        else:
            newConstruct.save()
        abc = request.is_ajax()
        return JsonResponse({'result': content})


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

    roomTable = Room.objects.all()
    print(roomTable)

    # now = datetime.datetime.now()
    # datetime.today()
    # datetime.date.today() + datetime.timedelta(days=1)
    days = []
    for dayR in range(7):
        day = datetime.date.today() + datetime.timedelta(days=dayR)
        print(day)
        days.append(day)

    print(days[-1].strftime("%A"))
    print(days)

    context = {'headerPhoto':headerPhoto, 'nameOfHotel_form':nameOfHotel_form,
               'starsForm':starsForm, 'nameOfHotelInfo':nameOfHotelInfo,
               'telephoneNumberForm':telephoneNumberForm, 'addressForm':addressForm,
               'localityForm':localityForm, 'regionForm':regionForm,
               'postal_codeForm':postal_codeForm, 'mapLinkForm':mapLinkForm,
               'uploadPhotoInfoForm':uploadPhotoInfoForm, 'longDescriptionOfHotel':longDescriptionOfHotel,
               'featureForm':featureForm, 'termsAndConditions':termsAndConditions, 'roomTable':roomTable, 'days':days}

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