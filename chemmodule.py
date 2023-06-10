import numpy as np
from scipy.constants import Avogadro

class ChemModule:
	def __init__(self, temperature=298.15):
		self.temperature = temperature

	def calculate_molar_mass(self, formula):
		elements = parse_formula(formula)
		molar_mass = 0.0
		for element, count in elements.items():
			molar_mass += get_atomic_mass(element) * count
		return molar_mass

	def calculate_molarity(self, concentration, volume):
		return concentration / volume

	def calculate_concentration(self, molarity, volume):
		return molarity * volume

	def calculate_volume(self, concentration, molarity):
		return concentration / molarity

	def calculate_number_of_particles(self, moles):
		return moles * Avogadro

	def calculate_boiling_point_elevation(self, molality, constant):
		return molality * constant

	def calculate_freezing_point_depression(self, molality, constant):
		return molality * constant

	def calculate_pH(self, hydrogen_concentration):
		return -np.log10(hydrogen_concentration)

	def calculate_hydrogen_concentration(self, pH):
		return 10 ** (-pH)

	# Helper functions

	def parse_formula(self, formula):
		elements = {}
		element = ""
		count = ""
		for char in formula:
			if char.isalpha():
				if element != "":
					if count == "":
						count = 1
					elements[element] = int(count)
					count = ""
				element = char
			elif char.isdigit():
				count += char
		if count != "":
			elements[element] = int(count)
		return elements