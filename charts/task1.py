import plotly.graph_objects as go


def task1_chart(df):

    filtered = df[
        (df['Rating'] >= 4.0) &
        (df['SizeMB'] < 10) &
        (df['Last Updated'].dt.month == 1)
    ]

    grouped = (
        filtered
        .groupby('Category')
         .agg({
            'Rating': 'mean',
            'Reviews': 'sum',
            'Installs': 'sum'
        })
        .sort_values('Installs', ascending=False)
        .head(10)
    )

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=grouped.index,
            y=grouped['Rating'],
            name='Average Rating'
        )
    )

    fig.add_trace(
        go.Bar(
            x=grouped.index,
            y=grouped['Reviews'],
            name='Total Reviews'
        )
    )

    fig.update_layout(
        title='Top 10 Categories by Installs',
        barmode='group'
    )

    return fig