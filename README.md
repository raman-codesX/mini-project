# Air Quality Data Analysis (India)

This project analyzes city-wise air pollution data in India using Python.
The goal is to clean the data, handle outliers, and visualize pollution trends
to identify the most polluted cities and yearly AQI patterns.

---

## Tools & Libraries Used
- Python
- Pandas
- NumPy
- Matplotlib

---

## Dataset
- City-wise daily air quality data
- Columns include AQI, PM2.5, PM10, and various gaseous pollutants
- Dataset is stored in the `data/` folder

---

## Data Cleaning Steps
- Missing numerical values filled using median
- AQI bucket filled using mode
- Outliers handled using IQR (Interquartile Range) method
- Date column converted to Year for time-based analysis

---

## Analysis Performed
1. Top 10 Most Polluted Cities (based on average AQI)
2. Year-wise AQI Trend Analysis
3. City-wise AQI Heatmap (City vs Year)

---

## Visualizations
- Bar chart for top 10 polluted cities
- Line chart for year-wise AQI trends
- Heatmap to compare AQI levels across cities and years

---

## Key Insights
- Certain cities consistently show higher AQI levels
- AQI levels vary significantly across years
- Heatmap clearly highlights long-term pollution patterns

---

## How to Run
1. Clone the repository
2. Install required libraries
3. Run the analysis script

```bash
pip install -r requirements.txt
python analysis.py
