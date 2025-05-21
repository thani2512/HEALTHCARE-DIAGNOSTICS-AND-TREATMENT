Source code for phase 4

# Simulated login database
users = {
    "admin": "admin123",
    "doctor1": "healthcare2024"
}

# Login Function
def login():
    print("=== Healthcare Login ===")
    username = input("Username: ")
    password = input("Password: ")
   
    if username in users and users[username] == password:
        print("✅ Login successful!\n")
        return True
    else:
        print("❌ Invalid username or password.")
        return False

# Collect patient details
def get_patient_data():
    print("=== Patient Data Entry ===")
    name = input("Patient Name: ")
    age = input("Age: ")
    gender = input("Gender (M/F/O): ")
    disease = input("Type of Disease: ")
    heart_disease = input("Type of Heart Disease (if any): ")
    symptoms = input("Symptoms (comma-separated): ")
    bp = input("Blood Pressure (e.g. 120/80): ")
    cholesterol = input("Cholesterol (mg/dL): ")
   
    patient_info = {
        "Name": name,
        "Age": age,
        "Gender": gender,
        "Disease Type": disease,
        "Heart Disease Type": heart_disease,
        "Symptoms": symptoms.split(","),
        "Blood Pressure": bp,
        "Cholesterol": cholesterol
    }
    return patient_info

# Display patient data
def display_patient_info(data):
    print("\n=== Patient Record ===")
    for key, value in data.items():
        if isinstance(value, list):
            print(f"{key}: {', '.join([v.strip() for v in value])}")
        else:
            print(f"{key}: {value}")

# Main program
def main():
    if login():
        patient = get_patient_data()
        display_patient_info(patient)

if __name__ == "__main__":
    main()
