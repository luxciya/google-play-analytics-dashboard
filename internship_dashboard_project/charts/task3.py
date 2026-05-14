import plotly.graph_objects as go
from plotly.subplots import make_subplots


def task3_chart(df):

    filtered = df[
        (df['Installs'] > 10000) &
        (df['Revenue'] > 10000) &
        (df['Android Ver Numeric'] > 4.0) &
        (df['SizeMB'] > 15) &
        (df['Content Rating'] == 'Everyone') &
        (df['App'].str.len() < 30)
    ]

    top_categories = (
        filtered['Category']
        .value_counts()
        .head(3)
        .index
    )

    filtered = filtered[
        filtered['Category'].isin(top_categories)
    ]

    grouped = (
        filtered
        .groupby('Type')
        .agg({
            'Installs': 'mean',
            'Revenue': 'mean'
        })
    )

    fig = make_subplots(specs=[[{'secondary_y': True}]])

    fig.add_trace(
        go.Bar(
            x=grouped.index,
            y=grouped['Installs'],
            name='Average Installs'
        ),
        secondary_y=False
    )

    fig.add_trace(
        go.Scatter(
            x=grouped.index,
            y=grouped['Revenue'],
            name='Revenue'
        ),
        secondary_y=True
    )

    return fig