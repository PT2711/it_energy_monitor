import sys
import os
import django

# Setup standalone Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "energy_core.settings")
django.setup()

from tracker.models import ITLabEnergy

print("Received arguments:", sys.argv)

if len(sys.argv) < 4:
    print("Error: Missing arguments!")
    print("Usage: python3 seed_cli.py \"<Lab Name>\" \"<Device>\" <Units_kWh>")
    sys.exit(1)

lab_name = sys.argv[1]
device = sys.argv[2]

try:
    units = float(sys.argv[3])
except ValueError:
    print("Error: Units must be a number.")
    sys.exit(1)

entry = ITLabEnergy.objects.create(
    lab_name=lab_name,
    device_type=device,
    units_kwh=units
)

print(f"[SUCCESS] CLI Entry Created: {entry}")