-- Star Schema DDL for Agro-Industrial Manufacturing & Supply Chain
-- Author: Adil El Idrissi

-- ==========================================
-- DIMENSION TABLES
-- ==========================================

CREATE TABLE Dim_Plant (
    plant_id INT PRIMARY KEY,
    plant_code VARCHAR(20) NOT NULL,
    plant_name VARCHAR(100) NOT NULL,
    location VARCHAR(50) NOT NULL,
    capacity_liters_day DECIMAL(12, 2)
);

CREATE TABLE Dim_Product_SKU (
    sku_id INT PRIMARY KEY,
    sku_code VARCHAR(30) UNIQUE NOT NULL,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL, -- e.g. Huile de table, Savon, Margarine
    brand VARCHAR(50) NOT NULL,    -- e.g. Lesieur, Huilor, Cristal, Taous
    volume_liters DECIMAL(6, 2),
    standard_cost_mad DECIMAL(10, 2)
);

CREATE TABLE Dim_Warehouse (
    warehouse_id INT PRIMARY KEY,
    warehouse_name VARCHAR(100) NOT NULL,
    region VARCHAR(50) NOT NULL,  -- e.g. Casablanca, Fès, Tanger, Marrakech
    max_capacity_pallets INT
);

-- ==========================================
-- FACT TABLES
-- ==========================================

CREATE TABLE Fact_Production_Batch (
    batch_id BIGINT PRIMARY KEY,
    date_key INT NOT NULL,
    plant_id INT NOT NULL REFERENCES Dim_Plant(plant_id),
    sku_id INT NOT NULL REFERENCES Dim_Product_SKU(sku_id),
    line_number VARCHAR(10) NOT NULL,
    planned_runtime_min DECIMAL(8, 2) NOT NULL,
    downtime_min DECIMAL(8, 2) DEFAULT 0.0,
    downtime_reason VARCHAR(100),
    units_planned INT NOT NULL,
    units_produced INT NOT NULL,
    units_defective INT DEFAULT 0,
    energy_kwh DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Fact_Shipment_Delivery (
    shipment_id BIGINT PRIMARY KEY,
    order_id VARCHAR(50) NOT NULL,
    date_key INT NOT NULL,
    warehouse_id INT NOT NULL REFERENCES Dim_Warehouse(warehouse_id),
    sku_id INT NOT NULL REFERENCES Dim_Product_SKU(sku_id),
    quantity_ordered INT NOT NULL,
    quantity_delivered INT NOT NULL,
    promised_delivery_date DATE NOT NULL,
    actual_delivery_date DATE NOT NULL,
    delivery_status VARCHAR(20) NOT NULL -- On-Time, Delayed, Cancelled
);
