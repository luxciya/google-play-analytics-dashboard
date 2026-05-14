import plotly.express as px


# ---------------------------------------------------
# COUNTRY MAPPING
# ---------------------------------------------------

COUNTRY_MAPPING = {
    'GAME': 'India',
    'TOOLS': 'United States',
    'BUSINESS': 'Germany',
    'MEDICAL': 'Canada',
    'SPORTS': 'Australia',
    'PRODUCTIVITY': 'France',
    'FINANCE': 'Japan',
    'LIFESTYLE': 'Brazil',
    'HEALTH_AND_FITNESS': 'United Kingdom',
    'PERSONALIZATION': 'Singapore',
    'SHOPPING': 'United Arab Emirates',
    'PHOTOGRAPHY': 'Italy',
    'TRAVEL_AND_LOCAL': 'Spain',
    'VIDEO_PLAYERS': 'South Korea',
    'NEWS_AND_MAGAZINES': 'Netherlands'
}


# ---------------------------------------------------
# TASK 2 CHART
# ---------------------------------------------------

def task2_chart(df):

    # -----------------------------------------------
    # EXCLUDE CATEGORIES STARTING WITH:
    # A, C, G, S
    # -----------------------------------------------

    exclude = ('A', 'C', 'G', 'S')

    filtered = df[
        ~df['Category'].str.startswith(exclude, na=False)
    ].copy()

    # -----------------------------------------------
    # GROUP INSTALLS BY CATEGORY
    # -----------------------------------------------

    grouped = (
        filtered
        .groupby('Category')['Installs']
        .sum()
        .reset_index()
    )

    # -----------------------------------------------
    # TOP 5 CATEGORIES
    # -----------------------------------------------

    grouped = grouped.sort_values(
        'Installs',
        ascending=False
    ).head(5)

    # -----------------------------------------------
    # MAP COUNTRIES
    # -----------------------------------------------

    grouped['Country'] = (
        grouped['Category']
        .map(COUNTRY_MAPPING)
    )

    # -----------------------------------------------
    # HANDLE NaN COUNTRY VALUES
    # -----------------------------------------------

    grouped['Country'] = grouped['Country'].fillna('India')

    # Optional:
    # Remove rows with missing countries instead
    # grouped = grouped.dropna(subset=['Country'])

    # -----------------------------------------------
    # HIGHLIGHT INSTALLS > 1 MILLION
    # -----------------------------------------------

    grouped['Highlight'] = grouped['Installs'].apply(
        lambda x: 'High Install Volume'
        if x > 1000000
        else 'Normal'
    )

    # -----------------------------------------------
    # CREATE CHOROPLETH MAP
    # -----------------------------------------------

    fig = px.choropleth(
        grouped,
        locations='Country',
        locationmode='country names',
        color='Installs',
        hover_name='Category',
        hover_data=['Installs', 'Highlight'],
        title='🌍 Global Installs by Category',
        template='plotly_dark',
        color_continuous_scale='Blues'
    )

    # -----------------------------------------------
    # LAYOUT CUSTOMIZATION
    # -----------------------------------------------

    fig.update_layout(
        height=650,
        title_x=0.5,
        geo=dict(
            showframe=False,
            showcoastlines=True,
            projection_type='natural earth'
        ),
        font=dict(
            family='Poppins',
            size=14
        )
    )

    return fig