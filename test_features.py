import sys
if sys.platform == "win32":
    try: sys.stdout.reconfigure(encoding="utf-8")
    except: pass

import asyncio
from backend.app.routers.centers import compare_mandi_prices
from backend.app.routers.earnings import get_farmer_earnings

def test():
    print("=== Testing Mandi Price & Distance Comparison ===")
    res = compare_mandi_prices('Wheat (गेहूं)', 50.0, 'price')
    print("Crop:", res['crop'], "Base MSP:", res['base_msp_rate'])
    for m in res['mandis']:
        print(f"- {m['center_name']} | Type: {m['mandi_type']} | Rate: Rs {m['buying_price_per_qtl']}/Qtl (Delta: +Rs {m['price_delta_per_qtl']}) | Total Payout: Rs {m['total_net_payout_inr']} (+Rs {m['profit_delta_inr']}) | Dist: {m['distance_km']} km ({m['travel_time_mins']} mins)")

    print("\n=== Testing Farmer Earnings & Sales Passbook ===")
    earnings = asyncio.run(get_farmer_earnings())
    print("Farmer Name:", earnings['farmer_name'])
    print("Lifetime Earnings:", "Rs", earnings['lifetime_earnings_inr'])
    print("Total Qty Sold:", earnings['total_quantity_sold_qtl'], "Quintals")
    print("Private Mandi Bonus Earned:", "Rs", earnings['bonus_earned_over_msp'])
    print("Total Sales Count:", earnings['total_sales_count'])
    print("Sample Transactions:")
    for t in earnings['transactions'][:4]:
        print(f"  * Token: {t['id']} | Center: {t['center_name']} ({t.get('mandi_type')}) | Crop: {t['crop_name']} | Amount: Rs {t.get('total_amount_inr')} | Status: {t['stage']}")

if __name__ == "__main__":
    test()
