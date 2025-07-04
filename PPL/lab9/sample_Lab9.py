

# Global discount
global_discount = 0.1
event_discounts = {
    "Concert": 0.20,    
    "Sports": 0.15,     
    "Theatre": 0.25     
}
user_discounts = {
    "VIP": 0.15,       
    "Student": 0.10,    
    "General": 0.05     
}
def compute_final_price(base_price, event, role, global_discount_val=None, event_discounts_val=None, user_discounts_val=None):
    if global_discount_val is None:
        global_discount_val = global_discount
    if event_discounts_val is None:
        event_discounts_val = event_discounts
    if user_discounts_val is None:
        user_discounts_val = user_discounts
    g = global_discount_val
    e = event_discounts_val.get(event, 0)
    u = user_discounts_val.get(role, 0)
    price_after_global = base_price * (1 - g)
    price_after_event  = price_after_global * (1 - e)
    final_price        = price_after_event * (1 - u)
    desc = f"Global={g*100:.0f}%, Event={e*100:.0f}%, User={u*100:.0f}%"
    return final_price, desc

def test():
    tickets = [
        {"event": "Concert", "role": "VIP",     "base_price": 100},
        {"event": "Sports",  "role": "Student", "base_price":  80},
        {"event": "Theatre", "role": "General", "base_price": 120},
    ]
    for t in tickets:
        final, applied = compute_final_price(t["base_price"], t["event"], t["role"])
        print(f"Ticket: {t['role']} for {t['event']}, Price: ${t['base_price']:.2f}")
        print(f"Applied Discounts:{applied}")
        print(f"Final Price:${final:.2f}")

test()
#checkout(items)