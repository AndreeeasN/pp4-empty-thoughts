from django.shortcuts import render

# Create your views here.
def get_thoughts(request):
    return render(request, 'thoughts/thoughts.html')