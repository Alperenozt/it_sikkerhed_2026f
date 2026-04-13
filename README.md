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
Nedenfor er et screenshot af kørte unit tests (pytest -v -s).

![alt image](https://github.com/Alperenozt/it_sikkerhed_2026f/blob/ea0530c5946b9b636a794868a6161e715fb28fc8/10-02-26%20unit%20test%20af%20db.png) 

![alt image](https://github.com/Alperenozt/it_sikkerhed_2026f/blob/f931edd24c334fb20194c74d4ca4e518adab348a/10-02-26%20unit%20test%20af%20dbpart2.png)

Udvalgte tests med risici-kommentarer
Her er nogle af de tests med Given → When → Then-struktur og en kort risikovurdering:

![alt image](https://github.com/Alperenozt/it_sikkerhed_2026f/blob/f931edd24c334fb20194c74d4ca4e518adab348a/udvalgte%20test%20med%20given%2C%20when%2C%20then.png)


## Sikkerhed – GDPR og password-beskyttelse

For at efterleve GDPR (særligt artikel 5 og 32 om dataminimering, integritet og fortrolighed) samt moderne principper for sikker password-håndtering, er der implementeret både kryptografisk hashing og symmetrisk kryptering.

Formålet er at sikre:

- At passwords aldrig kan genskabes ved datalæk  
- At lagrede data er beskyttet mod uautoriseret adgang  
- At eksponering i hukommelsen minimeres  
- At løsningen følger “defense-in-depth”-princippet  

---

### Valgte algoritmer

#### Hashing af passwords

**Valgt:** Argon2id  
**Alternativer:** bcrypt, scrypt, PBKDF2-SHA256  

**Begrundelse:**  
Argon2id vandt Password Hashing Competition og er fortsat (2026) anbefalet af OWASP, NIST og ENISA. Algoritmen er memory-hard, hvilket betyder, at brute-force-angreb – især via GPU eller specialhardware (ASIC) – bliver markant dyrere og langsommere.

Anvendte parametre:

- `time_cost = 2`  
- `memory_cost = 102400`  
- `parallelism = 8`  

Disse værdier giver en solid balance mellem høj sikkerhed og acceptabel performance på almindelige systemer.

---

#### Kryptering af følsomme data

**Valgt:** AES-256-GCM  
**Alternativer:** ChaCha20-Poly1305, AES-256-CBC (med HMAC)

**Begrundelse:**  
AES-256-GCM er NIST-godkendt og understøtter autentificeret kryptering (AEAD), hvilket betyder, at både fortrolighed og integritet sikres. Eventuelle ændringer i ciphertext opdages automatisk.  

Derudover understøttes hardware-acceleration (AES-NI) på næsten alle moderne CPU’er, hvilket giver høj ydeevne uden at gå på kompromis med sikkerheden.  

GCM-mode er generelt sikrere og mere moderne end CBC-mode, som kræver en separat MAC for at opnå samme beskyttelsesniveau.

---

### Hvornår og hvorfor krypterer jeg data?

Kryptering og hashing udføres ved:

- Oprettelse af bruger (`create_user`)  
- Opdatering af password  

**Hvad krypteres?**  
Det rå password krypteres med AES-256-GCM (som et ekstra beskyttelseslag) og hashes derefter med Argon2id, før det lagres.

**Hvorfor?**

- Hashing sikrer, at original-password ikke kan rekonstrueres ved datalæk (zero-knowledge-princip).
- AES-kryptering beskytter selve JSON-filen mod fysisk kompromittering (f.eks. stjålet laptop eller uautoriseret adgang på delt server).
- Understøtter GDPR artikel 32 om passende tekniske og organisatoriske sikkerhedsforanstaltninger.

---

### Hvornår og hvorfor dekrypterer jeg data?

Aldrig for gemte passwords ved normal brug.

Ved login dekrypteres det gemte password ikke.  
I stedet hashes det indtastede password og sammenlignes med det lagrede hash via `verify_password`.

**Hvorfor?**

Dekryptering af passwords i hukommelsen øger risikoen for:

- Memory scraping  
- Debugging-angreb  
- Cold-boot-angreb  
- RAM-dump analyse  

Ved at anvende zero-knowledge-validering elimineres behovet for dekryptering fuldstændigt.

---

### Hvornår og hvorfor fjerner jeg dekrypteret data fra hukommelsen?

Straks efter brug:

- Efter `create_user` (når password er hashed og krypteret)  
- Efter `verify_password` (når login-validering er gennemført)

Hvordan? del variabel + gc.collect()

Hvorfor?
GDPR artikel 5(1)e kræver dataminimering – data må kun opbevares så længe det er nødvendigt. Dekrypteret data i RAM er sårbar over for hukommelses-dump-angreb (malware, cold-boot, law-enforcement tools). Ved at fjerne det med det samme minimeres risikoen.

# 🛡️ Andre hensyn jeg har taget

## 🔑 Nøglehåndtering
AES-master-nøglen er ikke hard-coded (kun i demo).  
I produktion hentes den fra miljøvariabler (`os.getenv`) eller en sikker secret manager (fx AWS Secrets Manager eller HashiCorp Vault).

---

## 🔄 Key rotation
Kryptografiske nøgler bør roteres periodisk.  
Ved rotation skal eksisterende data gen-krypteres.

---

## 🚫 Ingen logging
Passwords, hashes og rå følsomme data logges aldrig.

---

## 💾 Backup-sikkerhed
Backup af JSON-filen skal enten:
- Krypteres  
- Eller opbevares i et sikkert miljø  

---

## 🧂 Salt
Salt håndteres automatisk af Argon2id.  
Ingen manuel implementering er nødvendig.

---

## ⏱ Side-channel-beskyttelse
Argon2id er designet til at reducere risikoen for timing- og cache-baserede angreb.

![alt image](https://github.com/Alperenozt/it_sikkerhed_2026f/blob/f931edd24c334fb20194c74d4ca4e518adab348a/screenafdbmedkryptering.png)

![alt image](https://github.com/Alperenozt/it_sikkerhed_2026f/blob/f931edd24c334fb20194c74d4ca4e518adab348a/test10-10-26.png) 

# OPGAVE – 1 REST API
**Dato:** 19-02-26

### 🛠 Beskrivelse
Udvikling af et REST API i **Python + Fast API**.

---

### 🚦 Test
Alle funktioner kan testes via: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

* **Create**: Oprette data - (via flat_file eller [repo](https://bitbucket.org/BartlomiejRohardWarszawski/it_sikkerhed/src/main/)
![alt image](https://github.com/Alperenozt/it_sikkerhed_2026f/blob/afae4345d66a5d037385ac0346e20759a3ba3984/user1.png) 

![alt image](https://github.com/Alperenozt/it_sikkerhed_2026f/blob/afae4345d66a5d037385ac0346e20759a3ba3984/user2del.png)

* **Read**: Læse data
![alt image](https://github.com/Alperenozt/it_sikkerhed_2026f/blob/788a3d33ad6600e8f1f3d7b5773e19f04c638e2f/getdel1.png)

* **Update**: Opdatere data
![alt image](https://github.com/Alperenozt/it_sikkerhed_2026f/blob/788a3d33ad6600e8f1f3d7b5773e19f04c638e2f/putdel1.png)

![alt image](https://github.com/Alperenozt/it_sikkerhed_2026f/blob/788a3d33ad6600e8f1f3d7b5773e19f04c638e2f/putdel2.png)
  
* **Delete**: Slette data (Evt.)
![alt image](https://github.com/Alperenozt/it_sikkerhed_2026f/blob/788a3d33ad6600e8f1f3d7b5773e19f04c638e2f/deletedel1.png)

![alt image](https://github.com/Alperenozt/it_sikkerhed_2026f/blob/788a3d33ad6600e8f1f3d7b5773e19f04c638e2f/deletedel2.png)
  
### Liste over brugere (List)
* **Endpoint:** `GET /users`
* **Beskrivelse:** Returnerer en samlet oversigt over samtlige brugere, der er registreret i databasen.
* **Funktion:** Giver et hurtigt overblik over systemets data i et læsbart JSON-format.
![alt image](https://github.com/Alperenozt/it_sikkerhed_2026f/blob/788a3d33ad6600e8f1f3d7b5773e19f04c638e2f/gelalluserfromdbdel1.png)


# OPGAVE – 2 AUTH
**Dato:** 19-02-26

### 🔐 Beskrivelse
Udvikling af et **Authorization REST API**, der kan udstede security tokens.

---

### 🚦 Test
Alle funktioner testes via: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

* **Admin Bruger**: Oprettelse af standard admin (hvis ingen `user_db`).
* **Security Token**: Hent token via admin bruger.
* **Password**: Ændre password på admin.
* **Accounts**: Registrere nye konti.
* **Deaktivering**: Deaktivere egen konto.
* **Reaktivering**: Genaktivere konto via admin.
* **Sikkerhed**: Kun `test-secrets` ligger i Git; `prod-secrets` ligger i environment variables.


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


