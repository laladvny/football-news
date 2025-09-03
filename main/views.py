from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406410121',
        'name': 'Adzradevany Aqiila',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)