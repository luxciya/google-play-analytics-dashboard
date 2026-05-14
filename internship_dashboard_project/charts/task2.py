import plotly.express as px


COUNTRY_MAPPING = {
    'GAME': 'India',
    'TOOLS': 'United States',
    'BUSINESS': 'Germany',
    'MEDICAL': 'Canada',
    'SPORTS': 'Australia'
}


def task2_chart(df):

    exclude = ('A', 'C', 'G', 'S')

    filtered = df[
        ~df['Category'].str.startswith(exclude, na=False)
    ]

    grouped = (
        filtered
        .groupby('Category')['Installs']
        .sum()
        .reset_index()
    )

    grouped = grouped.sort_values(
        'Installs',
        ascending=False
    ).head(5)

    grouped['Country'] = grouped['Category'].map(COUNTRY_MAPPING)

    fig = px.choropleth(
        grouped,
        locations='Country',
        locationmode='country names',
        color='Installs',
        hover_name='Category',
        title='Global Installs by Category'
    )

    return fig