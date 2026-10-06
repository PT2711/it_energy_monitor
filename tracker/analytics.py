import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64

def run_it_analytics(records):
    if not records.exists():
        return None, None, None

    # List comprehension & dictionary mapping
    data = [
        {"lab": r.lab_name, "device": r.device_type, "units": r.units_kwh}
        for r in records
    ]

    # Pandas DataFrame & Summary Statistics
    df = pd.DataFrame(data)
    summary_stats = df['units'].describe().to_dict()

    # NumPy Array processing & surge detection
    units_np = np.array(df['units'])
    mean_val = round(float(np.mean(units_np)), 2)
    max_val = round(float(np.max(units_np)), 2)
    high_surge_count = int(np.sum(units_np > 50.0))

    numpy_metrics = {
        "mean_units": mean_val,
        "peak_units": max_val,
        "surges_above_50": high_surge_count
    }

    # Matplotlib Chart
    fig, ax = plt.subplots(figsize=(6.5, 3.5))
    lab_totals = df.groupby('lab')['units'].sum()
    lab_totals.plot(kind='barh', color='#2563eb', edgecolor='black', ax=ax)
    ax.set_title("Total Energy Consumption by IT Lab (kWh)", fontsize=12, fontweight='bold')
    ax.set_xlabel("Units (kWh)")
    ax.set_ylabel("IT Department Labs")
    plt.tight_layout()

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', dpi=100)
    buffer.seek(0)
    chart_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()
    plt.close(fig)

    return summary_stats, numpy_metrics, chart_base64