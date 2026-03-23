# Network Request Guide

## Overview
This document explains the process to validate raise network requests for:
- Vertical
- APT (Project)

**Link of cloudHelper to raise request:**
- Hosting Portal --> https://hosting-portal.intel.com/cloud-helper/accounts?type=Standard&status=Active

It also standardizes naming conventions and required configurations.

---

## Required Inputs

Before raising any request, collect the following details:

1. **Subscription ID**  
   - Must belong to the request owner

2. **Superzone**  
   - Example: 'ip', 'cp', 'if' etc.

3. **Vertical Name**  
   - Example: 'smg', 'schain', 'finance' etc.

4. **Project Name (APT)**  
   - Example: 'dmbi', 'fincap', 'fintnc', 'mtlpln' etc.

5. **Environment (env)**  
   - Example: 'dev', 'dev1', 'qa', 'prod', 'dr', 'm1-m7' etc.

---

## Step 1: Validation

- Open VS Code
- Navigate to:  
  **superzone → {vertical_name} → vertical**
- Check whether the required **environment (env)** exists

### If environment exists:
- Vertical network is already provisioned  
- Only raise network request for:
- APT (Project)

### If environment does NOT exist:
- Vertical network is not present  
- Raise network requests for:
  - Vertical
  - APT (Project)
---

## Step 2: Location Mapping

| Environment        | Location       |
|------------------|---------------|
| dev, prod, qa    | westus2       |
| dev1, m1–m7      | westus        |
| dr               | westcentralus |

### Notes:
- `westus2` → Washington DC
- `westus`, `westcentralus` → NorCal

---

## 📏 Step 3: Network Sizing

| Component              | Size         | CIDR |
|----------------------|-------------|------|
| APT Private Endpoint | Extra Small | /28  |
| Vertical PE          | Small       | /27  |
| ADB Network          | Medium      | /26  |

---

## Step 4: Network Request Details

# VERTICAL PRIVATE ENDPOINT
- {superzone} {vertical} {env} pe --> RITM: (small/27)
1. Resource Group Name: {superzone}-rg-{vertical}-exvnet-{env}
2. VNet Name: {superzone}-exvnet-{vertical}-{env}
3. Location: {location}
4. Subnet name and number of subnets needed: subnet-{vertical}-pe-{env}

# VERTICAL ADB
- {superzone} {vertical} {env} adb --> RITM: (medium/26)
1. Resource Group Name: {superzone}-rg-{vertical}-exvnet-{env}
2. VNet Name: {superzone}-exvnet-{vertical}-adb-{env}
3. Location: {location}
4. Subnet name and number of subnets needed: Not Required

# APT PRIVATE ENDPOINT
- {superzone} {project} {env} pe --> RITM: (extra small/28)
1. Resource Group Name: {superzone}-rg-{vertical}-exvnet-{env}
2. VNet Name: {superzone}-exvnet-{vertical}-{env}
3. Location: {location}
4. Subnet name and number of subnets needed: subnet-{project}-pe-{env}

# APT ADB 
- {superzone} {project} {env} adb --> RITM: (medium/26)
1. Resource Group Name: {superzone}-rg-{vertical}-exvnet-{env}
2. VNet Name: {superzone}-exvnet-{project}-adb-{env}
3. Location: {location}
4. Subnet name and number of subnets needed: Not Required



---
# python NetworkRequest.py
# python -m streamlit run app.py

 