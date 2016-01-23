#####Instrukcja instalacji wtyczki RISE służącej do obsługi interaktywnego pokazu slajdów<br>
Konfigurację przeprowadzono z wykorzystaniem Pythona w wersji 3.5.1.<br>
Wszelnie uwagi na temat instalacji RISE pod Pythonem 2.X mile widziane<br>
W zależności od wersji IPythona należy pobrać repozytorium z odpowiedniej gałęzi:<br>
https://github.com/damianavila/RISE/releases


# UNIX 

1. Pobierz potrzebne pliki z repozytorium https://github.com/damianavila/RISE.git<br>
   ```
   cd
   git clone https://github.com/damianavila/RISE.git
   ```
           
2. Do instalacji należy wykorzystać skrypt `setup.py`, jednak wcześniej trzeba ustawić zmienną<br>
   JUPYTER_CONFIG_DIR dodając do pliku `~/.bashrc` następującą linię:<br><br>
   UWAGA - alternatywnie można wykonać kroki opisane w podpunkcie 3.<br>
   
   `export JUPYTER_CONFIG_DIR="<home_directory>/.jupyter/:$JUPYTER_CONFIG_DIR"`
   
   Przydatna może być też zmienna JUPYTER_PATH:
   
   `export JUPYTER_PATH="<home_directory>/.local/share/jupyter/:$JUPYTER_PATH"`
   
3. Zamiast ustawiać zmienną JUPYTER_CONFIG_DIR, można uruchomić instalację poleceniem<br>
`JUPYTER_CONFIG_DIR=<path_to_config> python setup.py install`<br>
Efekt powiniene być ten sam, naturalnie korzystając z tego rozwiązania należy pominąć punkt 4.
   
4. Użyj skryptu `setup.py` aby zainstalować wtyczkę

```
cd RISE/
python setup.py install
```

Sprawdzenie instalacji:

Po otwarciu w jupyter nootebook dowolnego wykładu w menu toolbar powinna pojawić <br>
się nowa ikona : "Enter/Exit Live Reveal Slideshow" (wygląda jak histogram)<br>
```
cd <path_to_python-lecture>
jupyter notebook LX.ipynb
```

## WAŻNE

Aby uzyskać najlepszy efekt, należy zmienić domyślny rozmiar czcionki<br>
(inaczej niektóre slajdy nie mieszczą się na ekranie)


Żeby to zrobić, należy zmodyfikować następujący plik <br>
(Szablon używany w tych wykładach to 'simple')<br>
`<path_to_RISE>/livereveal/reveal.js/css/theme/simple.css`<br><br>


W linii 19. parametr `font-size` powinien przyjmować wartość 16px:<br>
`font-size: 16px;`

Jeżeli w użyciu byłby inny szablon, należy znaleść go w folderze /theme<br>
i odpowiednio zmodyfikować wartość `font-size`

Po wykonaniu powyższych czynności można cieszyć się interaktywnym pokazem slajdów.<br>

Przydatne linki:<br>
https://github.com/agh-glk/python-lecture<br>
https://github.com/damianavila/RISE<br>
https://github.com/damianavila/RISE/releases
