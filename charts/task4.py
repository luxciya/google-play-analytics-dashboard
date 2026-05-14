import pandas as pd
import plotly.express as px

# ---------------------------------------------------
# CATEGORY TRANSLATIONS
# ---------------------------------------------------

TRANSLATIONS = {
    'BEAUTY': 'सौंदर्य',
    'BUSINESS': 'வணிகம்',
    'DATING': 'Partnersuche'
}


# ---------------------------------------------------
# TASK 4 CHART
# ---------------------------------------------------

def task4_chart(df):

    # -----------------------------------------------
    # APPLY FILTERS
    # -----------------------------------------------

    filtered = df[
        (~df['App'].str.startswith(('X', 'Y', 'Z'), na=False)) &
        (df['Category'].str.startswith(('E', 'C', 'B'), na=False)) &
        (df['Reviews'] > 500) &
        (~df['App'].str.contains('S', case=False, na=False))
    ].copy()

    # -----------------------------------------------
    # TRANSLATE CATEGORY NAMES
    # -----------------------------------------------

    filtered['Category'] = (
        filtered['Category']
        .replace(TRANSLATIONS)
    )

    # -----------------------------------------------
    # CREATE MONTH COLUMN
    # -----------------------------------------------

    filtered['Month'] = (
        filtered['Last Updated']
        .dt.to_period('M')
        .astype(str)
    )

    # -----------------------------------------------
    # GROUP DATA
    # -----------------------------------------------

    grouped = (
        filtered
        .groupby(['Month', 'Category'])['Installs']
        .sum()
        .reset_index()
    )

    # -----------------------------------------------
    # CALCULATE MONTH-OVER-MONTH GROWTH
    # -----------------------------------------------

    grouped['Growth_Percentage'] = (
        grouped
        .groupby('Category')['Installs']
        .pct_change() * 100
    )

    # -----------------------------------------------
    # CREATE LINE CHART
    # -----------------------------------------------

    fig = px.line(
        grouped,
        x='Month',
        y='Installs',
        color='Category',
        markers=True,
        title='📈 Install Trends Over Time by Category',
        template='plotly_dark'
    )

    # -----------------------------------------------
    # HIGHLIGHT GROWTH > 20%
    # -----------------------------------------------

    high_growth = grouped[
        grouped['Growth_Percentage'] > 20
    ]

    for _, row in high_growth.iterrows():

        fig.add_vrect(
            x0=row['Month'],
            x1=row['Month'],
            fillcolor='green',
            opacity=0.15,
            line_width=0
        )

    # -----------------------------------------------
    # LAYOUT CUSTOMIZATION
    # -----------------------------------------------

    fig.update_layout(
        height=650,
        title_x=0.5,
        xaxis_title='Month',
        yaxis_title='Total Installs',
        hovermode='x unified',
        legend_title='App Categories',
        font=dict(
            family='Poppins',
            size=14
        )
    )

    # -----------------------------------------------
    # UPDATE LINE STYLE
    # -----------------------------------------------

    fig.update_traces(
        line=dict(width=4),
        marker=dict(size=8)
    )

    return fig