import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

all_df = pd.read_csv("https://media.githubusercontent.com/media/yovelakalista23/project-structure/refs/heads/main/dashboard/all_df.csv")

st.title("Dashboard Hasil Analisis E-Commerce")

st.header("Metode pembayaran yang sering digunakan")
payment = all_df['payment_type'].value_counts(normalize=True).reset_index()
payment.columns = ['payment_type', 'percentage']
payment['percentage'] = payment['percentage'] * 100

# Visualisasi
fig, ax = plt.subplots()
sns.barplot(x='payment_type', y='percentage', data=payment, palette=['purple', 'green', 'blue', 'orange'], ax=ax)
ax.set_title('Persentase Metode Pembayaran yang Paling Banyak Digunakan')
ax.set_xlabel('Metode Pembayaran')
ax.set_ylabel('Persentase')
st.pyplot(fig)


st.header("Performa Penjualan Tiap Bulan")
avg_sales = all_df['order_purchase_timestamp'].value_counts(normalize=True).reset_index()
avg_sales.columns = ['order_purchase_timestamp', 'percentage']
avg_sales['percentage'] = avg_sales['percentage'] * 100

# Visualisasi
fig, ax = plt.subplots()
sns.barplot(x='order_purchase_timestamp', y='percentage', data=avg_sales, palette=['purple'], ax=ax)
ax.set_title('Persentase Metode Pembayaran yang Paling Banyak Digunakan')
ax.set_xlabel('Metode Pembayaran')
ax.set_ylabel('Persentase')
st.pyplot(fig)

