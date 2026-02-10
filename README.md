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

# Flat File JSON Brugerdatabase
**Dato:** 10. februar 2026

Dette projekt implementerer en **simpel brugerdatabase**, der gemmer alle data i én JSON-fil uden brug af en traditionel relationsdatabase.

---

## Hvorfor er det smart at bruge en flat-file database (JSON-fil)?

- **Ingen installation eller opsætning** – ingen database-server, ingen Docker-container, ingen cloud-tjeneste  
- **Kun Python standardbibliotek** – kræver ingen eksterne pakker (udover pycryptodome og argon2-cffi)  
- **Meget nem at forstå og debugge** – åbn filen `db_flat_file.json` i enhver teksteditor og se alle data med det samme  
- **Perfekt til små projekter, prototyper, undervisning og PoC** – typisk < 1.000 brugere og lav skrivefrekvens  
- **100 % portabel** – kopier bare JSON-filen til en anden maskine → databasen følger med  
- **Ingen runtime-afhængigheder** – ingen process kører i baggrunden, ingen port-konflikter  
- **Menneskelæselig backup og versionering** – nem at tage backup af, nem at se ændringer i git  

### Begrænsninger

- Ikke egnet til mange samtidige skrivninger  
- Ingen transaktioner / ACID-garanti  
- Ingen indeksering → langsom ved meget store datasæt  
- Ingen rettighedsstyring / brugeradgangskontrol  

> Flat-file JSON er smart til læringsformål, små applikationer og hurtige prototyper – men ikke til produktion med høj belastning.

---

## Unit tests – bevis for at databasen virker

Projektet indeholder omfattende unit tests med `pytest`.  
Alle vigtige funktioner testes: oprettelse, læsning, kryptering, dekryptering, password-verifikation, aktivering/deaktivering og persistens.  
De tests, der fejler, er bevidst sat til at demonstrere assert-fejl, exceptions og edge-cases.

---

## Udvalgte tests med risici-kommentarer

Eksempler på tests med **Given → When → Then** struktur:

- Opret bruger → Antal brugere stiger → Risiko: manglende oprettelse  
- Kryptering/dekryptering → Data er ikke i klartekst → Risiko: læk af følsom info  
- Verify password → korrekt password godkendes → Risiko: forkert håndtering tillader login  
- Aktivering/deaktivering → korrekt ændring af flag → Risiko: sikkerhedsbrud eller uautoriseret adgang  

---

## Sikkerhed – GDPR og password-beskyttelse

For at opfylde GDPR-krav (især artikel 5 og 32 om dataminimering, integritet og fortrolighed) samt generel god password-sikkerhed, har jeg implementeret både hashing og kryptering af passwords.

### Valgte algoritmer

#### Hashing af passwords

- **Valgt:** Argon2id  
- **Alternativer:** bcrypt, scrypt, PBKDF2-SHA256  
- **Begrundelse:**  
  Argon2id vandt Password Hashing Competition 2015 og er i 2026 stadig OWASP, NIST og ENISA's førstevalg. Den er memory-hard, hvilket gør brute-force og GPU/ASIC-angreb meget dyre. Parametre: `time_cost=2`, `memory_cost=102400`, `parallelism=8` giver god balance mellem sikkerhed og performance på almindelige computere.

#### Kryptering af følsomme data

- **Valgt:** AES-256-GCM  
- **Alternativer:** ChaCha20-Poly1305, AES-256-CBC (med HMAC)  
- **Begrundelse:**  
  AES-256-GCM er NIST-godkendt, understøtter autentificeret kryptering (ingen ændring af ciphertext uden opdagelse), og har hardware-acceleration (AES-NI) på næsten alle moderne processorer. Den er hurtig og giver både fortrolighed og integritet – bedre end CBC-mode (som kræver ekstra MAC).

---

### Hvornår og hvorfor krypterer jeg data?

- Ved oprettelse af bruger (`create_user`) og ved password-opdatering.  
- Hvad krypteres? Rå-password krypteres med AES-256-GCM (valgfrit ekstra lag) + password hashes med Argon2id før lagring.  
- Hvorfor?  
  - Hashing gør det umuligt at gendanne original-password ved datalæk (zero-knowledge).  
  - AES-kryptering beskytter JSON-filen mod fysisk tyveri eller uautoriseret læsning (f.eks. på delt server eller stjålen laptop).  
- Opfylder GDPR artikel 32 krav om "passende tekniske og organisatoriske foranstaltninger".

---

### Dekryptering og fjernelse fra hukommelsen

- Hvornår og hvorfor dekrypteres data?  
  - Aldrig for gemte passwords ved normal brug!  
  - Ved login: Jeg dekrypterer ikke det gemte password. Jeg hasher det indtastede password og sammenligner med det gemte hash (`verify_password`).  
- Hvorfor?  
  - Dekryptering af passwords i hukommelse er et stort sikkerhedshul (memory scraping, debugging, cold-boot-angreb). Zero-knowledge-validering eliminerer behovet fuldstændigt.  
- Hvornår og hvorfor fjerner jeg dekrypteret data fra hukommelsen?  
  - Straks efter brug – efter `create_user` (når rå-password er hashed/krypteret) og efter `verify_password` (når indtastet password er tjekket).  
- Hvordan?  
  - `del` variabel + `gc.collect()`  
- Hvorfor?  
  - GDPR artikel 5(1)e kræver dataminimering – data må kun opbevares så længe det er nødvendigt. Dekrypteret data i RAM er sårbar over for hukommelses-dump-angreb (malware, cold-boot, law-enforcement tools). Ved at fjerne det med det samme minimeres risikoen.

---

### Andre hensyn jeg har taget

- **Nøglehåndtering:** Master-nøglen til AES er ikke hard-coded i kode (demo-brug kun). I produktion skal den hentes fra miljøvariabel (`os.getenv`) eller en secure vault (f.eks. AWS Secrets Manager, HashiCorp Vault).  
- **Key rotation:** Nøglen bør roteres periodisk – ved rotation skal alle passwords gen-krypteres/hashes.  
- **Ingen logging:** Passwords eller rå-data logges aldrig.  
- **Backup-sikkerhed:** JSON-backup skal krypteres eller opbevares sikkert.  
- **Salt:** Håndteres automatisk af Argon2id (ingen manuel salt nødvendig).  
- **Side-channel-beskyttelse:** Argon2id er designet til at modstå timing- og cache-angreb.


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


