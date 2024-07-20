import pandas as pd
df=pd.read_csv("C:\\Users\\user\\OneDrive\\Desktop\\birthdate.csv")
data_column='values'
print(df)

import matplotlib.pyplot as plt
plt.bar(df["Period"],df["Count"])
plt.xlabel('x-axis label')
plt.xlabel('y-axis label')
plt.title('bar plot')
plt.show()
plt.stem(df["Count"],df["Period"])
plt.xlabel('x-axis label')
plt.xlabel('y-axis label')
plt.title('stem plot')
plt.show()
plt.stackplot(df["Period"],df["Count"])
plt.xlabel('x-axis label')
plt.xlabel('y-axis label')
plt.title('stack plot')
plt.show()
plt.scatter(df["Period"],df["Count"])
plt.xlabel('x-axis label')
plt.xlabel('y-axis label')
plt.title('scatter plot')
plt.show()
plt.hist(df["Period"],weight=df["Count"])
plt.xlabel('x-axis label')
plt.xlabel('y-axis label')
plt.title('histogram plot')
plt.show()


