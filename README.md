🌍 Air Quality Health Advisory
📌 Project Description
The Air Quality Health Advisory is a Streamlit-based web application that monitors air quality using PM2.5 concentration and calculates the Air Quality Index (AQI). It provides real-time health recommendations based on AQI levels and allows users to explore air quality datasets through interactive tables and charts.
---
🚀 Features
Real-time AQI calculator using PM2.5 values
U.S. EPA 2024 AQI calculation
Health advisory based on AQI category
Interactive PM2.5 slider
Upload CSV or JSON datasets
Color-coded AQI table
Comparative AQI bar chart
Default sample dataset for quick testing
---
🛠️ Technologies Used
Python 3
Streamlit
Pandas
Matplotlib
---
📁 Project Structure
```text
Air Quality Advisor/
│── app.py
│── README.md
```
---
▶️ Installation
Clone the repository:
```bash
git clone <repository-url>
```
Navigate to the project folder:
```bash
cd "Air Quality Advisor"
```
Install the required packages:
```bash
pip install streamlit pandas matplotlib
```
Run the application:
```bash
streamlit run app.py
```
---
📊 How to Use
Live AQI Calculator
Adjust the PM2.5 slider.
View the calculated AQI.
Read the corresponding health advisory.
Dataset Explorer
Upload a CSV or JSON file containing PM2.5 data.
If no file is uploaded, the app uses a default sample dataset.
View AQI values in a color-coded table.
Compare AQI values using a bar chart.
---
🌈 AQI Categories
AQI Range	Category	Health Advisory
0–50	Good	Air quality is satisfactory.
51–100	Moderate	Acceptable for most people.
101–150	Unhealthy for Sensitive Groups	Sensitive individuals should limit outdoor activities.
151–200	Unhealthy	Everyone should reduce prolonged outdoor exposure.
201–300	Very Unhealthy	Health alert; avoid outdoor activities.
301+	Hazardous	Emergency conditions; remain indoors if possible.
---
✅ Future Enhancements
Live AQI data using public APIs
Weather integration
Location-based AQI monitoring
Email and SMS alerts
AQI prediction using Machine Learning
