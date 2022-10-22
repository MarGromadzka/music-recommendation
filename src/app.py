import streamlit as st

st.title('Music Recommendations')
n_songs = st.slider("How many songs would you like on your playlist?", min_value=1, max_value=50, value=30)


mood = st.multiselect('Mood', ['happy', 'sad', 'angry'])
mood_impact = st.slider("How much should mood impact your playlist?", min_value=1, max_value=100, value=50)


situation = st.multiselect('Situation', ['Party', 'Gym', 'Deep focus', 'In the background'])
situation_impact = st.slider("How much should situation impact your playlist?", min_value=1, max_value=100, value=50)

tempo = st.selectbox('Tempo', ['Fast', 'Medium', 'Slow'])
tempo_impact = st.slider("How much should tempo impact your playlist?", min_value=1, max_value=100, value=50)

key_sounds = st.multiselect('Key sounds', ['guitar', 'male voice', 'female voice', 'piano'])
key_sounds_impact = st.slider("How much should key_sounds impact your playlist?", min_value=1, max_value=100, value=50)

similar_users = st.checkbox('I want songs listened by similar users to be included')
similar_users_impact = st.slider("How much should similar users impact your playlist?", min_value=1, max_value=100, value=50)

top_hits = st.checkbox('I want most listened songs to be included')
top_hits_impact = st.slider("How much should top hits impact your playlist?", min_value=1, max_value=100, value=50)

st.button('Create playlist')
