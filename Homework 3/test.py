#Ryan Nguyen PSID: 1805277

#Making the class
class FoodItem:
    def __init__(self, name = "None", fat = 0.0, carbs = 0.0, protein = 0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

#Making a function to calculate the calories
    def get_calories(self, num_servings):
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protien * 4)) * num_servings;
        return calories