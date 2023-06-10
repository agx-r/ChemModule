from chemmodule import ChemModule

chem = ChemModule()

print("Chemistry Calculation Module")
print("============================")

while True:
	print("\nAvailable options:")
	print("1. Calculate molar mass")
	print("2. Calculate molarity")
	print("3. Calculate concentration")
	print("4. Calculate volume")
	print("5. Calculate number of particles")
	print("6. Calculate boiling point elevation")
	print("7. Calculate freezing point depression")
	print("8. Calculate pH")
	print("9. Calculate hydrogen concentration")
	print("0. Exit")

	choice = input("Enter your choice (0-9): ")

	if choice == "0":
		print("Exiting...")
		break

	elif choice == "1":
		formula = input("Enter the chemical formula: ")
		molar_mass = chem.calculate_molar_mass(formula)
		print(f"The molar mass of {formula} is: {molar_mass:.2f} g/mol")

	elif choice == "2":
		concentration = float(input("Enter the concentration in mol/L: "))
		volume = float(input("Enter the volume in L: "))
		molarity = chem.calculate_molarity(concentration, volume)
		print(f"The molarity is: {molarity:.2f} mol/L")

	elif choice == "3":
		molarity = float(input("Enter the molarity in mol/L: "))
		volume = float(input("Enter the volume in L: "))
		concentration = chem.calculate_concentration(molarity, volume)
		print(f"The concentration is: {concentration:.2f} mol/L")

	elif choice == "4":
		concentration = float(input("Enter the concentration in mol/L: "))
		molarity = float(input("Enter the molarity in mol/L: "))
		volume = chem.calculate_volume(concentration, molarity)
		print(f"The volume is: {volume:.2f} L")

	elif choice == "5":
		moles = float(input("Enter the number of moles: "))
		particles = chem.calculate_number_of_particles(moles)
		print(f"The number of particles is: {particles:.2e}")

	elif choice == "6":
		molality = float(input("Enter the molality in mol/kg: "))
		constant = float(input("Enter the constant value: "))
		elevation = chem.calculate_boiling_point_elevation(molality, constant)
		print(f"The boiling point elevation is: {elevation:.2f} °C")

	elif choice == "7":
		molality = float(input("Enter the molality in mol/kg: "))
		constant = float(input("Enter the constant value: "))
		depression = chem.calculate_freezing_point_depression(molality, constant)
		print(f"The freezing point depression is: {depression:.2f} °C")

	elif choice == "8":
		hydrogen_concentration = float(input("Enter the hydrogen concentration in mol/L: "))
		pH = chem.calculate_pH(hydrogen_concentration)
		print(f"The pH is: {pH:.2f}")

	elif choice == "9":
		pH = float(input("Enter the pH: "))
		hydrogen_concentration = chem.calculate_hydrogen_concentration(pH)
		print(f"The hydrogen concentration is: {hydrogen_concentration:.2e} mol/L")

	else:
		print("Invalid choice. Please try again.")
