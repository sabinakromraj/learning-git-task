print("Lista zakupów:")
shopping_dict = {
    'piekarnia': ['chleb', 'pączek', 'bułki'],
    'warzywniak': ['marchew', 'seler', 'rukola', 'ogórek', 'pomidor', 'papryka']
}
upper_shopping_dict = {key.upper(): [value.upper() for value in values] for key, values in shopping_dict.items()}

value_count = 0
shop_count = 0
for key, value in upper_shopping_dict.items():
    print(f"Idę do {key}, kupuję tu następujące rzeczy: {value}")
    value_count += len(value)
    shop_count += 1
    
print(f"W sumie kupuję {value_count} produktów w {shop_count} sklepach.")