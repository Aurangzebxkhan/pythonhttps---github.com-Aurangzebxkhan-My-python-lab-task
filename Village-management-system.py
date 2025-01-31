# Village Information Management System
print("🌟 Welcome to the Village Information Management System 🌟")

# Initialize village data
village_info = {
    "village_name": "Shashoo",  # Replace with your village name
    "population": 0,
    "families": {},  # Family data
    "births": [],
    "deaths": [],
    "organizations": {
        "street_cleaning": [],
        "education_for_poor": [],
        "poor_support": [],
        "ramazan_ticket_distributors": [],
        "security": []
    }
}

# Menu options
def display_menu():
    print("\n📋 Main Menu:")
    print("1. Add Family")
    print("2. Add New Birth Record")
    print("3. Add Death Record")
    print("4. Add Organization Member")
    print("5. View Family Details")
    print("6. View Village Report")
    print("7. Exit")

# Add a new family
def add_family():
    family_name = input("🏠 Enter the family name: ")
    mobile_number = input("📞 Enter the family head's mobile number: ")
    total_members = int(input("👥 Enter the total number of members in the family: "))
    village_info["families"][family_name] = {
        "mobile_number": mobile_number,
        "total_members": total_members,
        "alive_members": total_members
    }
    village_info["population"] += total_members
    print(f"✅ Family '{family_name}' has been added.")

# Add a new birth record
def add_birth():
    family_name = input("🏠 Enter the family name: ")
    if family_name not in village_info["families"]:
        print("❌ Family not found. Please add the family first.")
        return
    name = input("👶 Enter the baby's name: ")
    date = input("📅 Enter the birth date (DD-MM-YYYY): ")
    village_info["births"].append({"name": name, "date": date, "family": family_name})
    village_info["families"][family_name]["total_members"] += 1
    village_info["families"][family_name]["alive_members"] += 1
    village_info["population"] += 1
    print(f"✅ Birth record for {name} has been added.")

# Add a new death record
def add_death():
    family_name = input("🏠 Enter the family name: ")
    if family_name not in village_info["families"]:
        print("❌ Family not found.")
        return
    name = input("⚰️ Enter the person's name: ")
    date = input("📅 Enter the date of death (DD-MM-YYYY): ")
    village_info["deaths"].append({"name": name, "date": date, "family": family_name})
    village_info["families"][family_name]["alive_members"] -= 1
    village_info["population"] -= 1
    print(f"✅ Death record for {name} has been added.")

# Add a member to an organization
def add_organization_member():
    print("\n🏢 Select Organization:")
    print("1. Street Cleaning Organization")
    print("2. Poor Study Organization")
    print("3. Poor People Support Organization")
    print("4. Ramazan Ticket Distributors")
    print("5. Security Organization")
    choice = int(input("Enter your choice: "))
    name = input("👤 Enter the member's name: ")
    if choice == 1:
        village_info["organizations"]["street_cleaning"].append(name)
    elif choice == 2:
        village_info["organizations"]["education_for_poor"].append(name)
    elif choice == 3:
        village_info["organizations"]["poor_support"].append(name)
    elif choice == 4:
        village_info["organizations"]["ramazan_ticket_distributors"].append(name)
    elif choice == 5:
        village_info["organizations"]["security"].append(name)
    else:
        print("❌ Invalid choice. Returning to main menu.")
        return
    print(f"✅ {name} has been added to the organization.")

# View family details
def view_family_details():
    family_name = input("🏠 Enter the family name: ")
    if family_name not in village_info["families"]:
        print("❌ Family not found.")
        return
    family = village_info["families"][family_name]
    print("\n📋 Family Details:")
    print(f"🏠 Family Name: {family_name}")
    print(f"📞 Mobile Number: {family['mobile_number']}")
    print(f"👥 Total Members: {family['total_members']}")
    print(f"🟢 Alive Members: {family['alive_members']}")

# Display the village report
def display_report():
    print("\n🌟 Village Report 🌟")
    print(f"📍 Village Name: {village_info['village_name']}")
    print(f"👥 Population: {village_info['population']}")
    print("\n👶 Birth Records:")
    for birth in village_info["births"]:
        print(f"- {birth['name']} (Born on {birth['date']}, Family: {birth['family']})")
    print("\n⚰️ Death Records:")
    for death in village_info["deaths"]:
        print(f"- {death['name']} (Died on {death['date']}, Family: {death['family']})")
    print("\n🏢 Organizations:")
    for org, members in village_info["organizations"].items():
        print(f"- {org.replace('_', ' ').title()}: {', '.join(members) if members else 'No members yet'}")
    print("\n🏠 Families:")
    for family_name, family_data in village_info["families"].items():
        print(f"- {family_name}: {family_data['alive_members']} alive out of {family_data['total_members']} members")

# Main loop
while True:
    display_menu()
    option = int(input("Enter your choice: "))
    if option == 1:
        add_family()
    elif option == 2:
        add_birth()
    elif option == 3:
        add_death()
    elif option == 4:
        add_organization_member()
    elif option == 5:
        view_family_details()
    elif option == 6:
        display_report()
    elif option == 7:
        print("👋 Thank you for using the Village Information Management System. Goodbye!")
        break
    else:
        print("❌ Invalid choice. Please try again.")
