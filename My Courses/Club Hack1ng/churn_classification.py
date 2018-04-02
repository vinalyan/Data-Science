import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
#from sklearn.metrics import confusion_matrix
#from sklearn.metrics import roc_curve
#import matplotlib
#import matplotlib.pyplot as plt
from IPython.display import display, HTML

# https://www.ibm.com/communities/analytics/watson-analytics-blog/guide-to-sample-datasets/
df = pd.read_csv("datasets/churn.csv")
#display(df.head(5))

df = df.drop(["customerID", "SeniorCitizen", "Partner", "MultipleLines", "InternetService", "Contract", "PaymentMethod",
              "InternetService", "tenure", "MonthlyCharges", "TotalCharges", "OnlineBackup", "StreamingTV",
              "StreamingMovies"], axis=1)

d = {'Female': True, 'Male': False}
d2 = {'Yes': True, 'No': False}

display(df.head(5))
display(df.dtypes)

df['gender'].map(d)
df['Dependents'].map(d2)
df['PhoneService'].map(d2)
df['OnlineSecurity'].map(d2)
df['PaperlessBilling'].map(d2)
df['Churn'].map(d2)
df['DeviceProtection'].map(d2)
df['TechSupport'].map(d2)
df['PaperlessBilling'].map(d2)

df['gender'] = df.gender.astype(bool)
df['Dependents'] = df.Dependents.astype(bool)
df['PhoneService'] = df.PhoneService.astype(bool)
df['OnlineSecurity'] = df.OnlineSecurity.astype(bool)
df['PaperlessBilling'] = df.PaperlessBilling.astype(bool)
df['Churn'] = df.Churn.astype(bool)
df['DeviceProtection'] = df.DeviceProtection.astype(bool)
df['TechSupport'] = df.TechSupport.astype(bool)
df['PaperlessBilling'] = df.PaperlessBilling.astype(bool)



display(df.dtypes)
features = df.drop(["Churn"], axis=1).columns
df_train, df_test = train_test_split(df, test_size=0.25)


# Set up our RandomForestClassifier instance and fit to data
clf = RandomForestClassifier(n_estimators=30)
clf.fit(df_train[features], df_train["Churn"])

# Make predictions
predictions = clf.predict(df_test[features])
probs = clf.predict_proba(df_test[features])
display(predictions)

score = clf.score(df_test[features], df_test["Churn"])
print("Accuracy: ", score)