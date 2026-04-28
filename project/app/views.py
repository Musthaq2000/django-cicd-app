from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Insurance

def index(request):
    if request.method == "POST":
        age = request.POST.get('age')

        if not age:
            messages.error(request, "Age is required")
            return redirect('/')

        Insurance.objects.create(
            name=request.POST.get('name'),
            age=int(age),
            gender=request.POST.get('gender'),
            policy_type=request.POST.get('policy_type'),
            nominee=request.POST.get('nominee'),
            coverage_amount=request.POST.get('coverage_amount')
        )

        messages.success(request, "Your insurance application submitted successfully!")
        return redirect('/')   # 🔥 no query params now

    return render(request, "index.html")
