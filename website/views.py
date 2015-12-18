from django.shortcuts import render

# Create your views here.
def homeenglish(request):
    return render(request, 'website/homeenglish.html', {})