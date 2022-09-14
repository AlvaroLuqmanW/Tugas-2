from django.shortcuts import render

# TODO: Create your views here.
def katalog(request):
    return render(request, 'katalog.html')