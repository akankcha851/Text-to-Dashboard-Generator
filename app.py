import streamlit as st
from data_loader import load_mock_data, load_csv, analyze_dataframe
from charts import generate_chart

st.set_page_config(
    page_title="AI Dashboard Generator",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
<div style="text-align:center; padding:20px;">
    <h1>AI Text-to-Dashboard Generator</h1>
    <p style="font-size:18px; color:gray;">
        Upload any dataset or use sample data to build dashboards instantly
    </p>
</div>
""", unsafe_allow_html=True)

st.sidebar.header("⚙️ Settings")
data_source = st.sidebar.radio(
    "Choose Data Source",
    ["Use Sample Data", "Upload CSV"]
)
uploaded_file = None
if data_source == "Upload CSV":
    uploaded_file = st.sidebar.file_uploader("Upload CSV File", type=["csv"])

st.sidebar.markdown("---")

if uploaded_file:
    df = load_csv(uploaded_file)
else:
    df = load_mock_data()

st.success("✅ Data loaded successfully")

numeric_cols, categorical_cols = analyze_dataframe(df)

if not numeric_cols or not categorical_cols:
    st.warning("Dataset must contain at least one numeric and one categorical column.")
    st.stop()


st.markdown("###  Key Metrics")

c1, c2, c3 = st.columns(3)

c1.metric("Rows", df.shape[0])
c2.metric("Numeric Columns", len(numeric_cols))
c3.metric("Categorical Columns", len(categorical_cols))

# ---------------- CHART BUILDER ----------------
st.markdown("### 📊 Build Your Chart")

col1, col2, col3 = st.columns(3)

with col1:
    chart_type = st.selectbox("Chart Type", ["bar", "line", "pie"])

with col2:
    x_col = st.selectbox("X Axis", categorical_cols)

with col3:
    y_col = st.selectbox("Y Axis", numeric_cols)

# ---------------- GENERATE CHART ----------------
if st.button("🚀 Generate Chart", use_container_width=True):
    fig = generate_chart(chart_type, x_col, y_col, df)

    if fig:
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.error("❌ Unable to generate chart with selected columns")

# ---------------- DATA PREVIEW ----------------
with st.expander("🔍 Preview Dataset"):
    st.dataframe(df)



