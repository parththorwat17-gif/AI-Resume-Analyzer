import streamlit as st

def show_metrics(
    score,
    role,
    matched
):

    col1,col2,col3,col4 = st.columns(4)

    col1.metric(
        "🚀 Resume Score",
        f"{score}%"
    )

    col2.metric(
        "🎯 Career Match",
        role
    )

    col3.metric(
        "🔥 Skills",
        len(matched)
    )

    col4.metric(
        "💼 Ready",
        "High"
    )