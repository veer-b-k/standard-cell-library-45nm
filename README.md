# Development of a Standard Cell Library Using 45 nm CMOS Technology for ASIC Design

> **Bachelor of Engineering Major Project**  
> **Department of Electronics and Communication Engineering**

---

## Overview

This repository presents the complete design and development of a **Standard Cell Library (SCL)** using **45 nm CMOS Technology** for ASIC design applications.

The project demonstrates the complete custom IC design flow, beginning with standard cell architecture and beta ratio optimization, followed by schematic design, layout development, physical verification, parasitic extraction, timing analysis, and Process-Voltage-Temperature (PVT) validation.

The standard cells were designed and verified using the **Cadence Virtuoso Design Suite** with **GPDK45 technology**, following industry-standard custom CMOS design methodologies.

---

## Project Objectives

- Design a Standard Cell Library using 45 nm CMOS technology.
- Optimize transistor sizing using Beta Ratio Optimization.
- Develop schematic and layout views for standard cells.
- Perform Design Rule Check (DRC) verification.
- Perform Layout Versus Schematic (LVS) verification.
- Generate extracted views through parasitic extraction.
- Analyze propagation delay characteristics.
- Perform Process, Voltage and Temperature (PVT) validation.
- Evaluate Setup Time and Hold Time for sequential cells.
- Document the complete ASIC standard cell design methodology.

---

## Standard Cells Developed

The developed library includes representative combinational and sequential standard cells designed using CMOS logic.

### Combinational Cells

- Inverter (INV)
- Buffer (BUF)
- NAND Gate
- NOR Gate
- XOR Gate
- XNOR Gate

### Sequential Cells

- D Flip-Flop

> **Note:** The exact set of cells depends on the scope of the implemented library for this academic project.

---

## Design Flow

The project follows the complete custom ASIC standard cell development flow.

```
Beta Ratio Optimization
          │
          ▼
Schematic Design
          │
          ▼
Layout Development
          │
          ▼
Design Rule Check (DRC)
          │
          ▼
Layout Versus Schematic (LVS)
          │
          ▼
Parasitic Extraction
          │
          ▼
Timing Analysis
          │
          ▼
PVT Validation
          │
          ▼
Performance Evaluation
```

---

## Repository Structure

```
standard-cell-library-45nm
│
├── README.md
│
├── docs/
│   ├── 01_Project_Overview.md
│   ├── 02_Standard_Cell_Architecture.md
│   ├── 03_Beta_Ratio_Optimization.md
│   ├── 04_Layout_Development.md
│   ├── 05_Timing_Analysis_and_PVT_Validation.md
│   ├── 06_Results.md
│   └── 07_References.md
│
├── images/
│
├── layouts/
│
├── schematics/
│
├── spice/
│
├── scripts/
│
└── results/
```

---

## Documentation

Detailed project documentation is available in the **docs** directory.

- 📘 Project Overview
- 📗 Standard Cell Architecture
- 📙 Beta Ratio Optimization
- 📕 Layout Development
- 📒 Timing Analysis and PVT Validation
- 📓 Results
- 📚 References

---

## Technology

| Item | Description |
|------|-------------|
| Technology Node | 45 nm CMOS |
| Design Methodology | Standard Cell Based ASIC Design |
| CAD Tool | Cadence Virtuoso |
| Process Design Kit | GPDK45 |
| Verification | DRC, LVS |
| Extraction | Parasitic Extraction |
| Simulation | Spectre |
| Programming | Python |
| Platform | Linux |

---

## Tools Used

- Cadence Virtuoso
- Cadence Layout Suite
- Cadence Spectre Simulator
- GPDK45 Technology
- Python

---

## Project Highlights

- Complete custom CMOS standard cell development flow.
- Beta ratio optimization for improved switching performance.
- Schematic and layout implementation of representative standard cells.
- DRC and LVS verified layouts.
- Parasitic extraction using extracted views.
- Timing characterization of standard cells.
- PVT validation across multiple operating conditions.
- Setup Time and Hold Time analysis for sequential circuits.
- Well-structured technical documentation with design methodology and results.

---

## Project Status

- ✅ Standard Cell Architecture
- ✅ Beta Ratio Optimization
- ✅ Schematic Design
- ✅ Layout Development
- ✅ DRC Verification
- ✅ LVS Verification
- ✅ Parasitic Extraction
- ✅ Timing Characterization
- ✅ PVT Validation
- ✅ Setup and Hold Time Analysis
- ✅ Project Documentation Completed

---

## Applications

The developed Standard Cell Library can serve as a reference for:

- ASIC Design
- Digital CMOS VLSI Design
- Physical Design Flow
- Standard Cell Characterization
- VLSI Laboratory Courses
- Academic Research and Education

---

## Acknowledgement

This repository was developed as part of the **Bachelor of Engineering Major Project** in **Electronics and Communication Engineering**.

The project demonstrates the practical implementation of custom CMOS standard cell design using industry-standard EDA tools and established VLSI design methodologies.

---

