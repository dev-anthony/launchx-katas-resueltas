# By: Anthony Solano López

def main():
  try:
    open("/path/to/mars.jpg")
  except FileNotFoundError as err:
    print(err);
    print('El archivo no existe');
if __name__ == '__main__':
    main()
