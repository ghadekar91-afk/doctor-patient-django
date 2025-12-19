from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Patient_Info


@login_required
def patient_list(request):
    patients = Patient_Info.objects.all()
    return render(request, "patient_list.html", {"patients": patients})


@login_required
def patient_detail(request, pk):
    patient = get_object_or_404(Patient_Info, pk=pk)
    return render(request, "patient_detail.html", {"patient": patient})


@login_required
def patient_create(request):
    if request.method == "POST":
        data = request.POST
        Patient_Info.objects.create(
            patient_name=data.get("patient_name"),
            age=data.get("age"),
            gender=data.get("gender"),
            address=data.get("address"),
            contact=data.get("contact"),
            disease=data.get("disease"),
            admitted_date=data.get("admitted_date"),
        )
        return redirect("patient_list")

    return render(request, "patient_form.html")


@login_required
def patient_update(request, pk):
    patient = get_object_or_404(Patient_Info, pk=pk)

    if request.method == "POST":
        data = request.POST
        patient.patient_name = data.get("patient_name")
        patient.age = data.get("age")
        patient.gender = data.get("gender")
        patient.address = data.get("address")
        patient.contact = data.get("contact")
        patient.disease = data.get("disease")
        patient.admitted_date = data.get("admitted_date")
        patient.save()

        return redirect("patient_detail", pk=pk)

    return render(request, "patient_form.html", {"patient": patient})


@login_required
def patient_delete(request, pk):
    patient = get_object_or_404(Patient_Info, pk=pk)
    patient.delete()
    return redirect("patient_list")

