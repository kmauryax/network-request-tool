import streamlit as st
import pyperclip
import streamlit.components.v1 as components


# -------------------------- CSS ------------------------

st.markdown("""
<style>
/* Generate Button */
.stButton button {
    background-color: #03a9f4;
    color: white;
    border-radius: 6px;
    height: 42px;
    width: 100%;
    font-weight: 500;
}
.stButton button:hover {
    background-color: #0288d1;
}
</style>
""", unsafe_allow_html=True)

# ---------- Functions -----------------------------------

def get_location(env):
    if env in ["dev", "prod", "qa"]:
        return ("westus2", "Washington")
    elif env in ["m1", "m2", "m3", "m4", "m5", "m6", "m7", "dev1"]:
        return ("westus", "NorCal")
    elif env == "dr":
        return ("westcentralus", "NorCal")
    else:
        raise ValueError(f"{env} is invalid env, Pls check.")
    

# ---------------------------------------------------------


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


# -----------------------------------------------------------------


def generate_output(superzone, vertical, project, env, include_vertical):
    location, region = get_location(env)

    if superzone == "corp":
        superzone = "cp"

    rg, vnet_vertical, vnet_vertical_adb, vnet_apt, vnet_apt_adb = get_names(
        superzone, vertical, project, env
    )

    output = ""

    if include_vertical:
        output += "\n|----- VERTICAL PRIVATE ENDPOINT -----|\n\n"
        output += f"{superzone} {vertical} {env} pe\n"
        output += "Network Size: small/27 (28 IPs)\n"
        output += f"Network Region: {region}\n\n"
        output += f"1. Resource Group Name: {rg}\n"
        output += f"2. VNet Name: {vnet_vertical}\n"
        output += f"3. Location: {location}\n"
        output += f"4. Subnet name and number of subnets needed: subnet-{vertical}-pe-{env}\n\n"

        output += "|----- VERTICAL ADB -----|\n\n"
        output += f"{superzone} {vertical} {env} adb\n"
        output += "Network Size: medium/26 (60 IPs)\n"
        output += f"Network Region: {region}\n\n"
        output += f"1. Resource Group Name: {rg}\n"
        output += f"2. VNet Name: {vnet_vertical_adb}\n"
        output += f"3. Location: {location}\n"
        output += "4. Subnet name and number of subnets needed: Not Required\n\n"

    output += "|----- APT PRIVATE ENDPOINT -----|\n\n"
    output += f"{superzone} {project} {env} pe\n"
    output += "Network Size: extra small/28 (12 IPs)\n"
    output += f"Network Region: {region}\n\n"
    output += f"1. Resource Group Name: {rg}\n"
    output += f"2. VNet Name: {vnet_apt}\n"
    output += f"3. Location: {location}\n"
    output += f"4. Subnet name and number of subnets needed: subnet-{project}-pe-{env}\n\n"

    output += "|----- APT ADB -----|\n\n"
    output += f"{superzone} {project} {env} adb\n"
    output += "Network Size: medium/26 (60 IPs)\n"
    output += f"Network Region: {region}\n\n"
    output += f"1. Resource Group Name: {rg}\n"
    output += f"2. VNet Name: {vnet_apt_adb}\n"
    output += f"3. Location: {location}\n"
    output += "4. Subnet name and number of subnets needed: Not Required\n"

    return output


# ---------- UI --------------------------------------

st.title("🌐 Network Request Generator")

# Superzone dropdown
superzone_option = st.selectbox(
    "Select Superzone",
    ["cp", "if", "ip", "Other"]
)

if superzone_option == "Other":
    superzone = st.text_input("Enter Superzone")
else:
    superzone = superzone_option

vertical = st.text_input("Enter Vertical Name")
project = st.text_input("Enter Project Name")

env = st.selectbox(
    "Select Environment",
    ["dev", "qa", "prod", "dev1", "m1", "m2", "m3", "m4", "m5", "m6", "m7", "dr"]
)

include_vertical = st.checkbox("Include Vertical Details")

# Generate
if st.button("Generate"):
    try:
        if not superzone or not vertical or not project or not env:
            st.error("All inputs are required")
        else:
            st.session_state.result = generate_output(
                superzone.lower(),
                vertical.lower(),
                project.lower(),
                env.lower(),
                include_vertical
            )
    except Exception as e:
        st.error(str(e))


if "result" in st.session_state:

    with st.container():
        st.markdown("### Output")
        st.code(st.session_state.result, language="text")

    st.download_button(
        label="⬇️ Download Output",
        data=st.session_state.result,
        file_name="network_request.txt",
        mime="text/plain"
    )