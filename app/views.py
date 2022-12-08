from django.shortcuts import render

# Create your views here.
def generic_url(request):
    return render(request,'generic_url.html')

def generic_url2(request):
    return render(request,'generic_url2.html')