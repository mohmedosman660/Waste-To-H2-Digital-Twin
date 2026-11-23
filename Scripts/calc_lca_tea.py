import csv
import os

# Locate inputs_baseline.csv relative to this script inside COP31_Waste_to_H2_Project
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_path = os.path.join(base_dir, "data", "inputs_baseline.csv")

data = {}
with open(csv_path, mode="r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for row in reader:
        data[row["parameter"].strip()] = float(row["value"])

h2_kg_h = data["h2_output_kg_h"]
grid_kwh_h = data["grid_elec_kwh_h"]
ren_share = data["renewable_elec_share"]
grid_ef = data["grid_ef_kg_co2_per_kwh"]
ren_ef = data["ren_ef_kg_co2_per_kwh"]
heat_mj_h = data["heat_duty_mj_h"]
heat_ef = data["heat_ef_kg_co2_per_mj"]
elec_price = data["elec_price_usd_per_kwh"]

# Effective electricity emission factor based on renewable share (Grid Dependency Paradox check)
eff_elec_ef = (1.0 - ren_share) * grid_ef + ren_share * ren_ef

# Hourly emissions (kg CO2e/h)
elec_ghg_h = grid_kwh_h * eff_elec_ef
heat_ghg_h = heat_mj_h * heat_ef
total_ghg_h = elec_ghg_h + heat_ghg_h

# LCA metric: kg CO2e per kg H2
ghg_per_kg_h2 = total_ghg_h / h2_kg_h

# Simple TEA utility cost metric: USD per kg H2 (electricity cost basis)
elec_cost_per_kg_h2 = (grid_kwh_h * elec_price) / h2_kg_h

print(f"H2 production: {h2_kg_h:.2f} kg/h")
print(f"Effective electricity EF: {eff_elec_ef:.4f} kg CO2e/kWh")
print(f"Total utility GHG: {total_ghg_h:.2f} kg CO2e/h")
print(f"LCA (Utility Carbon Footprint): {ghg_per_kg_h2:.2f} kg CO2e / kg H2")
print(f"TEA (Electricity Utility Cost): ${elec_cost_per_kg_h2:.2f} / kg H2")