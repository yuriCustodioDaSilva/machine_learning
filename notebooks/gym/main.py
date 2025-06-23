import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import NearestNeighbors

df = pd.read_csv('megaGymDataset.csv')
df = df.dropna(subset=['BodyPart', 'Rating','Desc'])

le_bodypart = LabelEncoder()
df['BodyPart_encoded'] = le_bodypart.fit_transform(df['BodyPart'])

le_equipment = LabelEncoder()
df['Equipment_encoded'] = le_equipment.fit_transform(df['Equipment'])

X = df[['BodyPart_encoded', 'Equipment_encoded', 'Rating']]

knn = NearestNeighbors(n_neighbors=5, algorithm='auto')
knn.fit(X)

user_input = 'Chest' 
user_input_encoded = le_bodypart.transform([user_input])[0]

distances, indices = knn.kneighbors([[user_input_encoded, 0, 0]]) 

recommended_exercises = df.iloc[indices[0]]

# print(recommended_exercises[['Title', 'Rating','Desc','BodyPart']])

recommended_exercises[['Title', 'Rating', 'BodyPart']].to_excel('recommended_exercises.xlsx', index=False)

print("Recommendations have been saved to 'recommended_exercises.xlsx'.")