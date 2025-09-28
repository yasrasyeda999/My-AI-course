import pandas as pd
df = pd.read_csv('C:\\Users\\AA laptops\\Documents\\Fullstack-WITH-AI-B-3-SAT-SUN-6Months-Explorer\\DataSetForPractice\RealEstate-USA.csv')
print(df.head())
print(df.describe())


df = df.dropna(subset=['bed', 'price'])

x = df[['bed']]
y = df[['price']]

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

print(x_train)


from sklearn.linear_model import LinearRegression
regression=LinearRegression()
regression.fit(x_train,y_train)

y_pred=regression.predict(x_test)
print(y_pred)


from sklearn.metrics import r2_score
score=r2_score(y_pred,y_test)

print("accuracy",score)


import matplotlib.pyplot as plt

plt.scatter(x_test, y_test, color='gray')
plt.plot(x_test, y_pred, color='')
plt.xlabel('Number of Bedrooms')
plt.ylabel('Price')
plt.title('Actual vs Predicted Prices') 
plt.show()


