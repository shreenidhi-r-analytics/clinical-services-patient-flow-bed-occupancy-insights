import pandas as pd

# =========================================

excel_file = pd.ExcelFile(
    r"C:\Users\Shreenidhi Rajasekar\Downloads\Hospital_Dataset_All6.xlsx"
)


# =========================================

patients = pd.read_excel(
    excel_file,
    sheet_name='patients'
)

doctors = pd.read_excel(
    excel_file,
    sheet_name='doctors'
)

appointments = pd.read_excel(
    excel_file,
    sheet_name='appointments'
)

treatments = pd.read_excel(
    excel_file,
    sheet_name='treatments'
)

billing = pd.read_excel(
    excel_file,
    sheet_name='billing'
)

bed_occupancy = pd.read_excel(
    excel_file,
    sheet_name='bed_occupancy'
)


# =========================================

print("\nPATIENTS DATA INFO\n")
print(patients.info())

print("\nDOCTORS DATA INFO\n")
print(doctors.info())

print("\nAPPOINTMENTS DATA INFO\n")
print(appointments.info())

print("\nTREATMENTS DATA INFO\n")
print(treatments.info())

print("\nBILLING DATA INFO\n")
print(billing.info())

print("\nBED OCCUPANCY DATA INFO\n")
print(bed_occupancy.info())


# =========================================

print("\nNULL VALUES - PATIENTS\n")
print(patients.isnull().sum())

print("\nNULL VALUES - DOCTORS\n")
print(doctors.isnull().sum())

print("\nNULL VALUES - APPOINTMENTS\n")
print(appointments.isnull().sum())

print("\nNULL VALUES - TREATMENTS\n")
print(treatments.isnull().sum())

print("\nNULL VALUES - BILLING\n")
print(billing.isnull().sum())

print("\nNULL VALUES - BED OCCUPANCY\n")
print(bed_occupancy.isnull().sum())


# =========================================

print("\nDUPLICATES - PATIENTS\n")
print(patients.duplicated().sum())

print("\nDUPLICATES - DOCTORS\n")
print(doctors.duplicated().sum())

print("\nDUPLICATES - APPOINTMENTS\n")
print(appointments.duplicated().sum())

print("\nDUPLICATES - TREATMENTS\n")
print(treatments.duplicated().sum())

print("\nDUPLICATES - BILLING\n")
print(billing.duplicated().sum())

print("\nDUPLICATES - BED OCCUPANCY\n")
print(bed_occupancy.duplicated().sum())


# =========================================

patients.drop_duplicates(inplace=True)

doctors.drop_duplicates(inplace=True)

appointments.drop_duplicates(inplace=True)

treatments.drop_duplicates(inplace=True)

billing.drop_duplicates(inplace=True)

bed_occupancy.drop_duplicates(inplace=True)

# =========================================

patients['date_of_birth'] = pd.to_datetime(
    patients['date_of_birth']
)

patients['registration_date'] = pd.to_datetime(
    patients['registration_date']
)

appointments['appointment_date'] = pd.to_datetime(
    appointments['appointment_date']
)

treatments['treatment_date'] = pd.to_datetime(
    treatments['treatment_date']
)

billing['bill_date'] = pd.to_datetime(
    billing['bill_date']
)

bed_occupancy['admission_date'] = pd.to_datetime(
    bed_occupancy['admission_date']
)

bed_occupancy['discharge_date'] = pd.to_datetime(
    bed_occupancy['discharge_date']
)

# =========================================

patients['Age'] = (
    pd.Timestamp.now().year -
    patients['date_of_birth'].dt.year
)

# =========================================

def age_group(age):

    if age < 18:
        return 'Child'

    elif age < 40:
        return 'Adult'

    elif age < 60:
        return 'Middle Age'

    else:
        return 'Senior'


patients['Age_Group'] = (
    patients['Age'].apply(age_group)
)

# =========================================

doctors['Doctor_Name'] = (
    doctors['first_name'] + ' ' +
    doctors['last_name']
)

# =========================================

patients.to_csv(
    r"C:\Users\Shreenidhi Rajasekar\Downloads\cleaned_patients.csv",
    index=False
)

doctors.to_csv(
    r"C:\Users\Shreenidhi Rajasekar\Downloads\cleaned_doctors.csv",
    index=False
)

appointments.to_csv(
    r"C:\Users\Shreenidhi Rajasekar\Downloads\cleaned_appointments.csv",
    index=False
)

treatments.to_csv(
    r"C:\Users\Shreenidhi Rajasekar\Downloads\cleaned_treatments.csv",
    index=False
)

billing.to_csv(
    r"C:\Users\Shreenidhi Rajasekar\Downloads\cleaned_billing.csv",
    index=False
)

bed_occupancy.to_csv(
    r"C:\Users\Shreenidhi Rajasekar\Downloads\cleaned_bed_occupancy.csv",
    index=False
)


# =========================================
# FINAL MESSAGE
# =========================================

print("\n===================================")
print("DATA CLEANING COMPLETED SUCCESSFULLY")
print("CLEANED CSV FILES GENERATED")
print("READY FOR POWER BI")
print("===================================")
