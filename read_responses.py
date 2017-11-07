import csv
from pathlib import Path
import pandas
from accelegator_NLP import gensim_analysis
""" Reads the .cvs file and returns the information stored inside """


def read_responses_question(data, arg2):
    (rows, columns) = data.shape
    responses = list()
    # Checking if the argument passed was an in representing the question
    # number
    if(isinstance(arg2, int)):
        column = arg2
        column += 1
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
