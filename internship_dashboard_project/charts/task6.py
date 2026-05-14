import pandas as pd
import plotly.express as px


TRANSLATIONS = {
    'TRAVEL_AND_LOCAL': 'Voyage et Local',
    'PRODUCTIVITY': 'Productividad',
    'PHOTOGRAPHY': '写真'
}


def task6_chart(df):

    # Apply filters
    filtered = df[
        (df['Rating'] >= 4.2) &
        (~df['App'].str.contains(r'\d', regex=True, na=False)) &
        (df['Category'].str.startswith(('T', 'P'), na=False)) &
        (df['Reviews'] > 1000) &
        (df['SizeMB'].between(20, 80))
    ].copy()

    # Translate categories
    filtered['Category'] = filtered['Category'].replace(TRANSLATIONS)

    # Create Month column
    filtered['Month'] = (
        filtered['Last Updated']
        .dt.to_period('M')
        .astype(str)
    )

    # Group installs
    grouped = (
        filtered
        .groupby(['Month', 'Category'])['Installs']
        .sum()
        .reset_index()
    )

    # Calculate month-over-month growth
    grouped['Growth_Percentage'] = (
        grouped
        .groupby('Category')['Installs']
        .pct_change() * 100
    )

    # Create highlight flag
    grouped['Growth_Flag'] = grouped[
        'Growth_Percentage'
    ].apply(
        lambda x: 'High Growth'
        if x > 25 else 'Normal Growth'
    )

    # Create stacked area chart
    fig = px.area(
        grouped,
        x='Month',
        y='Installs',
        color='Category',
        line_group='Category',
        hover_data=[
            'Growth_Percentage'
        ],
        title='Cumulative Installs Over Time'
    )

    # Highlight high growth periods
    for i, row in grouped.iterrows():

        if row['Growth_Flag'] == 'High Growth':

            fig.add_vrect(
                x0=row['Month'],
                x1=row['Month'],
                fillcolor='yellow',
                opacity=0.2,
                line_width=0
            )

    # Layout customization
    fig.update_layout(
        template='plotly_dark',
        xaxis_title='Month',
        yaxis_title='Total Installs',
        legend_title='Categories',
        height=700
    )

    return fig