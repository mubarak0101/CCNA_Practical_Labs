# It seems that there was an issue with character encoding. Let's ensure we are using plain ASCII text.

# Create a new PDF document
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Set title
pdf.set_font("Arial", 'B', 16)
pdf.cell(0, 10, 'OSPF Multi-Area Network Topology with DR/BDR Election', ln=True, align='C')

# Add overview
pdf.set_font("Arial", 'I', 12)
pdf.cell(0, 10, 'Overview', ln=True)
pdf.set_font("Arial", size=12)
overview_text = (
    "This document describes the OSPF (Open Shortest Path First) multi-area "
    "network topology, focusing on the Designated Router (DR) and Backup "
    "Designated Router (BDR) election process. The topology consists of three areas: "
    "Area 0 (Backbone), Area 1, and Area 2, each containing multiple devices including "
    "PCs, laptops, printers, and routers."
)
pdf.multi_cell(0, 10, overview_text)

# Add topology description
pdf.set_font("Arial", 'I', 12)
pdf.cell(0, 10, 'Topology Description', ln=True)
pdf.set_font("Arial", size=12)

# Area 0
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, 'Area 0 (Backbone)', ln=True)
pdf.set_font("Courier", size=12)
router0_config = (
    "Router0 Configuration:\n"
    "Router(config)#router ospf 1\n"
    "Router(config-router)#router-id 1.1.1.1\n"
    "Router(config-router)#network 192.10.1.0 0.0.0.255 area 0\n"
    "Router(config-router)#network 192.10.3.0 0.0.0.255 area 1\n"
    "Router(config-router)#network 192.10.6.0 0.0.0.255 area 2\n"
    "Router(config-router)#exit\n"
)
pdf.multi_cell(0, 10, router0_config)
pdf.set_font("Arial", size=12)
devices_area_0 = (
    "Devices and IP Addresses:\n"
    "Printer0: 192.10.1.60 / 255.255.255.0 / 192.10.1.5\n"
    "Laptop0: 192.10.1.50 / 255.255.255.0 / 192.10.1.5\n"
    "PC0: 192.10.1.10 / 255.255.255.0 / 192.10.1.5\n"
    "PC3: 192.10.1.20 / 255.255.255.0 / 192.10.1.5\n"
    "PC5: 192.10.1.30 / 255.255.255.0 / 192.10.1.5\n"
)
pdf.multi_cell(0, 10, devices_area_0)

# Area 1
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, 'Area 1', ln=True)
pdf.set_font("Courier", size=12)
router2_config = (
    "Router2 Configuration:\n"
    "Router(config)#router ospf 1\n"
    "Router(config-router)#network 192.10.3.0 0.0.0.255 area 1\n"
    "Router(config-router)#network 192.10.5.0 0.0.0.255 area 1\n"
    "Router(config-router)#exit\n"
)
pdf.multi_cell(0, 10, router2_config)
pdf.set_font("Arial", size=12)
devices_area_1 = (
    "Devices and IP Addresses:\n"
    "PC2: 192.10.5.10 / 255.255.255.0 / 192.10.5.5\n"
    "PC4: 192.10.5.20 / 255.255.255.0 / 192.10.5.5\n"
    "PC7: 192.10.5.40 / 255.255.255.0 / 192.10.5.5\n"
    "Printer1: 192.10.5.60 / 255.255.255.0 / 192.10.5.5\n"
    "Laptop1: 192.10.5.50 / 255.255.255.0 / 192.10.5.5\n"
)
pdf.multi_cell(0, 10, devices_area_1)

# Area 2
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, 'Area 2', ln=True)
pdf.set_font("Courier", size=12)
router1_config = (
    "Router1 Configuration:\n"
    "Router(config)#router ospf 1\n"
    "Router(config-router)#network 192.10.6.0 0.0.0.255 area 2\n"
    "Router(config-router)#network 192.10.2.0 0.0.0.255 area 2\n"
    "Router(config-router)#exit\n"
)
pdf.multi_cell(0, 10, router1_config)
pdf.set_font("Arial", size=12)
devices_area_2 = (
    "Devices and IP Addresses:\n"
    "PC2: 192.10.2.10 / 255.255.255.0 / 192.10.2.5\n"
    "PC4: 192.10.2.20 / 255.255.255.0 / 192.10.2.5\n"
    "PC6: 192.10.2.30 / 255.255.255.0 / 192.10.2.5\n"
    "PC7: 192.10.2.40 / 255.255.255.0 / 192.10.2.5\n"
    "Printer2: 192.10.2.60 / 255.255.255.0 / 192.10.2.5\n"
    "Laptop2: 192.10.2.50 / 255.255.255.0 / 192.10.2.5\n"
)
pdf.multi_cell(0, 10, devices_area_2)

# Add DR and BDR election process
pdf.set_font("Arial", 'I', 12)
pdf.cell(0, 10, 'DR and BDR Election Process', ln=True)
pdf.set_font("Arial", size=12)
election_purpose = (
    "Purpose: The DR and BDR are elected to reduce the amount of OSPF traffic on "
    "multi-access networks (e.g., Ethernet). They manage the exchange of routing "
    "information between routers in the same area."
)
pdf.multi_cell(0, 10, election_purpose)

# Election criteria
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, 'Election Criteria:', ln=True)
pdf.set_font("Arial", size=12)
criteria = (
    "OSPF Priority: Each router on a multi-access network has an OSPF priority value. "
    "The router with the highest priority becomes the DR. If there's a tie, the router "
    "with the highest Router ID (RID) wins.\n\n"
    "Default Priority: By default, all routers have a priority of 1. You can change "
    "this using the ip ospf priority command.\n\n"
    "BDR Election: The router with the second highest priority becomes the BDR. If "
    "there's a tie, the router with the second highest RID becomes the BDR."
)
pdf.multi_cell(0, 10, criteria)

# Election process
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, 'Election Process:', ln=True)
pdf.set_font("Arial", size=12)
process = (
    "BDR First: The BDR is elected first. If no other router declares itself as the DR, "
    "the BDR becomes the DR.\n\n"
    "DR Election: If a router declares itself as the DR, the BDR compares its "
    "priority/RID to the DR’s attributes. If the BDR has a higher priority/RID, it "
    "becomes the DR."
)
pdf.multi_cell(0, 10, process)

# Save the PDF to a file
pdf_file_path = '/mnt/data/OSPF_Multi_Area_Network_Topology.pdf'
pdf.output(pdf_file_path)

pdf_file_path
