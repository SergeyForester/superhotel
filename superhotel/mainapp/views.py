from django.shortcuts import render
from timetable.models import Room
from timetable.models import DataImages
from timetable.models import Data
import datetime
from django.utils import timezone
from django.shortcuts import get_object_or_404, HttpResponseRedirect
from mainapp.forms import HeaderPhotoForm, NameOfHotelForm, StarsForm, NameOfHotelInfoForm
from mainapp.forms import TelephoneNumberForm, AddressForm, LocalityForm, RegionForm, PostalCodeForm
from mainapp.forms import MapLinkForm, UploadPhotoInfoForm, LongDescriptionOfHotel, FeatureForm, TermsAndConditionsForm
from mainapp.forms import FirstStepDirections, HeaderDescription, RoomSelectionText, AdvantagesForm, \
    RoomBookingInstructions, \
    SecondStepDirections, BookAHotelRoom, JoinUsForm, ThreeWordsForm, TextAfterThreeWords, PhotoDescriptions
# Create your views here.
from django.urls import reverse
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

    if request.method == 'POST':
        headerPhoto = HeaderPhotoForm(request.POST, request.FILES)
        nameOfHotel_form = NameOfHotelForm(request.POST)
        starsForm = StarsForm(request.POST)
        nameOfHotelInfo = NameOfHotelInfoForm(request.POST)
        telephoneNumberForm = TelephoneNumberForm(request.POST)
        addressForm = AddressForm(request.POST)
        localityForm = LocalityForm(request.POST)
        regionForm = RegionForm(request.POST)
        postal_codeForm = PostalCodeForm(request.POST)
        mapLinkForm = MapLinkForm(request.POST)
        uploadPhotoInfoForm = UploadPhotoInfoForm(request.POST, request.FILES)
        longDescriptionOfHotel = LongDescriptionOfHotel(request.POST)
        featureForm = FeatureForm(request.POST)
        termsAndConditions = TermsAndConditionsForm(request.POST)
        joinUsForm = JoinUsForm(request.POST)
        advantagesForm = AdvantagesForm(request.POST)
        headerDescription = HeaderDescription(request.POST)
        threeWordsForm = ThreeWordsForm(request.POST, request.FILES)
        textAfterThreeWords = TextAfterThreeWords(request.POST)
        photoDescriptions = PhotoDescriptions(request.POST, request.FILES)
        bookAHotelRoom = BookAHotelRoom(request.POST)

        if headerPhoto.is_valid():
            DataImages.objects.create(nameOfImage = 'headerPhoto',image = headerPhoto.cleaned_data['photos'])

        if nameOfHotel_form.is_valid():
            Data.objects.create(nameOfText = 'nameOfHotel',valueOfText = nameOfHotel_form.cleaned_data['name_of_hotel'])

        if starsForm.is_valid():
            Data.objects.create(nameOfText = 'stars',valueOfText = starsForm.cleaned_data['stars'])

        if nameOfHotelInfo.is_valid():
            Data.objects.create(nameOfText = 'nameOfHotelInfo',valueOfText = nameOfHotelInfo.cleaned_data['info'])

        if telephoneNumberForm.is_valid():
            Data.objects.create(nameOfText = 'telephoneNumber',valueOfText = telephoneNumberForm.cleaned_data['number'])

        if addressForm.is_valid():
            Data.objects.create(nameOfText = 'address',valueOfText = addressForm.cleaned_data['address'])

        if localityForm.is_valid():
            Data.objects.create(nameOfText = 'locality',valueOfText=localityForm.cleaned_data['locality'])

        if regionForm.is_valid():
            Data.objects.create(nameOfText = 'region',valueOfText=regionForm.cleaned_data['region'])

        if postal_codeForm.is_valid():
            Data.objects.create(nameOfText = 'postalCode',valueOfText=postal_codeForm.cleaned_data['postalCode'])

        if mapLinkForm.is_valid():
            Data.objects.create(nameOfText = 'mapCode',valueOfText=mapLinkForm.cleaned_data['mapCode'])

        if uploadPhotoInfoForm.is_valid():
            DataImages.objects.create(nameOfImage = 'infoPhoto1',image=uploadPhotoInfoForm.cleaned_data['photo1'])
            DataImages.objects.create(nameOfImage = 'infoPhoto2',image=uploadPhotoInfoForm.cleaned_data['photo2'])
            DataImages.objects.create(nameOfImage = 'infoPhoto3',image=uploadPhotoInfoForm.cleaned_data['photo3'])

        if longDescriptionOfHotel.is_valid():
            Data.objects.create(nameOfText = 'longDescription',valueOfText=longDescriptionOfHotel.cleaned_data['longdescr'])

        if featureForm.is_valid():
            Data.objects.create(nameOfText = 'feature1',valueOfText=featureForm.cleaned_data['feature1'])
            Data.objects.create(nameOfText = 'feature2',valueOfText=featureForm.cleaned_data['feature2'])
            Data.objects.create(nameOfText = 'feature3',valueOfText=featureForm.cleaned_data['feature3'])
            Data.objects.create(nameOfText = 'feature4',valueOfText=featureForm.cleaned_data['feature4'])
            Data.objects.create(nameOfText = 'feature5',valueOfText=featureForm.cleaned_data['feature5'])
            Data.objects.create(nameOfText = 'feature6',valueOfText=featureForm.cleaned_data['feature6'])
            Data.objects.create(nameOfText = 'feature7',valueOfText=featureForm.cleaned_data['feature7'])
            Data.objects.create(nameOfText = 'feature8',valueOfText=featureForm.cleaned_data['feature8'])

        if termsAndConditions.is_valid():
            Data.objects.create(nameOfText='termsAndConditions',
                                valueOfText=termsAndConditions.cleaned_data['terms'])

        if joinUsForm.is_valid():
            Data.objects.create(nameOfText='joinUs',
                                valueOfText=joinUsForm.cleaned_data['text'])

        if advantagesForm.is_valid():
            Data.objects.create(nameOfText='advantages',
                                valueOfText=advantagesForm.cleaned_data['text'])

        if headerDescription.is_valid():
            Data.objects.create(nameOfText='headerDescription',
                                valueOfText=headerDescription.cleaned_data['text'])

        if threeWordsForm.is_valid():
            Data.objects.create(nameOfText='threeWords',
                                valueOfText=threeWordsForm.cleaned_data['text'])

        if textAfterThreeWords.is_valid():
            Data.objects.create(nameOfText='textAfterThreeWords',
                                valueOfText=textAfterThreeWords.cleaned_data['text'])

        if photoDescriptions.is_valid():
            DataImages.objects.create(nameOfImage='photoDescription1',image=photoDescriptions.cleaned_data['photo1'])
            DataImages.objects.create(nameOfImage='photoDescription2',image=photoDescriptions.cleaned_data['photo2'])
            DataImages.objects.create(nameOfImage='photoDescription3',image=photoDescriptions.cleaned_data['photo3'])
            DataImages.objects.create(nameOfImage='photoDescription4',image=photoDescriptions.cleaned_data['photo4'])

        if bookAHotelRoom.is_valid():
            Data.objects.create(nameOfText='threeWords',
                                valueOfText=bookAHotelRoom.cleaned_data['text'])

        return HttpResponseRedirect(reverse('main:dataFromInputBookARoom'))

    else:
        headerPhoto = HeaderPhotoForm()
        nameOfHotel_form = NameOfHotelForm()
        starsForm = StarsForm()
        nameOfHotelInfo = NameOfHotelInfoForm()
        telephoneNumberForm = TelephoneNumberForm()
        addressForm = AddressForm()
        localityForm = LocalityForm()
        regionForm = RegionForm()
        postal_codeForm = PostalCodeForm()
        mapLinkForm = MapLinkForm()
        uploadPhotoInfoForm = UploadPhotoInfoForm()
        longDescriptionOfHotel = LongDescriptionOfHotel()
        featureForm = FeatureForm()
        termsAndConditions = TermsAndConditionsForm()
        joinUsForm = JoinUsForm()
        advantagesForm = AdvantagesForm()
        headerDescription = HeaderDescription()
        threeWordsForm = ThreeWordsForm()
        textAfterThreeWords = TextAfterThreeWords()
        photoDescriptions = PhotoDescriptions()
        bookAHotelRoom = BookAHotelRoom()

    context = {'headerPhoto': headerPhoto, 'nameOfHotel_form': nameOfHotel_form,
               'starsForm': starsForm, 'nameOfHotelInfo': nameOfHotelInfo,
               'telephoneNumberForm': telephoneNumberForm, 'addressForm': addressForm,
               'localityForm': localityForm, 'regionForm': regionForm,
               'postal_codeForm': postal_codeForm, 'mapLinkForm': mapLinkForm,
               'uploadPhotoInfoForm': uploadPhotoInfoForm, 'longDescriptionOfHotel': longDescriptionOfHotel,
               'featureForm': featureForm, 'termsAndConditions': termsAndConditions, 'roomTable': roomTable,
               'days': days, 'JoinUsForm': joinUsForm, 'AdvantagesForm': advantagesForm,
               'headerDescription': headerDescription, 'threeWordsForm': ThreeWordsForm,
               'textAfterThreeWords': textAfterThreeWords, 'photoDescriptions':photoDescriptions,
               'bookAHotelRoom':bookAHotelRoom}

    return render(request, 'mainapp/booking.html', context)


# из cleaned_data достаем данные и помещаем в файлы

def dataFromInputBookARoom(request):
    firstStepDirections = FirstStepDirections(request.POST)
    roomSelectionText = RoomSelectionText(request.POST)
    roomBookingInstructions = RoomBookingInstructions(request.POST)
    secondStepDirections = SecondStepDirections(request.POST)

    context = {'firstStepDirections': firstStepDirections,
               'roomSelectionText': roomSelectionText,
               'roomBookingInstructions': roomBookingInstructions,
               'secondStepDirections': secondStepDirections}

    return render(request, 'mainapp/book_a_room.html', context)
