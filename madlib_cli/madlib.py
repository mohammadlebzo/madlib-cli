import re


def print_message():
    """
    This function returns the welcoming message for the user, where we can tell the user what we are doing.
        :return: string
    """
    return """
    *************************************
    *** Welcome to my Madlib CLI game ***
    ***      The rules are simple     ***
    ***    Enter the requested words  ***
    ***   One by one, and in the end  ***
    *** You will get a paragraph with ***
    ***   All the words you entered   ***
    ***        OK! Let's start        ***
    *************************************
    """


def read_template(file_path):
    """
    This function takes a string, which is the path of a file, after that it opens and reads the file,
    finally it returns the content of the file as a string.
        :param file_path: A string
        :return: string
    """
    with open(file_path.replace("/", "\\"), "r") as text_file:
        return text_file.read()


def parse_template(txt_string):
    """
    This function takes a string and replaces all the curly brackets and their content, with empty curly brackets.
    As for the content of the curly brackets, they are all placed into a tuple, for later use.
        :param txt_string: A string
        :return: string, tuple
    """
    return re.sub(r"{.*?}", "{}", txt_string), tuple(re.findall(r"{(.*?)}", txt_string))


def merge(txt_string, parts_list):
    """
    This function takes a string format and the user input,
    after that it merges them together where the placeholders are located.
        :param txt_string: the string format
        :param parts_list: A list
        :return: string
    """
    temp_str = txt_string
    for i in parts_list:
        temp_str = re.sub(r"{}", i, temp_str, 1)

    return temp_str


def input_receiver(parts_list):
    """
    This function takes the user input according to a given list of requirements, and then store it in a list.
        :param parts_list: A list
        :return: list
    """
    user_input_list = []
    for i in parts_list:
        user_input = input(f"Please enter ({i}) :")
        user_input_list.append(user_input)

    return user_input_list


def program_manager():
    """
    This function is the manager for the program, printing the final result.
    """
    print(print_message())
    print(merge(parse_template(read_template("assets\\madlib_cli.txt"))[0],
                input_receiver(parse_template(read_template("assets\\madlib_cli.txt"))[1])))


if __name__ == "__main__":
    program_manager()
    # print(read_template('assets\\dark_and_stormy_night_template.txt'))
    # print(text_file_path)
    # print(parse_template(read_template("assets\\madlib_cli.txt"))[1])
    # print(merge(parse_template(read_template("assets\\madlib_cli.txt"))[0],
    #             parse_template(read_template("assets\\madlib_cli.txt"))[1]))
