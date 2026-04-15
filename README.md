🚦 AI SafeRoute X
Smart Mobility Intelligence System
📌 Chosen Vertical

Urban Mobility – Route Safety Optimization

This project focuses on improving urban commuting safety by recommending routes based not only on travel time but also on safety factors like crime risk, lighting, and traffic conditions.

🧠 Approach & Logic

Traditional navigation systems prioritize fastest routes, but they ignore safety, especially during night travel.

Our approach introduces an AI-based scoring model that evaluates each route using:

🚨 Crime rate (risk factor)
💡 Lighting conditions
🚗 Traffic congestion
⏱ Travel time
🌙 Time of day (day/night)
🔢 Scoring Formula
Score = (2.5 × Safety) - (1.5 × Time) - (1.2 × Traffic)

Where:

Safety = (10 - Crime) + Lighting

👉 Additional penalty is applied for unsafe routes at night.

⚙️ How the Solution Works
1. User Input

The user enters:

Source location
Destination
Time of travel (Day/Night)
2. Backend Processing (Flask API)
Generates multiple route options (simulated or API-based)
Calculates a final AI score for each route
Generates smart advice based on score
Returns ranked routes (best → worst)
3. Frontend Interaction
Displays routes in a clean UI
Highlights the best route 🏆
Shows:
Travel time
Traffic level
Safety score
AI recommendation
4. Map Integration
Uses Google Maps API to:
Display map
Draw route between source and destination
5. Voice Assistant 🎤
Announces the best route recommendation
Enhances user experience and accessibility
🧩 Tech Stack
Backend
Python (Flask)
REST API
Frontend
HTML, CSS, JavaScript
APIs
Google Maps JavaScript API
Directions API
🚀 Features
✅ AI-powered route ranking
✅ Night-time safety adjustment
✅ Real-time map visualization
✅ Voice-based route recommendation
✅ Clean and responsive UI
✅ Fast response (< 2 seconds)
⚠️ Assumptions Made
Route data (crime, lighting, traffic) is simulated
Real-world data sources can be integrated in future:
Government crime datasets
Live traffic APIs
IoT-based lighting data
Google Maps API is used for visualization only
Internet connection is required for map functionality
🔮 Future Improvements
🔥 Real-time data integration (traffic + safety)
🤖 Machine Learning model trained on real datasets
📱 Mobile app version
🌐 Live deployment
📊 User feedback-based personalization
🎯 Problem Solved

Urban commuters often face:

Unsafe routes at night
Lack of safety awareness
Poor route decisions

👉 AI SafeRoute X solves this by combining safety + efficiency into one intelligent system.
