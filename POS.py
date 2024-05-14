import streamlit as st
import nltk
from annotated_text import annotated_text
import pandas as pd

st.set_page_config(page_title="Annotate POS")
st.title('Annotate Parts of Speech')


posData = pd.read_csv('pos_info.csv')
# st.dataframe(posData[['Tag', 'Family', 'Description']])


def input_():
    inp = st.text_input('Enter your sentence')

    options = st.sidebar.multiselect('Choose POS you want to see', ['Noun', 'Pronoun', 'Verb', 'Adverb', 'Adjective'],
                                     ['Noun', 'Pronoun', 'Verb', 'Adverb', 'Adjective'])

    if len(inp) > 0:
        print('searching.', inp, options)

        tokenized = nltk.word_tokenize(inp)
        ans = nltk.pos_tag(tokenized)
        print(ans)

        # st.write(ans)

        annotatedString = []

        for i in range(len(ans)):
            tag = ans[i][1]
            fam = posData.query('Tag == @tag')['Family'].values[0]
            # print(tag, '=', ans[i][0], fam)

            if fam in options:
                print(tag, '=', ans[i][0], fam)
                if fam == 'Noun':
                    annotatedString.append((f"{ans[i][0]}", f"{fam.title()}", '#F2D03A'))
                    annotatedString.append(' ')
                elif fam == 'Pronoun':
                    annotatedString.append((f"{ans[i][0]}", f"{fam.title()}", '#9BD916'))
                    annotatedString.append(' ')
                elif fam == 'Verb':
                    annotatedString.append((f"{ans[i][0]}", f"{fam.title()}", '#46EBE8'))
                    annotatedString.append(' ')
                elif fam == 'Adverb':
                    annotatedString.append((f"{ans[i][0]}", f"{fam.title()}", '#BFC7BF', 'black'))
                    annotatedString.append(' ')
                elif fam == 'Adjective':
                    annotatedString.append((f"{ans[i][0]}", f"{fam.title()}", '#535C68', 'white'))
                    annotatedString.append(' ')
            else:
                annotatedString.append((f"{ans[i][0]}", "", '#F5BCBA'))
                annotatedString.append(' ')
                
        annotated_text(annotatedString)
        # print(annotatedString)

input_()
