import pandas as pd
import random
import numpy as np

# Set seed for reproducibility
random.seed(42)
np.random.seed(42)

# Sample values
airlines = ['AA', 'DL', 'UA', 'WN', 'SW', 'AS']
airports = ['ATL', 'LAX', 'ORD', 'DFW', 'DEN', 'SFO', 'SEA', 'JFK']


def generate_flight_data(num_rows=5000):
    data = []

    for _ in range(num_rows):
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        day_of_week = random.randint(1, 7)
        airline = random.choice(airlines)
        origin = random.choice(airports)
        dest = random.choice([a for a in airports if a != origin])
        scheduled_dep = random.randint(0, 2359)

        # Delay reasons
        weather_delay = random.randint(0, 60) if random.random() < 0.1 else 0
        late_aircraft_delay = random.randint(0, 90) if random.random() < 0.15 else 0
        carrier_delay = random.randint(0, 45) if random.random() < 0.2 else 0

        departure_delay = weather_delay + late_aircraft_delay + carrier_delay + random.randint(-5, 10)
        departure_delay = max(departure_delay, 0)

        delayed = 1 if departure_delay > 15 else 0

        data.append({
            'MONTH': month,
            'DAY': day,
            'DAY_OF_WEEK': day_of_week,
            'AIRLINE': airline,
            'ORIGIN_AIRPORT': origin,
            'DESTINATION_AIRPORT': dest,
            'SCHEDULED_DEPARTURE': scheduled_dep,
            'DEPARTURE_DELAY': departure_delay,
            'WEATHER_DELAY': weather_delay,
            'LATE_AIRCRAFT_DELAY': late_aircraft_delay,
            'CARRIER_DELAY': carrier_delay,
            'DELAYED': delayed
        })

    return pd.DataFrame(data)


# Generate and save
df = generate_flight_data(5000)
df.to_csv('flight_data.csv', index=False)
print("✅ Dataset 'flight_data.csv' generated with", len(df), "records.")
