"""
Petroleum Engineering Calculators

A collection of calculation functions for common oil & gas engineering tasks:
- Drilling hydraulics
- Cementing volumes
- Pressure drop calculations
- Well control
- Production engineering

Usage:
    from calculators import drilling_hydraulics, cementing_volumes
    
    # Calculate annular pressure drop
    result = drilling_hydraulics.annular_pressure_drop(
        flow_rate=500,  # gpm
        annular_id=8.5,  # inches
        pipe_od=5.0,  # inches
        mud_weight=12.0,  # ppg
        plastic_viscosity=35,  # cP
        yield_point=12  # lb/100ft²
    )
"""

import math
from typing import Dict, Tuple, Optional
from dataclasses import dataclass


# ============================================================================
# DRILLING HYDRAULICS CALCULATORS
# ============================================================================

@dataclass
class HydraulicsResult:
    """Results from drilling hydraulics calculations."""
    annular_velocity: float  # ft/min
    annular_pressure_drop: float  # psi
    ecd_at_depth: float  # ppg
    bit_pressure_drop: float  # psi
    surface_pressure: float  # psi
    hydraulic_hp: float  # HP
    hsi: float  # Hydraulic horsepower per sq inch


def annular_velocity(
    flow_rate: float,  # gpm
    annular_capacity: float  # bbl/ft
) -> float:
    """
    Calculate annular velocity.
    
    Args:
        flow_rate: Pump flow rate in gallons per minute
        annular_capacity: Annular capacity in barrels per foot
        
    Returns:
        Annular velocity in feet per minute
    """
    return (24.5 * flow_rate) / (annular_capacity * 42)


def annular_pressure_drop_bingham(
    flow_rate: float,  # gpm
    annular_id: float,  # inches
    pipe_od: float,  # inches
    mud_weight: float,  # ppg
    plastic_viscosity: float,  # cP
    yield_point: float,  # lb/100ft²
    length: float  # ft
) -> float:
    """
    Calculate annular pressure drop using Bingham plastic model.
    
    Args:
        flow_rate: Flow rate in gpm
        annular_id: Annular inner diameter (hole or casing ID)
        pipe_od: Pipe outer diameter
        mud_weight: Mud weight in ppg
        plastic_viscosity: PV in cP
        yield_point: YP in lb/100ft²
        length: Section length in ft
        
    Returns:
        Pressure drop in psi
    """
    # Annular dimensions
    dh = annular_id  # Hydraulic diameter approximation
    dp = pipe_od
    
    # Average annular velocity (ft/min)
    va = flow_rate / (2.448 * (dh**2 - dp**2))
    
    # Shear rate (1/sec)
    shear_rate = (1.6 * va) / (dh - dp)
    
    # Effective viscosity (cP)
    effective_visc = plastic_viscosity + (100 * yield_point / shear_rate)
    
    # Pressure drop (psi)
    # Simplified Bingham model
    pressure_drop = (effective_visc * va * length) / (1500 * (dh - dp))
    
    return pressure_drop


def ecd_calculation(
    mud_weight: float,  # ppg
    annular_pressure_drop: float,  # psi
    true_vertical_depth: float,  # ft
) -> float:
    """
    Calculate Equivalent Circulating Density (ECD).
    
    Args:
        mud_weight: Static mud weight in ppg
        annular_pressure_drop: Annular pressure drop in psi
        true_vertical_depth: TVD in ft
        
    Returns:
        ECD in ppg
    """
    return mud_weight + (annular_pressure_drop / (0.052 * true_vertical_depth))


def bit_pressure_drop(
    flow_rate: float,  # gpm
    mud_weight: float,  # ppg
    total_flow_area: float  # in²
) -> float:
    """
    Calculate pressure drop across bit nozzles.
    
    Args:
        flow_rate: Flow rate in gpm
        mud_weight: Mud weight in ppg
        total_flow_area: Total flow area (TFA) of nozzles in sq inches
        
    Returns:
        Bit pressure drop in psi
    """
    return (mud_weight * flow_rate**2) / (12031 * total_flow_area**2)


def hydraulic_horsepower(
    flow_rate: float,  # gpm
    pressure: float  # psi
) -> float:
    """
    Calculate hydraulic horsepower.
    
    Args:
        flow_rate: Flow rate in gpm
        pressure: Pressure in psi
        
    Returns:
        Hydraulic horsepower
    """
    return (flow_rate * pressure) / 1714


def hsi_calculation(
    hydraulic_hp: float,  # HP
    bit_diameter: float  # inches
) -> float:
    """
    Calculate Hydraulic Horsepower per Square Inch (HSI).
    
    Args:
        hydraulic_hp: Hydraulic horsepower
        bit_diameter: Bit diameter in inches
        
    Returns:
        HSI in HP/sq inch
    """
    bit_area = math.pi * (bit_diameter / 2)**2
    return hydraulic_hp / bit_area


def nozzle_velocity(
    flow_rate: float,  # gpm
    total_flow_area: float  # in²
) -> float:
    """
    Calculate fluid velocity through bit nozzles.
    
    Args:
        flow_rate: Flow rate in gpm
        total_flow_area: TFA in sq inches
        
    Returns:
        Nozzle velocity in ft/sec
    """
    return (0.32086 * flow_rate) / total_flow_area


def jet_impact_force(
    mud_weight: float,  # ppg
    flow_rate: float,  # gpm
    total_flow_area: float  # in²
) -> float:
    """
    Calculate jet impact force.
    
    Args:
        mud_weight: Mud weight in ppg
        flow_rate: Flow rate in gpm
        total_flow_area: TFA in sq inches
        
    Returns:
        Jet impact force in lbs
    """
    velocity = nozzle_velocity(flow_rate, total_flow_area)
    return (mud_weight * flow_rate * velocity) / 1930


# ============================================================================
# CEMENTING CALCULATORS
# ============================================================================

def cement_volume_annular(
    hole_diameter: float,  # inches
    pipe_od: float,  # inches
    length: float  # ft
) -> float:
    """
    Calculate cement volume required for annular fill.
    
    Args:
        hole_diameter: Hole or casing ID in inches
        pipe_od: Pipe outer diameter in inches
        length: Length to cement in ft
        
    Returns:
        Cement volume in cubic feet
    """
    hole_area = math.pi * (hole_diameter / 2)**2
    pipe_area = math.pi * (pipe_od / 2)**2
    annular_area = hole_area - pipe_area  # sq inches
    
    # Convert to cubic feet
    volume_cuft = (annular_area * length * 12) / 1728
    return volume_cuft


def cement_volume_open_hole(
    hole_diameter: float,  # inches
    length: float  # ft
) -> float:
    """
    Calculate cement volume for open hole section.
    
    Args:
        hole_diameter: Hole diameter in inches
        length: Length in ft
        
    Returns:
        Cement volume in cubic feet
    """
    hole_area = math.pi * (hole_diameter / 2)**2  # sq inches
    volume_cuft = (hole_area * length * 12) / 1728
    return volume_cuft


def cement_volume_casing(
    casing_id: float,  # inches
    length: float  # ft
) -> float:
    """
    Calculate cement volume to fill casing (shoe track, etc.).
    
    Args:
        casing_id: Casing inner diameter in inches
        length: Length in ft
        
    Returns:
        Cement volume in cubic feet
    """
    area = math.pi * (casing_id / 2)**2  # sq inches
    volume_cuft = (area * length * 12) / 1728
    return volume_cuft


def sacks_required(
    cement_volume: float,  # cu ft
    yield_per_sack: float = 1.15  # cu ft per sack
) -> int:
    """
    Calculate number of cement sacks required.
    
    Args:
        cement_volume: Total cement volume in cubic feet
        yield_per_sack: Cement yield per sack (default 1.15 for Class G)
        
    Returns:
        Number of sacks (rounded up)
    """
    return math.ceil(cement_volume / yield_per_sack)


def mixing_water_volume(
    sacks: int,
    water_per_sack: float = 4.96  # gallons per sack
) -> float:
    """
    Calculate mixing water volume required.
    
    Args:
        sacks: Number of cement sacks
        water_per_sack: Water requirement per sack in gallons
        
    Returns:
        Total water volume in gallons
    """
    return sacks * water_per_sack


def displacement_volume(
    casing_id: float,  # inches
    depth: float  # ft
) -> float:
    """
    Calculate displacement volume to bump plug.
    
    Args:
        casing_id: Casing inner diameter in inches
        depth: Depth to bump plug in ft
        
    Returns:
        Displacement volume in barrels
    """
    capacity_bbl_per_ft = (casing_id**2) / 1029.4
    return capacity_bbl_per_ft * depth


def hydrostatic_pressure(
    fluid_density: float,  # ppg
    true_vertical_depth: float  # ft
) -> float:
    """
    Calculate hydrostatic pressure.
    
    Args:
        fluid_density: Fluid density in ppg
        true_vertical_depth: TVD in ft
        
    Returns:
        Hydrostatic pressure in psi
    """
    return 0.052 * fluid_density * true_vertical_depth


def formation_breakdown_pressure(
    fracture_gradient: float,  # psi/ft
    true_vertical_depth: float  # ft
) -> float:
    """
    Calculate formation breakdown pressure.
    
    Args:
        fracture_gradient: Fracture gradient in psi/ft
        true_vertical_depth: TVD in ft
        
    Returns:
        Formation breakdown pressure in psi
    """
    return fracture_gradient * true_vertical_depth


# ============================================================================
# PRESSURE DROP CALCULATORS
# ============================================================================

def reynolds_number(
    density: float,  # lb/ft³
    velocity: float,  # ft/sec
    diameter: float,  # ft
    viscosity: float  # lb/(ft·sec)
) -> float:
    """
    Calculate Reynolds number.
    
    Args:
        density: Fluid density in lb/cu ft
        velocity: Flow velocity in ft/sec
        diameter: Pipe diameter in ft
        viscosity: Dynamic viscosity in lb/(ft·sec)
        
    Returns:
        Reynolds number (dimensionless)
    """
    return (density * velocity * diameter) / viscosity


def friction_factor(
    reynolds_number: float,
    relative_roughness: float  # ε/D
) -> float:
    """
    Calculate Darcy friction factor using Colebrook approximation.
    
    Args:
        reynolds_number: Reynolds number
        relative_roughness: Pipe relative roughness (ε/D)
        
    Returns:
        Darcy friction factor
    """
    # Haaland approximation
    if reynolds_number < 2300:
        # Laminar flow
        return 64 / reynolds_number
    else:
        # Turbulent flow - Haaland equation
        term1 = (relative_roughness / 3.7)**1.11
        term2 = 6.9 / reynolds_number
        return 0.25 / (math.log10(term1 + term2))**2


def pipe_pressure_drop(
    flow_rate: float,  # bbl/day
    pipe_id: float,  # inches
    length: float,  # ft
    density: float,  # lb/ft³
    viscosity: float,  # cP
    roughness: float = 0.00015  # ft (commercial steel)
) -> float:
    """
    Calculate pressure drop in pipe using Darcy-Weisbach.
    
    Args:
        flow_rate: Flow rate in barrels per day
        pipe_id: Pipe inner diameter in inches
        length: Pipe length in ft
        density: Fluid density in lb/cu ft
        viscosity: Fluid viscosity in centipoise
        roughness: Pipe roughness in ft
        
    Returns:
        Pressure drop in psi
    """
    # Convert units
    d_ft = pipe_id / 12  # diameter in ft
    area = math.pi * (d_ft / 2)**2  # sq ft
    
    # Velocity in ft/sec
    q_cfs = flow_rate * 5.615 / 86400  # cu ft/sec
    velocity = q_cfs / area
    
    # Viscosity in lb/(ft·sec)
    viscosity_lbftsec = viscosity * 0.000672
    
    # Reynolds number
    re = reynolds_number(density, velocity, d_ft, viscosity_lbftsec)
    
    # Friction factor
    rel_roughness = roughness / d_ft
    f = friction_factor(re, rel_roughness)
    
    # Pressure drop (Darcy-Weisbach)
    # ΔP = f * (L/D) * (ρv²/2)
    delta_p_psf = f * (length / d_ft) * (density * velocity**2 / 2)
    delta_p_psi = delta_p_psf / 144
    
    return delta_p_psi


# ============================================================================
# WELL CONTROL CALCULATORS
# ============================================================================

def kill_mud_weight(
    current_mud_weight: float,  # ppg
    shut_in_drill_pipe_pressure: float,  # psi
    true_vertical_depth: float  # ft
) -> float:
    """
    Calculate required kill mud weight.
    
    Args:
        current_mud_weight: Current mud weight in ppg
        shut_in_drill_pipe_pressure: SIDPP in psi
        true_vertical_depth: TVD in ft
        
    Returns:
        Kill mud weight in ppg
    """
    return current_mud_weight + (shut_in_drill_pipe_pressure / (0.052 * true_vertical_depth))


def initial_circulating_pressure(
    slow_circulating_rate_pressure: float,  # psi
    shut_in_drill_pipe_pressure: float  # psi
) -> float:
    """
    Calculate initial circulating pressure (driller's method).
    
    Args:
        slow_circulating_rate_pressure: SCR pressure at selected rate
        shut_in_drill_pipe_pressure: SIDPP
        
    Returns:
        Initial circulating pressure in psi
    """
    return slow_circulating_rate_pressure + shut_in_drill_pipe_pressure


def final_circulating_pressure(
    slow_circulating_rate_pressure: float,  # psi
    kill_mud_weight: float,  # ppg
    original_mud_weight: float  # ppg
) -> float:
    """
    Calculate final circulating pressure.
    
    Args:
        slow_circulating_rate_pressure: SCR pressure
        kill_mud_weight: Kill mud weight in ppg
        original_mud_weight: Original mud weight in ppg
        
    Returns:
        Final circulating pressure in psi
    """
    return slow_circulating_rate_pressure * (kill_mud_weight / original_mud_weight)


def influx_gradient(
    shut_in_casing_pressure: float,  # psi
    shut_in_drill_pipe_pressure: float,  # psi
    influx_height: float  # ft
) -> float:
    """
    Calculate influx fluid gradient.
    
    Args:
        shut_in_casing_pressure: SICP in psi
        shut_in_drill_pipe_pressure: SIDPP in psi
        influx_height: Height of influx in annulus in ft
        
    Returns:
        Influx gradient in psi/ft
    """
    return (shut_in_casing_pressure - shut_in_drill_pipe_pressure) / influx_height


def influx_type(
    influx_gradient: float  # psi/ft
) -> str:
    """
    Determine influx fluid type from gradient.
    
    Args:
        influx_gradient: Influx gradient in psi/ft
        
    Returns:
        String describing influx type
    """
    if influx_gradient < 0.1:
        return "Gas (likely)"
    elif influx_gradient < 0.3:
        return "Gas/oil mixture"
    elif influx_gradient < 0.4:
        return "Oil (likely)"
    else:
        return "Water or salt water"


# ============================================================================
# PRODUCTION ENGINEERING CALCULATORS
# ============================================================================

def gas_flow_rate_standard(
    gas_rate_actual: float,  # cu ft/day at reservoir conditions
    reservoir_pressure: float,  # psia
    reservoir_temperature: float,  # °R
    standard_pressure: float = 14.696,  # psia
    standard_temperature: float = 520.0  # °R (60°F)
) -> float:
    """
    Convert gas flow rate from reservoir to standard conditions.
    
    Args:
        gas_rate_actual: Gas rate at reservoir conditions
        reservoir_pressure: Reservoir pressure in psia
        reservoir_temperature: Reservoir temperature in °R
        standard_pressure: Standard pressure (14.696 psia)
        standard_temperature: Standard temperature (520°R = 60°F)
        
    Returns:
        Gas flow rate at standard conditions (SCF/day)
    """
    return gas_rate_actual * (reservoir_pressure / standard_pressure) * (standard_temperature / reservoir_temperature)


def bottom_hole_pressure_static(
    wellhead_pressure: float,  # psia
    gas_gradient: float,  # psi/ft
    true_vertical_depth: float  # ft
) -> float:
    """
    Calculate bottom hole pressure (static gas column).
    
    Args:
        wellhead_pressure: Wellhead pressure in psia
        gas_gradient: Gas gradient in psi/ft
        true_vertical_depth: TVD in ft
        
    Returns:
        Bottom hole pressure in psia
    """
    return wellhead_pressure + (gas_gradient * true_vertical_depth)


def productivity_index(
    flow_rate: float,  # STB/day
    reservoir_pressure: float,  # psi
    bottom_hole_flowing_pressure: float  # psi
) -> float:
    """
    Calculate productivity index (PI).
    
    Args:
        flow_rate: Oil flow rate in STB/day
        reservoir_pressure: Average reservoir pressure in psi
        bottom_hole_flowing_pressure: Flowing BHP in psi
        
    Returns:
        Productivity index in STB/day/psi
    """
    drawdown = reservoir_pressure - bottom_hole_flowing_pressure
    if drawdown <= 0:
        return 0
    return flow_rate / drawdown


def skin_factor(
    actual_productivity_index: float,  # STB/day/psi
    theoretical_productivity_index: float  # STB/day/psi
) -> float:
    """
    Calculate skin factor from productivity index ratio.
    
    Args:
        actual_productivity_index: Measured PI
        theoretical_productivity_index: Ideal PI (no skin)
        
    Returns:
        Skin factor (dimensionless)
    """
    if theoretical_productivity_index <= 0:
        return 0
    ratio = theoretical_productivity_index / actual_productivity_index
    return math.log(ratio)


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def convert_ppg_to_sg(mud_weight_ppg: float) -> float:
    """Convert mud weight from ppg to specific gravity."""
    return mud_weight_ppg / 8.33


def convert_sg_to_ppg(specific_gravity: float) -> float:
    """Convert specific gravity to mud weight in ppg."""
    return specific_gravity * 8.33


def convert_psi_to_kpa(pressure_psi: float) -> float:
    """Convert pressure from psi to kPa."""
    return pressure_psi * 6.89476


def convert_kpa_to_psi(pressure_kpa: float) -> float:
    """Convert pressure from kPa to psi."""
    return pressure_kpa / 6.89476


def convert_ft_to_m(length_ft: float) -> float:
    """Convert length from feet to meters."""
    return length_ft * 0.3048


def convert_m_to_ft(length_m: float) -> float:
    """Convert length from meters to feet."""
    return length_m / 0.3048


def convert_bbl_to_m3(volume_bbl: float) -> float:
    """Convert volume from barrels to cubic meters."""
    return volume_bbl * 0.158987


def convert_m3_to_bbl(volume_m3: float) -> float:
    """Convert volume from cubic meters to barrels."""
    return volume_m3 / 0.158987


# Example usage
if __name__ == "__main__":
    # Drilling hydraulics example
    print("=== Drilling Hydraulics ===")
    
    flow_rate = 500  # gpm
    mud_weight = 12.0  # ppg
    annular_id = 8.5  # inches
    pipe_od = 5.0  # inches
    
    va = annular_velocity(flow_rate, 0.1)  # Assuming 0.1 bbl/ft capacity
    print(f"Annular velocity: {va:.1f} ft/min")
    
    bit_dp = bit_pressure_drop(flow_rate, mud_weight, 0.5)  # 0.5 sq in TFA
    print(f"Bit pressure drop: {bit_dp:.1f} psi")
    
    # Cementing example
    print("\n=== Cementing ===")
    
    hole_dia = 12.25  # inches
    casing_od = 9.625  # inches
    length = 1000  # ft
    
    vol = cement_volume_annular(hole_dia, casing_od, length)
    sacks = sacks_required(vol)
    print(f"Cement volume: {vol:.1f} cu ft")
    print(f"Sacks required: {sacks}")
    
    # Well control example
    print("\n=== Well Control ===")
    
    current_mw = 12.0  # ppg
    sidpp = 500  # psi
    tvd = 10000  # ft
    
    kmw = kill_mud_weight(current_mw, sidpp, tvd)
    print(f"Kill mud weight: {kmw:.2f} ppg")
    print(f"Weight increase: {kmw - current_mw:.2f} ppg")