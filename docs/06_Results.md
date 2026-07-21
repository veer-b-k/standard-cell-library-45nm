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
