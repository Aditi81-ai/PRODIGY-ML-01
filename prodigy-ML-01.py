import pandas as pd
from sklearn.linear_model import LinearRegression
data = pd.read_csv(r"C:\Users\HP\Downloads\train.csv")

print(data[['GrLivArea', 'BedroomAbvGr', 'FullBath', 'SalePrice']].head())

X= data[["GrLivArea","BedroomAbvGr","FullBath"]]
y= data["SalePrice"]
model = LinearRegression()
model.fit(X, y)
area = float(input("Enter house area (sq ft): "))
bedrooms = int(input("Enter number of bedrooms: "))
bathrooms = int(input("Enter number of bathrooms: "))
predicted_price = model.predict([[area, bedrooms, bathrooms]])
print("Predicted House Price: ₹", round(predicted_price[0], 2))
