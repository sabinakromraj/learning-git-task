print("Lista zakupów:")
shopping_dict = {
    'piekarnia': ['chleb', 'pączek', 'bułki'],
    'warzywniak': ['marchew', 'seler', 'rukola']
}
capi_shopping_dict = {key.capitalize(): [value.capitalize() for value in values] for key, values in shopping_dict.items()}