#!/usr/bin/env python3
"""
FMCG Manufacturing & Supply Chain Data Generator
Generates realistic CSV tables for Power BI Star Schema ingestion.
Author: Adil El Idrissi
"""

import csv
import random
from datetime import datetime, timedelta

def generate_fmcg_data():
    random.seed(42)

    # 1. Dim_Plant
    plants = [
        {"plant_id": 1, "plant_code": "PLANT-CASA-01", "plant_name": "Usine Aïn Harrouda (Huiles)", "location": "Casablanca", "capacity_liters_day": 250000},
        {"plant_id": 2, "plant_code": "PLANT-CASA-02", "plant_name": "Usine Roches Noires (Savons)", "location": "Casablanca", "capacity_liters_day": 120000},
    ]
    with open("dim_plant.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=plants[0].keys())
        writer.writeheader()
        writer.writerows(plants)

    # 2. Dim_Product_SKU
    skus = [
        {"sku_id": 101, "sku_code": "SKU-LES-5L", "product_name": "Lesieur Huile de Table 5L", "category": "Huile de table", "brand": "Lesieur", "volume_liters": 5.0, "standard_cost_mad": 62.50},
        {"sku_id": 102, "sku_code": "SKU-HUI-1L", "product_name": "Huilor Tournesol 1L", "category": "Huile de table", "brand": "Huilor", "volume_liters": 1.0, "standard_cost_mad": 14.80},
        {"sku_id": 103, "sku_code": "SKU-CRI-2L", "product_name": "Cristal Huile Végétale 2L", "category": "Huile de table", "brand": "Cristal", "volume_liters": 2.0, "standard_cost_mad": 27.00},
        {"sku_id": 104, "sku_code": "SKU-TAO-SAV", "product_name": "Taous Savon Traditionnel 250g", "category": "Savonnerie", "brand": "Taous", "volume_liters": 0.25, "standard_cost_mad": 4.50},
    ]
    with open("dim_product_sku.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=skus[0].keys())
        writer.writeheader()
        writer.writerows(skus)

    # 3. Fact_Production_Batch
    production_records = []
    base_date = datetime(2025, 1, 1)
    downtime_reasons = ["Changement de format", "Maintenance préventive", "Rupture approvisionnement emballage", "Panne ensacheuse", "Nettoyage CIP"]

    for i in range(1, 201):
        dt = base_date + timedelta(days=i % 30)
        plant = random.choice(plants)
        sku = random.choice(skus)
        planned_units = random.choice([2000, 3000, 5000, 8000])
        planned_runtime = 480.0  # 8 hours shift

        # Introduce some downtime
        has_downtime = random.random() < 0.35
        downtime = round(random.uniform(15.0, 95.0), 1) if has_downtime else 0.0
        reason = random.choice(downtime_reasons) if has_downtime else "Aucun"

        units_produced = int(planned_units * (1.0 - (downtime / planned_runtime) * 0.8) * random.uniform(0.95, 1.02))
        defective = int(units_produced * random.uniform(0.005, 0.035))

        production_records.append({
            "batch_id": 10000 + i,
            "date": dt.strftime("%Y-%m-%d"),
            "plant_id": plant["plant_id"],
            "sku_id": sku["sku_id"],
            "line_number": f"L{random.randint(1, 4)}",
            "planned_runtime_min": planned_runtime,
            "downtime_min": downtime,
            "downtime_reason": reason,
            "units_planned": planned_units,
            "units_produced": units_produced,
            "units_defective": defective,
            "energy_kwh": round(units_produced * 0.42, 2)
        })

    with open("fact_production_batch.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=production_records[0].keys())
        writer.writeheader()
        writer.writerows(production_records)

    print(f"✓ Generated FMCG datasets: dim_plant.csv, dim_product_sku.csv, and {len(production_records)} rows in fact_production_batch.csv")

if __name__ == "__main__":
    generate_fmcg_data()
