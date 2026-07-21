import subprocess
import re

# Define the range and step for 'w' values
start_w = 120      # Starting width in nanometers
stop_w = 300       # Stopping width in nanometers
step_size = 20     # Step size in nanometers

# Generate the list of w values
w_values = list(range(start_w, stop_w + 1, step_size))

# Template for the contents of the .scs file
scs_template = """// Generated for: spectre
// Generated on: Nov 13 14:54:07 2024
// Design library name: bhuscell
// Design cell name: invpy
// Design view name: schematic

simulator lang=spectre
global 0

include "/home/install/FOUNDRY/analog/180nm/models/spectre/gpdk.scs" section=stat
include "/home/install/FOUNDRY/analog/45nm/gpdk045/../models/spectre/gpdk045.scs" section=mc

// Library name: bhuscell
// Cell name: invpy
// View name: schematic

PM0 (y a vdd vdd) g45p1svt w=({}n) l=45n nf=1 as=16.8f ad=16.8f ps=520n \
        pd=520n nrd=1.16667 nrs=1.16667 sa=140n sb=140n sd=160n \
        sca=226.00151 scb=0.11734 scc=0.02767 m=(1)

NM0 (y a gnd gnd) g45n1svt w=(120n) l=45n nf=1 as=16.8f ad=16.8f ps=520n \
        pd=520n nrd=1.16667 nrs=1.16667 sa=140n sb=140n sd=160n \
        sca=226.00151 scb=0.11734 scc=0.02767 m=(1)

_va (a 0) vsource data="010101" rptstart=1 rpttimes=0 val1=1.8 val0=0 delay=0 rise=1n fall=1n period=20n type=bit
_vgnd (gnd 0) vsource dc=0 type=dc
_vvdd (vdd 0) vsource dc=1.8 type=dc

simulatorOptions options psfversion="1.4.0" reltol=1e-3 vabstol=1e-6 \
    iabstol=1e-12 temp=27 tnom=27 scalem=1.0 scale=1.0 gmin=1e-12 rforce=1 \
    maxnotes=5 maxwarns=5 digits=5 cols=80 pivrel=1e-3 \
    sensfile="../psf/sens.output" checklimitdest=psf

tran tran stop=100n errpreset=moderate write="spectre.ic" \
    writefinal="spectre.fc" annotate=status maxiters=5

simulator lang=spice
.meas tran fd trig V(y) val='0.9' fall=1 targ V(a) val='0.9' rise=1
.meas tran rd trig V(a) val='0.9' fall=1 targ V(y) val='0.9' rise=1

simulator lang=spectre

finalTimeOP info what=oppoint where=rawfile
modelParameter info what=models where=rawfile
element info what=inst where=rawfile
outputParameter info what=output where=rawfile
designParamVals info what=parameters where=rawfile
primitives info what=primitives where=rawfile
subckts info what=subckts where=rawfile
saveOptions options save=allpub
"""

# Open the result file
with open("simulation_results.txt", "w") as result_file:

    result_file.write("w (nm)\tfd (s)\trd (s)\n")
    result_file.write("-" * 40 + "\n")

    # Generate .scs files and run simulations
    for w in w_values:

        # Create SCS content
        scs_content = scs_template.format(w)

        scs_file_name = f"{w}.scs"
        measure_file_name = f"{w}.measure"

        # Write SCS file
        with open(scs_file_name, "w") as file:
            file.write(scs_content)

        print(f"Generated file: {scs_file_name}")

        try:
            # Run Spectre
            print(f"Running simulation for {scs_file_name}...")
            subprocess.run(["spectre", scs_file_name], check=True)

            print(f"Simulation for {scs_file_name} completed successfully.")

            # Read .measure file
            with open(measure_file_name, "r") as measure_file:
                measure_content = measure_file.read()

            # Extract fd and rd
            fd_match = re.search(r'fd\s*=\s*([\d.eE+-]+)', measure_content)
            rd_match = re.search(r'rd\s*=\s*([\d.eE+-]+)', measure_content)

            fd_value = fd_match.group(1) if fd_match else "N/A"
            rd_value = rd_match.group(1) if rd_match else "N/A"

            # Save results
            result_file.write(f"{w}\t{fd_value}\t{rd_value}\n")

            print(f"Extracted for w={w}nm: fd={fd_value}, rd={rd_value}")

        except subprocess.CalledProcessError:
            print(f"Error running simulation for {scs_file_name}.")

        except FileNotFoundError:
            print(f"Measure file '{measure_file_name}' not found.")

print("All simulations completed.")
print("Results saved to 'simulation_results.txt'.")