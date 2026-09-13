import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="IPL Analytics Hub (2008-2020)",
    page_icon="🏏",
    layout="wide"
)

@st.cache_data
def load_data():
    m = pd.read_csv('matches_cleaned.csv')
    d = pd.read_csv('deliveries_cleaned.csv')
    return m, d

matches, deliveries = load_data()

# Detect column names dynamically
batsman_col = 'batsman' if 'batsman' in deliveries.columns else 'batter'
bowler_col = 'bowler' if 'bowler' in deliveries.columns else 'bowling_team'

st.title("🏏 IPL Performance & Strategy Intelligence Dashboard")
st.markdown("Comprehensive match trends, toss impact, and player performance metrics (2008–2020).")

# Sidebar Filter
st.sidebar.header("Filter Options")
teams = sorted(matches['team1'].dropna().unique().tolist())
selected_team = st.sidebar.selectbox("Select Franchise", ["All Teams"] + teams)

# Filter Data
filtered_matches = matches.copy()
if selected_team != "All Teams":
    filtered_matches = filtered_matches[
        (filtered_matches['team1'] == selected_team) | (filtered_matches['team2'] == selected_team)
    ]

# KPI Metrics
col1, col2, col3, col4 = st.columns(4)
total_matches = len(filtered_matches)
total_runs = deliveries['total_runs'].sum()
top_winner = filtered_matches['winner'].value_counts().idxmax() if not filtered_matches.empty else "N/A"
win_count = filtered_matches['winner'].value_counts().max() if not filtered_matches.empty else 0

col1.metric("Total Matches", f"{total_matches}")
col2.metric("Total Tournament Runs", f"{total_runs:,}")
col3.metric("Top Winning Team", f"{top_winner}")
col4.metric("Most Wins", f"{win_count}")

st.divider()

# Row 1 Charts: Wins and Toss
c1, c2 = st.columns(2)

with c1:
    st.subheader("Total Match Wins by Team")
    wins_df = filtered_matches['winner'].value_counts().reset_index()
    wins_df.columns = ['Team', 'Wins']
    fig_wins = px.bar(
        wins_df.head(10), x='Wins', y='Team', orientation='h',
        color='Wins', color_continuous_scale='Blues',
        title="Top 10 Teams by Wins"
    )
    fig_wins.update_layout(yaxis={'categoryorder': 'total ascending'}, height=380)
    st.plotly_chart(fig_wins, use_container_width=True)

with c2:
    st.subheader("Toss Decision Distribution")
    toss_df = filtered_matches['toss_decision'].value_counts().reset_index()
    toss_df.columns = ['Decision', 'Count']
    fig_toss = px.pie(
        toss_df, names='Decision', values='Count',
        hole=0.4,
        color_discrete_sequence=px.colors.sequential.Teal,
        title="Fielding vs Batting Decision"
    )
    fig_toss.update_layout(height=380)
    st.plotly_chart(fig_toss, use_container_width=True)

st.divider()

# Row 2 Charts: Batting & Bowling Leaders
c3, c4 = st.columns(2)

with c3:
    st.subheader("Top 10 Batsmen (Orange Cap Contenders)")
    top_bat = deliveries.groupby(batsman_col)['batsman_runs'].sum().reset_index()
    top_bat.columns = ['Player', 'Runs']
    top_bat = top_bat.sort_values(by='Runs', ascending=False).head(10)
    
    fig_bat = px.bar(
        top_bat, x='Player', y='Runs',
        color='Runs', color_continuous_scale='Oranges',
        title="Leading Run Scorers"
    )
    fig_bat.update_layout(xaxis_tickangle=-45, height=400)
    st.plotly_chart(fig_bat, use_container_width=True)

with c4:
    st.subheader("Top 10 Bowlers (Purple Cap Contenders)")
    if 'dismissal_kind' in deliveries.columns:
        valid_wickets = deliveries[deliveries['dismissal_kind'].isin([
            'caught', 'bowled', 'lbw', 'stumped', 'caught and bowled', 'hit wicket'
        ])]
        top_bowl = valid_wickets[bowler_col].value_counts().reset_index().head(10)
        top_bowl.columns = ['Player', 'Wickets']
        
        fig_bowl = px.bar(
            top_bowl, x='Player', y='Wickets',
            color='Wickets', color_continuous_scale='Purples',
            title="Leading Wicket Takers"
        )
        fig_bowl.update_layout(xaxis_tickangle=-45, height=400)
        st.plotly_chart(fig_bowl, use_container_width=True)
    else:
        st.info("Wicket data not available for plotting.")
