import streamlit as st # web development
import numpy as np # np mean, np random 
import pandas as pd # read csv, df manipulation
import time # to simulate a real time data, time loop 
import plotly.express as px # interactive charts 
import seaborn as sns
from sklearn.linear_model import LinearRegression
import smtplib
import ssl
from email.message import EmailMessage
import random
import warnings 
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')
import mysql.connector


# read csv from a github repo
# data = pd.read_csv(r"C:\Users\karan\OneDrive\Desktop\major_project03_files\CR.csv")


st.set_page_config(
    page_title = 'Water Quality Analysis Dashboard',
    page_icon = '✅',
    layout = 'wide'
)

# dashboard title

st.title("Aquaprobe")

#connecting to mysql database
connection=mysql.connector.connect(host='localhost',
user='root',password='',database='test')
print('connected')
cursor=connection.cursor()
cursor.execute("Select * from aquaprobe")
dt=cursor.fetchall()
print(cursor.column_names)
df=pd.DataFrame(dt,columns=cursor.column_names)



#label encoding for categorial values
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
data['MONTH']= le.fit_transform(data['MONTH'])
n=9
data=data.iloc[:n]
# data.drop(columns=['Unnamed: 3'], inplace=True)
# data.drop(columns=['Unnamed: 4'], inplace=True)
#training the model
x=np.array(data['BOD mg/lt']).reshape(-1,1)
lr=LinearRegression()
lr.fit(x, np.array(data['Feacal Coliform  (mpn/100ml)']))

#predicting the value
st.header("Know the Fecal Coliform level in water")
# Initialize connection.
# conn = st.connection('mysql', type='sql')
# conn = st.experimental_connection('mysql', type='sql')
# df2 = conn.query('SELECT * from aquaprobe;', ttl=600)
# for row in df2.itertuples():
#     print(row)


val=st.number_input("Enter the BOD level in water", 0.0, 8.0, step=0.25)
val=np.array(val).reshape(-1,1)
pred=lr.predict(val)[0]
st.success(f"The predicted value of FC is {round(pred)}")

# creating a single-element container.
placeholder = st.empty()

st.markdown("### Detailed Data View")
st.dataframe(df)
time.sleep(1)
#placeholder.empty()

#Sending Email

# Define email sender and receiver
# email_sender = 'karantara30@gmail.com'
# email_password = 'zdpk xyzn rnem grou'
# email_receiver = 'shivangi010375@gmail.com'

# # Set the subject and body of the email
# subject = 'Check out the parameters!'
# body = """
# WQI crossed the bar.
# """

# em = EmailMessage()
# em['From'] = email_sender
# em['To'] = email_receiver
# em['Subject'] = subject
# em.set_content(body)

# #Add SSL (layer of security)
# context = ssl.create_default_context()
# while True:
#  random_number = random.randint(1, 10)
#  print("Random number:", random_number)


# #Log in and send the email
#  if (random_number%2==0):
#   with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
#     smtp.login(email_sender, email_password)
#     smtp.sendmail(email_sender, email_receiver, em.as_string())






















# import streamlit as st # web development
# import numpy as np # np mean, np random 
# import pandas as pd # read csv, df manipulation
# import time # to simulate a real time data, time loop 
# import plotly.express as px # interactive charts 
# import seaborn as sns
# from sklearn.linear_model import LinearRegression
# import warnings 
# import matplotlib.pyplot as plt
# warnings.filterwarnings('ignore')
# import mysql.connector


# # read csv 
# data = pd.read_csv(r"C:\Users\HP 2511\Desktop\CR.csv")


# st.set_page_config(
#     page_title = 'Water Quality Analysis Dashboard',
#     page_icon = '✅',
#     layout = 'wide'
# )

# # dashboard title

# st.title("Real-Time Water Quality Analysis Dashboard")

# #connecting to mysql database
# connection=mysql.connector.connect(host='127.0.0.1',
# user='root',password='',database='happy')
# print('connected')
# cursor=connection.cursor()
# cursor.execute("Select * from yaay")
# dt=cursor.fetchall()
# print(cursor.column_names)
# df=pd.DataFrame(dt,columns=cursor.column_names)



# #label encoding for categorial values
# from sklearn.preprocessing import LabelEncoder
# le=LabelEncoder()
# data['MONTH']= le.fit_transform(data['MONTH'])
# n=9
# data=data.iloc[:n]
# data.drop(columns=['Unnamed: 3'], inplace=True)
# data.drop(columns=['Unnamed: 4'], inplace=True)
# #training the model
# x=np.array(data['BOD mg/lt']).reshape(-1,1)
# lr=LinearRegression()
# lr.fit(x, np.array(data['Feacal Coliform  (mpn/100ml)']))

# #predicting the value
# st.header("Know the Fecal Coliform level in water")
# # conn = st.experimental_connection('mysql', type='sql')
# # df2 = conn.query('SELECT * from yaay;', ttl=600)
# # for row in df2.itertuples():


# val=st.number_input("Enter the BOD level in water", 1.0, 8.0, step=0.25)
# val=np.array(val).reshape(-1,1)
# pred=lr.predict(val)[0]
# st.success(f"The predicted value of FC is {round(pred)}")


# # creating a single-element container.
# placeholder = st.empty()


# st.markdown("### Detailed Data View")
# st.dataframe(df)
# time.sleep(1)
#     #placeholder.empty()










# import streamlit as st # web development
# import numpy as np # np mean, np random 
# import pandas as pd # read csv, df manipulation
# import time # to simulate a real time data, time loop 
# import plotly.express as px # interactive charts 
# import seaborn as sns
# from sklearn.linear_model import LinearRegression
# import warnings 
# import matplotlib.pyplot as plt
# warnings.filterwarnings('ignore')
# import mysql.connector


# # read csv from a github repo
# data = pd.read_csv(r"C:\Users\karan\OneDrive\Desktop\CR.csv")


# st.set_page_config(
#     page_title = 'Water Quality Analysis Dashboard',
#     page_icon = '✅',
#     layout = 'wide'
# )

# # dashboard title

# st.title("Real-Time Water Quality Analysis Dashboard")

# #connecting to mysql database
# connection=mysql.connector.connect(host='localhost',
# user='',password='',database='')
# print('connected')
# cursor=connection.cursor()
# cursor.execute("Select * from tablename")
# dt=cursor.fetchall()
# print(cursor.column_names)
# df=pd.DataFrame(dt,columns=cursor.column_names)



# #label encoding for categorial values
# from sklearn.preprocessing import LabelEncoder
# le=LabelEncoder()
# data['MONTH']= le.fit_transform(data['MONTH'])
# n=9
# data=data.iloc[:n]
# data.drop(columns=['Unnamed: 3'], inplace=True)
# data.drop(columns=['Unnamed: 4'], inplace=True)
# #training the model
# x=np.array(data['BOD mg/lt']).reshape(-1,1)
# lr=LinearRegression()
# lr.fit(x, np.array(data['Feacal Coliform  (mpn/100ml)']))

# #predicting the value
# st.header("Know the Fecal Coliform level in water")
# # conn = st.experimental_connection('mysql', type='sql')
# # df2 = conn.query('SELECT * from mytable;', ttl=600)
# # for row in df2.itertuples():


# val=st.number_input("Enter the BOD level in water", 1.0, 8.0, step=0.25)
# val=np.array(val).reshape(-1,1)
# pred=lr.predict(val)[0]
# st.success(f"The predicted value of FC is {round(pred)}")


# # creating a single-element container.
# placeholder = st.empty()


# st.markdown("### Detailed Data View")
# st.dataframe(df)
# time.sleep(1)
#     #placeholder.empty()
