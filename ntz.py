import sys
import dictionary as dictionary
import yaml

FILEPATH = 'note_storage.yaml'


def yaml_loader(filepath: str) -> dictionary:
    """
    Loads a yaml file specified by the filepath and returns it as a dictionary
    :param filepath: A string containing the filepath to load
    :return: A dictionary containing the contents of the yaml file
    """
    with open(filepath, 'r') as file_descriptor:
        data = yaml.load(file_descriptor, Loader=yaml.FullLoader)
    return data


def yaml_dump(filepath: str, data: dictionary):
    """
    Saves contents of data to the yaml file specified by the filepath.
    :param filepath: A string containing the name of the file to save to.
    :param data: A dictionary containing the notes to save.
    :return: None
    """
    with open(filepath, 'w') as file_descriptor:
        yaml.dump(data, file_descriptor)


def get_arguments() -> list:
    """
    Gets arguments from user.
    :return: A list containing the arguments.
    """
    if len(sys.argv) <= 1:
        return -1
    return sys.argv


def get_user_note() -> str:
    """
    Gets contents of the note entered by user.
    :return: A string containing the note.
    """
    return get_arguments()[2]


def display_all():
    """
    Displays all categories and notes within those categories.
    :return: None
    """
    data = yaml_loader(FILEPATH)
    if len(data) < 1:
        print("No notes or categories!")
    else:
        for category in data.keys():
            print(f"{category}:")
            for index, note in enumerate(data[category], start=1):
                print(f"{'':2} ({index}) {note}")


def display_notes(data: dictionary, category: str):
    """
    Prints all notes from given category.
    :param data: A dictionary containing all categories and notes.
    :param category: A string representing the category that contains the notes.
    :return: None
    """
    for index, note in enumerate(data[category], start=1):
        print(f"({index}) {note}")


def display_categories(data: dictionary):
    """
    Prints all categories.
    :param data: A dictionary containing all categories and notes.
    :return: None
    """
    for category in data.keys():
        print(category)


def sort_notes(data: dictionary) -> dictionary:
    """
    Sorts data by keys (category name)
    :param data: A dictionary containing all categories and notes.
    :return:
    """
    return dict(sorted(data.items()))


def remember(data: dictionary):
    """
    Saves a note if entered at command line. Otherwise prompts user for category and note to be entered.
    :param data: A dictionary containing all categories and notes.
    :return: None
    """
    if len(get_arguments()) == 3:
        note = get_arguments()[2]
    else:
        note = input("Enter note: ")
    category = input("Add to category? (1)Yes or (2)No: ")
    if category == 'yes' or category == 'y' or category == '1':
        while True:
            display_categories(data)
            category_choice = input("Choose Category: ")
            if category_choice in data.keys():
                data[category_choice].append(note)
                print(f'Successfully added to {category_choice}!')
                break
            print('Category not found.')
    elif category == 'no' or category == 'n' or category == '2':
        if 'other' in data.keys():
            data['other'].append(note)
        else:
            data['other'] = [note]
    yaml_dump(FILEPATH, data)
    print("Note remembered!")


def create_category(data: dictionary):
    """
    Creates a category based on argument from command line. If none input, it will prompt user.
    :param data: A dictionary containing all categories and notes.
    :return: None
    """
    if len(get_arguments()) == 3:
        category_name = get_arguments()[2]
    else:
        category_name = input("Enter new category name: ")
    data[category_name] = []
    yaml_dump(FILEPATH, sort_notes(data))
    print(f"Successfully created {category_name} category!")


def forget_note(data: dictionary):
    """
    Prompts user for category and individual note to delete.
    :param data: A dictionary containing all categories and notes.
    :return: None
    """
    display_categories(data)
    category_choice = input("Choose Category: ")
    if len(data[category_choice]) > 0:
        display_notes(data, category_choice)
        note_choice = int(input('Choose Note to delete: '))
        data[category_choice].remove(data[category_choice][note_choice - 1])
        print(f"Successfully deleted note!")
    else:
        print("No notes in this category!")


def forget_category(data: dictionary):
    """
    Deletes a category as well as notes within category.
    :param data: A dictionary containing all categories and notes.
    :return: None
    """
    display_categories(data)
    category_choice = input("Choose Category: ")
    del data[category_choice]
    print("Successfully deleted category!")


def forget(data: dictionary):
    """
    Prompts user for a note or a category to delete.
    :param data: A dictionary containing all categories and notes.
    :return: None
    """
    category_or_note = input("Forget (1)Note or (2)Category? ")
    if category_or_note == '1':
        forget_note(data)
        yaml_dump(FILEPATH, data)
    elif category_or_note == '2':
        forget_category(data)
        yaml_dump(FILEPATH, data)
    else:
        print("Invalid selection!")


def edit_note(data: dictionary):
    """
    Prompts user for a note to edit.
    :param data: A dictionary containing all categories and notes.
    :return:
    """
    display_categories(data)
    category_choice = input("Choose Category: ")
    display_notes(data, category_choice)
    if len(data[category_choice]) > 0:
        note_choice = int(input('Choose Note to edit: '))
        new_note = input("Enter new note: ")
        data[category_choice][note_choice - 1] = new_note
        yaml_dump(FILEPATH, sort_notes(data))
        print("Successfully edited note!")
    else:
        print("No notes in this category!")


def edit_category_name(data: dictionary):
    """
    Prompts user for a category name to edit.
    :param data: A dictionary containing all categories and notes.
    :return:
    """
    display_categories(data)
    category_choice = input("Choose Category: ")
    if category_choice in data.keys():
        new_category = input("Enter new category name: ")
        data.update({new_category: data[category_choice]})
        del data[category_choice]
        yaml_dump(FILEPATH, sort_notes(data))
        print("Successfully edited category name!")
    else:
        print("Category not found!")


def edit(data):
    """
    Prompts user for a note or category to edit.
    :param data: A dictionary containing all categories and notes.
    :return: None
    """
    category_or_note = input("Edit (1)Note or (2)Category? ")
    if category_or_note == '1':
        edit_note(data)
    elif category_or_note == '2':
        edit_category_name(data)


def create_and_remember(category: str, note: str):
    """
    If category already exists, it will add given note to it. If it doesn't, it will create new category and add note to new category.
    :param category: A string representing the category to save to.
    :param note: A string representing the note to save.
    :return: None
    """
    data = yaml_loader(FILEPATH)
    if category in data.keys():
        data[category].append(note)
        print(f"Successfully created note and added to {category} category!")
    else:
        data[category] = [note]
        print(f"Successfully created {category} category and added note!")
    yaml_dump(FILEPATH, data)


def clear(data: dictionary):
    """
    Clears all categories and notes.
    :param data: A dictionary containing all categories and notes.
    :return: None
    """
    delete = input("Are you sure you want to delete all notes? (1)Yes or (2)No.").strip().lower()
    if delete == '1' or delete == 'yes' or delete == 'y':
        data.clear()
        yaml_dump(FILEPATH, data)
        print("Successfully deleted all notes!")


def command_menu(user_input: str):
    """
    Runs specified command based on user input from command line.
    :param user_input: A string representing the command the user wants to run.
    :return:
    """
    data = yaml_loader(FILEPATH)
    commands = {
        'r': remember,
        '-c': create_category,
        'f': forget,
        'e': edit,
        'clear': clear,
    }
    return commands[user_input](data)


# main function
def cli():
    if get_arguments() == -1:
        display_all()
    elif len(get_arguments()) == 5:
        create_and_remember(get_arguments()[4], get_arguments()[3])
    else:
        command_menu(get_arguments()[1])


# run the main function
cli()
