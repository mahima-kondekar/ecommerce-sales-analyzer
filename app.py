import streamlit as st
import pandas as pd

st.title("📊 AI Sales Analyzer")

df = pd.read_csv("sales_data.csv")

st.subheader("Our Sales Data")
st.dataframe(df)

total_sales = df["Sales"].sum()
total_quantity = df["Quantity"].sum()

col1, col2 = st.columns(2)

col1.metric("Total Revenue", f"₹{total_sales:,}")
col2.metric("Total Units Sold", total_quantity)

st.subheader("🏆 Best-Selling Revenue Product")
best_product = df.loc[df["Sales"].idxmax(), "Product"]
st.success(f"{best_product} has the highest sales revenue!")
st.subheader("📈 Sales by Product")

st.bar_chart(
    df,
    x="Product",
    y="Sales"
)
st.subheader("🛍️ Sales by Category")

category_sales = df.groupby("Category")["Sales"].sum()

st.bar_chart(category_sales)
st.subheader("📂 Upload Your Sales Data")

uploaded_file = st.file_uploader(
    "Choose a sales CSV file",
    type=["csv"]

)

if uploaded_file is not None:
    uploaded_df = pd.read_csv(uploaded_file)

    st.subheader("📋 Uploaded Data")
    st.dataframe(uploaded_df, use_container_width=True)

    if "Sales" in uploaded_df.columns:
        total_revenue = uploaded_df["Sales"].sum()
        st.metric("💰 Uploaded Total Revenue", f"₹{total_revenue:,.0f}")

        st.subheader("📈 Uploaded Sales Chart")
        st.bar_chart(uploaded_df, x="Product", y="Sales")
    else:
        st.warning("Your CSV must contain a 'Sales' column.")
        