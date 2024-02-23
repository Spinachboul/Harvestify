import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv('sample.csv')

# Assuming 'Crop' is the column name
crop_counts = data['Crop'].value_counts()

# Plotting the pie chart
plt.figure(figsize=(8, 8))
plt.pie(crop_counts, labels=crop_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Crop Distribution')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
