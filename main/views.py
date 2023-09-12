from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Luhur Budi Arbilianto',
        'class': 'PBP B',
        'npm' : '2206824262'
    }

    return render(request, "main.html", context)