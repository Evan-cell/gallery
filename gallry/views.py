from django.shortcuts import render,redirect
from django.http  import HttpResponse, Http404
import datetime as dt
from .models import photos #import photos model

def index(request):
    # imports photos and save it in database
    photo = photos.objects.all()
    # adding context 
    ctx = {'photo':photo}
    return render(request, 'index.html', ctx)


# Create your views here.
def welcome(request):
    return render(request, 'index.html')
def news_of_day(request):
    date = dt.date.today()
    return render(request, 'index.html', {"date": date,})

def past_days_news(request, past_date):
    
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(news_of_day)

    return render(request, 'index.html', {"date": date})