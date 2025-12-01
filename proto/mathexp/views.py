

from django.shortcuts import render

def home(request):
    power = None

    if request.method == "POST":
        I = float(request.POST.get("intensity"))
        R = float(request.POST.get("resistance"))
        power = I * I * R  # Formula P = I²R

    return render(request, "mathexp/formula.html", {"power": power})
