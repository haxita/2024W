pizzas = {
    'margarita': 10,
    'provenzale': 12,
    'rusticana': 17,
    'funghi': 16,
    'cipolla': 13
}

available_extras = ['egg', 'cheese', 'salami', 'pepperoni', 'garlic', 'ham']

print("Hello at the JKU Pizza Service!")
print("Please select your pizza:")
for pizza in pizzas:
    print(f"Pizza {pizza}: {pizzas[pizza]} Euros")

while True:
    print("Enter name of pizza: ", end='')
    selected_pizza = input()
    if selected_pizza in pizzas:
        print(f"You have selected pizza {selected_pizza} for {pizzas[selected_pizza]} Euros.")
        break
    else:
        print("Pizza not available, please try again.")

print("Which extras would you like? Please enter them separated by a ';'.")
for extra in available_extras:
    print(extra)
extras_input = input()

available_selected = []
unavailable_selected = []

if extras_input.strip() == '':
    print("No extras selected.")
    total_price = float(pizzas[selected_pizza])
else:
    requested_extras = [extra.strip() for extra in extras_input.split(';') if extra.strip() != '']
    for extra in requested_extras:
        if extra in available_extras:
            available_selected.append(extra)
        else:
            unavailable_selected.append(extra)

    total_price = float(pizzas[selected_pizza]) + 1.5 * len(available_selected)

    if len(unavailable_selected) == 0:
        print("All extras available and added.")
    else:
        print("Extras not available: " + ", ".join(unavailable_selected))
        print("Extras available and added: " + ", ".join(available_selected))

print(f"Your total price is now {total_price:.1f} Euros.")
print("Thank you for your order!")