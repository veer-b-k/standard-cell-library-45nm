# Results

## Introduction

This chapter presents the overall results obtained during the development of the **45 nm CMOS Standard Cell Library** for ASIC design. The outcomes summarize the transistor sizing optimization, physical layout implementation, design rule verification, timing analysis, and Process-Voltage-Temperature (PVT) validation performed throughout the project.

The developed standard cell library consists of combinational and sequential logic cells designed using a common architecture and layout methodology. Representative cells were analyzed to evaluate timing performance and verify reliable operation under different operating conditions.

The results presented in this chapter demonstrate that the proposed design methodology successfully achieves balanced performance, layout regularity, and robustness, making the developed library suitable for digital ASIC design applications.

---
# Beta Ratio Optimization Results

Beta ratio optimization was performed to determine the optimum PMOS-to-NMOS width ratio that provides balanced rising and falling propagation delays for representative combinational cells.

Propagation delay simulations were carried out using Spectre on schematic-level designs while keeping the NMOS transistor width fixed at **120 nm**. The PMOS width was varied over a range of beta ratios, and the corresponding delays were measured.

The optimized beta ratios obtained for the representative cells are summarized in Table 6.1.

### Table 6.1 Optimized Beta Ratios

| Standard Cell | Optimum Beta Ratio |
|--------------|-------------------:|
| Inverter | 1.55 |
| NAND Gate | 1.2875 |
| NOR Gate | 1.90 |

Based on the optimization results, a common beta ratio of **1.5** was selected for the implementation of the standard cell library. This value provides a practical compromise between performance, layout uniformity, and ease of library development while maintaining balanced switching characteristics across multiple logic gates.
# Layout Development Results

The physical implementation of the standard cell library was carried out using the Cadence Virtuoso Layout Editor following standard ASIC layout design practices. Each cell was designed with a uniform height to facilitate row-based placement and improve compatibility with automated digital design flows.

A common standard cell height of **1.76 µm** was adopted throughout the library, while the cell widths were determined based on the complexity and transistor count of each logic function. The layouts were optimized to minimize area while maintaining proper routing and transistor placement.

During layout development, careful attention was given to transistor folding, diffusion sharing, metal routing, and power rail alignment. These techniques contributed to efficient utilization of silicon area and improved layout regularity.

The developed layouts include combinational logic cells such as inverters, NAND gates, NOR gates, XOR gates, multiplexers, and arithmetic cells, along with representative sequential elements. All layouts follow a consistent design methodology suitable for standard cell library development.

> **Figure 6.1:** Representative Standard Cell Layouts

---

# DRC and LVS Verification Results

After layout implementation, each representative standard cell was verified using **Design Rule Check (DRC)** and **Layout Versus Schematic (LVS)** verification.

The DRC process ensured that all layouts satisfied the fabrication constraints specified by the 45 nm CMOS technology, including minimum spacing, enclosure, width, and overlap requirements. Successful completion of DRC confirms that the layouts comply with the technology design rules and are suitable for fabrication.

LVS verification was then performed to compare the extracted layout netlist with the original schematic. The LVS results confirmed that the electrical connectivity of the layouts matched their corresponding schematics, ensuring functional correctness.

The successful completion of both DRC and LVS verification demonstrates the correctness and manufacturability of the developed standard cells.

> **Figure 6.2:** DRC Verification Results

> **Figure 6.3:** LVS Verification Results

---
