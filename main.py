import streamlit as st 
import matplotlib.pyplot as plt
import requests
import datetime
import json
import urllib.request

st.title('Exchange Calculator')

st.write("""
# Explore different Exchange rates
Today's exchange rate?
""")

res=urllib.request.urlopen('http://data.fixer.io/api/latest?access_key=49caf6c328ef6cdb10d122186ae543e3').read()
json_data=json.loads(res)
# st.write(f"{str(json_data)}")

dataset_name = st.sidebar.selectbox(
    'Base',
    ('EUR',)
)

st.write(f"## {dataset_name}")
tup=[]

for i in json_data['rates']:
   tup.append(i)

classifier_name = st.sidebar.selectbox(
    'Select Country',
    tuple(tup)
)

amount=st.sidebar.slider("slide to know your returns", min_value=0, max_value=100)

st.write('Value:',json_data['rates'][dataset_name])
st.write(f"## {classifier_name}")
st.write('Value:',json_data['rates'][classifier_name])
st.write('Equivalent amount:',amount*json_data['rates'][classifier_name])


# res1=urllib.request.urlopen('http://api.exchangeratesapi.io/v1/2020-09-06?access_key=8c05e51c1e3d6afe73393dcd960f0db2&symbols=INR,AUD,CAD,PLN,MXN').read()
#json_data1=json.loads(res1)
# st.write(f"{str(json_data1)}")

history={}
day=''
# json_data1=''
st.write("""
## last 10 days exchange rates
""")
for i in range(10,0,-1):
   Previous_Date = datetime.datetime.today() - datetime.timedelta(days=i)
   Previous_Date_Formatted = Previous_Date.strftime ('%Y-%m-%d')
   day="http://api.exchangeratesapi.io/v1/{}?access_key=8c05e51c1e3d6afe73393dcd960f0db2&symbols={},{}".format(Previous_Date_Formatted,dataset_name,classifier_name)
   res1=urllib.request.urlopen(day).read()
   json_data1=json.loads(res1)
   st.write(f"on {Previous_Date_Formatted} the exchange rate was {str(json_data1['rates'][classifier_name])}")
   # history[Previous_Date_Formatted]=json_data1['rates'][classifier_name]

# print(tabulate(results, headers=["Date", "Exchange rate"]))

# x1 = list(history.keys())
# # st.write(f"{x1}")
# x2 = list(history.values())
# # st.write(f"{x2}")

# fig = plt.figure()
# plt.bar(x1, x2)

# plt.xlabel('Last 10 days')
# plt.ylabel('Exchange rates')

# # plt.show()
# st.pyplot(fig)

