# Projekt (Inżynieria Oprogramowania) - "Projekty Gminne"
Aplikacja internetowa umożliwiająca mieszkańcom gminy głosowanie na wybrane projekty gminne, prowadzone w ramach konkursów organizowanych przez władze gminy.

* * *
## Zawartość
- [Założenia projektowe](#założenia-projektowe)
- [Do zrobienia](#do-zrobienia)
- [Modele bazy danych](#modele-bazy-danych)
- [Administracja](#administracja)
- [Technologie](#technologie)
* * *

### Założenia projektowe
- Konkursy
  - Konkursy dotyczą dzielnic.
  - Jeden konkurs może się składać z wielu projektów. Jeden projekt może należeć do jednego konkursu.
  - Wyłaniany jest jeden zwycięski projekt w ramach konkursu na podstawie ilości oddanych głosów przez mieszkańców.
- Autoryzacja - oddający głosy
  - Autoryzacja polega na wprowadzeniu numeru PESEL. Na jego podstawie wysyłane jest zapytanie do API (symulacja API) i odbierana jest odpowiedź czy dana osoba może zagłosować czy nie. (Brak potrzeby rejestracji mieszkańców)
- Autoryzacja - pracownicy gminy
  - Istnieje konto administratora posiadające nieograniczone prawa.
  - Istnieją konta urzędników mogących tworzyć projekty i modyfikować projekty (lecz w stopniu uniemożliwiającym możliwe przekłamanie głosów, zakończenie konkursu przed czasem itd.).
  - w obu przypadkach następuje logowanie.
- Proces głosowania
  - Po zagłosowaniu dana osoba ma dostęp do ilości głosów oddanych na dany projekt (to bez logowania da się zrobić tylko ciasteczkami i przechowywaniem informacji jaki PESEL na co głosował)
  - Na jeden **poprawny PESEL* przypada jeden głos w danym konkursie.
  - Nie można zmienić raz oddanego głosu.
  - Kiedy następuje remis, organizowana jest dogrywka ze skróconym czasem trwania konkursu.
  - Lista zakończonych konkursów jest wywieszana na stronie z informacją kto wygrał.
  - Rozkład głosów w postaci wykresu słupkowego (na kazdy projekt w ramach konkursu)

**poprawny PESEL* - PESEL poprawny pod względem praw oddania głosu w ramach danej gminy/dzielnicy.

### Do zrobienia
- [ ] favicon.ico
- [ ] Proces zamykania głosowania (w widoku na pewno)


### Modele bazy danych

```
                   +---------+     +-------+
                   | Konkurs |     | Gmina |
                   +---------+     +-------+
                        |              |
                        v              v
       +------+    +---------+     +-----------+
       | Głos +<---+ Projekt +<----+ Dzielnica |
       +------+    +---------+     +-----------+

                 +----------------->
                Jeden              Wiele
```


- Model:Konkurs
  - Nazwa (str)
  - Koniec konkursu (datetime)

- Model:Projekt
  - id (pk)
  - Konkurs (fk)
  - Dzielnica (fk) [Dzielnica miasta - Wikipedia](https://pl.wikipedia.org/wiki/Dzielnica_miasta)
  - Nazwa/Tytuł projektu (str)
  - Okres realizacji od (date)
  - Okres realizacji do (date)
  - Całkowita wartość projektu w PLN (str)
  - Kwota dofinansowania w PLN (str)
  - Dokumentacja projektu .pdf, .doc itd. (file)

- Model:Dzielnica
  - id (pk)
  - Gmina (fk)
  - Nazwa (str)

- Model:Gmina
  - id (pk)
  - Nazwa (str - unique)

- Model:Głos
  - id (pk)
  - Projekt (fk)
  - PESEL (str)

*Do wszystkich modeli dodać date_added i date_modified.

### Administracja
>Panel administracyjny Django

URL: /admin/

Użytkownik: admin

Hasło: 123456789


### Technologie
- Django 2.2
- SQLite3
- Bootstrap 4
- JQuery 3
- PopperJS
- PYTHON 3
