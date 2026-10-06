from django.shortcuts import render, redirect
from .models import ITLabEnergy
from .analytics import run_it_analytics

def dashboard(request):
    try:
        if request.method == "POST":
            lab = request.POST.get('lab_name')
            device = request.POST.get('device_type')
            units = float(request.POST.get('units_kwh', 0.0))

            if lab and device and units > 0:
                ITLabEnergy.objects.create(
                    lab_name=lab,
                    device_type=device,
                    units_kwh=units
                )
            return redirect('dashboard')

        readings = ITLabEnergy.objects.all().order_by('-logged_at')[:20]
        stats, numpy_metrics, chart = run_it_analytics(readings)

        context = {
            'readings': readings,
            'stats': stats,
            'numpy_metrics': numpy_metrics,
            'chart': chart
        }
        return render(request, 'tracker/dashboard.html', context)

    except Exception as e:
        return render(request, 'tracker/dashboard.html', {'error': str(e)})