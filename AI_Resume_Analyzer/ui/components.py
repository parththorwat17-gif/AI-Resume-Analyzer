import streamlit as st

def show_skills(
    matched,
    missing
):

    col1,col2 = st.columns(2)

    with col1:

        st.subheader(
            "✅ Strength Zone"
        )

        for skill in matched:
            st.success(skill)

    with col2:

        st.subheader(
            "🔥 Growth Zone"
        )

        for skill in missing:
            st.warning(skill)