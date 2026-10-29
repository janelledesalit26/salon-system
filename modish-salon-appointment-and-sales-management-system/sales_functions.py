"""
SALES FUNCTIONS
"""

def log_service(transactions_list, transaction_data):

    transactions_list.append(transaction_data)
    return True

def apply_discount(amount, discount_rate):

    discount_amount = amount * discount_rate
    final_amount = amount - discount_amount
    return final_amount

def compute_total(services_with_prices, senior_discount=False):

    subtotal = sum([price for _, price in services_with_prices])
    
    if senior_discount:
        discount = subtotal * 0.20  # 20% senior discount
    else:
        discount = 0
    
    total = subtotal - discount
    
    return {
        "subtotal": subtotal,
        "discount": discount,
        "total": total
    }

def get_daily_sales(transactions_list):

    if not transactions_list:
        return {
            "total_sales": 0,
            "total_transactions": 0,
            "total_discounts": 0,
            "average_transaction": 0
        }
    
    total_sales = sum([trans['total'] for trans in transactions_list])
    num_transactions = len(transactions_list)
    
    return {
        "total_sales": total_sales,
        "total_transactions": num_transactions,
        "average_transaction": total_sales / num_transactions
    }

def get_sales_by_staff(transactions_list, staff_name):

    staff_sales = 0
    count = 0
    
    for trans in transactions_list:
        if trans.get('staff', '').lower() == staff_name.lower():
            staff_sales += trans['total']
            count += 1
    
    return {
        "staff": staff_name,
        "total_sales": staff_sales,
        "transaction_count": count
    }

def calculate_commission(sales_amount, commission_rate=0.10):

    return sales_amount * commission_rate

