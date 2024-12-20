# Warsztat – Konfiguracja bazy danych

Projekt zawiera skrypt create_db.py, który:

- Tworzy bazę danych workshop (jeśli już istnieje, informuje o tym).
- Tworzy tabele users i messages.
- Obsługuje błędy takie jak `DuplicateDatabase`, `DuplicateTable`, `OperationalError`.
- Zamyka połączenia po zakończeniu pracy.

## Instrukcja uruchomienia

1. **Zainstaluj wymagane biblioteki**:
Aby uruchomić skrypt, musisz mieć zainstalowane odpowiednie biblioteki Pythona, w tym `psycopg2` (do obsługi bazy danych PostgreSQL)
Skonfiguruj połączenie z bazą danych: Upewnij się, że masz dostęp do serwera PostgreSQL i poprawnie skonfigurowaną bazę danych. Skrypt zakłada, że baza danych PostgreSQL jest dostępna i poprawnie skonfigurowana na Twoim serwerze.
Uruchom skrypt: Aby uruchomić skrypt create_db.py, przejdź do katalogu, w którym znajduje się ten plik, a następnie uruchom go:

python create_db.py

Skrypt utworzy bazę danych workshop, jeśli jeszcze jej nie ma, oraz tabele users i messages. W przypadku wystąpienia błędów, skrypt wyświetli odpowiednie komunikaty.
Obsługa błędów: Skrypt obsługuje kilka rodzajów błędów:

    DuplicateDatabase – gdy baza danych już istnieje.
    DuplicateTable – gdy tabela już istnieje.
    OperationalError – ogólny błąd operacyjny związany z połączeniem lub zapytaniami do bazy danych.

Zamknięcie połączeń: Po zakończeniu pracy skrypt automatycznie zamknie połączenie z bazą danych.