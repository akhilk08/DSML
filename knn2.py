import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
df=pd.read_csv('csv.file.csv')
print(df)
x=df.iloc[:,:-1]
print(x)
y=df.iloc[:,-1]
print(y)
x_train,x_test,y_train,Y_test=train_test_split(x,y,test_size=0.3,random_state=1)
c_knn=KNeighborsClassifier(n_neighbors=3)
c_knn.fit(x_train,y_train)
y_pred=c_knn.predict(x_test)
print("Accuracy:",metrics.accuracy_score(Y_test,y_pred))
print("enter the test data:")
a=int(input("enter x:"))
b=int(input("enter y:"))
pred_v=pd.dataframe({"height":[a],"weight":[b]})
pred=c_knn.predict(pred_v)
print(pred)
