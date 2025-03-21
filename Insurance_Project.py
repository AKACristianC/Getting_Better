# project: Codecademy Insurance Cost Project
age = 28
sex = 0
bmi = 26.2
num_of_children = 3
smoker = 0

# Add insurance estimate formula below
insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
print("This person's insurance cost is "  + str(insurance_cost) + "dollars.")
# Age Factor
age += 4
print(age)
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
print(new_insurance_cost)
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in cost of insurance after increasing the age by 4 years is " + str(change_in_insurance_cost) + "dollars.")

# BMI Factor
age = 28
bmi += 3.1
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
change_in_insurance_cost =  new_insurance_cost - insurance_cost 
print("The change in estimated insurance cost after increasing BMI by 3.1 is " 
+ str(change_in_insurance_cost) + " dollars.")
# Male vs. Female Factor
bmi = 26.2
sex = 1 
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
change_in_insurance_cost =  new_insurance_cost - insurance_cost 
print("The change in estimated cost for being male instead of female is " + str(change_in_insurance_cost) + "dollars.")

# Extra Practice

# Smoker Factor
smoker = 1
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in estimated cost for being a smoker is " + str(change_in_insurance_cost) + " dollars.")

# Number of Children Factor
smoker = 0
num_of_children += 1
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in estimated cost for having one more child is " + str(change_in_insurance_cost) + " dollars.")

# Second part of the extra practice

def analyze_smoker(smoker_status):
  if smoker_status == 1:
        print("To lower your cost, you should consider quitting smoking.")
  else:
        print("Smoking is not an issue for you.")
  
  print(smoker_status)
  


# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, num_of_children, smoker):
  estimated_cost = 400*age - 128*sex + 425*num_of_children + 10000*smoker - 2500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  analyze_smoker(smoker)
  return estimated_cost
 
# Estimate Keanu's insurance cost
keanu_insurance_cost = estimate_insurance_cost(name = 'Keanu', age = 29, sex = 1, num_of_children = 3, smoker = 1)

cristian_insurance_cost = estimate_insurance_cost(name='Cristian', age=28, sex=1, num_of_children=0, smoker=0)

# Python Lists: Medical Insurance Estimation Project


# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  return estimated_cost
 
# Estimate Maria's insurance cost
maria_insurance_cost = estimate_insurance_cost(name = "Maria", age = 31, sex = 0, bmi = 23.1, num_of_children = 1, smoker = 0)

# Estimate Rohan's insurance cost
rohan_insurance_cost = estimate_insurance_cost(name = 
"Rohan", age = 25, sex = 1, bmi = 28.5, num_of_children = 3, smoker = 0)

# Estimate Valentina's insurance cost
valentina_insurance_cost = estimate_insurance_cost(name = "Valentina", age = 53, sex = 0, bmi = 31.4, num_of_children = 0, smoker = 1)

# Add your code here
names = ["Maria", "Rohan", "Valentina"]

insurance_cost = [4150.0, 5320.0, 35210.0]

insurance_data = list(zip(names, insurance_cost ))

print(insurance_data)

estimated_insurance_data = []

estimated_insurance_data.extend(insurance_data)

print(estimated_insurance_data)

print("Here is the actual insurance cost data: " + str(insurance_data))
print("Here is the estimated insurance cost data: " + str(estimated_insurance_data))