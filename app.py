import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Cars24 Used Car Analysis",
    page_icon="🚗",
    layout="wide"
)

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

try:
    df = pd.read_csv("cars24_data.csv")
except FileNotFoundError:
    st.error("cars24_data.csv not found. Please upload the dataset.")
    st.stop()
# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🚗 Cars24 Used Car Analysis Dashboard")
st.markdown("### Web Scraping & Data Analysis Project")

# --------------------------------------------------
# PROJECT SUMMARY
# --------------------------------------------------

st.subheader("📌 Project Summary")

col1, col2, col3 = st.columns(3)

col1.metric("Website", "Cars24")
col2.metric("Records", len(df))
col3.metric("Columns", len(df.columns))

# --------------------------------------------------
# TABS
# --------------------------------------------------

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📄 Dataset",
    "📊 Visualizations",
    "📈 Statistics",
    "💡 Insights",
    "🕷️ Web Scraping"
])

# --------------------------------------------------
# DATASET TAB
# --------------------------------------------------

with tab1:

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Dataset Information")

    info_df = pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes.astype(str),
        "Null Count": df.isnull().sum().values
    })

    st.dataframe(info_df)

    st.subheader("Column Names")
    st.write(df.columns.tolist())

# --------------------------------------------------
# VISUALIZATION TAB
# --------------------------------------------------

with tab2:

    numeric_cols = df.select_dtypes(include="number").columns

    if len(numeric_cols) > 0:

        column = st.selectbox(
            "Select Numeric Column",
            numeric_cols
        )

        st.subheader("Histogram")

        fig, ax = plt.subplots(figsize=(8,4))
        sns.histplot(df[column], kde=True, ax=ax)
        st.pyplot(fig)

        st.subheader("Box Plot")

        fig2, ax2 = plt.subplots(figsize=(8,4))
        sns.boxplot(x=df[column], ax=ax2)
        st.pyplot(fig2)

        st.subheader("Correlation Heatmap")

        fig3, ax3 = plt.subplots(figsize=(8,5))

        sns.heatmap(
            df[numeric_cols].corr(),
            annot=True,
            cmap="coolwarm",
            ax=ax3
        )

        st.pyplot(fig3)

        st.subheader("Pivot Table")

        row_col = st.selectbox(
            "Select Row Column",
            df.columns,
            key="pivot_row"
        )

        value_col = st.selectbox(
            "Select Value Column",
            numeric_cols,
            key="pivot_value"
        )

        pivot = pd.pivot_table(
            df,
            index=row_col,
            values=value_col,
            aggfunc="mean"
        )

        st.dataframe(pivot)

        st.subheader("Top 10 Records")

        top10 = df.nlargest(
            10,
            value_col
        )

        st.dataframe(top10)

# --------------------------------------------------
# STATISTICS TAB
# --------------------------------------------------

with tab3:

    st.subheader("Summary Statistics")
    st.dataframe(df.describe())

# --------------------------------------------------
# INSIGHTS TAB
# --------------------------------------------------

with tab4:

    st.success("Business Insights")

    st.markdown("""
    - Understand market trends.
    - Identify high-value vehicles.
    - Detect pricing patterns.
    - Analyze customer preferences.
    - Support buying decisions.
    """)

    st.subheader("Conclusion")

    st.info("""
Cars24 data analysis helps understand
pricing patterns and trends in the
used car market.
""")

# --------------------------------------------------
# WEB SCRAPING TAB
# --------------------------------------------------

with tab5:

    st.header("🕷️ Web Scraping Process")

    st.markdown("""
### Project Workflow

1. Open Cars24 website using Selenium
2. Load dynamic car listings
3. Extract vehicle information
4. Save data into CSV
5. Clean the dataset
6. Perform analysis using Streamlit

### Tools Used

- Python
- Selenium
- Pandas
- Streamlit
- Matplotlib
- Seaborn

### Output

cars24_data.csv
""")
