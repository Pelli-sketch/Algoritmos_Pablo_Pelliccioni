arepa_recipe = {'masa_arepas': (1, 'kg', 'de masa para arepas (harina)'),
			   'agua': (1, 'tza', 'agua potable'),
			   'sal': (2, 'cditas', 'sal'),
               'aceite': (2, 'cdas', 'de aceite vegetal')}
			   
def print_recipe(arepa_recipe):
   print("Receta de Arepa Venezolana:")
   for ingredient, (quantity, unit, description) in arepa_recipe.items():
       print(f"- {quantity} {unit} {description}")
	   
def customize_recipe(arepa_recipe):
   custom_recipe = {}
   print("\nPersonaliza tu receta de arepa venezolana:")
   for ingredient, (quantity, unit, description) in arepa_recipe.items():
       print(f"Cantidad actual de {description}: {quantity} {unit}")
       user_input = input(f"Ingresa una cantidad personalizada de {ingredient} ({quantity} {unit} por defecto): ")
       if user_input:
           try:
               custom_quantity = float(user_input)
               custom_recipe[ingredient] = (custom_quantity, quantity, unit, description)
           except ValueError:
               print(f"Error: '{user_input}' no es un número válido.")
       else:
           custom_recipe[ingredient] = (quantity, quantity, unit, description)
   return custom_recipe
   
print_recipe(arepa_recipe)
customized_recipe = customize_recipe(arepa_recipe)
print("\nTu receta de arepa venezolana personalizada:")
print_recipe(customized_recipe)
