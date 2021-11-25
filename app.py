import streamlit as st
import pandas as pd
import time

st.write(""" # Web Scraping App """)

movie_db = pd.read_csv('./csvfiles/moviedb.csv')

genre_list = movie_db['genre'].str.split(',').explode()
actors_list = movie_db['actors'].str.split(',').explode()
movie_db['duration'] = movie_db['duration'].fillna(0)
movie_db['duration'] = movie_db['duration'].apply(lambda f: format(f, '.1f'))
movie_db['duration'] = pd.to_datetime(movie_db['duration'], unit='m').dt.strftime('%H:%M')
movie_db['years'] = movie_db['years'].fillna(0)
movie_db['years'] = movie_db['years'].apply(lambda f: format(f, '.0f'))
movie_db['note'] = movie_db['note'].apply(lambda f: format(f, '.1f'))
movie_db['genre'] = movie_db['genre'].fillna('')
movie_db['original_title'] = movie_db['original_title'].fillna('')
movie_db['synopsis'] = movie_db['synopsis'].fillna('')
movie_db['public'] = movie_db['public'].fillna('')

country_list = movie_db['original_country'].str.split(',').explode().value_counts()


st.write('### Top 250 greatest movies ')
st.write(movie_db)

my_cont = st.container() 


def search_by_name():
    title_df = movie_db[movie_db['title'].str.contains(by_title_input)]
    
    return st.write('### Your researched movie :', title_df)

def search_by_actor():
    
    actor_df = movie_db[movie_db['actors'].str.contains(by_actor_input)]
    
    return st.write(f'### The movies with {by_actor_input} :', actor_df)

def search_by_genre():
    genre_df = movie_db[movie_db['genre'].str.contains(by_genre_input)]
    
    return st.write(f'### All the {by_genre_input} related movies :', genre_df)

def search_by_duration():
    duration_df = movie_db[movie_db['duration'].astype(str).str.contains(str(by_duration_input))]
    
    return st.write(f'### Movies that length {by_duration_input} :', duration_df)

def search_by_rating():    
    rating_df = movie_db[movie_db['note'].astype(str).str.contains(str(by_rating_input))]

    return st.write(f'### Movies rated with {by_rating_input} :', rating_df)

by_title_input = st.sidebar.selectbox("Search by title", movie_db['title'].unique())
by_actor_input = st.sidebar.selectbox("Search by actor", actors_list.unique())
by_genre_input = st.sidebar.selectbox("Search by genre", genre_list.unique())
by_duration_input = st.sidebar.selectbox("Search by duration", sorted(movie_db['duration'].unique(), reverse=True))
by_rating_input = st.sidebar.selectbox("Search by rating", sorted(movie_db['note'].unique(), reverse=True))
yes_top_ten = st.sidebar.button("You want to see a cool graph ???")
start_load = st.sidebar.button("load load")

with my_cont:
    if by_title_input:
        search_by_name()
    if by_actor_input:
        search_by_actor()
    if by_genre_input:
        search_by_genre()
    if by_duration_input:
        search_by_duration()
    if by_rating_input:
        search_by_rating()
    if yes_top_ten:
        st.write('### Number of movie for each countries')
        st.bar_chart(country_list)
    if start_load:
        my_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.1)
            my_bar.progress(percent_complete + 1) 