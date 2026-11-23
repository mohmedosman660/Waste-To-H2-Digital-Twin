# Waste-to-Hydrogen Climate Digital Twin (COP31 / AIChE BAİBÜ)

Baseline process simulation, data schema, and interactive LCA/TEA scenario model for waste-to-hydrogen production.

## Baseline Model & Key Outputs
- **Functional Unit:** $1\text{ kg}$ of $\text{H}_2$
- **DWSIM Equilibrium Reactor (`RGIBBS-1`):** `100 kg/h` feed (`CH4/CO2`) + `200 kg/h` `H2O` at `800 °C`, `1.01325 bar` (`Peng-Robinson`)
- **Simulated Outputs:** `~30.65 kg/h` $\text{H}_2$ and `566.306 kW` (`2038.7 MJ/h`) reactor heat duty
- **Baseline Utility LCA & TEA (Colab):** `4.59 kg CO2e / kg H2` utility carbon footprint and `$0.16 / kg H2` electricity utility cost (at baseline settings)

## Repository Contents
- `inputs_baseline.csv`: Baseline process, utility, emission factor, and cost inputs
- DWSIM simulation file: Baseline equilibrium reactor flowsheet
- `.ipynb` notebook: LCA/TEA calculation and interactive sliders for renewable electricity share, heat recovery, and grid electricity
