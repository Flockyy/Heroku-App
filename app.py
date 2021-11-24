import streamlit as st
import pandas as pd

st.write("""
# Web Scraping App
""")

movie_db = pd.read_csv('./csvfiles/moviedb.csv')

def search_by_name():
    name_indexes = movie_db.index[movie_db['actors'].str.contains(by_name_input)].tolist()
    
    return st.write(movie_db.iloc[name_indexes])

def search_by_actor():
    pass

def search_by_genre():
    pass

def search_by_length():
    pass

def search_by_rating():
    pass

by_name_input = st.text_input("Search by name", on_change=search_by_name)

by_actor_input = st.text_input("Search by actor", on_change=search_by_actor)

by_genre_input = st.text_input("Search by genre", on_change=search_by_genre)

by_length_input = st.text_input("Search by length", on_change=search_by_length)

by_rating_input = st.text_input("Search by rating", on_change=search_by_rating)

st.dataframe(movie_db)

top_100_highest_rated = movie_db['note'].nlargest(n=10)
st.bar_chart(top_100_highest_rated)