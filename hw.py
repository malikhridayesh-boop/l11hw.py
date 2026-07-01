def calculate_due_amount(total_bill,amount_paid):
    due_amount = total_bill - amount_paid
    print(f"Total bill: {total_bill} ")
    print(f"Amount paid: {amount_paid}")
    if due_amount > 0:
        print(f"Due amount: {due_amount}")
    elif due_amount < 0:
        credit = abs(due_amount)
        print(f"Change to be returned: {credit}")
    else:
        print("No due amount. Payment is complete.")
    return due_amount
calculate_due_amount(total_bill = 150.00, amount_paid = 100.00)
