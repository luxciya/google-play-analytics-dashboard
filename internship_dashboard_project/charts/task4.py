import plotly.express as px


TRANSLATIONS = {
    'Beauty': 'सौंदर्य',
    'Business': 'வணிகம்',
    'Dating': 'Partnersuche'
}


def task4_chart(df):

    filtered = df[
        (~df['App'].str.startswith(('X', 'Y', 'Z'), na=False)) &
        (df['Category'].str.startswith(('E', 'C', 'B'), na=False)) &
        (df['Reviews'] > 500) &
        (~df['App'].str.contains('S', case=False, na=False))
    ]

    filtered['Category'] = filtered['Category'].replace(TRANSLATIONS)

    grouped = (
        filtered
        .groupby([
            filtered['Last Updated'].dt.to_period('M'),
            'Category'
        ])['Installs']
        .sum()
        .reset_index()
    )
    grouped['Last Updated'] = grouped['Last Updated'].astype(str)

    fig = px.line(
        grouped,
        x='Last Updated',
        y='Installs',
        color='Category',
        title='Install Trends Over Time'
    )

    return fig