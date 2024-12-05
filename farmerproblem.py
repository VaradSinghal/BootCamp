
total_land = 80 
segments = 5
segment_land = total_land / segments 

crops = {
 "tomatoes": {"yield_per_acre_30": 10, "yield_per_acre_70": 12, "price_per_kg": 7},
 "potatoes": {"yield_per_acre": 10, "price_per_kg": 20},
 "cabbage": {"yield_per_acre": 14, "price_per_kg": 24},
 "sunflower": {"yield_per_acre": 0.7, "price_per_kg": 200},
 "sugarcane": {"yield_per_acre": 45, "price_per_ton": 4000},
}

total_sales = 0

yield_30 = crops["tomatoes"]["yield_per_acre_30"] * segment_land * 0.30 
yield_70 = crops["tomatoes"]["yield_per_acre_70"] * segment_land * 0.70 # 
total_yield_tomatoes = yield_30 + yield_70
total_sales += total_yield_tomatoes * 1000 * crops["tomatoes"]["price_per_kg"] 

total_yield_potatoes = crops["potatoes"]["yield_per_acre"] * segment_land
total_sales += total_yield_potatoes * 1000 * crops["potatoes"]["price_per_kg"]

total_yield_cabbage = crops["cabbage"]["yield_per_acre"] * segment_land
total_sales += total_yield_cabbage * 1000 * crops["cabbage"]["price_per_kg"]

total_yield_sunflower = crops["sunflower"]["yield_per_acre"] * segment_land
total_sales += total_yield_sunflower * 1000 * crops["sunflower"]["price_per_kg"]

total_yield_sugarcane = crops["sugarcane"]["yield_per_acre"] * segment_land
total_sales += total_yield_sugarcane * crops["sugarcane"]["price_per_ton"]

chemical_free_sales = 0

chemical_free_sales += total_yield_tomatoes * 1000 * crops["tomatoes"]["price_per_kg"]
chemical_free_sales += total_yield_potatoes * 1000 * crops["potatoes"]["price_per_kg"]
chemical_free_sales += total_yield_cabbage * 1000 * crops["cabbage"]["price_per_kg"]

chemical_free_sales += total_yield_sunflower * 1000 * crops["sunflower"]["price_per_kg"]

chemical_free_sales += total_yield_sugarcane * crops["sugarcane"]["price_per_ton"]

print(f"Overall sales achieved by Mahesh from 80 acres: Rs. {total_sales:,.2f}")
print(f"Sales realisation from chemical-free farming after 11 months: Rs. {chemical_free_sales:,.2f}")