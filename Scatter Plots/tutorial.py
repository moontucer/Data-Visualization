import seaborn as sns
import pandas as pd

# Path of the file to read
insurance_filepath = "../input/insurance.csv"

# Read the file into a variable insurance_data
insurance_data = pd.read_csv(insurance_filepath)

insurance_data.head()

sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'])

sns.regplot(x=insurance_data['bmi'], y=insurance_data['charges'])

sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'], hue=insurance_data['smoker'])