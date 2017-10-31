import display_list
import display_show
import display_show_with_field
import display_search
import display_search_with_field
import queries
def repl(command, dataframe, key1, key2, key3):

    if command == "list":
        print(display_list(queries.query_list(dataframe)))

    if command == "show":
        if key2 == "":
            print(display_show(queries.query_show(dataframe, key1)))
        else:
            print(display_show_with_field(queries.query_show_field(dataframe, key1, key2)))

    if command == "search":
        if key2 == "":
            print(display_search(queries.query_search(dataframe, key1)))
        else:
            print(display_search_with_field(queries.query_search_field(dataframe, key1, key2)))

    if command == "latest":
        queries.determine_latest(dataframe, key1, key2, key3)
