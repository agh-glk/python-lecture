python-lecture
==============

Wykłady z Pythona na AGH w formacie Jupyter Notebook.

Ten wykład dotyczy Pythona w wersji 3.x.

Gałąź python2x (https://github.com/agh-glk/python-lecture/tree/python2x) dotyczy... Pythona 2.x, ale nie jest aktualizowana jeszcze dłużej niż sam Python 2. 

### Jak używać?

#### Na Linuksie (Debian i podobne)

https://jupyter.org/install

W celu uruchomienia Jupyter Notebooka (dawniej IPython Notebook) należy:

0. Zainstaluj dodatkowe pakiety systemowe (jeśli jeszcze ich nie masz):
  
  ```
  $ sudo apt-get install git python3-pip
  ```

1. Zainstaluj pełny moduł Jupyter:

  ```
  $ sudo pip3 install jupyter
  ```

2. Pobierz źródła:

  ```
  $ git clone https://github.com/agh-glk/python-lecture.git
  ```
  
3. Wejdź do katalogu z wykładem:

  ```
  $ cd python-lecture
  ```

4. (Opcjonalnie) Jeśli chcesz uaktualnić źródła wykładu, wykonaj:

  ```
  $ git pull
  ```

5. Uruchom Notebook:

  ```
  $ jupyter notebook
  ```
  
  albo Jupyter Lab:
  
  ```
  $ jupyter lab
  ```
  
  
Po wykonaniu powyższych czynności, w przeglądarce pod adresem `http://localhost:8888/` powinien odpowiadać Jupyter Notebook/Lab.


#### Na Windowsie

W celu uruchomienia Jupyter Notebooka:

1. Zainstaluj Anacondę: [strona pobierania](http://continuum.io/downloads).

2. Zaktualizuj Anacondę oraz Jupytera:

  ```
  $ conda update conda
  $ conda update jupyter
  ```

3. Pobierz źródła poprzez polecenie w Git Bash (jeśli nie masz Gita, [zainstaluj go](http://git-scm.com/download/win)):

  ```
  $ git clone https://github.com/agh-glk/python-lecture.git
  ```
4. Wejdź do katalogu z wykładem:

  ```
  $ cd python-lecture
  ```

5. (Opcjonalnie) Jeśli chcesz uaktualnić źródła wykładu, wykonaj:

  ```
  $ git pull
  ```

6. Uruchom Notebook:

  ```
  $ jupyter notebook
  ```

Jeśli powyższa komenda nie działa, spróbuj

  ```
  $ jupyter notebook nazwa_pliku.ipynb
  ```

Po wykonaniu powyższych czynności, w przeglądarce pod adresem `http://localhost:8888/` powinien odpowiadać Jupyter Notebook.



### Poprawki zauważonych błędów

Wszelkie erraty i poprawki mile widziane, proszę zrobić fork + pull request. Albo po prostu wysłać maila. 
