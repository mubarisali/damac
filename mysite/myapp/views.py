from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "main/index.html")

def island(request):
    return render(request, "main/damac_island_phase2.html")

def riverside(request):
    return render(request, "main/riverside_view.html")

def safagate(request):
    return render(request, "main/damac_safegate.html")

def district(request):
    return render(request, "main/damac_district.html")


