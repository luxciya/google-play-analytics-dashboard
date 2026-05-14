import streamlit as st
import pandas as pd

from utils.preprocessing import preprocess_data
from utils.time_filters import is_time_between

from charts.task1 import task1_chart
from charts.task2 import task2_chart
from charts.task3 import task3_chart
from charts.task4 import task4_chart
from charts.task5 import task5_chart
from charts.task6 import task6_chart


# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title='Google Play Analytics Dashboard',
    page_icon='📊',
    layout='wide',
    initial_sidebar_state='expanded'
)


# ---------------------------------------------------
# CUSTOM CSS STYLING
# ---------------------------------------------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* Main Background */
.stApp {
    background: linear-gradient(to right, #0f172a, #111827);
    color: white;
}

/* Main Dashboard Title */
.main-title {
    font-size: 48px;
    font-weight: 700;
    text-align: center;
    color: #ffffff;
    padding-top: 10px;
    letter-spacing: 1px;
}

/* Dashboard Subtitle */
.main-subtitle {
    text-align: center;
    font-size: 18px;
    color: #cbd5e1;
    margin-bottom: 30px;
}

/* Section Header */
.section-header {
    font-size: 32px;
    font-weight: 600;
    color: #38bdf8;
    margin-top: 30px;
    margin-bottom: 10px;
    border-left: 6px solid #38bdf8;
    padding-left: 15px;
}

/* Task Description */
.task-description {
    font-size: 16px;
    line-height: 1.8;
    color: #d1d5db;
    background-color: rgba(255,255,255,0.04);
    padding: 18px;
    border-radius: 12px;
    margin-bottom: 20px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(to bottom, #111827, #1e293b);
}

/* Sidebar Text */
section[data-testid="stSidebar"] * {
    color: white !important;
}

/* Metric Cards */
.metric-box {
    background-color: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
}

/* Footer */
.footer {
    text-align: center;
    font-size: 15px;
    color: #94a3b8;
    margin-top: 40px;
}

/* Horizontal Divider */
hr {
    border: 1px solid rgba(255,255,255,0.08);
}

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------
# DASHBOARD TITLE
# ---------------------------------------------------

st.markdown(
    """
    <div class="main-title">
        📱 Google Play Store Analytics Dashboard
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="main-subtitle">
        Advanced Interactive Visualization & Analytics Platform for Google Play Store Insights
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")


# ---------------------------------------------------
# LOAD DATASETS
# ---------------------------------------------------

main_df = pd.read_csv('data/googleplaystore.csv')
review_df = pd.read_csv('data/googleplaystore_user_reviews.csv')

review_df = review_df.drop_duplicates(subset='App')

main_df = preprocess_data(main_df)


# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

st.sidebar.markdown("# 📌 Dashboard Overview")

st.sidebar.info(
    """
    ### Included Visualizations

    ✅ Grouped Bar Chart  
    ✅ Choropleth Map  
    ✅ Dual Axis Chart  
    ✅ Time Series Chart  
    ✅ Bubble Chart  
    ✅ Stacked Area Chart  

    ---
    
    ### Technologies Used

    - Python
    - Pandas
    - Plotly
    - Streamlit
    
    ---
    
    ### Features

    - Interactive Dashboard
    - Dynamic Filtering
    - Time-based Visibility
    - Advanced Analytics
    - Sentiment Analysis
    """
)


# ---------------------------------------------------
# TASK 1
# ---------------------------------------------------

st.markdown(
    '<div class="section-header">📊 Task 1 — Grouped Bar Chart</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="task-description">
    This visualization presents a comparative analysis of average user ratings and total review engagement across the top-performing app categories based on installation count. The chart highlights user satisfaction trends while emphasizing categories that maintain high ratings despite compact application sizes and recent January updates.
    </div>
    """,
    unsafe_allow_html=True
)

if is_time_between(15, 17):

    fig1 = task1_chart(main_df)

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

else:

    st.warning(
        '⏰ This chart is visible only between 3 PM IST and 5 PM IST.'
    )

st.markdown("---")


# ---------------------------------------------------
# TASK 2
# ---------------------------------------------------

st.markdown(
    '<div class="section-header">🌍 Task 2 — Choropleth Map</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="task-description">
    This interactive choropleth map visualizes global installation distribution across leading application categories. By highlighting categories with exceptionally high installation volumes, the visualization provides geographical insight into worldwide app adoption and category popularity trends.
    </div>
    """,
    unsafe_allow_html=True
)

if is_time_between(18, 20):

    fig2 = task2_chart(main_df)

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

else:

    st.warning(
        '⏰ This chart is visible only between 6 PM IST and 8 PM IST.'
    )

st.markdown("---")


# ---------------------------------------------------
# TASK 3
# ---------------------------------------------------

st.markdown(
    '<div class="section-header">📈 Task 3 — Dual Axis Chart</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="task-description">
    This dual-axis visualization compares average installations and estimated revenue between free and paid applications within the top-performing categories. The chart offers deeper insight into monetization performance, user reach, and platform compatibility among high-quality Android applications.
    </div>
    """,
    unsafe_allow_html=True
)

if is_time_between(13, 14):

    fig3 = task3_chart(main_df)

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

else:

    st.warning(
        '⏰ This chart is visible only between 1 PM IST and 2 PM IST.'
    )

st.markdown("---")


# ---------------------------------------------------
# TASK 4
# ---------------------------------------------------

st.markdown(
    '<div class="section-header">📅 Task 4 — Time Series Chart</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="task-description">
    This time-series visualization illustrates the evolution of application installations over time across selected categories. Significant month-over-month growth periods are highlighted to reveal emerging trends, user adoption patterns, and category-level performance dynamics in the app ecosystem.
    </div>
    """,
    unsafe_allow_html=True
)

if is_time_between(18, 21):

    fig4 = task4_chart(main_df)

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

else:

    st.warning(
        '⏰ This chart is visible only between 6 PM IST and 9 PM IST.'
    )

st.markdown("---")


# ---------------------------------------------------
# TASK 5
# ---------------------------------------------------

st.markdown(
    '<div class="section-header">🫧 Task 5 — Bubble Chart</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="task-description">
    This bubble chart explores the relationship between application size and user ratings, while the bubble dimensions represent installation volume. The visualization combines sentiment analysis and category-level filtering to uncover engagement patterns and performance behavior among highly reviewed applications.
    </div>
    """,
    unsafe_allow_html=True
)

if is_time_between(17, 19):

    fig5 = task5_chart(
        main_df,
        review_df
    )

    st.plotly_chart(
        fig5,
        use_container_width=True
    )

else:

    st.warning(
        '⏰ This chart is visible only between 5 PM IST and 7 PM IST.'
    )

st.markdown("---")


# ---------------------------------------------------
# TASK 6
# ---------------------------------------------------

st.markdown(
    '<div class="section-header">📉 Task 6 — Stacked Area Chart</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="task-description">
    This stacked area chart visualizes cumulative installation growth across multiple application categories over time. The layered representation highlights category contribution, growth intensity, and evolving market trends while emphasizing periods of exceptional installation acceleration.
    </div>
    """,
    unsafe_allow_html=True
)

if is_time_between(16, 18):

    fig6 = task6_chart(main_df)

    st.plotly_chart(
        fig6,
        use_container_width=True
    )

else:

    st.warning(
        '⏰ This chart is visible only between 4 PM IST and 6 PM IST.'
    )

st.markdown("---")


# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.markdown(
    """
    <div class="footer">
        Developed with ❤️ using Streamlit | Google Play Analytics Dashboard
    </div>
    """,
    unsafe_allow_html=True
)