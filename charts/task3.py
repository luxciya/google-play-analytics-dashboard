import plotly.graph_objects as go
from plotly.subplots import make_subplots


# ---------------------------------------------------
# TASK 3 — DUAL AXIS CHART
# ---------------------------------------------------

def task3_chart(df):

    # -----------------------------------------------
    # APPLY FILTERS
    # -----------------------------------------------

    filtered = df[
        (df['Installs'] > 10000) &
        (df['Revenue'] > 10000) &
        (df['Android Ver Numeric'] > 4.0) &
        (df['SizeMB'] > 15) &
        (df['Content Rating'] == 'Everyone') &
        (df['App'].str.len() < 30)
    ].copy()

    # -----------------------------------------------
    # TOP 3 CATEGORIES
    # -----------------------------------------------

    top_categories = (
        filtered['Category']
        .value_counts()
        .head(3)
        .index
    )

    filtered = filtered[
        filtered['Category'].isin(top_categories)
    ]

    # -----------------------------------------------
    # GROUP DATA
    # -----------------------------------------------

    grouped = (
        filtered
        .groupby('Type')
        .agg({
            'Installs': 'mean',
            'Revenue': 'mean'
        })
        .reset_index()
    )

    # -----------------------------------------------
    # CREATE SUBPLOTS
    # -----------------------------------------------

    fig = make_subplots(
        specs=[[{'secondary_y': True}]]
    )

    # -----------------------------------------------
    # BAR CHART — INSTALLS
    # -----------------------------------------------

    fig.add_trace(
        go.Bar(
            x=grouped['Type'],
            y=grouped['Installs'],
            name='📥 Average Installs',
            text=grouped['Installs'].round(0),
            textposition='outside',
            marker=dict(
                color=['#38bdf8', '#818cf8'],
                line=dict(
                    color='white',
                    width=1.5
                )
            ),
            hovertemplate=
            '<b>%{x}</b><br>' +
            'Average Installs: %{y:,.0f}<extra></extra>'
        ),
        secondary_y=False
    )

    # -----------------------------------------------
    # LINE CHART — REVENUE
    # -----------------------------------------------

    fig.add_trace(
        go.Scatter(
            x=grouped['Type'],
            y=grouped['Revenue'],
            name='💰 Average Revenue',
            mode='lines+markers+text',
            text=grouped['Revenue'].round(0),
            textposition='top center',
            line=dict(
                color='#f472b6',
                width=4
            ),
            marker=dict(
                size=12,
                color='#f472b6',
                line=dict(
                    color='white',
                    width=2
                )
            ),
            hovertemplate=
            '<b>%{x}</b><br>' +
            'Revenue: $%{y:,.0f}<extra></extra>'
        ),
        secondary_y=True
    )

    # -----------------------------------------------
    # UPDATE LAYOUT
    # -----------------------------------------------

    fig.update_layout(

        title={
            'text': '📊 Free vs Paid Apps — Installs & Revenue Analysis',
            'x': 0.5,
            'xanchor': 'center'
        },

        template='plotly_dark',

        height=650,

        font=dict(
            family='Poppins',
            size=14,
            color='white'
        ),

        legend=dict(
            orientation='h',
            yanchor='bottom',
            y=1.02,
            xanchor='center',
            x=0.5
        ),

        plot_bgcolor='rgba(0,0,0,0)',

        paper_bgcolor='rgba(0,0,0,0)',

        hoverlabel=dict(
            font_size=14
        )
    )

    # -----------------------------------------------
    # X AXIS
    # -----------------------------------------------

    fig.update_xaxes(
        title_text='Application Type',
        showgrid=False
    )

    # -----------------------------------------------
    # LEFT Y AXIS
    # -----------------------------------------------

    fig.update_yaxes(
        title_text='Average Installs',
        secondary_y=False,
        showgrid=True,
        gridcolor='rgba(255,255,255,0.08)'
    )

    # -----------------------------------------------
    # RIGHT Y AXIS
    # -----------------------------------------------

    fig.update_yaxes(
        title_text='Average Revenue ($)',
        secondary_y=True,
        showgrid=False
    )

    return fig