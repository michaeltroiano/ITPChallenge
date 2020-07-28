import json


# Contacts class
class Contact:
    def __init__(self, name, email=None, phone=None):
        self.name = name
        self.email = email
        self.phone = phone


# Leads class
class Lead:
    def __init__(self, name=None, email=None, phone=None):
        self.name = name
        self.email = email
        self.phone = phone


# Add contact to contact list
def add_contact(registrant):
    new_registrant = registrant["registrant"]

    is_contact_new = True

    for contact in ContactsList:  # Compare and update contact phone and email to registrant.
        if new_registrant["email"] == contact.email:
            is_contact_new = False
            update_contact(contact, new_registrant)
        elif new_registrant["phone"] == contact.phone:
            is_contact_new = False
            update_contact(contact, new_registrant)
        else:
            for lead in LeadsList[:]:  # If registrant isnt a current contact, compare to leads and update contacts.
                if new_registrant["email"] == lead.email:
                    is_contact_new = False
                    ContactsList.append(Contact(new_registrant["name"], new_registrant["email"], new_registrant["phone"]))
                    LeadsList.remove(lead)
                elif new_registrant["phone"] == lead.phone:
                    is_contact_new = False
                    ContactsList.append(Contact(new_registrant["name"], new_registrant["email"], new_registrant["phone"]))
                    LeadsList.remove(lead)
    if is_contact_new:  # If registrant is not a current contact or lead, create a new contact with registrant data.
        new_contact = Contact(new_registrant["name"], new_registrant["email"], new_registrant["phone"])
        ContactsList.append(new_contact)


# Function to update contacts when registrant has updated data and current value is None.
def update_contact(contact, registrant):
    for attr, value in contact1.__dict__.items():
        if value is None:
            contact.__setattr__(attr, registrant[attr])


# Initialize lists.
ContactsList = []
LeadsList = []


# Test data.
contact1 = Contact("Alice Brown", None, "1231112223")
contact2 = Contact("Bob Crown", "bob@crowns.com", None)
contact3 = Contact("Carlos Drew", "carl@drewess.com", "3453334445")
contact4 = Contact("Doug Emerty", None, "4564445556")
contact5 = Contact("Egan Fair", "eg@fairness.com", "5675556667")
ContactsList.extend([contact1, contact2, contact3, contact4, contact5])

lead1 = Lead(None, "kevin@keith.com", None)
lead2 = Lead("Lucy", "lucy@liu.com", None)
lead3 = Lead("Mary Middle", "mary@middle.com", "3331112223")
lead4 = Lead(None, None, "4442223334")
lead5 = Lead(None, "ole@olson.com", None)
LeadsList.extend([lead1, lead2, lead3, lead4, lead5])

luci = '''{
    "registrant":
        {
            "name": "Luci Liu",
            "email": "lucy@liu.com",
            "phone": "3210001112"
        }
}'''

doug = '''{
    "registrant":
        {
            "name": "Doug",
            "email": "doug@emmy.com",
            "phone": "4564445556"
        }
}'''

uma = '''{
    "registrant":
        {
            "name": "Uma Thurman",
            "email": "uma@thurs.com",
            "phone": "None"
        }
}'''


# Add registrants from JSON.
add_contact(json.loads(luci))
add_contact(json.loads(doug))
add_contact(json.loads(uma))


# Print results.
print("Updated Contacts: ")
for c in ContactsList:
   print(c.name, c.email, c.phone)


print("\nRemaining Leads: ")
for c in LeadsList:
    print(c.name, c.email, c.phone)







