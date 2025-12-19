from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Doctor_Info


@login_required
def doctor_list(request):
    doctors = Doctor_Info.objects.all()
    return render(request, "doctor_list.html", {"doctors": doctors})


@login_required
def doctor_detail(request, pk):
    doctor = get_object_or_404(Doctor_Info, pk=pk)
    return render(request, "doctor_detail.html", {"doctor": doctor})


@login_required
def doctor_create(request):
    if request.method == "POST":
        data = request.POST
        Doctor_Info.objects.create(
            Registration_number=data.get("Registration_number"),
            name=data.get("name"),
            age=data.get("age"),
            Qulification=data.get("Qulification"),
            specialization=data.get("specialization"),
            Experiance=data.get("Experiance"),
            timing=data.get("timing"),
            contact_number=data.get("contact_number"),
            email=data.get("email"),
            gender=data.get("gender"),
            Hospital_address=data.get("Hospital_address"),
        )
        return redirect("doctor_list")

    return render(request, "doctor_form.html")


@login_required
def doctor_update(request, pk):
    doctor = get_object_or_404(Doctor_Info, pk=pk)

    if request.method == "POST":
        data = request.POST
        doctor.Registration_number = data.get("Registration_number")
        doctor.name = data.get("name")
        doctor.age = data.get("age")
        doctor.Qulification = data.get("Qulification")
        doctor.specialization = data.get("specialization")
        doctor.Experiance = data.get("Experiance")
        doctor.timing = data.get("timing")
        doctor.contact_number = data.get("contact_number")
        doctor.email = data.get("email")
        doctor.gender = data.get("gender")
        doctor.Hospital_address = data.get("Hospital_address")
        doctor.save()
        return redirect("doctor_detail", pk=pk)

    return render(request, "doctor_form.html", {"doctor": doctor})


@login_required
def doctor_delete(request, pk):
    doctor = get_object_or_404(Doctor_Info, pk=pk)
    doctor.delete()
    return redirect("doctor_list")

