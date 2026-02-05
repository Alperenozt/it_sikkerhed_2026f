# 📘 Skoleprojekt – IT-Sikkerhed (2. semester)

**ID:** Alo001  
**Institution:** Zealand – Sjællands Erhvervsakademi, Næstved

---

### 🛡️ Projektbeskrivelse
Dette repository indeholder et skoleprojekt udarbejdet som en del af **IT-Sikkerhed-uddannelsen**. Projektet vægter teknisk dokumentation og praktisk implementering af sikkerhedsstandarder.

**Fokusområder:**
* **Programkvalitet:** Ren og vedligeholdelsesvenlig kodebase.
* **Software-sikkerhed:** Beskyttelse mod gængse sårbarheder.
* **Secure Design Principles:** Sikkerhed indtænkt fra første kodelinje.

*Projektet er udviklet i overensstemmelse med læringsmålene i studieordningen.*

Mine opgaver for neden 
dato: 04-02-2026 

![alt image](https://github.com/Alperenozt/it_sikkerhed_2026f/blob/f472f8b44438062d3497f3799dd4794e812cc521/unittest1.png)

Min egen repo -test 
![alt image](https://github.com/Alperenozt/it_sikkerhed_2026f/blob/e1c9788759eeafa1897eeb48c9aa0c959f3d093d/minegenrepounittest.png)

Auto test igang ved push

![alt image](https://github.com/Alperenozt/it_sikkerhed_2026f/blob/e1c9788759eeafa1897eeb48c9aa0c959f3d093d/Auto%20test%20push%20igang%20-.png)

Auto test push afsluttet

![alt image](https://github.com/Alperenozt/it_sikkerhed_2026f/blob/e1c9788759eeafa1897eeb48c9aa0c959f3d093d/Auto%20test%20push%20afsluttet%20.png)

Detaljeret beskrivelse af test - i action

![alt image](https://github.com/Alperenozt/it_sikkerhed_2026f/blob/e1c9788759eeafa1897eeb48c9aa0c959f3d093d/Detaljeret%20beskrivelse%20af%20test%20i%20action.png)

Ny branch for test - alt rettet 

![alt image](https://github.com/Alperenozt/it_sikkerhed_2026f/blob/e1c9788759eeafa1897eeb48c9aa0c959f3d093d/Ny%20branch%20test%20-%20alt%20rettet%20.png)

# Password-sikkerhed i et login-system

Dette projekt demonstrerer forskellige software-testteknikker anvendt på et simpelt login-system. Fokus er på password-sikkerhed, herunder input-validering, grænseværdier, brute-force beskyttelse og CRUD-operationer.

---

## 1) Ækvivalensklasser

Formål: Opdele input i gyldige og ugyldige grupper.

### Eksempel – Brugernavn (3–20 tegn)

| Klasse | Eksempel | Beskrivelse | Forventning |
|--------|----------|-------------|-------------|
| Gyldig | "abc" | Minimum gyldig længde | Accepteres |
| Gyldig | "brugernavn123" | Normal længde | Accepteres |
| Ugyldig | "ab" | For kort | Afvises |
| Ugyldig | "" | Tom streng | Afvises |
| Ugyldig | "a"*21 | For langt | Afvises |

Testfil: test_aekvivalensklasser.py  
Funktion: validate_username()

---

## 2) Grænseværdianalyse

Formål: Teste værdier omkring en kritisk grænse.

### Eksempel – Password længde (min. 8 tegn)

| Test | Password | Forventning |
|------|----------|-------------|
| Lige under | "1234567" | Afvist |
| Lige på | "12345678" | Gyldig |
| Lige over | "123456789" | Gyldig |

Testfil: test_graensevaerdi.py  
Funktion: validate_password()

---

## 3) CRUD(L)

CRUD bruges til at teste hele livscyklussen for en bruger.

- Create: system.create_user("alice", "password123")
- Read: system.users["alice"]
- Update: system.users["alice"] = "nytpassword"
- Delete: del system.users["alice"]

Testfil: test_crud.py

---

## 4) Cycle Process Test

Formål: Teste hele login-flowet inkl. brute-force beskyttelse.

Scenarie:
1. Opret bruger
2. Login korrekt -> "ok"
3. Login forkert 3 gange -> "forkert"
4. Konto låses -> "låst"
5. Selv korrekt password afvises efter låsning

Testfil: test_cycle_process.py

---

## 5) Decision Table Test

Formål: Teste alle kombinationer af login-regler.

| Regel | Password korrekt | Konto låst | Resultat |
|-------|------------------|------------|----------|
| R1 | Ja | Nej | ok |
| R2 | Nej | Nej | forkert |
| R3 | Nej | Ja | låst |
| R4 | Ja | Ja | låst |

Testfil: test_decision_table.py

---

## 6) Testpyramiden

Unit tests:
- Validering af brugernavn
- Validering af password
- Login med korrekt password
- Fejltæller

Integration tests:
- CRUD + login
- Kontolåsning

System tests:
- Hele login-flowet

Testfil: test_unit_example.py

---

## 7) Security Gates

| Gate | Hvad testes |
|------|-------------|
| Code/Dev Gate | Unit tests for password, brugernavn, login |
| Input Validation Gate | Ækvivalensklasser og grænseværdier |
| Integration Security Gate | Cycle process (brute-force) |
| System Security Gate | Decision table |
| Release Gate | CRUD + login samlet |

---

## Testkørsel

Kommando:

---

### 💻 Terminal & Status

```text
      /\_/\      .-----------------------.
     ( o.o )     |  Coding in progress.. |
      > ^ <      '-----------------------'

          ________________________________________________
         /                                                \
         |  >_ System.out.println("Hello, Zealand!");      |
         |  >_ Loading learning modules...                 |
         |  [==================================>] 100%     |
         \________________________________________________/
                ||                           ||
                ||      ________________     ||
                ||     |                |    ||
                ||     |      AL0001    |    ||
                ||     |________________|    ||
                ||                           ||
         _______||___________________________||_______
        /                                             \
       /        ZEALAND ERHVERVSAKADEMI - 2026         \
      /_________________________________________________\
UNIT TEST - LEG OPGAVE


