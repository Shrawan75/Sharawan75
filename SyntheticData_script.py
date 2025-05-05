import pandas as pd
from faker import Faker
import random
from datetime import datetime

fake = Faker('en_AU')  # Australian locale

def generate_client_data(num_records):
    data = []
    for _ in range(num_records):
        first_name = fake.first_name()
        last_name = fake.last_name()
        gender = random.choice(['Male', 'Female', 'Other'])
        dob = fake.date_of_birth(minimum_age=65, maximum_age=95)
        age = (datetime.now().date() - dob).days // 365
        address = fake.street_address()
        city = fake.city()
        state = fake.state()
        postcode = fake.postcode()
        phone = fake.phone_number()
        email = fake.email()
        admission_date = fake.date_between(start_date='-5y', end_date='today')
        service_type = random.choice(['Residential Care', 'Home Care', 'Wellness Program'])
        care_plan_status = random.choice(['Active', 'Inactive', 'Completed'])
        last_assessment = fake.date_between(start_date=admission_date, end_date='today')
        wellness_score = round(random.uniform(1.0, 5.0), 2)
        primary_carer = fake.name()
        notes = fake.sentence(nb_words=6)
        
        data.append({
            'ClientID': fake.uuid4(),
            'FirstName': first_name,
            'LastName': last_name,
            'Gender': gender,
            'DateOfBirth': dob,
            'Age': age,
            'Address': address,
            'City': city,
            'State': state,
            'Postcode': postcode,
            'PhoneNumber': phone,
            'Email': email,
            'AdmissionDate': admission_date,
            'ServiceType': service_type,
            'CarePlanStatus': care_plan_status,
            'LastAssessmentDate': last_assessment,
            'WellnessScore': wellness_score,
            'PrimaryCarer': primary_carer,
            'Notes': notes
        })
    return pd.DataFrame(data)

# Generate 500 records
df = generate_client_data(10000)

# Save to CSV
df.to_csv('ballycare_sample_data.csv', index=False)
