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

Alle tests er verificeret d. 05-02-2026. Brug følgende kommando for at eksekvere test-suiten:

```bash
# Kør alle tests med detaljeret output
pytest -v test_aekvivalensklasser.py test_graensevaerdi.py test_crud.py test_cycle_process.py test_decision_table.py


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


