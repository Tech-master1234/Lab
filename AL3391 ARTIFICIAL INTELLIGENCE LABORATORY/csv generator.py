import pandas as pd
import numpy as np

# Generating sample data for Logistic Regression
data = {
    'age': np.random.randint(20, 80, 100),
    'Sex_male': np.random.choice([0, 1], size=100),
    'cigsPerDay': np.random.randint(0, 30, 100),
    'totChol': np.random.randint(150, 300, 100),
    'sysBP': np.random.randint(90, 180, 100),
    'glucose': np.random.randint(70, 150, 100),
    'education': np.random.choice(['High School', 'Bachelor', 'Master', 'PhD'], size=100),  # New education column
    'TenYearCHD': np.random.choice([0, 1], size=100)
}

# Creating DataFrame
df = pd.DataFrame(data)

# Saving to CSV file
df.to_csv('logistic.csv', index=False)


'''
import pandas as pd
import numpy as np

# Generating sample data for SVM
signals_data = {
    f'signal_{i}': np.random.rand(100) for i in range(180)
}

labels_data = {
    'class': np.random.choice([0, 1], size=100)
}

signals = pd.DataFrame(signals_data)
labels = pd.DataFrame(labels_data)

signals.to_csv('signals_data.csv', index=False, header=False)
labels.to_csv('labels_data.csv', index=False, header=False)
'''