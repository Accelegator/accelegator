from gensim import corpora, models
from profanity import profanity
from stop_words import get_stop_words
from six import iteritems, viewitems
from colorama import Fore, Style
import logging
import pyLDAvis
import pyLDAvis.gensim
import gensim
import warnings
""" Uses gensim to analyze the text of the responses to accelegator"""


def gensim_analysis(list_responses):
    """Completes the analysis for each answer"""
    warnings.filterwarnings('ignore')
    tokens, nanNum = create_tokens(list_responses)
    if len(list_responses) == nanNum:
        return
    dictionary = dictionary_create(tokens)
    corpus = [dictionary.doc2bow(token) for token in tokens]
    corp_eval(dictionary, tokens, corpus)

    logging.info("Analyzes gensim and returns the repeated words")


def create_tokens(list_responses):
    """Takes in the list of responses and makes each word a token"""
    stoplist = get_stop_words('en')
    texts = []
    tokens = []
    nanNum = 0
    for i in list_responses:
        temp = []
        for i in i:
            if not isinstance(i, int):
                i = i.lower()
                if profanity.contains_profanity(i) is False:
                    if i not in stoplist:
                        if i != 'nan':
                            temp.append(i)
                        if i == 'nan':
                            nanNum += 1
        tokens.append(temp)
    print(tokens)
    return(tokens, nanNum)

    logging.info("creates tokens from the responses")


def dictionary_create(tokens):
    """Creates the dictionary from the tokens of the answer"""
    dictionary = corpora.Dictionary(tokens)
    logging.info("creates a dictionary using the tokens")
    return(dictionary)


def corp_eval(dictionary, tokens, corpus):
    i = len(tokens)
    lda = gensim.models.ldamodel.LdaModel(
        corpus,
        id2word=dictionary,
        num_topics=3,
        passes=1,
        alpha='symmetric',
        eta=None)
    corpus = [dictionary.doc2bow(token) for token in tokens]
    print(lda)
    vis = pyLDAvis.gensim.prepare(lda, corpus, dictionary)
    print(Fore.YELLOW + "These are the current topics:" + Style.RESET_ALL)
    print(lda.print_topics(i))
    print(
        Fore.CYAN +
        "Showing the lda visually, please hit control+c to access the next set of responses:",
        Style.RESET_ALL)
    pyLDAvis.show(vis)
    logging.info("Evaluates the dictionary to see if words are repeated")
    return(dictionary.dfs)


def read_responses_question(data, arg2):
    (rows, columns) = data.shape
    responses = list()
    # Checking if the argument passed was an in representing the question
    # number
    if(isinstance(arg2, int)):
        column = arg2
        texts = []
        for row in range(0, rows):
            texts.append(str(data.iat[row, column]))
        responses = [[word for word in document.split()]for document in texts]
        print(responses)
        gensim_analysis(responses)
    # If the argument is the default it prints every questions responses with
    # analysis
    else:
        for column in range(10, columns):
            print(column)
            texts = []
            for row in range(0, rows):
                # if(str(data.iat[row, column]) != "nan"):
                #     print(data.iat[row, column])
                texts.append(str(data.iat[row, column]))
            print("i am printing the texts")
            print(texts)
            responses = [[word for word in document.split()]
                         for document in texts]
            gensim_analysis(responses)


def read_responses_person(data, arg2):
    (rows, columns) = data.shape
    responses = list()
    column = 1
    texts = []
    for row in range(0, rows):
        if(arg2 == str(data.iat[row, column])):
            exists = True
            row = row
            break
        else:
            exists = False
    if(exists):
        for column in range(10, columns):
            texts.append(str(data.iat[row, column]))
        responses = [[word for word in document.split()]for document in texts]
        print(responses)
        gensim_analysis(responses)
    # runs every single person if the argument is not an email that appears in
    # a list
    else:
        for row in range(0, rows):
            texts = []
            for column in range(10, columns):
                # if(str(data.iat[row, column]) != "nan"):
                #     print(data.iat[row, column])
                texts.append(str(data.iat[row, column]))
            print("i am printing the texts")
            print(texts)
            responses = [[word for word in document.split()]
                         for document in texts]
            gensim_analysis(responses)


def read_responses_all(data):
    texts = []
    (rows, columns) = data.shape
    for row in range(0, rows):
        for column in range(10, columns):
            texts.append(str(data.iat[row, column]))
    responses = [[word for word in document.split()]for document in texts]
    # print(responses)
    gensim_analysis(responses)
