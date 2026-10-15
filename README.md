# FMCG Supply Chain & Production Performance BI Platform (Power BI + SQL + DAX)

An end-to-end operational Business Intelligence architecture modeled for high-volume agro-industrial manufacturing (e.g. Lesieur Cristal). Tracks production line efficiency (OEE), distribution logistics (OTIF), inventory holding costs, and automated stockout risk alerts across regional distribution centers.

---

## 🎯 Business Context & Alignment
In large manufacturing corporations like Lesieur Cristal (vegetable oils, soaps, consumer goods), production plants in Casablanca and regional hubs throughout Morocco generate thousands of daily records across production lines, packaging, warehouse inventory, and carrier dispatches.

Operations directors often struggle with:
1. Fragmented Excel sheets causing reporting delays (reports ready days after production issues occurred).
2. Lack of visibility into **OEE (Overall Equipment Effectiveness)**: Availability, Performance, and Quality.
3. Inability to track **OTIF (On-Time In-Full)** delivery rates across regional hubs (Fez, Marrakech, Tangier, Agadir).

This BI project provides a complete star-schema data warehouse model, automated mock data generator, and high-performance DAX measure library.

---

## 🏗️ Star-Schema Architecture

```text
       [Dim_Date]                  [Dim_Plant]
            │                           │
            └───────────┬───────────────┘
                        ▼
             [Fact_Production_Batches] ◄─── [Dim_Product_SKU]
                        ▲                           │
            ┌───────────┴───────────────┐           │
            ▼                           ▼           ▼
   [Fact_Inventory_Levels]   [Fact_Shipments_Deliveries]
            ▲                           ▲
            │                           │
     [Dim_Warehouse]             [Dim_Customer_Hub]
```

---

## 📊 Core KPI Formulations in DAX (Power BI)

- **OEE (%)**: `Availability * Performance * Quality`
  - *Availability*: `(Planned Production Time - Unplanned Downtime) / Planned Production Time`
  - *Performance*: `(Total Units Produced) / (Ideal Run Rate * Operating Time)`
  - *Quality*: `(Good Units Produced) / (Total Units Produced)`
- **OTIF (%)**: `% of order lines delivered on or before promised date with 100% quantity fulfilled`
- **Scrap Rate (%)**: `Total Scrap Weight / Total Input Material Weight`
- **Stockout Alert (Flag)**: `IF(Days of Inventory on Hand < Safety Stock Days, 1, 0)`

---

## 🚀 Quickstart

1. Generate realistic FMCG production and shipment data:
```bash
python3 generate_mock_data.py
```

2. Review the star-schema database architecture in `star_schema.sql`.
3. Import the generated CSV tables into Power BI Desktop and paste the DAX measures from `dax_measures.dax`.
