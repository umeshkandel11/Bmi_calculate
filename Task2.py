import csv

def calculate_bmi():
    with open('bmi_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Height (cm)", "Weight (kg)", "BMI", "Category"])

        while True:
            name = input("Enter your name: ")
            try:
                height_cm = float(input("Enter height in cm: "))
                weight_kg = float(input("Enter weight in kg: "))
                
                # Calculate BMI
                height_m = height_cm / 100
                bmi = weight_kg / (height_m ** 2)

                # Determine BMI category
                if bmi < 18.5:
                    category = "Underweight"
                elif 18.5 <= bmi < 24.9:
                    category = "Normal weight"
                elif 25 <= bmi < 29.9:
                    category = "Overweight"
                else:
                    category = "Obese"

                # Save data to the file
                writer.writerow([name, height_cm, weight_kg, round(bmi, 2), category])
                print(f"{name}'s BMI is {round(bmi, 2)} ({category})")

                repeat = input("Calculate another BMI? (yes/no): ").strip().lower()
                if repeat != 'yes':
                    print("BMI calculations complete.")
                    break
            except ValueError:
                print("Please enter a valid number for height and weight.\n")

calculate_bmi()
