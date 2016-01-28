#####Instrukcja instalacji wtyczki RISE służącej do obsługi interaktywnego pokazu slajdów<br>
Konfigurację przeprowadzono z wykorzystaniem Pythona w wersji 3.5.1.<br>
Wszelnie uwagi na temat instalacji RISE pod Pythonem 2.X mile widziane<br>
W zależności od wersji IPythona należy pobrać repozytorium z odpowiedniej gałęzi:<br>
https://github.com/damianavila/RISE/releases


# UNIX 

1. Pobierz potrzebne pliki z repozytorium https://github.com/damianavila/RISE.git<br>
   ```
   git clone https://github.com/damianavila/RISE.git
   ```
           
2. Instalacja polega na uruchomieniu skryptu `setup.py` z parametrem install.<br>
3. 
  ```
cd RISE/
python setup.py install
```

   Jeżeli instalacja nie przebiega prawidowo (pojawiaja sie bledy dotyczace JUPYTERa),<br>
   Należy dodatkowo ustawić zmienna `JUPYTER_CONFIG_DIR`. Prawdopodobnie powinna wskazywać na <br>
   `~/.jupyter`, szczegolowy opis znaduje sie tutaj: http://jupyter-core.readthedocs.org/en/latest/paths.html <br><br>
`JUPYTER_CONFIG_DIR=<path_to_config> python setup.py install`<br>


#### Sprawdzenie instalacji:

Po otwarciu w jupyter nootebook dowolnego wykładu w menu toolbar powinna pojawić <br>
się nowa ikona : "Enter/Exit Live Reveal Slideshow" (wygląda jak histogram)<br>
```
cd <path_to_python-lecture>
jupyter notebook LX.ipynb
```

##### !!!
   Aby osiagnac najlepszy efekt zaleca sie wykonanie instrukcji<br>
   zawartej w dziale <b>WAŻNE</b>

# Windows

1. Pobierz potrzebne pliki z repozytorium https://github.com/damianavila/RISE.git<br>
   ```
   git clone https://github.com/damianavila/RISE.git
   ```
   (jeżeli nie masz Gita - zainstaluj go)<br>
   
2. W tym przypadku nie jest konieczne ustawianie żadnych zmiennych,<br>
   należy przejć do folderu RISE i rozpoczć instalacje:<br>
   ```
   cd <path_to_RISE>
   python setup.py install
   ```
   
3. Instalacja powinna zakończyć sie bez żadnych bledów<br>
   Aby zweryfikować, sprawdź czy możesz wlaczyc pokaz slajdów<br>
   tak jak opisano w <b>Sprawdzenie instalacji</b> w dziale powswieconym<br>
   instalacji na UNIX.<br><br>


## WAŻNE
#### Jak tylko znajde dobry sposob od razu zamieszcze rozwiazanie w tym miejscu

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
https://github.com/damianavila/RISE/releases<br>
https://github.com/damianavila/RISE.git
