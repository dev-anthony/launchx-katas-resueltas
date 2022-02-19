# Agregamos una validacion con try/except para evitar que el programa se cierre

# En esta sección para ejecutar archivos sin permisos de ejecución, no conozco muy bien
# como cambiar el permiso de un archivo en windows por lo que omití esta parte, una disculpa :'(

def main():
    try:
        configuration = open('config.txt');
        for line in configuration:
            print(line);

    except OSError as err:
     if err.errno == 2:
         print("Couldn't find the config.txt file!")
     elif err.errno == 13:
         print("Found config.txt but couldn't read it")

    # except FileNotFoundError as FnF:
    #     print(FnF);
    #     print("El archivo no existe");
    # except IsADirectoryError:
    #     print("Found config.txt but it is a directory, couldn't read it");
    # except (BlockingIOError, TimeoutError):
    #     print("Filesystem under heavy load, can't complete reading configuration file");

if __name__ == '__main__':
    main()
