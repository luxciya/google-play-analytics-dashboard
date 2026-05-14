import pandas as pd
import plotly.express as px


TRANSLATIONS = {
    'BEAUTY': 'सौंदर्य',
    'BUSINESS': 'வணிகம்',
    'DATING': 'Partnersuche'
}


def task5_chart(df, review_df):

    allowed_categories = [
        'GAME',
        'BEAUTY',
        'BUSINESS',
        'COMICS',
        'COMMUNICATION',
        'DATING',
        'ENTERTAINMENT',
        'SOCIAL',
        'EVENTS'
    ]
    review_df = review_df.drop_duplicates(subset='App')
    # Merge datasets
    merged = pd.merge(
        df,
        review_df,
        on='App',
        how='left'
    )

    # Apply all required filters
    filtered = merged[
        (merged['Rating'] > 3.5) &
        (merged['Reviews'] > 500) &
        (merged['Installs'] > 50000) &
        (merged['Sentiment_Subjectivity'] > 0.5) &
        (~merged['App'].str.contains('S', case=False, na=False)) &
        (merged['Category'].isin(allowed_categories))
    ].copy()

    # Translate categories
    filtered['Category'] = filtered['Category'].replace(TRANSLATIONS)

    # Custom colors
    color_map = {
        'GAME': 'pink',
        'सौंदर्य': 'orange',
        'வணிகம்': 'green',
        'Partnersuche': 'purple',
        'COMICS': 'blue',
        'COMMUNICATION': 'red',
        'ENTERTAINMENT': 'brown',
        'SOCIAL': 'gray',
        'EVENTS': 'cyan'
    }

    # Create bubble chart
    fig = px.scatter(
        filtered,
        x='SizeMB',
        y='Rating',
        size='Installs',
        color='Category',
        hover_name='App',
        hover_data=[
            'Reviews',
            'Installs',
            'Sentiment_Subjectivity'
        ],
        size_max=60,
        color_discrete_map=color_map,
        title='Bubble Chart: App Size vs Average Rating'
    )

    # Improve layout
    fig.update_layout(
        template='plotly_dark',
        xaxis_title='App Size (MB)',
        yaxis_title='Average Rating',
        legend_title='App Categories',
        height=700
    )

    # Improve bubbles appearance
    fig.update_traces(
        marker=dict(
            sizemode='area',
            line=dict(width=1)
        )
    )

    return fig