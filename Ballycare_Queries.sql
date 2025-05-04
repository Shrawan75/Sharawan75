SQL Use Case Scenarios for BallyCare Dataset


1. Count of Active Clients

SELECT COUNT(*) AS Active_Clients
FROM ballycare_data
WHERE CarePlanStatus = 'Active';

👉 Shows how many clients currently have active care plans.

2. Clients by Service Type

SELECT ServiceType, COUNT(*) AS Total_Clients
FROM ballycare_data
GROUP BY ServiceType;

👉 Helps analyze the distribution of clients across Residential Care, Home Care, and Wellness Programs.

3. Clients with Low Wellness Scores (< 2.5)

SELECT FirstName, LastName, Age, ServiceType, WellnessScore
FROM ballycare_data
WHERE WellnessScore < 2.5
ORDER BY WellnessScore ASC;

👉 Identifies clients who may need urgent wellness support.

4. Average Wellness Score by State

SELECT State, ROUND(AVG(WellnessScore), 2) AS Avg_Wellness
FROM ballycare_data
GROUP BY State;

👉 Used for regional performance and wellness benchmarking.


5. Average Age by Service Type

SELECT ServiceType, ROUND(AVG(Age), 1) AS Avg_Age
FROM ballycare_data
GROUP BY ServiceType;

👉 Helps determine which services are used by older or younger aged clients.
