from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    # this is dynamic data! 
    context = {
        'name' : 'Makkali Gosala',
        'age' : 23,
        'nationality' : 'Magadhi'
    }
    return render(request, 'index.html', context)


# so when someone visits this url, this function will be called
# and it will return this response
def counter(request):
    # create a new variable which is equal to the text that is coming from the request
    # 'text' is the name of the variable in the form at index.html
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render (request, 'counter.html', {'amount_of_words' : amount_of_words})
