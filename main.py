import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix 
df = pd.read_csv('titanic.csv')
df.drop(['PassengerId','Name','Ticket','Cabin'], axis = 1, inplace = True)
df[list(pd.get_dummies(df['Embarked']).columns)] = pd.get_dummies(df['Embarked'])
df['Embarked'].fillna('S', inplace = True)
df.drop('Embarked', axis = 1, inplace = True)
age_1 = df[df['Pclass'] == 1]['Age'].median()
age_2 = df[df['Pclass'] == 2]['Age'].median()
age_3 = df[df['Pclass'] == 3]['Age'].median()
def fill_age(row):
    if pd.isnull(row['Age']):
        if row['Pclass'] == 1:
            return age_1
        if row['Pclass'] == 2:
            return age_2
        if row['Pclass'] == 3:
            return age_3
    return row['Age']
df['Age'] = df.apply(fill_age, axis = 1)
def fill_gender(gender):
    if gender == 'male':
        return 1
    return 0
df['Sex'] = df['Sex'].apply(fill_gender) 
X = df.drop('Survived', axis = 1)
Y = df['Survived']
sc = StandardScaler()
x_train, x_test, y_train, y_test = train_test_split(X , Y, test_size = 0.25)
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)
classifier = KNeighborsClassifier(n_neighbors = 5)
classifier.fit(x_train, y_train)
pred = classifier.predict(x_test)
print("Accuracy score:",accuracy_score(y_test, pred) * 100)




