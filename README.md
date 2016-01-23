python-lecture
==============

Wykłady z Pythona na AGH w formacie IPython Notebook.

Ten wykład dotyczy Pythona w wersji 3.x.
Jeśli jesteś zainteresowany wykładem dla Pythona 2.x, odwiedź gałąź python2x (https://github.com/agh-glk/python-lecture/tree/python2x)

### Jak używać?

#### Na Linuksie (Ubuntu 14.04)

W celu uruchomienia IPython Notebooka należy:

0. Zainstaluj dodatkowe pakiety systemowe, wymagane przy instalacji modułu iPython:
  
  ```
  $ sudo apt-get install git python3-pip
  ```

1. Zainstaluj pełny moduł iPython:

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
  $ ipython notebook
  ```
  
Po wykonaniu powyższych czynności, w przeglądarce pod adresem `http://localhost:8888/` powinien odpowiadać IPython Notebook.


#### Na Windowsie

W celu uruchomienia IPython Notebooka:

1. Zainstaluj Anacondę: [strona pobierania](http://continuum.io/downloads).

2. Zaktualizuj Anacondę oraz IPythona:

  ```
  $ conda update conda
  $ conda update ipython
  ```

3. Zainstaluj Jupytera:

  ```
  $ conda install jupyter
  ```

4. Pobierz źródła poprzez polecenie w Git Bash (jeśli nie masz Gita, [zainstaluj go](http://git-scm.com/download/win)):

  ```
  $ git clone https://github.com/agh-glk/python-lecture.git
  ```
5. Wejdź do katalogu z wykładem:

  ```
  $ cd python-lecture
  ```

6. (Opcjonalnie) Jeśli chcesz uaktualnić źródła wykładu, wykonaj:

  ```
  $ git pull
  ```

7. Uruchom Notebook:

  ```
  $ ipython notebook
  ```

Jeśli powyższa komenda nie działa, spróbuj

  ```
  $ ipython notebook nazwa_pliku.ipynb
  ```

Po wykonaniu powyższych czynności, w przeglądarce pod adresem `http://localhost:8888/` powinien odpowiadać IPython Notebook.

### RISE

Po wykonaniu powyższych czynności można przeglądać zeszyty oraz interaktywnie wykonywać kod.<br>
Instalacja wtyczki RISE umożliwia przeglądanie wykładów w postaci interaktywnego pokazu slajdów.<br>
Opis instalacji tego dodatku znajduje się w pliku README_RISE.md<br>


### Poprawki zauważonych błędów

Wszelkie erraty i poprawki mile widziane, proszę zrobić fork + pull request. 
