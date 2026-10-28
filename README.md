# Medical Data Visualizer

A Python data analysis and visualization project developed as part of the freeCodeCamp *Data Analysis with Python* certification[cite: 9]. This program uses **Pandas**, **Seaborn**, and **Matplotlib** to explore the relationship between cardiac disease, body measurements, blood markers, and lifestyle choices[cite: 9, 10].

---

## Key Features & Operations

* **BMI & Overweight Calculation:** Calculates patient Body Mass Index (BMI) and adds an `overweight` feature based on whether the BMI exceeds 25[cite: 5, 6].
* **Data Normalization:** Normalizes cholesterol and glucose values such that `0` represents good health and `1` represents bad health[cite: 6].
* **Categorical Visualizations:** Generates a categorical split bar chart (`catplot`) comparing cardiac disease outcomes against lifestyle indicators like smoking, alcohol intake, physical activity, and cholesterol[cite: 5, 6].
* **Data Cleaning:** Filters out incorrect patient data segments based on blood pressure constraints and height/weight percentiles (dropping the lowest 2.5% and highest 2.5%)[cite: 5, 6].
* **Correlation Heatmap:** Computes the correlation matrix for the cleaned dataset and plots a masked heatmap using Seaborn to visualize feature relationships[cite: 5, 6].

---

## Tech Stack

* **Language:** Python
* **Data Analysis:** Pandas, NumPy
* **Data Visualization:** Seaborn, Matplotlib
* **Testing:** Unittest framework

---

## Project Structure

* `medical_data_visualizer.py`: Contains the core logic for data preprocessing, categorical plotting, and heatmap generation.
* `main.py`: Entry point script used to run the visualizations and unit tests.
* `test_module.py`: Official unit test suite validating the generated Matplotlib figures.
* `medical_examination.csv`: The underlying medical examination dataset[cite: 5, 6].
