# This is a sample Python script.

# import pickle
# from urllib import request

import pandas as pd
import numpy as np
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask, render_template, request

Popular_df = pd.read_pickle('popular.pkl')
pt = pd.read_pickle('pt.pkl')
books = pd.read_pickle('books.pkl')
similarity_scores = pd.read_pickle('similarity_scores.pkl')
avg_Bookrating = pd.read_pickle('avg_Bookrating.pkl')
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


app = Flask(__name__, template_folder='template')


@app.route('/')
def index():
    return render_template('index.html',
                           book_name=list(Popular_df['Book-Title'].values),
                           author=list(Popular_df['Book-Author'].values),
                           image=list(Popular_df['Image-URL-L'].values),
                           votes=list(Popular_df['num_ratings'].values),
                           rating=list(Popular_df['avg_rating'].values)
                           )
@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')
# Press the green button in the gutter to run the script.
@app.route('/recommend_books', methods=['POST'])
def recommend():
    User_Input = request.form.get('User_Input')

    index = np.where(pt.index ==User_Input)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:6]

    ## Similar Items is a list of similar books
    data = []
    for i in similar_items:
        # print(pt.index[i[0]]) ## it is returning the index of the item
        item = []
        ## 0th column will give the Book-Title
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        ## Preparing the data of that similar book, to display it on a webpage
        Ratings = avg_Bookrating[avg_Bookrating['Book-Title'] == pt.index[i[0]]]
        ## extend add as a element of the existing list and where append add the list of that element to the existing  list
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        item.extend(list(Ratings.drop_duplicates('Book-Title')['avg_rating'].values))
        data.append(item)
    print(data)
    return render_template('recommend.html', data=data)

## end of the Function
if __name__ == '__main__':
    print_hi('PyCharm')
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
