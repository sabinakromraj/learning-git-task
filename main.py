print("Lista zakupów:")
shopping_dict = {
    'piekarnia': ['chleb', 'pączek', 'bułki'],
    'warzywniak': ['marchew', 'seler', 'rukola']
}
capi_shopping_dict = {key.capitalize(): [value.capitalize() for value in values] for key, values in shopping_dict.items()}

value_count = 0

for key, value in capi_shopping_dict.items():
    print(f"Idę do {key}, kupuję tu następujące rzeczy: {value}")
    value_count += len(value)
    
print(f"W sumie kupuję {value_count} produktów.")