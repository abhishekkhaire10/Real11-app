# -*- coding: utf-8 -*-
import streamlit as st 
def main():

    st.title('Welcome to Reality 11')
    leagues = ['Select','Premier League','Serie A','La Liga', 'Bundesliga', 'Ligue 1' ]
    league = st.selectbox('Select league', leagues)
    st.write('Selected League: ', league)

            
if __name__ == '__main__':
    main()            
            
            
            
            
        