import streamlit as st
from resources import TAGS_LIST
from features.PlaylistGenerator import PlaylistGenerator

st.title('Music Recommendations')

user_id = st.text_input('User id')
st.text(f"Hello {user_id}")


n_songs = st.slider("How many songs would you like on your playlist?", min_value=1, max_value=50, value=25)

tags = st.multiselect('Tags', TAGS_LIST)

show_playlist = st.button('Create playlist')

if show_playlist:
    playlist_generator = PlaylistGenerator(tags, user_id, n_songs)
    st.text(playlist_generator.get_recommendation())
