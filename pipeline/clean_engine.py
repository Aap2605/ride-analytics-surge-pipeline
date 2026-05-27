import pandas as pd

def run_cleaning_pipeline(input_path, output_path):

    df = pd.read_csv(input_path)

    # Remove negative fare values
    df = df[df['fare_amount'] > 0]

    # Fill missing ratings with median
    median_rating = df['driver_rating'].median()
    df['driver_rating'] = df['driver_rating'].fillna(median_rating)

    # Convert timestamp column
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Extract hour
    df['hour_of_day'] = df['timestamp'].dt.hour

    # Save cleaned data
    df.to_csv(output_path, index=False)

    print("Cleaned data saved successfully!")
    print(df.head())

if __name__ == "__main__":

    run_cleaning_pipeline(
        'pipeline/raw_stream_data.csv',
        'pipeline/production_ride_data.csv'
    )