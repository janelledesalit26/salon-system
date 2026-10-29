"""
STAFF MANAGEMENT
"""

import random

def assign_staff(staff_list):

    if not staff_list:
        return "Unassigned"
    
    return random.choice(staff_list)

def get_staff_list(staff_list):

    return staff_list

def add_staff_member(staff_list, name):

    if name not in staff_list:
        staff_list.append(name)
        return True
    return False

def remove_staff_member(staff_list, name):

    if name in staff_list:
        staff_list.remove(name)
        return True
    return False

def get_staff_workload(transactions_list, staff_name):

    if not staff_list:
        return "Unassigned"
    
    # Count transactions per staff
    workload = {}
    for staff in staff_list:
        workload[staff] = get_staff_workload(transactions_list, staff)
    
    # Return staff with minimum workload
    return min(workload, key=workload.get)

def display_staff_list(staff_list):

    print("\n" + "="*30)
    print("STAFF MEMBERS")
    print("="*30)
    
    for i, staff in enumerate(staff_list, 1):
        print(f"{i}. {staff}")
    
    print("="*30)

def get_staff_statistics(staff_list, transactions_list):

    stats = {}
    
    for staff in staff_list:
        workload = get_staff_workload(transactions_list, staff)
        total_sales = sum([trans['total'] for trans in transactions_list 
                          if trans.get('staff', '').lower() == staff.lower()])
        
        stats[staff] = {
            "transactions": workload,
            "total_sales": total_sales,
            "average_per_transaction": total_sales / workload if workload > 0 else 0
        }
    
    return stats

def promote_staff(staff_list, name):

    if name in staff_list:
        # In real system, this would update a database
        print(f"{name} has been promoted!")
        return True
    return False

