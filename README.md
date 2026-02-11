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

**Dato:** 05-02-2026  
**Projekt:** Demonstration af Software-test i Login-systemer
---

## 🛠 Testmetoder og Logik

### 1. Input-validering
Vi sikrer, at systemet kun accepterer data, der overholder de definerede forretningsregler.

#### **Ækvivalensklasser (Brugernavn: 3–20 tegn)**
Ved at opdele input i partitioner sikrer vi fuld dækning uden at teste hver eneste værdi.

| Type | Klasse | Eksempel | Forventet Resultat |
| :--- | :--- | :--- | :--- |
| **Gyldig** | Minimum længde | `"abc"` | ✅ Accepteres |
| **Gyldig** | Normal længde | `"brugernavn123"` | ✅ Accepteres |
| **Ugyldig** | For kort | `"ab"` | ❌ Afvises |
| **Ugyldig** | Tom streng | `""` | ❌ Afvises |
| **Ugyldig** | Over max grænse | `"a" * 21` | ❌ Afvises |

#### **Grænseværdianalyse (Password: min. 8 tegn)**
Vi tester de kritiske punkter lige omkring grænsen ($n-1, n, n+1$), hvor logiske fejl typisk opstår.

| Test Case | Password | Resultat | Test-funktion |
| :--- | :--- | :--- | :--- |
| **Lige under** | `"1234567"` | ❌ Afvist | `validate_password()` |
| **Lige på** | `"12345678"` | ✅ Gyldig | `validate_password()` |
| **Lige over** | `"123456789"` | ✅ Gyldig | `validate_password()` |

---

### 2. Avanceret Sikkerhedslogik

#### **Cycle Process (Brute-force beskyttelse)**
Denne test følger brugerens tilstand gennem et potentielt angreb:
1.  **Oprettelse:** Bruger initialiseres i systemet.
2.  **Success:** Korrekt login giver adgang.
3.  **Fejl:** Tre forkerte forsøg trigger en spærring.
4.  **Lockout:** Kontoen låses, og selv et korrekt password afvises, indtil nulstilling.



#### **Decision Table (Beslutningstabel)**
For at dække alle logiske kombinationer af systemtilstande:

| Regel | Password korrekt | Konto låst | Resultat |
| :--- | :---: | :---: | :--- |
| **R1** | Ja | Nej | `ADGANG GIVET` |
| **R2** | Nej | Nej | `ADGANG NÆGTET` |
| **R3** | Nej | Ja | `KONTO LÅST` |
| **R4** | Ja | Ja | `KONTO LÅST` |

---

### 3. CRUD(L) Livscyklus
Vi verificerer, at brugerdata kan håndteres sikkert gennem hele forløbet:
* **Create:** `system.create_user()`
* **Read:** `system.get_user()`
* **Update:** Opdatering af password/legitimation.
* **Delete:** Sikker sletning af brugerprofil.

---

## 🏗 Testpyramiden & Gates

Vi følger en lagdelt teststruktur for at sikre stabilitet:

* **Unit Tests:** Hurtig validering af enkeltfunktioner (username/password regler).
* **Integration Tests:** Samspil mellem login-forsøg og kontolås-logik.
* **System Tests:** Gennemgang af hele login-flowet fra start til slut.

### Security Gates
Inden koden kan godkendes, skal den passere:
1.  **Input Gate:** Overholdelse af grænseværdier.
2.  **Security Gate:** Beskyttelse mod brute-force (Cycle test).
3.  **Release Gate:** Fuld CRUD-funktionalitet og systemstabilitet.

---

## 🚀 Kørsel af Tests

![alt image](https://github.com/Alperenozt/it_sikkerhed_2026f/blob/f1d7eaafd8c45e7f4faf150bae29917b03fc4ee9/test-k%C3%B8rsel-05-02-26.png)

Alle tests er verificeret d. 05-02-2026. Brug følgende kommando for at eksekvere test: pytest -v eller -vv

## 📊 Data-dreven test (Decision Table + Grænseværdi)

Denne test kombinerer en **beslutningstabel** med **grænseværdianalyse** for password-længde. Ved at bruge en data-dreven tilgang via `pytest.mark.parametrize`, adskiller vi testdata fra selve testlogikken. Dette gør det meget lettere at læse, vedligeholde og udvide med nye scenarier.

### Testmatrix
Tabellen herunder viser, hvordan systemet skal reagere på forskellige kombinationer af input og konto-status:

| Password (Input) | Matcher DB? | Konto låst? | Forventet resultat | Beskrivelse |
| :--- | :---: | :---: | :--- | :--- |
| `1234567` | Nej | Nej | **forkert** | Fejler pga. grænseværdi (for kort) |
| `12345678` | Ja | Nej | **ok** | Præcis på grænsen og korrekt match |
| `12345678` | Ja | Ja | **låst** | Korrekt match, men kontoen er spærret |
| `forkertpw` | Nej | Ja | **låst** | Forkert input på en allerede låst konto |

**Testfil:** `test_login_datadreven.py`  
**Teknik:** Parametrisering sikrer, at vi tester alle logiske kombinationer (Edge Cases) i en samlet funktion.

# 📦 Flat File JSON User Database  
**Opdateret: 10. februar 2026**

Dette projekt demonstrerer en minimalistisk brugerdatabase, hvor alle data lagres i én enkelt JSON-fil – helt uden brug af traditionel relationsdatabase.

---

## 🚀 Hvorfor vælge en flat-file løsning?

En JSON-baseret database kan være et stærkt valg i mindre projekter:

- ✅ Ingen installation eller serveropsætning  
- ✅ Ingen database-engine, Docker eller cloud-afhængigheder  
- ✅ Kun Python standardbibliotek (inkl. `dataclasses`)  
- ✅ Let at læse og debugge – åbn `db_flat_file.json` direkte  
- ✅ Ideel til undervisning, prototyper og små systemer  
- ✅ 100 % portabel – kopiér JSON-filen og hele databasen følger med  
- ✅ Nem backup og versionsstyring via Git  
- ✅ Ingen baggrundsprocesser eller port-konflikter  

Typisk egnet til systemer med under ca. 1.000 brugere og lav skrivefrekvens.

---

## ⚠️ Begrænsninger

En flat-file database er ikke optimal i følgende situationer:

- ❌ Mange samtidige skrivninger  
- ❌ Krav om transaktioner (ACID)  
- ❌ Store datamængder med behov for indeksering  
- ❌ Avanceret adgangsstyring og rollebaseret sikkerhed  

**Konklusion:**  
Velegnet til læring, PoC og små applikationer – ikke til højbelastet produktion.

---

# 🧪 Unit Tests – Dokumentation for funktionalitet



# 🔐 Sikkerhed – GDPR & Password-beskyttelse

For at leve op til GDPR (særligt artikel 5 og 32 om dataminimering, integritet og fortrolighed) samt moderne sikkerhedsstandarder for password-håndtering, anvender systemet både **kryptografisk hashing** og **symmetrisk kryptering**.

Målet er:

- At forhindre gendannelse af passwords ved datalæk  
- At beskytte data mod fysisk kompromittering  
- At minimere eksponering i hukommelsen  
- At implementere “defense in depth”  

---

## 🔑 Valgte algoritmer

### 1️⃣ Password Hashing

**Primær algoritme:** `Argon2id`  
**Overvejede alternativer:** bcrypt, scrypt, PBKDF2-SHA256  

### Hvorfor Argon2id?

- Vinder af Password Hashing Competition  
- Anbefalet af OWASP, NIST og ENISA (stadig standard i 2026)  
- Memory-hard → gør GPU/ASIC brute-force ekstremt dyrt  
- Designet til at modstå timing- og cache-angreb  

**Konfiguration:**




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


