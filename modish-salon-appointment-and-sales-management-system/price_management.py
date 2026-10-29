"""
PRICE MANAGEMENT
"""

SERVICE_CATALOG = {
    # HAIR SERVICES
    "Hair Cut (Trim)": 190,
    "Hair Cut w/ Style": 240,
    "Blow-dry": 220,
    "Shampoo w/ Conditioner & Blow-dry": 290,
    "Iron or Curling (Hair Setting)": 390,
    "Make Up": 750,
    "Hair Rebond w/ Hair Treatment (L'Oreal)": 1950,
    "Hair Rebond w/ Hair Treatment (Botanique)": 1650,
    "Hair Color w/ Hair Treatment (L'Oreal)": 1200,
    "Hair Color w/ Hair Treatment (Naturtint Non-Ammonia)": 1100,
    "Hair Color w/ Hair Treatment (Botanique)": 950,
    "Hair Color w/ Hair Treatment (Regular Brand)": 750,
    "Additional Hair Highlights": 850,
    "Hair Spa Treatment (L'Oreal)": 720,
    "Hair Spa Treatment (Hot Oil)": 300,
    "Brazilian Keratin Treatment": 990,
    "Cysteine Straight": 1400,
    "U-Collagent Treatment": 1400,

    # EYELASH, EYEBROW, THREADING, FACIAL, AND WAXING
    "Eyelash Extensions - Natural": 890,
    "Eyelash Extensions - Alluring": 1120,
    "Eyelash Extensions - Retouch": 600,
    "Eyelash Extensions - Removal (No Extension After)": 290,
    "Eyelash Extensions - Removal (Apply Extension After)": 160,
    "Threading - Eyebrow": 170,
    "Threading - Upper Lip": 140,
    "Threading - Lower Lip": 140,
    "Threading - Face": 600,
    "Threading - Underarm": 240,
    "Eyebrow Tinting - Color Only": 390,
    "Keratin Lash Lift": 1250,
    "Deep Cleansing Facial": 490,
    "Deep Whitening Facial": 590,
    "Hair Waxing - Upper Lip": 210,
    "Hair Waxing - Lower Lip": 210,
    "Hair Waxing - Face": 720,
    "Hair Waxing - Underarm": 290,
    "Hair Waxing - Hands/Arm": 370,
    "Hair Waxing - Half Legs": 370,
    "Hair Waxing - Full Legs": 670,
    "Hair Waxing - Bikini Wax": 640,
    "Hair Waxing - Brazilian Wax": 770,

    # NAIL SERVICES
    "Spa MANI": 190,
    "Spa PEDI": 210,
    "Detoxifying SPA Pedi": 260,
    "Foot SPA": 280,
    "Foot SPA w/ Pedi": 440,
    "Foot SPA w/ Pedi & Mani": 590,
    "Hand SPA": 220,
    "Hand SPA w/ Mani": 380,
    "Total-Self Indulgence": 850,
    "Gel Mani": 450,
    "Gel Pedi": 470,
    "Gel Polish Removal (No Gel After)": 70,
    "Gel Polish Removal (Apply Gel After)": 20,
    "Nail Art (Gel Polish section)": 200,
    "French Tip (Gel Polish section)": 100,
    "Soft Gel Extensions - Short Length": 1220,
    "Soft Gel Extensions - Medium Length": 1320,
    "Soft Gel Extensions - Long Length": 1420,
    "Retouch per Nail": 320,
    "Soft Gel Removal": 220,
    "Add-on - Change Polish": 70,
    "Add-on - Nail Art": 100,
    "Add-on - Nail Studs (per 10 pieces)": 15,
    "Add-on - French Tip": 30,
    "Acrylic Nails Removal": 220,
    "Kiddie MANI": 80,
    "Kiddie PEDI": 110,
    "Kiddie Nail Art": 80,
    "Kiddie FOOT SPA": 210,

    # BODY MASSAGE AND SPA SERVICES
    "Swedish Body Massage": 430,
    "Combination Massage": 580,
    "Hot Stone Massage": 590,
    "Ventosa w/ Massage": 590,
    "Deluxe Body Scrub": 470,
    "Ultimate Body Indulgence": 800,
    "Back & Head Massage": 320,
    "Hand Massage": 250,
    "Foot Massage": 270,
    "Hand & Foot Massage": 350,
    "Head & Shoulder Massage": 270,
    "Electric Bootie Foot Treatment": 250,
    "Electric Mitten Hand Treatment": 220,
    "Ear Candling w/ Head Massage": 340,
}


def manage_price_list(price_list, action, service_name=None, price=None):
    """Add, update, or delete a service price."""
    if action == "add":
        if service_name and price is not None:
            price_list[service_name] = price
            return True

    elif action == "update":
        if service_name in price_list and price is not None:
            price_list[service_name] = price
            return True

    elif action == "delete":
        if service_name in price_list:
            del price_list[service_name]
            return True

    return False


def get_service_price(price_list, service_name):
    """Return a service price, or 0 if the service is not found."""
    return price_list.get(service_name, 0)


def apply_variable_pricing(base_price, multiplier):
    """Calculate a price using a multiplier."""
    return base_price * multiplier


def get_price_by_category(price_list, category):
    """Return the price list; categories are not stored separately."""
    return price_list


def display_price_list(price_list):
    """Display services and prices alphabetically."""
    print("\n" + "=" * 50)
    print("MODISH NAILS and HAIR SALON - PRICE LIST")
    print("=" * 50)

    for service, price in sorted(price_list.items()):
        print(f"{service:<55} PHP {price:>8.2f}")

    print("=" * 50)


def calculate_package_price(price_list, services_list):
    """Calculate the total base price of multiple services."""
    return sum(
        get_service_price(price_list, service)
        for service in services_list
    )


def apply_package_discount(total_price, discount_percentage=0.10):
    """Return the original price, discount, and final package price."""
    discount_amount = total_price * discount_percentage

    return {
        "original": total_price,
        "discount": discount_amount,
        "final": total_price - discount_amount,
    }

