def get_todos():
    with open("file.txt", "r")as file:
        liste = file.readlines()
        return liste


def write_todos(yaz):
    with open("file.txt", "w")as file:
        file.writelines(yaz)