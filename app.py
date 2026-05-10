import streamlit as st
from database import init_db, get_all_expenses
from ai_engine import ask_ai
import plotly.express as px
import pandas as pd


init_db()


st.title("💰 AI Finance Insight")


data = get_all_expenses()
df = pd.DataFrame(data)
if not df.empty:
    st.subheader("📝 Список твоїх витрат")
    summary = df.groupby('category')['amount'].sum().reset_index()


    for index, row in summary.iterrows():
        st.markdown(f"### {row['category']}")
        st.markdown(f"**{row['amount']} грн**")
        st.divider()


st.subheader("Додати витрату або запитати пораду")
user_input = st.text_input("Наприклад: 'Купив кросівки за 2500 грн' або 'Дай пораду по бюджету'")


if st.button("Відправити"):
    with st.spinner("ШІ думає..."):
        answer = ask_ai(user_input)
        st.write(answer)
        st.rerun()


if st.button("✨ Отримати AI-аналіз бюджету"):
    advice = ask_ai("Проаналізуй мої останні витрати з бази даних і дай коротку пораду, на чому зекономити.")
    st.info(advice)