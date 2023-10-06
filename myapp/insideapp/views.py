from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Price Graph'
    
    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'Indicator 1'
    
    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'Indicator 2'
    
    feature4 = Feature()
    feature4.id = 3
    feature4.name = 'Indicator 3'

    return render(request, 'index.html', {'Feature' : feature1,  })


# so when someone visits this url, this function will be called
# and it will return this response
def counter(request):
    # create a new variable which is equal to the text that is coming from the request
    # 'text' is the name of the variable in the form at index.html
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render (request, 'counter.html', {'amount_of_words' : amount_of_words})


