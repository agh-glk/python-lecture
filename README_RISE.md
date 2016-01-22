#####Instrukcja instalacji wtyczki RISE służącej do obsługi interaktywnego pokazu slajdów


# UNIX 

1. Pobierz potrzebne pliki z repozytorium https://github.com/damianavila/RISE.git
```
cd
git clone https://github.com/damianavila/RISE.git
```

2. Do instalacji należy wykorzystać skrypt `setup.py`, jednak wcześniej trzeba ustawić zmienną<br>
   JUPYTER_CONFIG_DIR dodając do pliku `~/.bashrc` następującą linię:<br>
   
   `export JUPYTER_CONFIG_DIR="<home_directory>/.jupyter/:$JUPYTER_CONFIG_DIR"`
   
   Przydatna może być też zmienna JUPYTER_PATH:
   
   `export JUPYTER_PATH="<home_directory>/.local/share/jupyter/:$JUPYTER_PATH"`
   
3. Użyj skryptu `setup.py` aby zainstalować wtyczkę

```
cd RISE/
python setup.py install
```

Sprawdzenie instalacji:

Po otwarciu w jupyter nootebook dowolnego wykładu w menu toolbar powinna pojawić <br>
się nowa ikona : "Enter/Exit Live Reveal Slideshow" (wygląda jak histogram)<br>
```
cd <path_to_python-lecutre>
jupyter notebook LX.ipynb
```

## WAŻNE

Aby uzyskać najlepszy efekt, należy zmienić domyślny rozmiar czcionki<br>
(inaczej niektóre slajdy nie mieszczą się na ekranie)


Żeby to zrobić, należy zmodyfikować następujący plik <br>
(Szablon używany w tych wykładach to 'simple')<br>
`<path_to_RISE>/livereveal/reveal.js/css/theme/simple.css`<br>

W linii 19. parametr `font-size` powinien przyjmować wartość 16px:<br>
`font-size: 16px;`


Po wykonaniu powyższych czynności można cieszyć się interaktywnym pokazem slajdów.<br>

Przydatne linki:<br>
https://github.com/agh-glk/python-lecture<br>
https://github.com/damianavila/RISE
