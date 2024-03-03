import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')


sellersperformance_df = pd.read_csv("sellersperformance.csv")
performance_by_state_df = pd.read_csv("performance_by_state.csv")
revenue_by_state_df = pd.read_csv("revenue_by_state.csv")
orderpayments_df = pd.read_csv("orderpayments.csv")

with st.sidebar:
    st.image("logo.png", width = 100)
    st.markdown("# Adira Rahmana Akbar E-commerce Dashboard")
    st.markdown("Welcome to Adira E-commerce Dashboard")


st.header(':chart_with_upwards_trend::shopping_trolley: Adira E-commerce Dashboard :shopping_trolley::chart_with_upwards_trend:')

#Tipe Payments paling banyak digunakan
grouped_data = orderpayments_df.groupby(by="payment_type").order_id.nunique().sort_values(ascending=True)

st.title('Distribution of Order Counts by Payment Type')

st.write("Bar Chart:")
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(grouped_data.index, grouped_data, color='skyblue')
ax.set_title('Distribution of Order Counts by Payment Type')
ax.set_xlabel('Payment Type')
ax.set_ylabel('Number of Unique Order Items')
ax.set_xticklabels(grouped_data.index, rotation=45, ha='right')  # Rotasi label sumbu x untuk keterbacaan
st.pyplot(fig)

#Good Orders by State
top_order_states = performance_by_state_df.head(5)

st.title('Top 5 States with the Highest Total Orders')

st.write("Bar Chart:")
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(top_order_states['seller_state'], top_order_states['total_orders'], color='skyblue')
ax.set_title('Top 5 States with the Highest Total Orders')
ax.set_xlabel('Seller State')
ax.set_ylabel('Total Orders')
ax.set_xticklabels(top_order_states['seller_state'], rotation=45, ha='right')  
ax.invert_xaxis()  # Invert the x-axis for better readability
st.pyplot(fig)

#Bad Orders by State
bot_order_states = performance_by_state_df.tail(5)

st.title('Top 5 Bad Total Revenue by State')

st.write("Bar Chart:")
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(bot_order_states['seller_state'], bot_order_states['total_orders'], color='skyblue')
ax.set_title('Top 5 Bad Total Revenue by State')
ax.set_xlabel('Seller State')
ax.set_ylabel('Total Orders')
ax.set_xticklabels(bot_order_states['seller_state'], rotation=45, ha='right')  
ax.invert_xaxis()  # Invert the x-axis for better readability
st.pyplot(fig)

#Good Revenue by State
top_revenue_states = revenue_by_state_df.head(5)

st.title('Top 5 Good Total Revenue by State')

st.write("Line Chart:")
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(top_revenue_states['seller_state'], top_revenue_states['total_revenue'], marker='o', color='skyblue', linestyle='-')
ax.set_xlabel('Negara Bagian')
ax.set_ylabel('Total Revenue')
ax.set_title('Top 5 Good Total Revenue by State (Line Chart)')
ax.yaxis.set_major_formatter(mticker.StrMethodFormatter('${x:,.2f}'))
ax.set_xticklabels(top_revenue_states['seller_state'], rotation=45, ha='right')  
ax.invert_xaxis()  
ax.grid(True)
st.pyplot(fig)


#Bad Revenue by State
bot_revenue_states = revenue_by_state_df.tail(5)

st.title('Top 5 Bad Total Revenue by State (Line Chart)')

st.write("Line Chart:")
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(bot_revenue_states['seller_state'], bot_revenue_states['total_revenue'], marker='o', color='skyblue', linestyle='-')
ax.set_xlabel('Negara Bagian')
ax.set_ylabel('Total Revenue')
ax.set_title('Top 5 Bad Total Revenue by State (Line Chart)')
ax.yaxis.set_major_formatter(mticker.StrMethodFormatter('${x:,.2f}'))
ax.set_xticklabels(bot_revenue_states['seller_state'], rotation=45, ha='right')  
ax.invert_xaxis() 
ax.grid(True)
st.pyplot(fig)

st.caption('Copyright (c) Adira Akbar')