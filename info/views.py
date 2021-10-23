from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from info.models import User, Review
from django.db import IntegrityError

def index(request):
    reviews = Review.objects.all()
    context = {'reviews': reviews}
    return render(request, 'info/index.html', context)

def survey(request):
    return render(request, 'info/survey.html')

def submit(request):    
    form_data = dict(request.POST)
    print(form_data)
    try:
        user = User(first_name = form_data['fname'][0], last_name = form_data['lname'][0], 
            organization = form_data['org'][0], profession = form_data['profession'][0], 
            email = form_data['email'][0], phone_number = form_data['phoneNumber'][0])
        user.save()
    except IntegrityError:
        return render(request, 'info/survey.html', {'error_message': "Phone number already exists. Please try again."})
    except Exception as e:
        print(e)
        return render(request, 'info/survey.html', {'error_message': "There was an error. Please try again."})
    else:
        if 'service' in form_data.keys():
            # If the user opted for service(s)
            for service in form_data['service']:
                user.service_set.create(service=service)
        
        if form_data['findUs'][0]:
            user.find_set.create(find_us=form_data['findUs'][0])
        
        if form_data['review'][0]:
            user.review_set.create(review=form_data['review'][0])

        return HttpResponseRedirect(reverse('info:index'))

def reviews(request):
    reviews = Review.objects.all()
    context = {'reviews': reviews}
    return render(request, 'info/reviews.html', context)