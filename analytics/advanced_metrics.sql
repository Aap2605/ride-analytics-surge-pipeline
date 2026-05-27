CREATE TABLE production_rides (
    ride_id VARCHAR(50) PRIMARY KEY,
    timestamp TIMESTAMP,
    pickup_location VARCHAR(100),
    fare_amount DECIMAL(10,2),
    driver_rating DECIMAL(3,2),
    ride_status VARCHAR(30),
    hour_of_day INT
);
WITH HourlyLocationMetrics AS (

    SELECT
        pickup_location,
        hour_of_day,

        COUNT(ride_id) AS total_requests,

        COUNT(
            CASE
                WHEN ride_status = 'NO_DRIVER_AVAILABLE'
                THEN 1
            END
        ) AS unfulfilled_demand,

        AVG(fare_amount) AS avg_base_fare

    FROM production_rides

    GROUP BY
        pickup_location,
        hour_of_day
),

SurgePricingEngine AS (

    SELECT
        pickup_location,
        hour_of_day,
        total_requests,
        unfulfilled_demand,

        ROUND(
            (unfulfilled_demand::DECIMAL / total_requests),
            2
        ) AS demand_supply_gap,

        avg_base_fare,

        CASE

            WHEN
                (unfulfilled_demand::DECIMAL / total_requests) > 0.25
            THEN 'TRIGGER 2.0x SURGE'

            WHEN
                (unfulfilled_demand::DECIMAL / total_requests)
                BETWEEN 0.10 AND 0.25
            THEN 'TRIGGER 1.5x SURGE'

            ELSE 'STANDARD PRICING'

        END AS dynamic_pricing_tier

    FROM HourlyLocationMetrics
)

SELECT *
FROM SurgePricingEngine

WHERE dynamic_pricing_tier <> 'STANDARD PRICING'

ORDER BY demand_supply_gap DESC;