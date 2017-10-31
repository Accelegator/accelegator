import queries
def repl(command, DATAFRAME, key1, key2):

    if command == "list":
        queries.query_list(dataframe)

    if command == "show":
        if key2 == "":
            queries.query_show(dataframe, key1)
        else:
            queries.query_show_field(dataframe, key1, key2)

    if command == "search":
        if key2 == "":
            queries.query_search(dataframe, key1)
        else:
            queries.query_search_field(dataframe, key1, key2)

    if command == "latest":
        queries.determine_latest(dataframe, key1, key3, key4 )
