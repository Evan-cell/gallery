from django.shortcuts import render
from django.http  import HttpResponse, Http404
import datetime as dt


# Create your views here.
def welcome(request):
    return render(request, 'index.html')
def news_of_day(request):
    date = dt.date.today()

    # FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY
   
    html = f'''
        <html>
            <body>
                <h1>News for  {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)

def past_days_news(request,past_date):
    
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()

  
    html = f'''
        <html>
            <body>
                <h1>News for {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)