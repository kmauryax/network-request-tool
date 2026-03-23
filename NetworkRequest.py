def get_location(env):
    if env in ["dev", "prod", "qa"]:
        return ("westus2", "Washington")
    elif env in ["m1", "m2", "m3", "m4", "m5", "m6", "m7", "dev1"]:
        return ("westus", "NorCal")
    elif env == "dr":
        return ("westcentralus", "NorCal")
    else:
        raise ValueError(f"{env} is invalid env, Pls check.")


def get_names(superzone, vertical, project, env):
    if superzone == "ip":
        rg = f"rg-{vertical}-exvnet-{env}"
        vnet_vertical = f"exvnet-{vertical}-{env}"
        vnet_vertical_adb = f"exvnet-{vertical}-adb-{env}"
        vnet_apt = f"exvnet-{vertical}-{env}"
        vnet_apt_adb = f"exvnet-{project}-adb-{env}"
    else:
        rg = f"{superzone}-rg-{vertical}-exvnet-{env}"
        vnet_vertical = f"{superzone}-exvnet-{vertical}-{env}"
        vnet_vertical_adb = f"{superzone}-exvnet-{vertical}-adb-{env}"
        vnet_apt = f"{superzone}-exvnet-{vertical}-{env}"
        vnet_apt_adb = f"{superzone}-exvnet-{project}-adb-{env}"

    return rg, vnet_vertical, vnet_vertical_adb, vnet_apt, vnet_apt_adb


def vertical_details(superzone, vertical, env, location, region, rg, vnet, vnet_adb):
    print("\n|----- VERTICAL PRIVATE ENDPOINT -----|\n")
    print(f"{superzone} {vertical} {env} pe")
    print("Network Size: small/27 (28 IPs)")
    print(f"Network Region: {region}\n")
    print(f"1. Resource Group Name: {rg}")
    print(f"2. VNet Name: {vnet}")
    print(f"3. Location: {location}")
    print(f"4. Subnet name and number of subnets needed: subnet-{vertical}-pe-{env}")

    print("\n|----- VERTICAL ADB -----|\n")
    print(f"{superzone} {vertical} {env} adb")
    print("Network Size: medium/26 (60 IPs)")
    print(f"Network Region: {region}\n")
    print(f"1. Resource Group Name: {rg}")
    print(f"2. VNet Name: {vnet_adb}")
    print(f"3. Location: {location}")
    print("4. Subnet name and number of subnets needed: Not Required")


def apt_details(superzone, vertical, project, env, location, region, rg, vnet, vnet_adb):
    print("\n|----- APT PRIVATE ENDPOINT -----|\n")
    print(f"{superzone} {project} {env} pe")
    print("Network Size: extra small/28 (12 IPs)")
    print(f"Network Region: {region}\n")
    print(f"1. Resource Group Name: {rg}")
    print(f"2. VNet Name: {vnet}")
    print(f"3. Location: {location}")
    print(f"4. Subnet name and number of subnets needed: subnet-{project}-pe-{env}")

    print("\n|----- APT ADB -----|\n")
    print(f"{superzone} {project} {env} adb")
    print("Network Size: medium/26 (60 IPs)")
    print(f"Network Region: {region}\n")
    print(f"1. Resource Group Name: {rg}")
    print(f"2. VNet Name: {vnet_adb}")
    print(f"3. Location: {location}")
    print("4. Subnet name and number of subnets needed: Not Required")


# ===== MAIN =====
if __name__ == "__main__":
    superzone = input("Enter Superzone: ").lower()
    vertical = input("Enter Vertical Name: ").lower()
    project = input("Enter Project Name: ").lower()
    env = input("Enter Environment: ").lower()
    
    if not superzone or not vertical or not project or not env:
        raise ValueError("All inputs are required")

    location, region = get_location(env)

    if superzone == "corp":
        superzone = "cp"

    # Generate naming
    rg, vnet_vertical, vnet_vertical_adb, vnet_apt, vnet_apt_adb = get_names(
        superzone, vertical, project, env
    )

    choice = input("\nDo you want details for Vertical as well? (y/n): ").strip().lower()

    if choice == "y":
        vertical_details(superzone, vertical, env, location, region, rg, vnet_vertical, vnet_vertical_adb)
        apt_details(superzone, vertical, project, env, location, region, rg, vnet_apt, vnet_apt_adb)
    else:
        apt_details(superzone, vertical, project, env, location, region, rg, vnet_apt, vnet_apt_adb)