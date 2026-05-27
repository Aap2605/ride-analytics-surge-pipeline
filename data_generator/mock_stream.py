import pandas as pd
import numpy as np
import uuid
from datetime import datetime, timedelta

def generate_live_ride_batch(batch_size=1000):

    locations = [
        'Mumbai_Andheri',
        'Mumbai_Bandra',
        'Mumbai_Colaba',
        'Mumbai_Thane'
    ]

    status_options = [
        'COMPLETED',
        'CANCELLED',
        'NO_DRIVER_AVAILABLE'
    ]

    data = {
        'ride_id': [str(uuid.uuid4())[:8] for _ in range(batch_size)],

        'timestamp': [
            datetime.now() - timedelta(seconds=np.random.randint(0, 3600))
            for _ in range(batch_size)
        ],

        'pickup_location': np.random.choice(locations, batch_size),

        'fare_amount': np.random.uniform(100.0, 1500.0, batch_size).round(2),

        'driver_rating': np.random.choice(
            [1, 2, 3, 4, 5, np.nan],
            batch_size,
            p=[0.05, 0.05, 0.1, 0.3, 0.4, 0.1]
        ),

        'ride_status': np.random.choice(
            status_options,
            batch_size,
            p=[0.7, 0.2, 0.1]
        )
    }

    df = pd.DataFrame(data)

    df.iloc[np.random.randint(0, batch_size, 20), 3] = -50.0

    df.to_csv('pipeline/raw_stream_data.csv', index=False)
    print("Ride data saved successfully!")
    print(df.head())

if __name__ == "__main__":
    generate_live_ride_batch()