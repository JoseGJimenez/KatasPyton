def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it!")
    except PermissionError:
        print ("Archivo encontrado pero requiere permiso para leer!")

if __name__ == '__main__':
    main()