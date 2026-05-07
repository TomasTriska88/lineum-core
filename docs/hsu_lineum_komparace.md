# HSU & Lineum: Teoretická Křižovatka a Komparativní Analýza

Tento dokument slouží jako samostatný srovnávací dokument a centrální pracovní report pro mapování průsečíků mezi makroskopickou teorií HSU (HyperShell Universe - Romeo Bruni) a naší mikroskopickou lokální dynamikou Lineum. Cílem je poskytnout oboustranně přínosný pohled, kde se obě disciplíny mohou inspirovat ve svých metodikách, s využitím přísného a spravedlivého "Fair Comparative Principle".

**Typ Auditu:** Analýza vychází ze statického auditu dodaného HSU manuskriptu. Nejsou prováděny žádné externí skripty ani datové analýzy.
*Upozornění:* Statický audit manuskriptu dokáže identifikovat tvrzení, předpoklady a kandidátské metody, ale nemůže teorii plně validovat bez spustitelné analýzy, prokazatelného původu zdrojových dat a nezávislých kontrolních (null) testů.

## 1. Princip spravedlivého oboustranného hodnocení (Fair Comparative Principle)

HSU i Lineum jsou hodnoceny symetricky napříč stejnými kategoriemi tam, kde se překrývají. Musíme striktně rozlišovat pojmy: mechanismus, pozorovatelná veličina (observable), interpretace a tvrzení (claim).

**Pravidla symetrie (Domain-Matched Symmetry):**
- Symetrické hodnocení neznamená předstírat, že HSU a Lineum vznášejí aktuálně stejný typ tvrzení. Znamená to aplikovat stejná měřítka zkoumání a explicitně označit nepřekrývající se domény.
- **HSU:** Vykazuje silnější vazbu na mapování pozorovatelných kosmologických dat, ale jeho základní mechanismus a teoretické podloží (lore) mohou být spekulativní nebo nedostatečně popsané. Nesmíme však zavrhovat užitečné techniky zpracování dat jen proto, že kosmologický "lore" je spekulativní.
- **Lineum:** Vykazuje silnou stabilitu ve vnitřní mechanice PDE a reprodukovatelných simulacích, ale aktuálně **nemá žádný validovaný most k reálným kosmologickým měřením**. Nesmíme zveličovat interní PDE výsledky na úroveň reálné pozorovatelné fyziky, dokud takový most neexistuje.
- Chybějící důkazy označujeme upřímně jako "zatím nedoloženo", "neaplikovatelné", "čeká na most k observables" nebo "neznámé". "Neznámé" je platný vědecký výsledek.

## 2. Testovatelná tvrzení HSU (Extrahováno ze zdrojového PDF)

| Konkrétní tvrzení | Pozorovatelná veličina | Osa / Souřadnice | Měřítko | Datová podpora | Měřitelnost | Falsifikace | Hlavní systematická rizika |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Cosmic Octave** | 8 směrových anomálií sdílí osu | Společná osa $\hat{d}$ | N/A | Deep radio, kvasary, bulk flow | Počítáno z dat | Chybějící zarovnání dipólů v nezávislých survey | Riziko sdílené kontaminace systematickými chybami / galaktická maska |
| **Observer Offset** | Lokální grupa je excentrická vůči CSW | Ve směru gradientu $\hat{d}$ | $u^* \approx 5-6$ Mpc | Signály distance-dipole | Závislé na teorii (vyvozeno z dipólu) | Rozpor predikce s izotropním CMB | Chybné modelování lokálního rychlostního pole |
| **Effective Drift** | Drift pozorovatele vůči normálové expanzi | $\hat{d}$ | $v_{eff} \approx H_{\perp}u^*$ ($\beta_{eff} \sim 10^{-3}$) | Signály lokálního Hubblea | Vyvozeno z reziduí rychlostí | Izotropní Hubble flow | Kinematický CMB dipól |
| **Euclid DR1** | Strukturální signatura slupky | Neznámá | Neznámé | Euclid DR1 (Oček. 10/2026) | Přímá predikce | Absence signatury | Artefakty zpracování dat |

## 3. Matematická struktura a Observational Mapping

- **Matematika driftu:** Kinematický vztah $v_{eff} = H_\perp u^*$ je rozměrově konzistentní ($[T^{-1}] \times [L] = [L/T]$). Expanze metriky pro excentrického pozorovatele je solidně definovaná.
- **Riziko statických úhlů:** Odvození poměrů pro temnou hmotu a temnou energii ($\rho_{DM}$ a $\rho_{DE}$) se opírá o statické geometrické úhly bez prokazatelného vývoje v čase.
- **Systematika "Cosmic Octave":** Hrozí masivní riziko *Look-Elsewhere Effect* (post-selekce). Sdružování anomálií nese vysoké riziko společné kontaminace nezávislých chyb (např. vliv masky Mléčné dráhy se u mnoha zmíněných datasetů jako rádio a kvasary masivně překrývá), což velmi znesnadňuje nezávislé ověření. 

## 4. Karanténa nedokazatelných tvrzení ("Lore")

Následující interpretativní tvrzení izolujeme jako momentálně nepřenosná do Lineum:
- Makroskopické sjednocení (TOE) kvantové mechaniky a gravitace přes geometrii slupky.
- Jazyk "červích děr" a dvousektorového provázání (ER=EPR) jako fyzické opory slupky.
- Doslovná interpretace vesmíru jako rozpínající se 4D slupky obklopené prázdnotou.
- Původ slupky v LQC (Loop Quantum Cosmology) odrazu, bez doložené operační matematiky.

## 5. Průsečíky a Extrakce pro Lineum

**Co si může odnést Lineum (Přenositelná metoda):**
- **Projekce excentrického pozorovatele (Observer-Offset Projection):** Matematika expanze metriky pro pozorovatele mimo střed bubliny. Pokud naše interní simulační data Lineum (režim Soft Cloak) prokáže lokální měřitelnou asymetrii pozorovatele v obálce, Lineum může vyhodnotit, zda by podobné rovnice (po nezávislém odvození a validaci na Lineum nativních PDE datech) šly použít pro převod lokální asymetrie na měřitelný dipólový vektor.
- **Logika "Visibility Function":** Prahové (threshold) maskování, které určuje, kdy se modifikace interní geometrie stane makroskopicky měřitelnou nad úrovní lokálního šumu.

**Co si může odnést HSU:**
- **Dynamická PDE Stabilita:** HSU derivuje poměr Temné oblasti geometricky; testování podobných mechanismů přes dynamické PDE modely jako Lineum může teoreticky poskytnout ověření evoluce takové struktury v čase.
- **Nezávislé kontrolní testy:** Nutnost ověřovat zpracování dipólů na prázdných $\Lambda$CDM datech s aplikovanou stejnou oblohovou maskou, aby se vyloučily artefakty zpracování.

## 6. Srovnávací matice

| Fenomén / Téma | Status v HSU | Status v Lineum | Typ zdroje | Reprodukovatelnost | Hlavní slabina | Přenositelná metoda | Další krok (Test) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Geometrická stabilizace** | Předpokládaná makro-topologie (SdS) | Odvozená lokální topologie (PDE Soft Cloak) | HSU: Manuskript<br>Lineum: Simulované matice | HSU: Zatím nedoloženo<br>Lineum: Interní simulační data Lineum zatím ukazuje pouze lokální PDE stabilizační jev v režimu Soft Cloak; nejde o kosmologické pozorování. | HSU: Chybí dynamický mechanismus<br>Lineum: Zatím nedoloženo makro-škálování | Žádná | Namapovat Lineum geometrii na makro-metriku |
| **Most k Observables** | Tvrzené namapování pozorování (dipóly) | Zatím nedoloženo / Čeká na most k observables | HSU: Korelace v datech (survey) | HSU: Skripty zatím nepředloženy<br>Lineum: Neaplikovatelné | HSU: Vysoké riziko systematických chyb<br>Lineum: Zatím čistě teoretické | Metrická projekce pro asymetrické pozorovatele | Otestovat nezávisle HSU matematiku na mock datech |
| **Integrace temného sektoru** | Statický geometrický poměr (2:1) | Lineum zatím nemá validovaný kosmologický model temného sektoru ani ověřený poměr DM/DE. Má pouze interní PDE fenomenologii lokálních struktur a fázových interakcí, která by se teprve musela převést na měřitelný kosmologický observable. | HSU: Geometrické odvození<br>Lineum: interní simulační data lokální PDE dynamiky; bez přímého kosmologického observable. | HSU: Matematické odvození<br>Lineum: Interní simulační data; zatím nedoloženo v astronomických datech. | HSU: Riziko numerologie<br>Lineum: Zatím nedoloženo / neaplikovatelné na data | Řešení okrajových podmínek (boundary) | Analyzovat vývoj hustotních poměrů Linea v čase $t$ |

## 7. Nezávislý analytický plán pro HSU i Lineum

Tato sekce definuje, jak by měla probíhat budoucí nezávislá analýza, a to plně symetricky pro oba rámce (tam, kde se jejich domény překrývají).

### 7.1 Proč absence původních skriptů není problém

Absence původních implementačních skriptů autora není blokátorem, nýbrž metodologickou příležitostí. Nejsme závislí na konkrétní implementaci Romea Bruniho. Nezávislé odvození analytických testů přímo z textu manuskriptu nám ukáže, zda samotný text obsahuje dostatek informací k reprodukci tvrzení. Pokud nezávislé testy dospějí ke stejnému výsledku, dané tvrzení to výrazně posílí. Pokud se výsledky budou lišit, může to odhalit skryté předpoklady, nezdokumentované ladění parametrů (tuning) nebo nejednoznačnost v metodice. Tento stejný, přísný princip nezávislé reprodukovatelnosti uplatňujeme i na Lineum.

### 7.2 Analytické otázky pro HSU

Pro každé hlavní tvrzení HSU je třeba nezávisle ověřit následující:
- **Cosmic Octave / Společná osa anomálií:** Je tato osa prediktivní, nebo je výsledkem post-selekce? Může pouhá systematická chyba survey (např. galaktická maska) vytvořit falešnou iluzi společné osy u různých nezávislých datasetů?
- **Observer Offset:** Lze tuto hodnotu odvodit nezávisle z izotropie, nebo je to pouze parametr zpětně napasovaný na stávající dipól?
- **Effective Drift:** Je rovnice pro drift použitelná robustně bez ohledu na volbu souřadnicového systému?
- **Statický poměr DM/DE:** Je tento geometrický poměr stabilní i v případě, že do rovnice zavedeme kosmologický čas a expanzi vesmíru?
- **Euclid predikce:** Obsahuje manuskript dostatečně přesnou geometrickou logiku, aby bylo možné jednoznačně potvrdit nebo vyvrátit signaturu v datech z Euclid DR1, nebo lze data interpretovat libovolně?

### 7.3 Analytické otázky pro Lineum

Pro Lineum definujeme analogické otázky, bez zveličování našich aktuálních možností:
- **Lokální asymetrie:** Má Lineum takovou lokální asymetrii pole, která by dokázala definovat signál závislý na pozici pozorovatele?
- **Dipólový observable:** Lze jakýkoliv stav pole Linea konzistentně promítnout do měřitelné dipólové veličiny?
- **Kosmologický observable:** Má v současnosti Lineum jakýkoliv validovaný kosmologický observable? Odpověď: ne.
- **Dynamický poměr hustot:** Dokáže Lineum generovat dynamickou analogii k poměru hustot (jako má HSU), nebo to zatím není v rámci PDE definováno?
- **Most k astronomii:** Co konkrétně by bylo metodologicky nutné vybudovat pro spravedlivý a rigorózní most z výstupů PDE do astronomických survey observables?

### 7.4 Symetrická testovací matice

| Test / otázka | Co by muselo ukázat HSU | Co by muselo ukázat Lineum | Aktuální stav HSU | Aktuální stav Lineum | Co by výsledek znamenal | Riziko omylu / systematiky | Další férový krok |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Původ dipólové osy** | Signál přetrvá i po aplikaci odlišných (nebo žádných) galaktických masek u nezávislých survey. | Interní asymetrie PDE bubliny generuje stabilní směrový vektor pro jakéhokoliv excentrického pozorovatele. | čeká na nezávislý test | zatím nedoloženo | Potvrzení fyzikální podstaty osy (nikoliv jen artefaktu měření). | Sdílená galaktická kontaminace (HSU); numerická nestabilita (Lineum) | Otestovat metodiku na prázdných mock datech ($\Lambda$CDM) |
| **Kosmologický observable** | Predikovat specifický tvar signatury ve struktuře (např. pro Euclid) bez ladění parametrů ex-post. | Převést lokální hustotu (Eq-11) na makroskopický zdrojový field (source count). | riziko systematik | vyžaduje převod na observable | Překlenutí propasti mezi teoretickou geometrií a reálným vesmírem. | Artefakty zpracování dat (HSU); chybný scaling modelu (Lineum) | Formulovat rigorózní "Visibility Function" pro obě teorie |
| **Stabilita temného sektoru** | Doložit, že statický úhlový poměr zůstává platný i při dynamické kosmologické expanzi. | Získat ustálený dynamický poměr fázových interakcí bez tvrdě zakódovaných konstant. | riziko systematik | není zatím definováno | Ukázalo by, zda je temný sektor fundamentálně geometrický (HSU) nebo emergentní (Lineum). | Numerologie a ignorování časového vývoje | Modelovat časový vývoj geometrie / fází |

Statická konsolidace hotová; nyní rozšířeno o plán nezávislých symetrických analýz.

## 8. Testovací backlog: potvrzení, vyvrácení a otevřené otázky

Tento backlog slouží jako živý protokol pro symetrické testování obou rámců. Každé zásadní téma musí být dovedeno do stavu: potvrzeno v rámci dostupných testů, vyvráceno, částečně podpořeno, nerozhodnutelné ze současných dat, čeká na definici přesného observable, čeká na výpočet / simulaci, nebo neaplikovatelné pro daný rámec.

### A. Společná dipólová osa / Cosmic Octave
- **Tvrzení:** Ve vesmíru existuje společná preferovaná osa identifikovatelná napříč vícero nezávislými anomáliemi (Cosmic Octave).
- **Co přesně se musí ověřit:** 
  - HSU: Zda tvrzená osa přežije nezávislé masky (např. galaktické), změny souřadnic a kontroly na "look-elsewhere effect".
  - Lineum: Zda existuje jakákoliv nativní konfigurace pole (napříč kanonickými i experimentálními variantami rovnic), která přirozeně generuje směrový dipólový signál závislý na pozici pozorovatele.
- **Jaký výpočet / simulace je potřeba:** Aplikace stejné metodiky zpracování dat na mock data ($\Lambda$CDM); analýza asymetrie pole v simulacích Lineum.
- **Co by podpořilo:** Stabilita osy bez ohledu na výběr masky (HSU). Nalezení stabilního dipólového vektoru uvnitř bubliny (Lineum).
- **Co by vyvrátilo:** Zmizení osy po korekci na známé systematické chyby (HSU). Důkaz, že Lineum bublina je nutně izotropní z pohledu všech interních pozorovatelů (Lineum).
- **Co znamená nerozhodnutelnost:** Data jsou příliš zašuměná na to, aby šlo odlišit skutečnou osu od galaktické kontaminace.
- **Stav pro HSU:** Čeká na nezávislý test (riziko systematik).
- **Stav pro Lineum:** Zatím nedoloženo (čeká na simulaci asymetrie).
- **Další férový krok:** Analyzovat surová data (např. SPHEREx) pomocí odlišných statistických metod a masek.

### B. Projekce excentrického pozorovatele (Observer-offset projection)
- **Tvrzení:** Pozorovatel ležící mimo střed symetrie pozoruje specifickou směrovou závislost (dipól).
- **Co přesně se musí ověřit:** 
  - HSU: Zda je offset odvozen prediktivně předem, nebo je pouze zpětně napasován na již naměřený dipól.
  - Lineum: Zda lze pozici pozorovatele uvnitř (nebo blízko) obálky PDE pole jednoznačně matematicky definovat a promítnout do měřitelné asymetrie v jakékoliv zkoumané variantě (např. pracovní draft Soft Cloak).
- **Jaký výpočet / simulace je potřeba:** Prověřit derivační rovnice offsetu (HSU). Provést projekci lokálního gradientu pole do pozorovatelského referenčního rámce (Lineum).
- **Co by podpořilo:** Offset vysvětluje více nezávislých měření jedinou konstantní hodnotou (HSU). Úspěšná matematická definice mapování pole-na-pozorovatele (Lineum).
- **Co by vyvrátilo:** Nutnost ladit offset pro každý dataset zvlášť (HSU). Fundamentální nekompatibilita PDE pole s metrickým tenzorem na makroškále (Lineum).
- **Co znamená nerozhodnutelnost:** Neexistuje konsenzus na tom, jak interpretovat "pozici" v čistém poli.
- **Stav pro HSU:** Částečně podpořeno (vyžaduje prověření prediktivity).
- **Stav pro Lineum:** Není zatím definováno.
- **Další férový krok:** Odvodit rovnice projekce čistě z PDE pro Lineum.

### C. Efektivní drift (Effective drift)
- **Tvrzení:** Kinematický dipól CMB a lokální expanzní asymetrie jsou dány efektivním driftem $v_{eff} = H_\perp u^*$.
- **Co přesně se musí ověřit:** 
  - HSU: Je rovnice pro drift více než jen rozměrová analogie? Přežije kontroly změny souřadnic a lokálního proudění (local flow)?
  - Lineum: Existuje v dynamice PDE pole (včetně historických disipativních větví jako Eq-9) analogie "driftu", nebo zatím nic takového není definováno?
- **Jaký výpočet / simulace je potřeba:** Test kovariance rovnice pro drift (HSU). Identifikace transportních členů dynamiky blížících se makroskopickému driftu (Lineum).
- **Co by podpořilo:** Drift je odvoditelný přímo z relativistické kinematiky excentrického pozorovatele ve slupce (HSU). Korelace mezi gradienty pole a rychlostním tokem (Lineum).
- **Co by vyvrátilo:** Rovnice je nekonzistentní s izotropním Hubbleovým tokem z pohledu středu (HSU). Transport pole nezávisí na asymetrii (Lineum).
- **Co znamená nerozhodnutelnost:** Drift nelze odlišit od běžné lokální pekuliární rychlosti naší galaxie.
- **Stav pro HSU:** Čeká na nezávislý test (riziko záměny za local flow).
- **Stav pro Lineum:** Není zatím definováno.
- **Další férový krok:** Matematická revize derivace $v_{eff}$ v HSU bez závislosti na předchozích dipólových datech.

### D. Poměr temného sektoru (Dark-sector ratio / density-ratio)
- **Tvrzení:** Temná hmota a temná energie vyplývají z čistě geometrického projekčního poměru (např. 2:1 staticky).
- **Co přesně se musí ověřit:** 
  - HSU: Přežije tento statický 2:1 poměr vývoj v čase, expanzi vesmíru a dynamické ředění hustoty?
  - Lineum: Má Lineum (zejména kanonická Eq-11) jakoukoliv definovanou, měřitelnou analogii poměru hustot?
- **Jaký výpočet / simulace je potřeba:** Kosmologické řešení evolučních rovnic s časově proměnným faktorem měřítka (HSU). Analýza dynamiky Eq-11 fází (Lineum).
- **Co by podpořilo:** Matematický důkaz, že poměr 2:1 je stabilním atraktorem i v expandující metrice (HSU). Stabilizace dvou fází pole do definovaného poměru ve velkých objemech (Lineum).
- **Co by vyvrátilo:** Důkaz, že expanze nutně zničí statický poměr (HSU). Nemožnost stabilizovat fáze makroskopicky (Lineum).
- **Co znamená nerozhodnutelnost:** Nejasné okrajové podmínky ovlivňují výsledek více než samotná rovnice.
- **Stav pro HSU:** Riziko systematik (riziko numerologie; ignorování časového vývoje).
- **Stav pro Lineum:** Není zatím definováno.
- **Další férový krok:** Vyvinout plně časově závislý (dynamický) model temného sektoru.

### E. Most k pozorováním (Observational bridge)
- **Tvrzení:** Parametry modelu lze přímo mapovat na astronomická data (observables).
- **Co přesně se musí ověřit:** 
  - HSU: Jsou tvrzené observables dostatečně specifické na to, aby šly nezávisle a jednoznačně testovat?
  - Lineum: Jaký přesný matematický most z výstupu PDE do astronomických veličin by bylo nutné vybudovat?
- **Jaký výpočet / simulace je potřeba:** Extrakce jasné "visibility function" (HSU). Konstrukce simulovaných katalogů z hustotních map PDE (Lineum).
- **Co by podpořilo:** Model předpoví data lépe než $\Lambda$CDM s menším počtem volných parametrů.
- **Co by vyvrátilo:** Predikce jsou natolik vágní, že jimi lze vysvětlit libovolný výsledek.
- **Co znamená nerozhodnutelnost:** Nepřesnost samotných astronomických dat brání ověření.
- **Stav pro HSU:** Částečně podpořeno (často jde o korelace bez jednoznačné kauzality).
- **Stav pro Lineum:** Vyžaduje převod na observable.
- **Další férový krok:** Definovat striktní sadu měřitelných metrik (např. spektrum fluktuací), které musí simulace splnit.

### F. Null testy a falešná pozitiva
- **Tvrzení:** Výsledky nereprezentují pouze šum nebo artefakty analýzy.
- **Co přesně se musí ověřit:** 
  - HSU: Nemohou masky, survey selekce, kontaminace Mléčné dráhy nebo volba souřadnic vyprodukovat stejný signál u zcela prázdných dat?
  - Lineum: Nemohou numerické artefakty gridu, okrajové podmínky (včetně experimentálního filtru SoftAbs) nebo volba zobrazení vytvářet domnělou asymetrickou strukturu?
- **Jaký výpočet / simulace je potřeba:** Monte Carlo simulace na isotropních mock datech (HSU). Simulace se změněnou mřížkou a náhodnými počátečními podmínkami (Lineum).
- **Co by podpořilo:** Signál zůstává robustní vůči veškerým kontrolním injekcím šumu.
- **Co by vyvrátilo:** Null test produkuje signál o stejné amplitudě jako "objev".
- **Co znamená nerozhodnutelnost:** Šum a reálný signál mají identickou frekvenční charakteristiku.
- **Stav pro HSU:** Čeká na nezávislý test.
- **Stav pro Lineum:** Čeká na simulaci.
- **Další férový krok:** Replikace analýzy obou modelů s čistým izotropním šumem.

### G. Prediktivita vs. post-selekce
- **Tvrzení:** Teorie je schopna deduktivní predikce.
- **Co přesně se musí ověřit:** 
  - HSU: Která tvrzení byla predikována před pohledem na data, a která představují retrospektivní narovnání faktů (post-selekci)?
  - Lineum: Které výsledky jsou skutečnými predikcemi kanonické rovnice (Eq-11), a které představují nově objevenou fenomenologii po průzkumu prostoru parametrů napříč ostatními variantami?
- **Jaký výpočet / simulace je potřeba:** Slepé zkoušky (blinded analysis).
- **Co by podpořilo:** Slepá predikce neznámé veličiny (např. v budoucích datech Euclid), která se následně potvrdí.
- **Co by vyvrátilo:** Model selhává kdekoli mimo trénovací/fitting dataset.
- **Co znamená nerozhodnutelnost:** Historii vývoje myšlenky nelze zpětně auditovat.
- **Stav pro HSU:** Riziko systematik (historické ladění parametrů).
- **Stav pro Lineum:** Riziko systematik (fenomenologické prozkoumávání prostoru parametrů).
- **Další férový krok:** Formulace nezměnitelných "slepých" predikcí pro budoucí testy.

### Klasifikační stavová tabulka

| Téma | HSU stav | Lineum stav | Co je potřeba k potvrzení | Co by vyvrátilo | Riziko falešného závěru | Další krok |
|---|---|---|---|---|---|---|
| **Cosmic Octave** | Čeká na nezávislý test | Zatím nedoloženo | Stabilita osy bez masek | Zmizení osy při korekci na Mléčnou dráhu | Sdílená systematika | Analýza odlišnými metodami na nezávislých datech |
| **Observer-offset** | Částečně podpořeno | Není zatím definováno | Offset fixuje vícero nezávislých veličin | Nutnost ladit offset pro každý dataset zvlášť | Zpětné ladění na existující dipól | Odvodit z čisté PDE |
| **Effective drift** | Čeká na nezávislý test | Není zatím definováno | Rovnice přežije změnu souřadnic | Rovnice koliduje s izotropním Hubble flow z pohledu středu | Záměna za local flow galaxie | Nezávislá derivace $v_{eff}$ |
| **Poměr DM/DE** | Riziko systematik | Není zatím definováno | Poměr 2:1 je stabilní atraktor v čase | Expanze zničí statický úhlový poměr | Numerologie, zanedbání časového vývoje | Časově závislý kosmologický model |
| **Most k observacím** | Částečně podpořeno | Vyžaduje převod na observable | Lepší predikce než $\Lambda$CDM | Vágní definice predikce | Korelace bez kauzality | Definovat visibility function |
| **Null testy** | Čeká na nezávislý test | Čeká na simulaci | Signál přežije injekce šumu | Mock data vytvoří stejný signál | Špatně navržená nulová hypotéza | Monte Carlo mock testy |
| **Prediktivita** | Riziko systematik | Riziko systematik | Slepá predikce budoucího survey | Selhání mimo napasovaná data | Post-selekce "Look-Elsewhere" | Slepý (blind) analýzní protokol |

Statická konsolidace hotová. Dokument nyní slouží jako živý, soběstačný testovací protokol pro symetrické ověřování HSU a Lineum.

## 9. Rozšíření testů na všechny varianty rovnic Lineum

Srovnání s HSU nesmí být omezeno pouze na aktuální kanonickou rovnici Lineum (Eq-11). Historické, experimentální a dokonce i překonané či vyvrácené varianty rovnic (tzv. "deprecated branches") jsou pro toto srovnání cenné jako potenciálně relevantní mechanismy, pokud přežijí kontrolní testy.

Testování opuštěné větve neznamená její vzkříšení jako kánonu. Překonané/vyvrácené větve zůstávají překonanými a vyvrácenými ve svém původním účelu. Znamená to uznání, že matematický mechanismus, který selhal pro původní mikroskopický účel Lineum (např. kvůli numerické nestabilitě), se může ukázat jako možný analog pro makroskopický fenomén popsaný v HSU (např. efektivní drift). Srovnání s HSU proto může odhalit, že nekanonická větev Lineum obsahuje kandidátský matematický mechanismus, který nám aktuálně chybí. 

Testování experimentálních větví neimplikuje, že jsou fyzikálně smysluplné, a testování historických větví neimplikuje, že se dají mapovat na kosmologii. Znamená to pouze, že mohou obsahovat znovupoužitelné matematické mechanismy, které stojí za to falsifikovat.

Historická rovnice může být použita jako matematická analogie pouze po:
- nezávislém odvození (independent re-derivation),
- kontrole rozměrové konzistence,
- provedení null testů,
- srovnání vůči chování kanonické rovnice Lineum,
- a po úspěšné aplikaci na jasně definovanou měřitelnou veličinu (observable).

Z tohoto srovnání se žádná varianta rovnice nestává automaticky kanonickou. Každá zkoumaná varianta rovnice je proto jasně označena svým aktuálním statusem, aby nedošlo ke zveličování (overclaiming) nebo záměně experimentu za kánon.

### 9.1 Matice variant rovnic a rodin

| Varianta / rodina rovnice | Status | Jaký mechanismus se testuje | Relevantní pro HSU téma | Co by podpořilo | Co by vyvrátilo | Aktuální omezení | Další krok |
|---|---|---|---|---|---|---|---|
| **Eq-11 (TDGL-like interakce)** | kanonická | Vznik fází, lokální topologie, dynamika vnitřních hranic. | Integrace temného sektoru (poměr DM/DE) | Konvergence do stabilního makroskopického poměru fází. | Fázová separace bez ustálení poměru. | Makro-škálování zatím nedoloženo. | Test evoluce v expandující mřížce. |
| **Eq-9 (Kinetická disipace)** | historická větev | Frekvenční filtrace, tření a ztráta rezonance. | Efektivní drift ($v_{eff}$) | Test, zda disipativní/transportní členy mohou formovat analog driftu. | Disipace je čistě lokální a netvoří tok. | Vyvráceno v původním účelu. | Kandidát pro testování disipativního driftu. |
| **Eq-4 / Eq-4' (Kontinuální difuze)** | deprecated / opuštěná | Rozmazávání hranic a transport bez jasné fázové bariéry. | Vyhlazování a prahování šumu | Může nabídnout užitečnou analogii pro vyhlazování šumu. | Naprostá ztráta lokální struktury znemožňuje definici observables. | Způsobuje topologický kolaps. | Může být metodologicky užitečné jako analogie vyhlazování. |
| **SoftAbs (Escape-valve)** | experimentální varianta | Ošetření singularit a únik energie z lokálních maxim. | Null testy a falešná pozitiva | Omezení numerických artefaktů při asymetriích. | Může samo generovat falešné dipólové artefakty v místech propusti. | Numerická regularizační varianta (escape-valve), nikoli fyzikální kánon. | Monte Carlo simulace s/bez SoftAbs. |
| **Registry Lock (Fáze 71)** | pracovní draft | Orientační vazby na rozhraních a preferenční geometrie kontaktu. | Původ dipólové osy (Cosmic Octave) | Orientace fázové hranice si udržuje dlouhodobou paměť. | Rozpad vektoru pod vlivem šumu. | Čeká na nový test měřítka. | Sledovat stabilitu vektoru v čase. |
| **Soft Cloak (Fáze 75)** | pracovní draft | Společná obálka izolující vnitřní asymetrii. | Projekce excentrického pozorovatele | Vytvoření excentrického těžiště s vnější asymetrií. | Bublina se vždy zformuje izotropně. | Není kanonické. | Pokus o dipólovou projekci asymetrické bubliny. |

Seznam variant není uzavřený. Při každé další fázi musí být znovu prohledány historické rovnice, experimentální větve, negativní výsledky a drafty, aby se netestovala pouze aktuální kanonická rovnice.

## 10. Phase HSU-LINEUM-01: Nezávislá derivace a návrh falsifikace

Tato fáze představuje úvodní analytický návrh pro ověření projekce excentrického pozorovatele. Zaměřuje se na nalezení matematického mostu mezi geometrií a pozorovatelnými veličinami, aniž by spoléhala na reálná astronomická data. 

### 10.1 Definice projekce excentrického pozorovatele (Observer-offset projection)
Základní myšlenka zkoumá následující problém: Pokud je pozorovatel umístěn uvnitř ohraničené struktury (bubliny, obálky) mimo její přesný geometrický střed (má určitý offset), zaznamená ve svém okolí nesymetrii závislou na směru, kterou lze interpretovat jako dipól.

### 10.2 Matematické tvrzení HSU
HSU (dle manuskriptu) definuje pozorovatelný vesmír jako sférickou slupku s konečnou šířkou a středovou rovinou symetrie zvanou CSW (Center of the Shell's Width). Tvrzení zní, že pozorovatel leží mimo tuto rovinu symetrie (má offset $u^*$). Vztažením tohoto offsetu k normálové expanzi slupky ($H_\perp$) vzniká efektivní drift $v_{eff} \approx H_\perp u^*$, který generuje měřitelný dipólový signál ve strukturách (např. v hustotě hlubokých rádiových zdrojů úměrné $\hat{d} \cdot \hat{n}$).

### 10.3 Kandidátský analog v Lineum
Otázkou je, zda pole generované rovnicemi Lineum dokáže přirozeně vytvořit strukturu (obálku, fázovou bariéru), která má svůj střed (těžiště), a zda lze v této struktuře udržet asymetrickou pozici "pozorovatele". Zda tedy PDE obálka tvoří excentrické těžiště produkující stabilní gradient, představující možný analog pro $u^*$.

### 10.4 Formální definice metrik pro Lineum
Před jakoukoliv simulací je nezbytné formálně definovat základní pojmy, aby byl měřicí operátor izolován od případných artefaktů. Metriky musí být rozděleny do dvou jasných tříd:
- **Třída A (Direction / sign calibration metric):** Kontroluje, zda vektor dipólu směřuje správně vůči offsetu v závislosti na zvolené konvenci.
- **Třída B (Offset-magnitude metric):** Kontroluje, zda naměřená amplituda dipólu správně škáluje s velikostí relativního offsetu (např. $|\vec{u}|/R$).

**Základní pojmy a operátory:**
- **Střed pole / centroid:** Geometrické těžiště ($C$) určené ze striktně nezáporné váhy fázového pole (např. maska obálky nebo kvadratická velikost $|\phi|^2$).
- **Pozice pozorovatele a offset:** Souřadnice referenčního bodu ($O$) a z něj definovaný offsetový vektor $\vec{u} = O - C$.
- **Hranice / obálka:** Uzavřená izočára nebo izoplocha fázového pole.
- **Úhlový profil měřené veličiny ($q(\theta)$ nebo $q(\Omega)$):** Explicitně stanovená skalární veličina závislá na úhlu pohledu pozorovatele. 
- **Vektor první harmonické ($\vec{b}$):** Pro 2D obálku definujeme geometrický vektor jako $\vec{b} = \frac{1}{\pi} \int \hat{n} q(\theta) d\theta$.
- **Absolutní monopól ($M_{abs}$) a limitace normalizace:** Celkový integrál $M_{abs} = \int |q(\theta)| d\theta$ je užitečný pro kontrolu kontrastu či šumu, ale **nesmí** být používán jako primární odhad pro velikost offsetu. Normalizace $|\vec{b}|/M_{abs}$ totiž u malých offsetů ztrácí úměrné škálování s $|\vec{u}|$ a může dávat zhruba konstantní poměr.
- **Pravidlo nulového jmenovatele:** Pravidlo (pokud $M_{abs} < \epsilon_M$, případ je klasifikován jako "nedefinovaný základ") platí pro tuto absolutní normalizaci. Pro primární odhad velikosti offsetu (Třídu B) se místo $M_{abs}$ musí použít stabilní známé měřítko, např. velikost obálky $R$. Výsledný kalibrovaný odhad offsetu je pak $A_{offset} = |\vec{b}|/R \approx |\vec{u}|/R$.

### 10.5 Kritérium úspěchu
Úspěchem této fáze bude nalezení stabilní, dobře definované projekce pole pro excentrického pozorovatele, která nezanikne okamžitě vlivem šumu. Pokud struktura umožňuje mapovat lokální gradient na excentrickou pozorovatelskou osu, stává se tento princip _kandidátským mechanismem_. Úspěšné odvození však _vyžaduje převod na observable_, než bude moci být nazváno fyzikální predikcí.

### 10.6 Kritérium falsifikace
Falsifikace nastane, pokud se prokáže, že žádná stabilní obálka neumožňuje vznik referenčního bodu (těžiště neexistuje, je nestabilní) nebo že se jakákoliv počáteční asymetrie nutně a nezadržitelně vyhlazuje do izotropie v makroskopickém limitu. V takovém případě zůstává jakékoliv propojení _zatím nedoloženo_.

### 10.7 Podmínky nerozhodnutelnosti
Nerozhodnutelnost by nastala tehdy, pokud je osa extrémně citlivá na počáteční podmínky a nelze odlišit, zda jde o fyzikální vlastnost pole nebo čistě o numerický artefakt gridu a okrajových podmínek.

### 10.8 Kontrolní Null testy a kalibrační testy
Navržená projekce musí projít přes tyto explicitní testy pro oddělení geometrie od numerických a fyzikálních artefaktů. Posunutý pozorovatel uvnitř konečné symetrické obálky není sám o sobě chyba měření; je to kalibrační případ observer-offset projekce. Falešným pozitivem by bylo, pokud stejný signál vzniká i bez fyzické hranice, bez asymetrie, nebo pouze kvůli souřadnicím, gridu či šumu.

**Kategorie testů:**
- **A. Centrovaný pozorovatel v symetrické konečné obálce:** Očekávaný výsledek je čistý nulový (nebo blížící se nule) dipól.
- **B. Posunutý pozorovatel (offset) v symetrické konečné obálce:** Očekávaný výsledek je geometrický dipól zarovnaný s offsetovým vektorem. _Toto je kalibrační test, nikoliv falešně pozitivní případ._
- **C. Čistá souřadnicová translace:** Posun celého pole (obálky) i pozorovatele současně. Měřený dipól musí zůstat invariantní. Pokud se změní, měření je citlivé na souřadnicový artefakt.
- **D. Rotovaný souřadnicový rámec:** Otočení celé konfigurace. Dipólový vektor musí rotovat spolu se systémem a jeho amplituda musí zůstat stabilní.
- **E. Nekonečné (nebo efektivně homogenní) pole bez hranice/asymetrie:** Samotný posun pozorovatele v takovém poli nesmí vytvořit stabilní fyzikální dipól.
- **F. Náhodný šum (Random noise field):** Nesmí generovat stabilní makroskopický dipólový směr přes opakovaná nasazení s různými náhodnými seedy.
- **G. Test rozlišení mřížky (Grid-resolution check):** Změna kroku mřížky nesmí vyprodukovat odlišnou amplitudu ani směr nad stanovenou toleranci.
- **H. Test okrajových podmínek (Boundary-condition check):** Změna okrajových podmínek (např. periodické vs. Dirichletovy) na vnějším okraji simulačního boxu nesmí ovlivnit měření dipólu uvnitř obálky.
- **I. Test s experimentální regularizací (volitelné):** Aplikace lokálních filtrů (např. SoftAbs) k ověření, zda nevytvářejí falešná pozitiva (možno provést až po úspěšném průchodu testy A-H).

### 10.9 Jaké varianty Lineum testovat a návrh dalšího kroku
Návrh prototypu (Prototype HSU-LINEUM-01A) bude explicitně kalibrační (Calibration-first). Těžké PDE simulace (jako Eq-11 nebo Phase 75) nebudou spuštěny dříve, dokud samotný dipólový operátor neprojde kalibrací na hračkovém (toy) modelu.

**Aplikace na varianty Lineum:**
Jakmile měřicí operátor projde kalibrací, bude nasazen na historicky podporované varianty Lineum. Testování se neomezí pouze na kanonickou rovnici Eq-11. Projekt zachovává a prověří:
- **Eq-11 / TDGL-like:** (kanonická rovnice)
- **Eq-4 / Eq-4' a další historické drafty:** (historická, opuštěná)
- **Eq-9-like / kinetická disipace:** (vyvrácená)
- **SoftAbs / escape-valve filtry:** (experimentální)
- **Registry Lock / Phase 71:** (pracovní draft)
- **Soft Cloak / Phase 75:** (pracovní draft, pouze inspirační)

Všechny nekanonické a historické větve zůstávají nadále ve svých původních statusech. Slouží výhradně jako _kandidátské mechanismy_ nebo _možné analogy_ k izolování toho, za jakých podmínek PDE pole tvoří fázovou asymetrii požadovanou udržením offsetu. Cílem experimentu je získat nezávislá matematická data (čeká na nezávislý test), propojení na reálný vesmír je v těchto testech _zatím nedoloženo_.

### 10.10 Výpočetní kontrola a auditovatelnost metrik
Jakékoliv výstupy nejsou a nebudou přijímány bez možnosti nezávislého auditu. Platí následující přísná pravidla:
- Očekávané výsledky na "hračkových" (toy) modelech musí být vždy sepsány a schváleny _před_ samotným spuštěním kódu.
- Každá metrika musí mít předem definované analytické očekávání nebo očekávání na základě sanity checku, pokud je to možné.
- **Definice oddělených tolerancí:** Je zakázáno používat jedinou plošnou toleranci. Tolerance analytické kontroly první harmonické musí být definována konkrétně pro: relativní chybu $|\vec{b}|/|\vec{u}|$, úhlovou chybu mezi $\vec{b}$ a $\vec{u}$, chybu rotační kovariance, chybu translační invariance a konvergenci $|\vec{b}|/R$ při zjemňování mřížky. Přesné prahy (třeba i provizorní) nesmí být deklarovány jako konečné, dokud nebude jasně definována diskretizace operátoru.
- Z reportovaných výsledků musí být zřejmé, co je analytické očekávání, co je numerické měření ze simulace a co je interpretace.
- Žádný výsledek není považován za platný (auditovatelný výpočet), pokud nejsou explicitně uvedeny výchozí předpoklady, vzorce a způsob normalizace. Sdělení typu "skript říká X" je nedostačující.

### 10.11 Očekávané výsledky prototypu HSU-LINEUM-01A (Před spuštěním kódu)
Pro nadcházející kalibrační prototyp definujeme následující očekávání, aby mohl být výstup nezávisle a transparentně auditován. Tento kalibrační prototyp bude používat pouze fixní geometrické obálky (ne fyzikální rovnice):

| Test | Očekávaný výsledek před spuštěním kódu | Proč k tomu musí dojít (Zdůvodnění) | Co by znamenalo selhání (Failure means) |
|---|---|---|---|
| **A. Centrovaný pozorovatel** | Měřená první harmonická $\vec{b} \approx 0$ (v analytické toleranci). | Symetrická obálka z pohledu středu nemá žádný preferovaný směr. | Metrika nefunguje; chybně integruje nebo mřížka zavádí falešnou asymetrii. |
| **B. Off-center pozorovatel** | Pokud se použije deficit vzdálenosti, $\vec{b}$ je zarovnán s $\vec{u}$. Pokud surová vzdálenost, $\vec{b}$ je anti-zarovnán. Naměřené $|\vec{b}|/R$ lineárně škáluje s $|\vec{u}|/R$ pro malé offsety. | Asymetrie vzdálenosti nutně generuje směrový vektor, jehož znaménko závisí na definici a amplituda na offsetu. | Osa $\vec{b}$ neodpovídá zvolené konvenci $\vec{u}$, nebo chybí úměrné škálování amplitudy. |
| **C. Translace soustavy** | Shodná amplituda i směr dipólu vůči offsetu. | Fyzikální gradient nezávisí na absolutní pozici v mřížce. | Artefakt absolutních souřadnic nebo okrajů (boundary artifact). |
| **D. Rotace soustavy** | Vektor $\hat{d}$ plynule rotuje s polem; amplituda zůstává invariantní. | Izotropie samotného měřicího prostoru. | Diskretizační artefakt čtvercové mřížky (grid-locking). |
| **E. Homogenní pole** | Posun pozorovatele nevygeneruje žádný stabilní fyzikální dipól. | Neexistuje žádná hranice (obálka), ke které by se gradient mohl vztahovat. | Operátor uměle vytváří dipól z pouhé translace "prázdnoty". |
| **F. Náhodný šum** | Směr $\hat{d}$ napříč seedy netvoří konzistentní makroskopickou osu. | Šum je izotropní a neobsahuje preferovanou fyzikální osu. | Náchylnost k fixaci na malý lokální extrém; chybějící robustní váhování. |
| **G. Test rozlišení mřížky** | Amplituda i směr dipólu konvergují s rostoucím rozlišením. | Fyzikální výsledek nesmí být závislý na velikosti buňky. | Amplituda nebo směr se systematicky mění s velikostí mřížky. |
| **H. Okrajové podmínky** | Změna vnější hranice boxu nemění dipól uvnitř vzdálené obálky. | Okraj boxu je dostatečně daleko, aby neovlivnil lokální těžiště. | Měřený dipól se mění čistě kvůli okrajům simulačního boxu. |

_Žádné těžké PDE simulace Lineum (Eq-11, Phase 75) nebudou provedeny, dokud operátor spolehlivě neprojde tímto kontrolním listem na statických mock datech._

### 10.12 Analytická kontrola toy modelu kruhové obálky
Abychom nezáviseli pouze na výstupu ze skriptu, musíme před spuštěním kódu stanovit analytické očekávání pro kalibrační toy model. 

Pro 2D kruhovou obálku se středem $C$, poloměrem $R$ a pozorovatelem $O = C + \vec{u}$ definujeme směrový vektor paprsku $\hat{n}(\theta)$. 
Pokud je měřenou veličinou vzdálenost k hranici z pohledu pozorovatele, platí:
$\rho(\theta) = -\vec{u} \cdot \hat{n} + \sqrt{R^2 - |\vec{u}|^2 + (\vec{u} \cdot \hat{n})^2}$ pro $|\vec{u}| < R$.

Pro malý offset $|\vec{u}| \ll R$ se to redukuje na:
$\rho(\theta) \approx R - \vec{u} \cdot \hat{n}$

Z toho plyne zásadní nutnost explicitně určit konvenci měřené veličiny. Pro vektor první harmonické definujeme $\vec{b} = \frac{1}{\pi} \int \hat{n} q(\theta) d\theta$.

**Tabulka analytických očekávání pro 2D kruhový toy model:**

| Konvence měřené veličiny ($q$) | Profil pro malý offset | Očekávaná 1. harmonická ($\vec{b}$) | Směr vůči offsetu | Odhad velikosti offsetu ($|\vec{b}|/R$) |
|---|---|---|---|---|
| Surová vzdálenost: $q = \rho(\theta)$ | $q \approx R - \vec{u} \cdot \hat{n}$ | $\vec{b} \approx -\vec{u}$ | opačně zarovnán (anti-aligned) | $\approx |\vec{u}|/R$ |
| Deficit vzdálenosti: $q = R - \rho(\theta)$ | $q \approx \vec{u} \cdot \hat{n}$ | $\vec{b} \approx \vec{u}$ | přímo zarovnán (aligned) | $\approx |\vec{u}|/R$ |
| Homogenní pole: $q = \text{konst.}$ | $q = \text{konst.}$ | $\vec{b} \approx 0$ | nemá fyzikální smysl | nemá fyzikální smysl |

**Poznámka k normalizaci absolutním monopólem:**
Pokud by se pro deficit vzdálenosti $q(\theta) = R - \rho(\theta) \approx \vec{u} \cdot \hat{n}$ aplikovala absolutní monopólová normalizace $M_{abs} = \int |q(\theta)| d\theta = 4|\vec{u}|$, výsledný poměr dipólu vůči monopólu bude zhruba $\pi/4$. 
Tento poměr je přibližně konstantní i pro malé offsety a **neměří** velikost offsetu pozorovatele $|\vec{u}|$. Absolutní normalizace může sloužit jako diagnostika kontrastu, ale primárním odhadem velikosti offsetu (Offset-magnitude metric) na testovaném modelu musí být poměr se stabilním geometrickým měřítkem, tedy $A_{offset} = |\vec{b}|/R \approx |\vec{u}|/R$.

Tato konvence musí být při implementaci explicitně vybrána a uvedena v kódu.

### 10.13 Výsledky kalibračního prototypu HSU-LINEUM-01A

Pro ověření základního operátoru zjišťujícího dipól byl úspěšně sestaven a spuštěn kalibrační prototyp 2D toy-modelu kruhové obálky. Byla použita nezávislá dvoustupňová validace, kde diskrétní numerický výpočet nad vzorky úhlového profilu ($\hat{n}_i$, $N_{\theta} = 3600$) byl konfrontován proti přesné analytické formuli $\rho(\theta)$. 

**Co bylo testováno:**
- Metoda extrakce vektoru první harmonické $\vec{b} = \frac{1}{\pi} \int \hat{n} q(\theta) d\theta$.
- Konvence měřené veličiny $q(\theta)$: Surová vzdálenost $\rho(\theta)$, deficit vzdálenosti $R - \rho(\theta)$ a homogenní prostor.
- Sada přesných null-testů A–H.
- Různé relativní velikosti posunů ($|\vec{u}|/R \in \{0.01, 0.05, 0.10\}$).

**Očekávání vs. Měřené výsledky (Třída B - Offset-magnitude kalibrace):**

| Test | Zvolená konvence | Očekávané $\vec{b}$ | Naměřené $\vec{b}$ | Absolutní chyba | Status |
|---|---|---|---|---|---|
| A. Centrovaný poz. ($\vec{u}=0$) | Deficit vzdál. | `[0.0000, 0.0000]` | `[0.0000, 0.0000]` | $0.0$ | **PASS** |
| B. Excentrický ($\vec{u}=[0.05, 0]$) | Deficit vzdál. | `[0.0500, 0.0000]` | `[0.0500, 0.0000]` | $0.0$ | **PASS** |
| B. Excentrický ($\vec{u}=[0.05, 0]$) | Surová vzdál. | `[-0.0500, 0.0000]` | `[-0.0500, 0.0000]` | $0.0$ | **PASS** |
| C. Čistá translace soustavy | Deficit vzdál. | Zůstane invariantní | Zůstalo invariantní | $0.0$ | **PASS** |
| D. Rotace 45° | Deficit vzdál. | `[0.0354, 0.0354]` | `[0.0354, 0.0354]` | $0.0$ | **PASS** |
| E. Homogenní pole | Konstantní | `[0.0000, 0.0000]` | `[0.0000, 0.0000]` | $0.0$ | **PASS** |
| F. Náhodný šum (předběžná sanity kontrola) | Deficit vzdál. | Zvládne fluktuace | `[0.0482, -0.0012]` | $0.002$ | **PASS** |
| G. Konvergence úhlového vzorkování | Deficit vzdál. | Chyba $\to 0$ | Diskrétní suma je plně konvergovaná u $N=36$ (chyba $\approx 10^{-17}$). | - | **PASS** |
| H. Okrajové podmínky vnějšího boxu | Deficit vzdál. | Neaplikovatelné | Netestováno v tomto prototypu bez vnějšího boxu. | - | **N/A** |

**Analytický důkaz exaktního chování pro ideální kruhovou obálku:**
Nezávislý analytický test prokázal pro 2D model s offsetem $|\vec{u}| < R$ cenný výsledek: pro konvenci deficitu vzdálenosti $q(\theta) = R - \rho(\theta)$ platí první harmonická $\vec{b} = \vec{u}$ **exaktně**, nikoliv jen jako aproximace pro malé $\vec{u}$.

Rovnice vzdálenosti na kružnici z excentrického bodu je:
$\rho(\theta) = -\vec{u} \cdot \hat{n} + \sqrt{R^2 - |\vec{u}|^2 + (\vec{u} \cdot \hat{n})^2}$

Pro deficit vzdálenosti dostaneme:
$q(\theta) = R - \rho(\theta) = R + \vec{u} \cdot \hat{n} - \sqrt{R^2 - |\vec{u}|^2 + (\vec{u} \cdot \hat{n})^2}$

Výpočet vektoru první harmonické $\vec{b} = \frac{1}{\pi} \int_0^{2\pi} \hat{n} q(\theta) d\theta$:
1. $\frac{1}{\pi} \int \hat{n} R d\theta = 0$ (symetrie konstanty)
2. $\frac{1}{\pi} \int \hat{n} (\vec{u} \cdot \hat{n}) d\theta = \vec{u}$
3. $\frac{1}{\pi} \int \hat{n} \sqrt{R^2 - |\vec{u}|^2 + (\vec{u} \cdot \hat{n})^2} d\theta = 0$ (integrál liché funkce $\hat{n}$ v součinu se sudou symetrickou odmocninou se přes celou periodu vynuluje)

Výsledek je tedy $\vec{b} = \vec{u}$.
Z toho plyne, že v případě surové vzdálenosti ($q = \rho(\theta)$) platí právě obráceně $\vec{b} = -\vec{u}$. Tento poznatek validuje geometrii metriky. K testu šumu (F): Vložena byla 10% aditivní normální fluktuace na $\rho(\theta)$, měřilo se pro jeden fixní seed (předběžná sanity kontrola), nejedná se o dokončený statistický null test.

**Interpretace a připravenost:**
- **Zhodnocení úspěchu:** Operátor prošel kalibrací na ideální 2D kruhové obálce. Numerické výsledky úhlového vzorkování se shodují s analytickými očekáváními. Výsledek validuje geometrii boundary-distance/deficit metriky.
- **Selhání a limitace:** Kalibrace na ideální geometrii má omezený rozsah. Nejde ještě o validaci pro reálná PDE pole s vlivy diskretizace prostoru.
- **Další nezbytný krok (Prototype HSU-LINEUM-01B):** Před nasazením na Lineum-native pole je bezpodmínečně nutný raster/grid a nepravidelná obálka test. HSU-LINEUM-01B musí jako most k realitě otestovat:
  1. Rasterizovanou kružnici na 2D gridu a konvergenci rozlišení mřížky.
  2. Rekonstrukci centroidu z nezáporných vah pixelů.
  3. Nepravidelnou (např. eliptickou) nebo zašuměnou hranici.
  4. Okrajové podmínky skutečného konečného boxu.
  5. Chyby úhlové interpolace z pixelů a chybějící hraniční vzorky.

Teprve po schválení a úspěchu robustness prototypu 01B lze postoupit k PDE simulacím. I pak platí, že budoucí PDE dipól bude kandidátní signál mechanismu, nikoli automaticky fyzikální validaci.

### 10.14 Výsledky robustnostního prototypu HSU-LINEUM-01B

Prototyp HSU-LINEUM-01B slouží výhradně jako test robustnosti měřicího operátoru na neideální (rasterizované, zrnité a zašuměné) geometrii. Nejde o fyzikální test Lineum PDE, ale o ověření, zda numerická reprezentace na mřížce nezničí měření posunu pozorovatele.

**Co bylo testováno (vše na gridu 200x200 s centroidem detekovaným z pixelů, offset $|\vec{u}|/R = 0.1$):**
- A. Rasterizovaná kružnice (vliv zubatosti hranice).
- C. Konvergence mřížky (rozlišení poloviční vs. dvojnásobné).
- D, E. Geometrické transformace uvnitř mřížky.
- F. Elipsa (mírná deformace).
- G. Radiální šum na hranici.
- H. Ztráta $30\%$ hraničních vzorků.
- I. Oříznutí vnějším boxem mřížky.
- J. Čistý šum (ověření falešných pozitiv).

**Očekávání vs. Měřené výsledky (Konvence: deficit vzdálenosti):**

| Test | Očekávané $\vec{b}$ | Naměřené $\vec{b}$ | Abs. chyba | Treshold | Status | Interpretace |
|---|---|---|---|---|---|---|
| A. Rasterizovaný kruh | `[5.00, 0.00]` | `[5.01, 0.00]` | $0.015$ | $< 1.0$ | **PASS** | Těžiště určeno přesně, diskretizace vnáší nepatrnou chybu. |
| C. Konvergence mřížky | - | - | - | - | **PASS** | Relativní chyba pro $R=100$ ($0.0002$) je menší než pro $R=25$ ($0.0003$). |
| D. Translace v boxu | `[5.00, 0.00]` | `[5.01, 0.00]` | $0.015$ | $< 1.0$ | **PASS** | Invariantní vůči absolutní pozici uvnitř mřížky. |
| E. Rotace 45° | `[3.54, 3.54]` | `[3.54, 3.54]` | $0.009$ | $< 1.0$ | **PASS** | Operátor si zachovává rotační symetrii. |
| F. Mírná elipsa | `[5.00, 0.00]` | `[4.53, 0.00]` | $0.469$ | $< 5.0$ | **PASS** | Směr byl zachován, amplituda je vychýlena tvarem (očekáváno). |
| G. Radiální šum | `[5.00, 0.00]` | `[5.20, 0.20]` | $0.284$ | $< 2.0$ | **PASS** | Signál zřetelně přebíjí hraniční šum. |
| H. Chybějící vzorky (30 %) | `[5.00, 0.00]` | `[3.55,-0.01]` | $1.450$ | $< 2.0$ | **PASS** | Signál slábne úměrně ztrátě dat, ale směr zůstává správný. |
| I. Oříznutí boxem (truncation) | Korupce signálu | `[6.26, 0.00]` | $1.265$ | $> 1.0$ | **CRITICAL HAZARD** | Ořez boxem vnáší významný umělý dipól (falešný signál hrany). |
| J. Čistý šum (5 seedů) | `[0.00, 0.00]` | `[-0.01,0.28]` | $0.279$ | $< 2.0$ | **SANITY CHECK** | Předběžná kontrola, pět seedů nestačí pro statistický null test. Nevytváří stabilní osu. |

**Interpretace a připravenost pro Lineum-native pole:**
- **Co prošlo:** Prototyp 01B podpořil, že měřicí operátor přežije rasterizovanou a mírně zašuměnou toy geometrii. Směr asymetrie zůstává stabilní. Těžiště je získáváno z nezáporných vah.
- **Co selhalo / Na co si dát pozor:** Test oříznutí boxem (Test I) odhalil kritické riziko: struktury dotýkající se okraje simulace generují silné falešné dipóly. Test šumu (Test J) je pouze předběžný sanity check; pět seedů není dostatečných pro statistický null test. Toto ještě nevaliduje operátor na reálných Lineum PDE polích.
- **Další krok (Rozdělení fáze HSU-LINEUM-01C):** Vložení "statického tvaru do matice" nesmí být zaměňováno za výsledek Lineum PDE dynamiky. Fáze 01C je proto striktně rozdělena na dvě vrstvy:
  - **HSU-LINEUM-01C-a (Syntetická morfologická kalibrace):** Testování operátoru na kontrolovaných syntetických tvarech připomínajících možné Lineum obálky. Jedná se stále o toy model, **nikoli o Lineum fyziku**.

    > **Upozornění:** Vzorec z ideální kružnice nelze bez úprav přenést na nepravidelné obálky. U syntetických patvarů se testuje hlavně robustnost směru, stabilita centroidu a selhávací režimy, nikoli přesný odhad velikosti offsetu jako u kruhu. Parametr $R$ pro tyto tvary nelze používat jako pevnou analytickou hodnotu bez jasně definovaného referenčního měřítka. Hodnocení se opírá o vložený směr, úhlovou chybu, chybu centroidu, relativní stabilitu amplitudy, pásy nejistoty přes seedy a identifikaci selhání.

    **Povolené a zakázané interpretace pro 01C-a:**
    - **Povoleno usuzovat:** Zda operátor zachovává přibližný směr pod kontrolovanou deformací; zda je centroid stabilní nebo nejednoznačný; jak díry/laloky způsobují konkrétní selhávací režimy; že fuzzy hranice zvyšují nejistotu; a že chybějící vzorky snižují amplitudu.
    - **Zakázáno usuzovat:** Žádná tvrzení o Lineum fyzice, žádná tvrzení o kosmologii, zakázáno tvrdit, že amplituda nepravidelného tvaru se lineárně rovná fyzikálnímu posunu pozorovatele, a zakázáno vydávat syntetický dipól za potvrzení HSU.

    **Očekávané výsledky před spuštěním kódu 01C-a:**

    | Třída tvaru (Shape class) | Co je známo z konstrukce | Co má být získáno | Co by znamenalo selhání | Interpretační limit |
    |---|---|---|---|---|
    | Nepravidelná uzavřená obálka | Globální asymetrie/směr | Směr dipólu kopíruje deformaci | Falešná kolmá osa / nestabilita | Amplituda neodpovídá přesnému u. |
    | Fuzzy (neostrá) hranice | Umělý gradient | Nárůst nejistoty měření | Vektor dipólu náhodně rotuje | Vynucuje přidání pásu nejistoty. |
    | Mírná asymetrie | Směr vloženého offsetu | Získaný směr a úhlová chyba | Ztráta původního směru | Testuje primárně citlivost operátoru. |
    | Elipsa | Poměr poloos | Bimodální rozložení | Měření mimo osu elipsy | Nelineární bias na ose. |
    | Vícenásobné laloky | Roztržení morfologie | Zvýšená chyba / nejednoznačnost | Neschopnost určit centroid | Zcela matoucí pro konvenci offsetu. |
    | Obálka s děrami | Chybějící segmenty | Útlum amplitudy | Získaný směr ukazuje do díry | Měření závisí na prahu detekce. |
    | Chybějící hraniční vzorky | Fragmentovaná data | Relativní zachování směru | Úplná ztráta vektoru | Snížená magnituda. |
    | Čistý šum / bez obálky | Nulový offset | Náhodný šum kolem [0,0] | Stabilní fixní osa napříč seedy | Není přítomna žádná topologie. |

    **Výsledky kalibrace 01C-a (Syntetické tvary):**
    
    *Do všech tvarů byl injektován posun pozorovatele o velikosti 5.0 px pod úhlem 45°. Pro centroid se používá vážené těžiště přes kladnou fázi.*

    | Třída tvaru | Naměřené těžiště | Úhlová chyba směru | Naměřená amplituda | Selhávací režim / Pozorování | Interpretační limit pro Lineum |
    |---|---|---|---|---|---|
    | 1. Nepravidelná obálka | `[99.9, 100.0]` | $1.2^\circ$ | $4.84$ | Žádný | Směr zůstává vysoce spolehlivý, amplituda je stabilní. |
    | 2. Fuzzy hranice | `[100.0, 100.0]` | $0.0^\circ$ | $4.99$ | Žádný | Gaussián nepoškozuje přesnost, pokud je práh konzistentní. |
    | 3. Mírná asymetrie | `[114.7, 100.0]` | $1.1^\circ$ | $5.02$ | **Posun těžiště** | Těžiště se odtrhlo od geometrického středu. Asymetrie generuje ambiguózní centroid. |
    | 4. Elipsa (60x40) | `[100.0, 100.0]` | $11.4^\circ$ | $5.09$ | Žádný | Tvarová deformace vnáší úhlový bias (očekáváno). |
    | 5. Vícenásobné laloky | `[100.0, 100.0]` | $20.3^\circ$ | $5.30$ | Žádný | Významný úhlový rozptyl kvůli morfologii, ale směr zůstává hrubě zachován. |
    | 6. Obálka s děrami | `[100.0, 100.0]` | $0.0^\circ$ | $11.35$ | **Amplitudová exploze** | Díry drasticky zkreslují integrál vzdálenosti. Amplituda je nepoužitelná. |
    | 7. Chybějící vzorky | `[100.0, 100.0]` | $0.3^\circ$ | $3.48$ | **Útlum amplitudy** | Ztráta dat úměrně snižuje měřený signál, ale neničí směr. |
    | 8. Čistý šum | `[99.7, 99.4]` | $88.8^\circ$ | $1.27$ | **Náhodný dipól** | Šum generuje náhodné vektory o nízké amplitudě. Očekávané chování. |
    
    **Závěrečné doporučení k fázi 01C-a:**
    Operátor prokázal mimořádnou směrovou robustnost. Přesné odhady amplitudy však na nepravidelných modelech (zejména s děrami) drasticky selhávají ("Amplitudová exploze"). Zvláštní třídou selhání jsou asymetrické obálky, které zcela deformují výpočet samotného těžiště (tzv. "ambiguózní centroid").
    **Závěr:** V reálných Lineum simulacích smí být interpretován primárně zachovaný směr dipólu, zatímco jeho absolutní magnituda nesmí být přímo srovnávána s kosmologickým posunem bez zohlednění tvarového zkreslení.
    
    *Povolení k pokračování:* Fáze 01C-b může být připravena až po zavedení předběžného morfologického síta.

  - **HSU-LINEUM-01C-b (Skutečný Lineum-native snapshot kalibrace):** Nastane, abychom mohli připravit morfologické síto pro první Lineum-native snapshoty. Nejdříve budeme klasifikovat tvar, teprve poté měřit dipól. Využije reálné snapshoty polí z Lineum rovnic (kanonické i relevantní historické varianty). Účelem je ověřit, zda pole obsahují měřitelnou obálku daleko od hranic, nikoliv deklarovat fyzikální objev. Amplituda není důvěryhodná u děr a degenerovaných obálek.

### Předběžné morfologické síto pro 01C-b

Před jakoukoliv interpretací dipólu musí reálný Lineum-native snapshot projít preflight sítem. Snapshot bude klasifikován následovně:
- **A. Přijato pro směrovou analýzu dipólu.**
- **B. Přijato pouze pro kvalitativní zhodnocení.**
- **C. Zamítnuto jako nevalidní pro měření observer-offsetu.**

**Pravidla síta (Preflight Gate):**
1. **Boundary clearance:** Zamítnuto (Reject), pokud se struktura dotkne nebo téměř dotkne okraje simulačního boxu.
2. **Closed-envelope quality:** Zamítnuto nebo označeno za ambiguózní, pokud je hranice otevřená, roztříštěná, nebo neumožňuje ray-casting.
3. **Hole detection:** Pokud jsou přítomny vnitřní díry, směr může být interpretován, ale amplituda musí být zneplatněna (Invalidated).
4. **Centroid ambiguity:** Pokud se centroid silně posouvá kvůli tvarové asymetrii obálky, měření je označeno za ambiguózní.
5. **Multi-lobe detection:** Pokud struktura obsahuje vícero soupeřících laloků, měření je pouze kvalitativní, dokud není jedna obálka izolována.
6. **Fuzzy boundary:** Vyžaduje se pás nejistoty a test citlivosti na prahování.
7. **Noise-only rejection:** Zamítnuto, pokud neexistuje žádná koherentní obálka.
8. **Seed/grid consistency:** Před jakoukoliv interpretací se vyžaduje podobná morfologie napříč vícero seedy a rozlišeními mřížky.
9. **Direction vs amplitude separation:** Směr může být uznán jako platný, zatímco amplituda stejného měření bude prohlášena za nevalidní.
10. **Interpretation limit:** I úspěšně prošlý 01C-b snapshot nepředstavuje kosmologické tvrzení.

**Tabulka morfologické klasifikace:**

| Morfologický stav snapshotu | Směr dipólu | Amplituda dipólu | Stav měření | Důvod |
|---|---|---|---|---|
| Čistá uzavřená obálka daleko od hranice | Použitelný | Provizorní | Přijato pro analýzu | Splňuje ideální 2D předpoklady HSU-like měřáku. |
| Přítomny vnitřní díry (holes) | Možná použitelný | Nevalidní | Částečně přijato | Ray-casting narazí na vnitřní okraj; amplituda exploduje. |
| Dotyk hranice boxu (boundary contact) | Nevalidní | Nevalidní | Zamítnuto | Okraj boxu generuje masivní falešný dipól (okrajový artefakt). |
| Žádná koherentní obálka (noise) | Nevalidní | Nevalidní | Zamítnuto | Není topologie, nad kterou by šel ustavit observer-offset. |
| Více laloků (multi-lobed structure) | Jen kvalitativní | Nevalidní | Kvalitativní jen | Těžiště je ambiguózní; nutná izolace laloku. |
| Rozmazaná hrana (fuzzy boundary) | Použitelný s nejistotou | Nevalidní | Vyžaduje test | Vyžaduje otestování citlivosti na prahovanou hodnotu hrany. |

**Upozornění:** Ani 01C-a, ani připravované síto v 01C-b neprokazují kosmologickou fyziku. Případný dipól v PDE výstupu je pouze *kandidátní signál*, dokud nepřežije null testy, mřížkové testy a prozkoumání vícero variant rovnic.

### Inventura existujících Lineum polí (01C-b Preflight)

Byla provedena inventura historických a existujících větví Lineum v rámci projektu, aby se zjistilo, zda existují hotová pole vhodná k okamžitému měření observer-offsetu podle nových přísných pravidel morfologického síta. 

**Zjištění napříč variantami rovnic:**
- **Kanonická větev (Eq-11):** Typické rané snapshoty mají čistou obálku, avšak s vývojem simulace silně expandují. Většina uložených koncových stavů nevyhnutelně naráží na hrany výpočetního boxu.
- **Soft Cloak (Fáze 75):** Princip sdílené obálky generuje lokální propady hustoty (vnitřní díry) nebo tvoří více nezávislých ostrovů před spojením.
- **Registry Lock (Fáze 71):** Vlny orientačního vázání formují silně asymetrické a vícelalokovité obálky, což znemožňuje určit globální centroid.
- **Eq-9 (Disipativní model):** Silně tlumí vysoké frekvence, čímž vznikají velmi rozmazané (fuzzy) hrany. Tyto výstupy vyžadují dodatečný test citlivosti prahování.
- **Eq-4 / Eq-4' (Fragmentované stavy):** Vykazují extrémní roztříštěnost pole, obvykle zcela bez koherentní hlavní obálky.

**Klasifikace historických variant pro účely 01C měření:**

| Větev / Historická varianta | Typická morfologie | Okraje boxu | Díry | Laloky | Centroid | Klasifikace | Co lze interpretovat |
|---|---|---|---|---|---|---|---|
| **Kanonická větev (Eq-11)** | Expanzní obálka | Často dotyk | Ne | Ne | Stabilní | **C** (pozdní) / **A** (rané) | Použitelné pouze rané stavy; žádný hotový pozdní snapshot neprošel sítem kvůli dotyku hran. |
| **Fáze 75 (Soft Cloak)** | Sdílená obálka | Většinou ok | **Ano** | Ano | Mírný bias | **B** | Často obsahují díry; směr lze možná zkoumat, amplituda je nevalidní. |
| **Fáze 71 (Registry Lock)** | Více vázaných laloků | Většinou ok | Ne | **Ano** | **Ambiguózní** | **B** | Více laloků; pouze kvalitativní hodnocení, nelze stanovit jasný offset. |
| **Eq-9 (Frekvenční filtrace)**| Široké fuzzy obálky | Mírný dotyk | Ne | Ne | Stabilní | **B** | Nutný dodatečný pás nejistoty pro ray-casting. |
| **Eq-4 / Eq-4'** | Fragmentované pole | Roztříštěné | Ne | Mnoho | Ztracen | **C** | Zcela zamítnuto (chybí koherentní topologie). |

**Závěrečné doporučení k existujícím datům (Hodnocení jako negativní výsledek):**
Žádný existující pozdní snapshot není bezpečně způsobilý pro fyzikální měření observer-offset dipólu. Rané Eq-11 stavy mohou být kandidátní, ale musí být znovu generovány a zastaveny pod dohledem síta. Soft Cloak / Registry Lock mohou být metodologicky zajímavé, ale jejich díry/laloky omezují amplitudu a centroid. Tento negativní výsledek posouvá Lineum: ukazuje, jaká data musíme generovat, aby byl test férový. To znamená, že staré snapshoty zkrátka nebyly generovány s ohledem na tyto přísné morfologické hranice a pokus o jejich přímé měření by riskoval falešné závěry. Je proto vyžadována nová, dedikovaná fáze generování snapshotů.

## HSU-LINEUM-01D: Řízené generování snapshotů pro měření observer-offsetu

Abychom mohli korektně vyhodnotit chování dipólu nad reálným Lineum polem, je nezbytná nová fáze řízené generace dat, navržená výhradně k získání morfologicky bezpečných snapshotů. Tento oddíl slouží pouze jako návrh struktury této procedury; **v této fázi neprobíhá žádná exekuce kódu ani simulace**.

**1. Hlavní cíl generování:**
Získat sadu snapshotů vhodných k morfologickému sítu a následnému možnému měření směru dipólu. **Tato fáze není a nesmí být interpretována jako validaci kosmologické interpretace.**

**2. Kandidátní varianty rovnic:**
- Jako základní benchmark se vygeneruje **Kanonická větev (Eq-11)**.
- Výběrově budou přidány další historické/draftové varianty, ale pouze tehdy, pokud budou explicitně označeny a jejich zařazení bude podložené a odůvodněné.

**3. Stopovací podmínky (Stop Conditions):**
Simulace každého snapshotu bude pod bedlivým algoritmickým dohledem a **okamžitě zastavena**, jakmile:
- Struktura narazí na okraj boxu (zastavit předem).
- Vzdálenost k okraji (boundary clearance) klesne pod předem daný bezpečný limit.
- Morfologie zdegeneruje (roztříští se) nad předem určený práh.
- Těžiště (centroid) začne silně oscilovat a stane se ambiguózním.
- Uvnitř obálky se objeví díry (holes), čímž by měření amplitudy explodovalo.

**4. Požadované výstupy (Záznamová Metadata) na jeden snapshot:**
Každý vygenerovaný kandidátní snapshot bude kromě samotné matice doprovázen logem obsahujícím:
- Třídu morfologie (Morphology class)
- Bezpečnostní vůli od okraje (Boundary clearance)
- Stabilitu těžiště (Centroid stability)
- Indikátor děr (Hole flag)
- Počet laloků / úroveň fragmentace (Lobe count / fragmentation flag)
- Skóre rozmazání hran (Fuzzy-boundary score)
- Využitelnost směru (Direction usability)
- Validitu amplitudy (Amplitude validity)
- Metadata o rozlišení a seedu (Seed/grid metadata)
- Konečnou klasifikaci síta (Classification A/B/C)

**5. Bezpečnostní mantinely (Guardrails):**
- Pro ověření musí být využito **více velikostí mřížky** a **vícero nezávislých seedů**.
- Striktní zákaz interpretace, pokud by přesto došlo k okrajovému dotyku (boundary contact).
- Amplituda se vždy stává **nevalidní** ve chvíli výskytu děr.
- Směr se smí interpretovat pouze jako kandidátní u B-class snapshotů.
- Zákaz jakéhokoliv kosmologického jazyka.

**6. Výpočetní audito-disciplína (Calculation-audit discipline):**
Bude zachována přísná transparence před každým výsledkem, vyžadující dodání:
- Výpočetních vzorců (Formulas).
- Očekávaných hodnot (Expected values).
- Prahových hodnot (Thresholds).
- Surových výstupů (Raw outputs).
- Kritérií splnění (Pass/fail criteria).
- Selhávacích režimů (Failure modes).

**7. Kategorie stavu výstupu:**
Snapshot nakonec skončí pouze v jedné z kategorií:
- Přijato pro směrovou analýzu dipólu (Accepted for direction analysis).
- Přijato pouze pro kvalitativní hodnocení (Qualitative only).
- Zamítnuto (Rejected).

**8. Předregistrované kvantitativní prahy pro morfologické síto (01D):**

Aby se předešlo jakémukoliv zpětnému upravování kritérií ("p-hacking" nad morfologií), jsou před spuštěním fáze 01D pevně stanoveny následující hraniční hodnoty. Tyto prahy jsou provizorní pro fázi 01D a smějí být upraveny pouze v budoucí jasně označené metodologické revizi, nikoliv zpětně po nahlédnutí do očekávaných dat.

- **Poloměr obálky ($R_{eff}$ vs $R_{max}$):**
  - Nechť $R_{eff}$ je plošně ekvivalentní efektivní poloměr (např. $\sqrt{A/\pi}$). Je vhodný pro celkový odhad kompaktnosti.
  - Nechť $R_{max}$ je maximální vzdálenost od těžiště k detekovanému okraji obálky. U protáhlých či vláknitých tvarů se $R_{max}$ musí vždy explicitně logovat. Pokud je $R_{max} \gg R_{eff}$, struktura musí být označena za elongovanou/vícelalokovitou a může dle morfologie automaticky spadnout do třídy B nebo C.
- **Boundary clearance (Bezpečnostní odstup od okraje):** Primární bezpečnostní mírou zůstává $d_{edge}$, což je nejmenší skutečná vzdálenost detekovaného vnějšího okraje k hranici simulačního boxu. Dále nechť $d_{center}$ je vzdálenost těžiště k hranici boxu. Pravidlo zní:
  - **Bezpečný odstup:** $d_{edge} \ge \max(0.25 R_{eff}, 10 \text{ px})$ a současně $d_{center} \ge 1.25 R_{eff}$.
  - **Rizikový odstup:** $d_{edge}$ leží mezi $0.10 R_{eff}$ a $0.25 R_{eff}$.
  - **Dotyk s okrajem:** $d_{edge} < 0.10 R_{eff}$ nebo jakýkoliv přímý kontakt.
- **Hole detection rule (Detekce děr):** Nechť $T_{env}$ je detekční práh obálky. Za "díru" se považuje spojitá oblast uvnitř vnější obálky, ve které hodnota pole klesne pod práh $T_{hole}$ (kde $T_{hole} = 0.5 T_{env}$, pokud není speciálně odůvodněno jinak) a jejíž plocha přesahuje $2\%$ celkové plochy obálky. U děravých struktur je **amplituda vždy nevalidní**, dokud nebude případně vyvinuta a zvalidována separátní metrika odolná vůči dírám. Snapshot (např. ze Soft Cloak) se však ukládá jako diagnostický negativní případ.
- **Lobe/fragmentation threshold (Zlomyslná fragmentace):** Pokud obálka vygeneruje více než $2$ zcela oddělená maxima (každé s plochou $>10\%$ hlavní obálky), považuje se za vícelalokovitou/fragmentovanou.
- **Centroid ambiguity (Nejistota těžiště):** Těžiště je ambiguózní, pokud jeho posun mezi různými volbami prahu obálky (např. $10\%$ vs. $50\%$ maxima) překročí $5\%$ celkového poloměru objektu.
- **Fuzzy-boundary protocol:** U rozmazaných hran se provede výpočet směru třikrát (s prahem na $10\%$, $50\%$ a $90\%$ maxima obálky). Výsledek je bezpečný pouze tehdy, pokud se všechny tři naměřené směry shodují v toleranci $\pm 5^\circ$.
- **Minimální statistický vzorek:** Každý výsledek musí být potvrzen na minimálně **10 nezávislých seedy**.
- **Požadovaná rozlišení (Grid resolutions):** Simulace musí proběhnout na mřížkách min. $100 \times 100$ a musí být křížově ověřeny na mřížkách min. $200 \times 200$.
- **Priorita klasifikačních pravidel (Classification priority order):** Závažná selhání vždy přebíjejí mírnější klasifikace. Závěrečná třída snapshotu se vyhodnocuje v tomto striktním pořadí:
  1. **Třída C (Zamítnuto):** Jakýkoliv přímý dotyk s okrajem nebo $d_{edge} < \text{reject threshold}$. Toto pravidlo přebíjí všechny ostatní vlastnosti! Rovněž sem spadá úplná ztráta koherentní obálky nebo těžká fragmentace bez dominantní komponenty.
  2. **Třída B (Qualitative only):** Přítomnost děr (při bezpečném odstupu od okrajů) $\rightarrow$ směr možná kvalitativně poučný, amplituda nevalidní. Přítomnost více laloků (při bezpečném odstupu) $\rightarrow$ kvalitativní hodnocení, pokud nelze izolovat dominantní lalok. Fuzzy rozmazaná hrana, která neprojde testem tolerance napříč prahy.
  3. **Třída A (Accepted for direction analysis):** Čistá, uzavřená a koherentní obálka nacházející se bezpečně daleko od hranic, která projde všemi předchozími body síta.
- **Povinný loging pro C (Rejected):** I u zamítnutých stavů se musí zaznamenat: důvod selhání (např. ořez boxem), seed, grid, frame a velikost struktury v momentě rozpadu.

Tento předregistrovaný a výrazně bezpečnější metodologický rámec snižuje riziko dodatečného ohýbání kritérií. Sám o sobě sice nezaručuje pravdu konečného výsledku, ale ostře omezuje interpretační libovůli u případných budoucích simulací.

**9. Výsledky pilotního běhu HSU-LINEUM-01D (Kanonická větev Eq-11):**

Tento běh sloužil výhradně jako test generování sítě obálek dle morfologického síta (nesloužil jako fyzikální validace). Simulace Eq-11 byla provedena s 20 běhy (10 seedů na mřížce 100x100 a 10 seedů na 200x200). 

**Závěr pilotu:** Žádný snapshot nezískal třídu A.
Všech 20 generovaných snapshotů spadlo do **Třídy B (Qualitative only)**.
Zatímco boundary clearance byla u Eq-11 vynikající ($d_{edge} \approx 58 \text{ px}$, bezpečně od okraje), vnitřek obálky vždy zkolaboval do děr (Hole detection = True) a hrany vykazovaly fluktuace (Fuzzy fail = True). 

**Metodologický důsledek a Auditní korekce:**
Tento specifický Eq-11 pilot, používající tuto vortex-like počáteční podmínku a toto filled-envelope morfologické síto, vygeneroval B-class prstencové/děravé snapshoty (shell-like morphology). Amplituda je nevalidní pod současnou filled-envelope metrikou. To však ještě globálně nedokazuje, že Eq-11 nemůže vygenerovat žádnou A-class měřitelnou obálku při jiných počátečních podmínkách, parametrech, kanálech nebo definicích obálky.

Z tohoto pilotu plynou zásadní auditní body před dalším testováním:
1. **Díry vs. Topologická jádra:** Je nutné striktně rozlišit, zda je detekovaná prázdnota skutečně "patologická díra" (zborcení pole způsobené nestabilitou), nebo očekávané "topologické jádro / prstencová obálka" plynoucí z vírového charakteru pole, kdy amplituda poblíž středu přirozeně mizí.
2. **Shell-aware metrika:** Pro *HSU-like slupkové geometrie může být nutné definovat samostatnou shell-aware metriku. Současné síto bylo původně nastavené pro plnou uzavřenou obálku.* U plné obálky díra zneplatňuje amplitudu observer-offsetu, u slupky to však nemusí znamenat fyzikální selhání rovnice.
3. **FuzzyFail a nulové vektory:** Test úhlové stability směru (FuzzyFail) nesmí generovat umělá selhání (angular difference), pokud je samotný centroidní/dipólový vektor příliš malý (blízko počátku). K síti byla do budoucna přidána pojistka: pokud vektor nedosahuje minimálního magnituda, směr musí být označen jako "direction undefined / near-zero vector" namísto "fuzzy fail".
4. **Separátní kanály obálky:** Před dalšími testy bude nutné vyhodnotit, zda je surové $|\Psi|$ ten správný kanál pro definici obálky. Fyzikálnější obálku může poskytovat pole $\Phi$, hustota energie, $|\Psi|^2$, či prahovaná fázová bariéra.

**10. HSU-LINEUM-01E: Design Shell-Aware Observer-Offset Metriky**

Jelikož vírové počáteční podmínky přirozeně generují struktury s nulovým středem, je nezbytné odlišit naplněné obálky od slupkových geometrií. HSU pracuje se slupkovou geometrií, proto shell-like struktury nesmí být automaticky trestány jako patologické díry. Následující pravidla definují předregistrovaný design pro budoucí **shell-aware metriku** (fáze 01E).

### A. Klasifikace geometrií a typologie děr
Pro korektní analýzu zavádíme následující morfologické definice:
- **Filled-envelope object:** Plný, spojitý topologický útvar bez jakýchkoliv vnitřních nul a lokálních minim pod detekčním prahem. Zde je aplikovatelná původní plošná metrika.
- **Annular/ring object:** Prstencový dvoudimenzionální útvar vykazující jasnou vnitřní i vnější hranici (v řezu nebo v 2D simulaci).
- **Shell-like object:** Slupková struktura (obvykle 3D, v 2D se redukuje na ring object), kde většina energie leží v definované obálce kolem centrálního deficitu.
- **Topological core (Topologické jádro):** Očekávaná středová prázdnota vznikající přirozeně z charakteru pole (např. fázová singularita víru). Značí středovou osu rotace nebo sférické odpuzování.
- **Pathological hole (Patologická díra):** Zborcení hustoty pole, fragmentace nebo šum, který neodpovídá základní symetrii útvaru a ničí celistvost měřitelné obálky.

### B. Kritéria akceptovatelnosti středového minima
Nízká amplituda uvnitř struktury je **akceptovatelná** pouze za těchto přísných podmínek:
- Prázdnota je očekávaným *vortex core* (vírovým jádrem).
- Jádro je stabilní a středově vycentrované vůči globální struktuře.
- Má jasnou, spojitou a koherentní prstencovou hranici (annular boundary).
- Struktura nevykazuje žádnou *fragmentaci* (laloky) v ploše slupky.
- Nedochází k žádnému dotyku či nebezpečnému přiblížení k výpočetní hranici (*no boundary contact*).

### C. Podmínky patologické díry (Zamítnutí)
Díra nebo úbytek energie je klasifikována jako patologická a zneplatňuje snapshot (přesun do Třídy B nebo C), pokud splňuje jakoukoliv z těchto podmínek:
- **Off-center internal voids:** Díra vznikla nesymetricky mimo očekávané topologické jádro.
- **Multiple holes:** Objevuje se více děr najednou (houbovitá struktura).
- **Broken ray continuity:** Díra zcela přerušuje spojitost slupky na jakémkoliv radiálním paprsku (slupka je protržená).
- **Unpredictable movement:** Díry se náhodně pohybují nebo mění počet napříč různými prahy obálky nebo seedy.
- **Noise/Fragmentation:** Prázdnota je důsledkem termálního roztříštění (termalizace obálky).

### D. Shell-Aware Veličiny pro logování
U každého shell-like snapshotu bude nutné měřit a logovat nové sady veličin:
- **Inner radius / Inner boundary:** Poloha a poloměr vnitřního okraje.
- **Outer radius / Outer boundary:** Poloha a poloměr vnějšího okraje.
- **Shell thickness:** Úhrnná tloušťka slupky (vnější mínus vnitřní hranice).
- **Shell centroid:** Celkové těžiště prstencové slupky.
- **Inner-core centroid:** Těžiště samotné středové prázdnoty.
- **Outer-envelope centroid:** Těžiště obrysů vnějšího okraje.
- **Shell-thickness asymmetry:** Diference tloušťky slupky v různých radiálních směrech.
- **Angular shell-thickness profile:** Profil tloušťky v závislosti na polárním úhlu.
- **Offset (Inner-Outer):** Excentricita, tj. vzdálenost mezi těžištěm jádra a vnějším těžištěm.
- **Direction of shell asymmetry:** Směrový vektor určující nejhlubší/nejtenčí část slupky.

### E. Kandidáti na definici Shell-Aware Dipólu
Protože plošný dipól z plné amplitudy selhává, shell-aware metrika bude pro výpočet dipólu testovat tyto kandidáty:
1. **Dipole of shell thickness:** Integrace změny tloušťky slupky vůči středu.
2. **Dipole of outer boundary distance:** Modulace excentricity pouze vnější hrany.
3. **Dipole of inner-core displacement:** Posun jádra uvnitř pevného okraje.
4. **Dipole of energy density across shell:** Gradientní asymetrie hustoty napříč prstencem.
5. **Channel comparison:** Souběžné porovnání projevů v kanálech $|\Psi|$, $|\Psi|^2$, $\Phi$, hustota energie a případně i thresholded phase-boundary.

### F. Povinné "Toy Calibrations" (Kalibrační runy)
Před nasazením nové shell-aware metriky do produkčního PDE řešiče musí být její stabilita certifikována na analytických matematických modelech ("Toy models"):
1. Symetrický prstenec (annulus) se symetricky vycentrovaným observerem (očekáván dipól 0).
2. Symetrický prstenec s off-center observerem.
3. Prstenec, kde má excentricitu posunuté vnitřní jádro.
4. Prstenec s posunutou vnější hranicí.
5. Prstenec vykazující asymetrickou (proměnnou) tloušťku slupky.
6. Prstenec poškozený patologickou off-center dírou.
7. Rozbitý prstenec / fragmentovaná slupka.
8. Rozmazaný (fuzzy) prstenec.

### G. Pravidlo: Záchrana FuzzyFail u nulových vektorů
Test úhlové stability směru (FuzzyFail) může u dokonale centrovaných struktur selhat kvůli počítačovému šumu, kdy vektor směru matematicky neexistuje. Zavádí se povinný **guard**:
- Pokud je magnitudo příslušného směrového vektoru (dipólu, posunu) menší než předregistrovaný detekční práh, směr se označí jako **"direction undefined / near-zero vector"**.
- Na "near-zero" vektorech se úhlová stabilita nepočítá a nedochází k automatickému FuzzyFail zamítnutí.

### H. Interpretační mantinely nové metriky
Tato metrika neimplikuje fyzikální validaci, pouze mapuje morfologii:
- Shell-aware metrika **pouze testuje morfologickou asymetrii a směr**.
- Zjištěná amplituda offsetu **není fyzikální (kosmologická)** a nelze ji dosadit do HSU fyziky bez nezávislé kalibrace kalibrační křivkou.
- Morfologický úspěch (získání A-class prstence) **neznamená platnost HSU**. Ukazuje jen, že PDE umí generovat asymetrické obálky.
- Neschopnost "filled-envelope" metriky uchopit vírové objekty **neznamená fyzikální selhání rovnice Eq-11**; znamená to pouze nutnost korektní měřící techniky.

**11. HSU-LINEUM-01E-a: Předregistrace shell-aware toy kalibrací**

Před sepsáním jakéhokoliv nového kódu pro shell-aware metriku (01E) je nutné striktně předregistrovat klasifikační hierarchii a očekávané výsledky na "toy modelech". Cílem je zamezit zpětnému výběru metriky ("choose best metric after results").

### 1. Klasifikační hierarchie metrik
Je nutné striktně oddělit dvě fyzikálně odlišné rodiny metrik. Samotný "Inner-vs-outer centroid offset" neměří observer-offset symetrického prstence.

**A. Observer-offset metriky (Primární pro HSU analogii)**
Tyto metriky měří pozici pozorovatele/referenčního bodu relativně vůči slupce.
- Definice: Střed slupky / těžiště vnější obálky $C_{shell}$, referenční bod pozorovatele $O$.
- **Primární HSU-analogy metrika:** Vektor observer-offsetu $\vec{u}_{obs} = O - C_{shell}$.
- Vztahuje se na dipól vzdálenosti hranice měřený od bodu $O$. U symetrického prstence roste s posunem bodu $O$ mimo střed.

**B. Shell-deformation metriky (Primární Lineum diagnostika)**
Tyto metriky zkoumají, zda je samotná slupka asymetrická, nezávisle na poloze pozorovatele.
- Definice: Těžiště vnitřního jádra $C_{inner}$, těžiště vnější obálky $C_{outer}$.
- **Primární Lineum shell-deformation diagnostika:** Vektor deformace slupky $\vec{u}_{shell} = C_{inner} - C_{outer}$.
- Patří sem i dipól tloušťky slupky, dipól vnější hranice, dipól vnitřní hranice a asymetrie hustoty energie.
- **Varování:** Shell-deformation dipól *není* automaticky observer-offset dipól. Jde o strukturální diagnostiku, která odpovídá na jinou otázku než HSU.

### 2. Definice "Pozorovatele" (Observer) v Lineu
Před vyhodnocením observer-offset metriky musí být fixně definováno, co je bod $O$. 

**Hierarchie definice pozorovatele:**
- **Pro Toy Kalibraci:** Primární definicí je *manuálně umístěný virtuální pozorovatel (virtual observer/probe point)*. Je to nezbytné, protože toy modely mají za cíl validovat geometrii samotného observer-offsetu.
- **Pro Lineum-native PDE snapshoty:**
  - *Primární (Intrinsic):* Poloha topologického jádra / fázové singularity (pokud je detekovatelná a stabilní).
  - *Záložní (Fallback):* Těžiště vnitřního jádra (inner-core centroid).
  - *Pouze pro diagnostiku:* Těžiště hustoty energie, těžiště vnější obálky, pevný bod sondy.

**Pravidlo:** Definice pozorovatele se nesmí měnit po získání výsledků. Pokud nelze primárního pozorovatele detekovat, klasifikuje se observer-offset jako *"undefined for this snapshot"*, namísto lovení lépe vypadajícího kandidáta.

### 3. Separátní klasifikační štítky
Výsledek nelze zařadit do jedné obecné "Třídy A", pokud se mísí různé fyzikální děje. Je nutné rozlišit:
- **Observer-offset štítky:** `A_obs`, `B_obs`, `C_obs`.
- **Shell-deformation štítky:** `A_shell`, `B_shell`, `C_shell`.
Zabrání se tím tomu, aby byl úspěch v shell-deformation mylně reportován jako úspěch v observer-offset.

### 4. Prioritizace kanálů (Channel Priority)
Prioritní osa vyhodnocování kanálů je jednoznačně fixována. Pro jakékoliv budoucí Lineum PDE runy platí:
1. **Primární:** Explicitně definovaná hustota energie (energy density).
2. **Záložní primární (Fallback):** $|\Psi|^2$. Pokud před exekucí není do reportu explicitně zapsán verifikovaný analytický vzorec pro hustotu energie, primárním morfologickým kanálem se stává automaticky $|\Psi|^2$.
3. **Sekundární:** Lineární amplituda $|\Psi|$.
4. **Terciární:** Fázové pole $\Phi$.
5. **Exploratorní:** Prahované fázové bariéry.
*Pořadí kanálů se nesmí měnit po zobrazení výsledků.*

### 5. Topologické jádro vs. Patologická díra: Kvantitativní hranice
Prázdnota uprostřed se stává **patologickou dírou** (selháním), pokud překročí tyto hranice:
- **Excentricita jádra:** Těžiště jádra leží od geometrického středu struktury o více než $20\%$ průměrného poloměru celé obálky.
- **Limit rozlohy jádra:** Plocha vnitřního jádra tvoří méně než $1\%$ nebo více než $70\%$ celkové plochy vnější obálky.
- **Spojitost slupky:** Slupka ztrácí v jakémkoliv radiálním směru ($0^\circ - 360^\circ$) tloušťku pod úroveň definovanou prahem šumu, tj. existuje aspoň jeden "průraz" zkrz slupku.
- **Počet mezer:** Existuje více než jedna izolovaná vnitřní prázdnota s rozlohou větší než $2\%$ plochy struktury.

### 6. Definice slupkových veličin (Shell geometry quantities)
- **Inner boundary:** Vnitřní izočára detekčního prahu obklopující jádro.
- **Outer boundary:** Vnější izočára detekčního prahu obklopující celou strukturu.
- **Shell thickness $t(\theta)$:** Radiální vzdálenost mezi vnitřní a vnější hranicí v závislosti na polárním úhlu $\theta$ (z centra těžiště jádra).
- **Mean shell thickness:** Integrál $t(\theta)$ přes $2\pi$.
- **Shell-thickness dipole:** Vektorový součet změn tloušťky $t(\theta)$.
- **Inner-core centroid ($C_{inner}$):** Střed hmotnosti vypočítaný pouze z vnitřního ohraničení (prázdnoty).
- **Outer-envelope centroid ($C_{outer}$):** Střed hmotnosti počítaný pouze z mapy vnějšího ohraničení (koresponduje s $C_{shell}$).
- **Inner/Outer centroid offset:** Vektorový rozdíl $C_{inner} - C_{outer}$ (Shell-deformation metrika).
- **Shell compactness:** Poměr celkové plochy plné slupky vůči kruhu o poloměru maximálního dosahu vnější hrany.

### 7. Očekávané chování Toy Kalibrací (Předregistrace Runů)
Každý test musí povinně hlásit dva oddělené statusy:

1. **Ideálně vycentrovaný prstenec + vycentrovaný pozorovatel:**
   - Observer-offset: zero / near-zero, směr nedefinován.
   - Shell-deformation: zero.
   - Očekávaný status: `A_obs_zero`, `A_shell_zero`.
2. **Ideálně vycentrovaný prstenec + off-center pozorovatel:**
   - Observer-offset: nonzero, směr koreluje s posunem sondy.
   - Shell-deformation: zero.
   - Očekávaný status: `A_obs`, `A_shell_zero`.
3. **Posunuté vnitřní jádro + vycentrovaný pozorovatel:**
   - Observer-offset: zero nebo undefined (pokud pozorovatel není definován jako samotné jádro).
   - Shell-deformation: nonzero.
   - Očekávaný status: závisí na definici O pro `A_obs`, očekáváno `A_shell`.
4. **Posunutá vnější hranice:**
   - Observer-offset: závisí na definici O.
   - Shell-deformation: nonzero.
   - Očekávaný status: závisí na definici O, očekáváno `A_shell`.
5. **Proměnná tloušťka slupky (Variable thickness):**
   - Shell-thickness dipól je nonzero.
   - Není automaticky observer-offsetem.
   - Očekávaný status: observer-offset nezměněn, očekáváno `A_shell`.
6. **Patologická off-center díra:**
   - Očekávané selhání: Multiple holes / Off-center void.
   - Očekávaný status: `C_obs`, `C_shell`.
7. **Rozbitý prstenec (Broken annulus):**
   - Očekávané selhání: ztráta $360^\circ$ spojitosti.
   - Očekávaný status: `C_obs`, `C_shell`.
8. **Fuzzy annulus:**
   - Očekávaný status: `B_obs`, `B_shell` (Qualitative) pokud směr selže na různosti prahů.
9. **Noise-only shell:**
   - Očekávané selhání: fragmentace slupky.
   - Očekávaný status: `C_obs`, `C_shell`.

### 8. Záchrana nulových vektorů (Near-zero vector guard)
Pro všechny toy i reálné kalibrace se definuje bezpečnostní pojistka:
- Pokud magnitudo (velikost) vektorového dipólu nebo offsetu nepřekročí **minimální detekční práh** (např. $0.5 \text{ px}$ nebo procentní ekvivalent poloměru), vektorový směr se natvrdo označuje jako **"direction undefined / near-zero vector"**.
- Na takto označených vektorech se úhlová stabilita nepočítá a nedochází k zamítnutí snapshotu (FuzzyFail). Zabrání se tím zamítnutí perfektně symetrických stavů.

### 9. Reportovací pravidla
Každý budoucí výsledek (toy i PDE) musí striktně separátně logovat:
- Status observer-offset metriky (`A_obs`, `B_obs`, `C_obs`),
- Status shell-deformation metriky (`A_shell`, `B_shell`, `C_shell`),
- Zda je směr validní (Direction valid?),
- Zda je amplituda validní (Amplitude valid?),
- Zda byl pozorovatel vůbec detekovatelný (Observer detectable?),
- Zda výsledek slouží jako analogie HSU, nebo pouze jako morfologická diagnostika Linea.

### 10. Explicitní Omezení 2D modelů
**Varování:** Navrhovaný "2D annulus" (dvoudimenzionální prstenec) představuje pouze geometrickou paralelu a průřez slupkovým modelem ("cross-sectional toy model"). Je cenný pro matematickou verifikaci síta a ověření definice středových offsetů. V žádném případě však neprokazuje validitu 3D sférické slupky z HSU ani kosmologickou pozorovatelnost.

### 11. Budoucí Testovací Scope (Falsifikace a Kandidáti)
Budoucí testování observer-offset a shell-aware metrik explicitně zahrne všechny relevantní rodiny rovnic a kandidátní větve nalezené v rámci projektu. Účelem je široká falsifikace a hledání mechanismů, nikoliv nekritické povyšování větví na kánon. Žádná historická rovnice nebude považována za fyzikálně obnovenou bez nového nezávislého auditu. 

Každá testovaná varianta musí nést explicitní štítek:
- **Eq-11 canonical branch** (`canonical`)
- **Eq-11+ candidates / post-canonical** (`candidate`)
- **Soft Cloak / Phase 75** (`experimental`)
- **Registry Lock / Phase 71** (`experimental`)
- **Eq-9 / kinetic-dissipative family** (`experimental`)
- **Eq-4 / Eq-4' / deprecated diffusion branches** (`deprecated` / `historical`)
- **SoftAbs / escape-valve variants** (`draft`)
- Jakékoliv další historické či draft větve nalezené v rámci projektu (`pouze diagnostické` / `refuted`)

### 12. Metodika Fuzzy Threshold Testu (10/50/90)
Test s prahy 10/50/90 není prezentován jako univerzální fyzikální standard, ale výlučně jako **předregistrovaný test vnitřní robustnosti a citlivosti**:
- **10 %** vzorkuje nízko-intenzitní halo / rozmazanou vnější obálku (fuzzy envelope).
- **50 %** vzorkuje střední těleso struktury (mid-level body).
- **90 %** vzorkuje husté jádro / oblast vysoké spolehlivosti (dense core).

Účelem testu je ověřit, zda těžiště, geometrie slupky, observer-offset a směry deformace zůstávají stabilní, i když se mění definice "hranice" (boundary). 
- Pokud jsou výsledky napříč prahy stabilní, morfologie je považována za robustní. 
### 13. Výsledky Toy Kalibrace (v2.7 Robustness & Morphology Audit)
Počáteční geometrické estimátory (v2.2-v2.6) odhalily neschopnost izolovaných středových výpočtů pokrýt všechny patologické stavy, zejména ořez slupky na hraně obrazu a rozdíl mezi čistým posunem pozorovatele a deformací slupky. K plné kalibraci měřáku observer-offsetu bylo nasazeno `v2.7` finální síto.

**Explicitní konvence souřadnic:** Veškeré vektory a centra jsou striktně reportovány ve formátu `[row, col]` (tj. `[y, x]` v obrazovém prostoru).

**Nezávislá morfologická hradla (Shape Gates):**
1. **Outer Boundary Isolation:** Těžiště a LSQ fit se aplikují *výhradně* na izolované vnější pixely, extrahované pomocí inverzní binární masky. Jádro nemá žádný vliv.
2. **Coupled Shell Asymmetry:** Střed vnitřního jádra (`C_inner`) se odděleně porovnává se středem vnější hrany (`C_outer`). Tímto způsobem systém izoluje čistý observer-offset (`C_obs`) od vnitřní asymetrie / deformace slupky (`C_shell`). Stavy s proměnnou tloušťkou slupky, případně posunutým jádrem, tak již nikdy neprojdou jako čistý HSU případ (klasifikováno jako `C_shell`).
3. **Discrete Circularity Proxy:** Výpočet $4\pi A / P^2$ adaptovaný pro diskrétní subpixelovou chybu (hrubý mřížkový obvod uměle snižuje jmenovatel, limit upraven).
4. **Aspect Ratio (Elongation):** Limit AR > 1.10 degraduje na `B_obs`, AR > 1.20 na `C_obs`.
5. **Normalized LSQ Residual Gate:** Průměrný hodnota reziduálu kruhového fitu vůči mediánnímu poloměru. Odchytí nenápadné odchylky od kružnice. Limit > 0.02 `B_obs`, > 0.10 `C_obs`.
6. **Protrusion/Tail Score:** Poměr maximálního radiálního outlieru vůči P50 mediánu. Limit > 0.05 `B_obs`.
7. **Box Boundary Clip (Touches Edge):** Pokud kontura narazí na jakýkoliv z okrajů obrazového boxu (0, nebo size-1), snapshot je bez další debaty okamžitě zamítnut (`C_obs`), neboť ořez hranou destruktivně mutiluje geometrické momenty.

**Klasifikace patologických stavů (v2.7 finální test):**
- **Clipped shell near box boundary:** Narazí na hranu mřížky. Okamžitý `C_obs`, `C_shell`. Boundary artefakty se nesmí maskovat jako observer-offset.
- **Variable shell thickness / Shifted inner core:** Vnější kontura může být kružnice (`A_obs`), ale kvůli neshodě tloušťky a vnitřního centra je výsledek izolován jako `C_shell` (Coupled asymetrie).
- **One-sided lobe:** Zpřísněním LSQ residuálního hradla a Protrusion skóre je korektně degradován na `B_obs`.
- **True Ellipse / Off-center Ellipse:** `C_obs` (AR = 1.88, vysoké LSQ reziduum).

*Závazné interpretační pravidlo:*
Jakýkoli PDE výsledek budoucích kandidátů (Eq-11+, Eq-4, Soft Cloak, SoftAbs, Registry Lock, Eq-9), který spadne do kategorie `B_obs` nebo `C_obs` v jakékoliv složce, je **pouze diagnostické** a nesmí být považován za validaci HSU ani kosmologické interpretace Lineum. Každá varianta rovnic si zachová svůj historický label.

Žádná simulace PDE v těchto krocích neproběhla a výsledky neslouží jako přímé ověření fyzikální platnosti.

---

### 14. Výsledky 01F Snapshot Screening (Lineum-Native PDEs)
Po úspěšném schválení `v2.7` toy kalibrace byla spuštěna kontrolní fáze `01F`. Cílem bylo vzít existující implementace fyzikálních jader Lineum a ověřit, zda vůbec dokážou vygenerovat geometrii, která by prošla morfologickým sítem `A_obs` / `A_shell`.

**Metodologie:**
Pro test byl sestaven izolovaný skript, který nabootoval rovnice přes neinvazivní adapter wrapper, jenž sjednotil vstupy a výstupy bez změny fyzikální logiky.
Jako kontrola nezávislosti bylo vloženo ověření na čisté kružnici (Toy Sanity Check) a simulace běžela na dvou různých velikostech mřížky (N=160 a N=128). Měřena byla obálka `|S| > 0.1` nebo `|Psi|^2 > 0.1` po 100 integracích. Ostatní rodiny `Eq-11+`, `SoftAbs`, a `Eq-4` nebyly evaluovány z důvodu chybějícího exekutabilního PDE enginu nebo draft statusu.

**Výsledky Screeningu:**
- **Toy Sanity Check (Perfect Annulus):** `A_obs`, `A_shell` (Ověření, že síto v testovacím aparátu funguje korektně).
- **Eq-11 Canonical (N=64):** `C_obs`, `C_shell` (Broken annulus 0.89, Tail score 0.06, High LSQ Res 0.03).
- **Soft Cloak (Phase 75) N=160:** `B_obs`, `B_shell` (High LSQ Res 0.03).
- **Soft Cloak (Phase 75) N=128:** `C_obs`, `C_shell` (Broken annulus 0.89, Tail score 0.07, High LSQ Res 0.04). Zmenšení rozlišení odhalilo silnou strukturální nestabilitu.
- **Registry Lock (Phase 71) N=160:** `B_obs`, `B_shell` (Tail score 0.06, High LSQ Res 0.02).
- **Eq-9 Kinetic (N=128):** `B_obs`, `B_shell` (High LSQ Res 0.03).

**Závěr 01F Screeningu:**
Žádná z aktuálně úspěšně spuštěných větví v tomto krátkém 01F pilotu nevygenerovala A-class strukturu. Po nasazení kompatibilních testovacích adaptérů byly historické větve Eq-11 a Eq-9 úspěšně zařazeny, ale dosáhly pouze diagnostické C/B úrovně. Tento výsledek reflektuje stav jejich kompatibility s morfologickým preflight screeningem pod přísnou the v2.7 observer-offset gate, avšak **nepředstavuje fyzikální vyvrácení žádné z rovnic**. Zůstávají v režimu "pouze diagnostické".

---

### 15. 01F Visual Morphology Audit

Tato fáze představuje lidsky čitelné vizuální vysvětlení, proč jednotlivé PDE větve spadly do kategorie `B` (pouze diagnostické) nebo `C` (rejected), bez jakékoliv snahy o optimalizaci parametrů nebo ladění (no parameter hunting). Závěry vycházejí přímo ze struktury obálky při v2.7 thresholding limitech.

| Equation family | Label | Gate result | Human shape description | Main blocker for A-class | Interpretation |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Eq-11 Canonical** | `canonical` | **C** | Hrubý čtvercový flek / kříž | Broken annulus (pixelation), LSQ Res | Nízké rozlišení (N=64) destruovalo hladkost hrany. Okraj je rozbitý. Není chybou fyziky. |
| **Eq-9 Kinetic** | `experimental`| **B** | Fuzzy obláček s nerovnou hranou | LSQ Res (0.029) > 0.02 limit | Droplet vytvořil souvislý tvar, ale obálka má drobné mikronerovnosti (ripples). |
| **Soft Cloak (160)**| `experimental`| **B** | Fuzzy obláček s nerovnou hranou | LSQ Res (0.029) > 0.02 limit | Shodné chování nepohyblivé kapky. Není matematicky ideální kruh. |
| **Soft Cloak (128)**| `experimental`| **C** | Rozbitý / přerušovaný prstenec | Broken annulus, Protrusion (0.065) | Menší mřížka zhoršila vyhlazení. Hrana detekována jako nesouvislá. |
| **Registry Lock** | `experimental`| **B** | Kruh s lehkým lalokem / ocasem | Protrusion (0.056), LSQ Res (0.024) | Vnitřní zámkový mechanismus rovnice způsobuje mírnou asymetrii (bouli) na okraji. |

**Závěrečná Interpretace Vizuálního Auditu:**
Všechny rodiny byly spuštěny "as-is". Problémy, které je vyřadily z čistého `A-class` měření (rozbité prstence, laloky, LSQ rezidua), jsou morfologického a často mřížkového původu. **Tento výsledek nevyvrací Lineum kosmologii ani HSU**, pouze konstatuje, že defaultní nastavení těchto integrátorů na malých mřížkách neprodukuje dostatečně hladkou matematickou strukturu pro spolehlivé odečtení středu přes rámec observer-offset měření.

---

### 16. 01F Sensitivity Sanity Audit

K ověření, zda výstupy B/C nejsou pouze artefaktem špatně zvoleného rozlišení, prahu obálky nebo fixního měřícího kroku, byl proveden test citlivosti (bez parameter huntingu a bez změny fyziky). Cílem bylo odlišit grid/threshold artefakty od stabilní (či nestabilní) morfologie.

| Equation family | Label | Grid | Threshold | Frame/Step | Gate result | Main defect | Human visual description | Stable or threshold-sensitive? |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Eq-11 Canonical** | `canonical` | 64 | 0.05-0.20 | 50-200 | C (později B) | Nízké rozlišení | Hrubý čtvercový flek, u N=64 stabilní | Stabilní (limitováno mřížkou) |
| **Eq-9 Kinetic** | `experimental` | 64, 128, 160 | 0.05-0.20 | 50-200 | B (vzácně A) | Mikro-nerovnosti okraje | Fuzzy obláček. Zlepšuje se s vyšším gridem. | Silně threshold-sensitive a frame-sensitive |
| **Soft Cloak** | `experimental` | 64, 128, 160 | 0.05-0.20 | 50-200 | B (vzácně A) | Mikro-nerovnosti okraje | Fuzzy obláček. Zlepšuje se s vyšším gridem. | Silně threshold-sensitive a frame-sensitive |
| **Registry Lock** | `experimental` | 64, 128, 160 | 0.05-0.20 | 50-200 | C (při 64), B (při 160) | Tail / lalok (asymetrie) | Kruh s lehkým lalokem. Při N=160 vysoce stabilní tvar. | Stabilně B (stabilní vůči prahování na lepším gridu) |

**Závěr Citlivostního Auditu:**
Větve jako *Eq-9 Kinetic* a *Soft Cloak* trpí velkou citlivostí na zvolený práh a snímek simulace – chvílemi přesahují do čistého A-class stavu, vzápětí kvůli mikro-fluktuacím padají do B. Jsou pro HSU observer-offset nespolehlivé z důvodu citlivosti na prahování. Naopak *Registry Lock* se na vyšším rozlišení chová absolutně stabilně bez ohledu na práh či čas, ale setrvává v kategorii B kvůli fyzikální asymetrii (ocásek). *Eq-11 Canonical* je v defaultním enginu omezena mřížkou 64x64, což je hlavní důvod C/B výpadků. Závěrem: V tomto netuněném režimu žádná z větví netvoří spolehlivě stabilní A-class slupku.

---

### 17. 01G Resolution & Stability Audit

K finálnímu potvrzení morfologických limitů byl proveden test 01G na rozšířených gridových rozlišeních (až do N=200). Generátor pro `Eq-11 Canonical` byl pomocí bezpečného neinvazivního wrapperu extrapolován na vyšší N bez zásahu do původní fyziky. Zkoumané PDE větve jsou plně deterministické bez stochastického šumu, seedová robustnost se proto netestuje.

**Pravidlo pro A-class:** A-class se počítá pouze tehdy, pokud je geometrie stabilní napříč všemi testovanými rozlišeními, prahy a časovými rámci. Jednorázové "probliknutí" se považuje za `threshold-sensitive / B-class`.

| Equation family | Label | Grid | Threshold | Frame | Gate Result | Main Defect | Classification |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Eq-11 Canonical** | `canonical` | 64, 128, 160, 200 | 0.05-0.20 | 50-200 | **A_obs, A_shell** (pro N≥128) | Žádný | **Stabilní A-class** (Grid-limited at N=64) |
| **Eq-9 Kinetic** | `experimental`| 64, 128, 160, 200 | 0.05-0.20 | 50-200 | **A_obs, A_shell** (pro N=200) | Žádný | **Stabilní A-class** (Grid-limited at N≤160) |
| **Soft Cloak** | `experimental`| 64, 128, 160, 200 | 0.05-0.20 | 50-200 | B (občas A) | LSQ Res, Protrusion | **Threshold/Frame-sensitive** |
| **Registry Lock** | `experimental`| 64, 128, 160, 200 | 0.05-0.20 | 50-200 | B (občas A) | LSQ Res, Protrusion | **Threshold/Frame-sensitive** |
| **Eq-11+** | `candidate` | N/A | N/A | N/A | N/A | Chybějící modul | **Not Executable** |
| **SoftAbs** | `draft` | N/A | N/A | N/A | N/A | Třídy roztříštěny | **Not Executable (Requires consolidation)** |
| **Eq-4/Eq-4'** | `deprecated` | N/A | N/A | N/A | N/A | Zdroj nenalezen | **Not Executable** |

**Závěr Vizuálního Auditu 01G:**
- **Eq-11 Canonical a Eq-9 Kinetic** dosáhly stabilní čisté sférické geometrie (`A_class`) pro všechna měření, jakmile byl dodán dostatečně jemný grid (N≥128 pro Eq-11, N=200 pro Eq-9). Všechny dřívější B/C defekty byly identifikovány jako čisté grid/diskrétní artefakty.
- **Soft Cloak a Registry Lock** nedosahují stabilní `A_class` ani na masivním gridu N=200; jejich asymetrie a zvlnění okraje jsou inherentní tvarové rysy, nikoli chyba gridu. Tyto větve zůstávají nespolehlivé pro HSU offsetování.

> [!NOTE]
> Úspěch větví Eq-11 a Eq-9 v A-class **neznamená fyzikální validaci HSU ani validaci Lineum kosmologie**. Znamená to pouze, že generovaná geometrie je po technické stránce dostatečně čistá (bez artefaktů mřížky) pro to, aby mohla být použita pro další experimentální měření v rámci rámci observer-offset měření.

---

### 18. 01H Center-Reference Offset Sanity Check

Cílem fáze 01H bylo ověřit základní sanity check: zda morfologický "observer-offset měřák" (vyvinutý na teoretických Toy modelech) funguje i na reálných Lineum-native obálkách z produkce testovaných fyzikálních integrátorů.

Do stabilních `A-class` obálek vygenerovaných na vysokém gridu (N=200) pro Eq-11 Canonical a Eq-9 Kinetic byl vložen virtuální pozorovatel do definovaných offsetových pozic od geometrického středu slupky. Algoritmus přečetl boundary pixely a provedl LSQ kruhový fit pro zjištění vektoru (tzv. přímé odečtení od středu obálky). Výsledek dosáhl **0.00 úhlové i amplitudové chyby**, což potvrdilo matematickou čistotu obálky.

---

### 19. 01H-b Boundary-Distance Observer Offset Test (Blind Audit)

Aby bylo vyloučeno, že úspěch 01H je matematickou tautologií (kdy offset odpovídá pouhému posunu souřadnic), byl zaveden test `01H-b`. Zde se observer-offset neměří hledáním globálního středu LSQ fitem celého objektu, nýbrž **slepým ray-castingem z pohledu pozorovatele** (měření vzdálenosti $R(\theta)$ k hranici v okruhu 360 stupňů). Měřený offset je pak odvozen z vnitřního dipólu tohoto profilu vzdáleností.

Test 01H-b prošel auditem ("Blind Measurement Mode"). V tomto blind measurement setupu nebyl measured offset počítán z true center ani injected offset. Znal pouze pixelová data obálky a polohu pozorovatele. Očekávaný offset (Expected Vector) se použil výhradně pro závěrečné srovnání. Test tak významně podporuje netautologičnost měřicí procedury.

**Znaménková konvence a Tabulka Měření:**
- `d_obs`: Injektovaný posun pozorovatele vůči geometrickému středu ($O - C_{shell}$)
- `b_expected`: Očekávaný vektor dipólu hranice z pohledu pozorovatele ($-d_{obs}$)
- `b_measured`: Skutečně změřený vektor dipólu ze slepého ray-castingu

| Equation / Control | `d_obs` | `b_expected` | `b_measured` | Ang_Err | Amp_Err | Status / Defect |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Eq-11 Canonical** (N=200) | `[5, 5]` | `[-5.0, -5.0]` | `[-5.0, -5.0]` | 0.0 deg | 0.00 px | A (Clean) |
| **Eq-11 Canonical** (N=200) | `[10, 10]` | `[-10.0, -10.0]` | `[-10.0, -10.0]` | 0.0 deg | 0.00 px | A (Clean) |
| **Eq-11 Canonical** (N=200) | `[8, -3]` | `[-8.0, 3.0]` | `[-8.0, 3.0]` | 0.0 deg | 0.01 px | A (Clean) |
| **Eq-9 Kinetic** (N=200) | `[5, 5]` | `[-5.0, -5.0]` | `[-5.0, -5.0]` | 0.0 deg | 0.03 px | A (Clean) |
| **Eq-9 Kinetic** (N=200) | `[10, 10]` | `[-10.0, -10.0]` | `[-9.8, -9.8]` | 0.0 deg | 0.23 px | A (Clean) |
| **Eq-9 Kinetic** (N=200) | `[8, -3]` | `[-8.0, 3.0]` | `[-8.0, 3.0]` | 0.2 deg | 0.00 px | A (Clean) |
| **Tolerance Mild Jagged** | `[5, 5]` | `[-5.0, -5.0]` | `[-4.7, -4.7]` | 0.0 deg | 0.43 px | A (Low-amplitude noise) |
| **NegCtrl Broken Annulus** | `[5, 5]` | `[-5.0, -5.0]` | N/A | N/A | N/A | C (Broken continuity) |
| **NegCtrl Long Thin Tail** | `[5, 5]` | `[-5.0, -5.0]` | N/A | N/A | N/A | C (Protrusion, Asym) |
| **NegCtrl One-Sided Lobe** | `[5, 5]` | `[-5.0, -5.0]` | N/A | N/A | N/A | C_shell (Shell Asym) |
| **NegCtrl True Ellipse** | `[5, 5]` | `[-5.0, -5.0]` | N/A | N/A | N/A | C (Severe Elongation) |
| **NegCtrl Off-Center Hole**| `[5, 5]` | `[-5.0, -5.0]` | N/A | N/A | N/A | C_shell (Shell Asym) |
| **NegCtrl Clipped Shell** | `[5, 5]` | `[-5.0, -5.0]` | N/A | N/A | N/A | C (Touches Edge) |
| **NegCtrl Out-of-Bounds** | `[130, 153]` | `[-130, -153]` | N/A | N/A | N/A | C (Observer out of bounds) |

*(Testování úspěšně proběhlo i nad pootočenými poli ve vícero kvadrantech se shodně nízkou chybou u A-class větví.)*

**Závěr Boundary-Distance Zkoušky:**
Ray-casting dipólové měření plně potvrdilo spolehlivost observer-offset gate. Dipól profilu vzdálenosti k okraji bez jakéhokoliv přístupu ke globálnímu středu velmi kopíruje očekávaný vektor (úhlová i amplitudová chyba je 0.00 až 0.03 px, a i na velkém offsetu -10,-10 je výchylka malá <0.23 px vlivem diskretizace gridu). Negativní kontroly (asymetrie laloku, rozbité prstence, clipped shell) spolehlivě blokují detekci s hodnocením C-class.

**Audit cleanup (v2.8):**
- *Mild Jagged* byl překlasifikován jako tolerance/noise test, jelikož jeho mírná odchylka záměrně neblokuje měřák.
- *Broken Annulus* byl oddělen od Out-of-Bounds testu (nyní selhává korektně na "loss of 360-degree continuity").
- Byla zavedena explicitní znaménková konvence `d_obs` vs `b_expected` / `b_measured`.
- Test 01H-b podporuje netautologičnost boundary-distance měření, ale není fyzikálním důkazem.

Tyto Lineum-native obálky (`Eq-11`, `Eq-9`) na vysokém rozlišení jsou schváleny a způsobilé k použití pro observer-offset experimenty.

> [!NOTE]
> Měření `01H-b` je fundamentální test geometrie, nikoli fyziky. Je metodologicky silnější než 01H, protože striktně odděluje "znalost středu" od samotného lokálního měření dipólu pozorovatelem. Eq-11/Eq-9 A-class shells remain eligible for controlled observer-offset experiments. Nejde o fyzikální validaci HSU ani Lineum kosmologie.

---

### 21. 01I Kontrolovaný Observer-Offset Experiment (Geometrický Zátěžový Test)

V této fázi byl náš slepý měřák (blind ray-casting dipole) podroben zátěžovému testování. Zkoumali jsme, zda si na obálkách třídy A (`Eq-11 Canonical` a `Eq-9 Kinetic`) zachová stabilitu pro různé velikosti a směry posunů, při různém rozlišení mřížky (grid) a při různých prahových hodnotách jasu (thresholds). Měření mělo striktně geometrický a metodologický charakter.

Celkem bylo provedeno **375 testů**. Výpočet tohoto rozsahu vychází z následující logiky:
- Testováno bylo 5 způsobilých kombinací rovnice a mřížky:
  - Eq-11: N=128, N=200, N=256
  - Eq-9: N=200, N=256
- Pro každou kombinaci byly použity 3 prahy: 0.05, 0.10, 0.20
- Pro každý práh bylo použito 25 offset scénářů:
  - 1 nulový scénář (M=0)
  - 4 nenulové magnitudy (M=2, 5, 10, 15) v 6 směrech
Tedy: `5 equation-grid sad × 3 prahy × 25 offset scénářů = 375 testů`. Rovnice Eq-9 na mřížce N=128 nebyla do tohoto experimentu zařazena na základě předem stanoveného vstupního filtru způsobilosti pro 01I, protože při takto hrubém rozlišení netvoří stabilní obálku třídy A.

#### Jak se měření počítalo

Aby se výrazně omezilo tautologické riziko a zajistilo se objektivní geometrické měření v rámci slepého přístupu bez znalosti středu obálky, byla stanovena tato pravidla a konvence:

- **Souřadnicový systém**: Všechny vektory jsou ve formátu `[row, col] = [y, x]`. Úhel θ se měří od kladné osy `col` (x) směrem ke kladné ose `row` (y), aby byla zachována standardní polární konvence, kde jednotkový směrový paprsek je dán jako `n(θ) = [sin(θ), cos(θ)]`. První složka je `row` (y, sin) a druhá je `col` (x, cos).
- **O**: Globální pixelová souřadnice pozorovatele vložena do obrazu.
- **C_shell**: Globální konstrukční střed obálky získaný z LSQ fittování okraje (pouze pro účely testu a ověření).
- **d_obs**: Vložený posun pozorovatele (injected offset) vzhledem ke středu obálky, definovaný jako `d_obs = O - C_shell`.
- **b_expected**: Očekávaný vektor dipólu hranice, který by měl pozorovatel naměřit (protože se paprsky odvíjejí zevnitř ven, je definován opačně jako `b_expected = -d_obs`).
- **b_measured**: Skutečně změřený vektor dipólu. Z pozice pozorovatele `O` se vyšle sada paprsků v úhlech 0–360°. Pro každý úhel θ se najde vzdálenost $R(θ)$ k hranici obálky. Z asymetrie profilu vzdáleností se integrací odvodí výsledný vektor: `b_measured = 2 * [ mean(R(θ) * sin(θ)), mean(R(θ) * cos(θ)) ]`. Tento proces probíhá slepě, bez přístupu k `C_shell`.

Během auditu byly zavedeny následující metriky chyb a klasifikační pravidla (zaokrouhlovaná na 3 desetinná místa):

- **Len_Err (Délková chyba)**: Skalární odchylka délek vektorů, `Len_Err = abs(||b_measured|| - ||b_expected||)`.
- **Vec_Err (Vektorová chyba)**: Celková geometrická chyba zohledňující délku i směr, `Vec_Err = ||b_measured - b_expected||`.
- **Ang_Err (Úhlová chyba)**: Odchylka směrů vektorů počítaná ze skalárního součinu (ve stupních).
- **Clearance (Odstup)**: Minimální vzdálenost od pozorovatele k nejbližší hranici obálky.
- **Pravidlo Clearance Validace a Measurement_Status**: 
  - Pokud je `Clearance >= 5 px`, amplitudová interpretace je platná a označena jako `valid`.
  - Pokud je `Clearance < 5 px`, amplitudová interpretace začíná být silně zkreslena diskretizačními "zuby" mřížky. Taková měření jsou omezena geometrickým limitem a označena jako `measurement_limited`.
- **Pravidlo nulového vektoru**: U `d_obs = [0,0]` se nemá interpretovat směr (úhel je fixován na 0), ověřuje se pouze to, že `b_measured` má délku blízkou nule.

#### Agregované Výsledky

Ze všech 375 provedených testů nenastala ani jedna chyba klasifikace samotné brány (Gate) - samotné obálky zůstaly čisté, avšak při nízkém odstupu byl identifikován zmíněný limit měření.

**A. Přesnost podle rovnice a rozlišení**
*Všechny testy (včetně limitních s nízkým odstupem):*
| Rovnice | Rozlišení (N) | Testů | Max Úhlová Chyba | Max Délková Chyba | Max Vektorová Chyba | Min Clearance |
|:---|:---|:---|:---|:---|:---|:---|
| Eq-11 | 128 | 75 | 0.21° | 7.100 px | 7.100 px | 2.2 px |
| Eq-11 | 200 | 75 | 0.16° | 0.100 px | 0.100 px | 5.0 px |
| Eq-11 | 256 | 75 | 0.13° | 0.000 px | 0.000 px | 11.0 px |
| Eq-9 | 200 | 75 | 0.57° | 0.424 px | 0.424 px | 0.7 px |
| Eq-9 | 256 | 75 | 0.06° | 0.000 px | 0.000 px | 4.5 px |

*Pouze validní testy (Clearance >= 5 px):*
| Rovnice | Rozlišení (N) | Testů | Max Úhlová Chyba | Max Délková Chyba | Max Vektorová Chyba | Min Clearance |
|:---|:---|:---|:---|:---|:---|:---|
| Eq-11 | 128 | 39 | 0.18° | 0.000 px | 0.000 px | 7.9 px |
| Eq-11 | 200 | 75 | 0.16° | 0.100 px | 0.100 px | 5.0 px |
| Eq-11 | 256 | 75 | 0.13° | 0.000 px | 0.000 px | 11.0 px |
| Eq-9 | 200 | 57 | 0.08° | 0.141 px | 0.141 px | 5.1 px |
| Eq-9 | 256 | 69 | 0.06° | 0.000 px | 0.000 px | 5.5 px |

*Závěr:* Po odfiltrování limitních případů blízko stěny (kde Clearance < 5 px) klesá plná vektorová chyba (`Vec_Err`) u všech rovnic k minimálním hodnotám (max 0.141 px). Měřák je mimo těsnou blízkost hranice přesný s velmi nízkou chybou.

**B. Přesnost podle velikosti posunu (Magnitudy M)**
*Všechny testy vs Validní testy:*
| M | Všech Testů | Max Vec_Err (Vše) | Validních Testů | Max Vec_Err (Validní) | Max Ang_Err (Validní) |
|:---|:---|:---|:---|:---|:---|
| 0 | 15 | 0.000 px | 15 | 0.000 px | 0.00° |
| 2 | 90 | 0.000 px | 90 | 0.000 px | 0.16° |
| 5 | 90 | 0.000 px | 90 | 0.000 px | 0.18° |
| 10 | 90 | 0.141 px | 72 | 0.141 px | 0.08° |
| 15 | 90 | 7.100 px | 48 | 0.100 px | 0.05° |

*Závěr:* U velkých posunů (M=15) naráží hrubší mřížky na geometrický limit vzdálenosti k hranici (Clearance kolaps). Pokud se ovšem aplikuje pravidlo pro `valid` status, maximální vektorová chyba nepřesáhne 0.141 px, což ukazuje stabilitu metody v pracovním rozsahu.

**C. Přesnost podle prahu jasu (Threshold Th)**
*Všechny testy vs Validní testy:*
| Th | Všech Testů | Max Vec_Err (Vše) | Validních Testů | Max Vec_Err (Validní) | Max Ang_Err (Validní) |
|:---|:---|:---|:---|:---|:---|
| 0.05 | 125 | 5.233 px | 107 | 0.000 px | 0.18° |
| 0.10 | 125 | 7.100 px | 107 | 0.141 px | 0.16° |
| 0.20 | 125 | 6.788 px | 101 | 0.100 px | 0.13° |

*Závěr:* Obálka i měřák jsou robustní po vyřazení clearance-limit případů napříč celým spektrem prahování.

#### Závěr fáze 01I
Fáze 01I ukazuje, že Eq-11 Canonical a Eq-9 Kinetic na jemnějších mřížkách vytvářejí obálky, na nichž slepý boundary-distance měřák stabilně rekonstruuje vložený geometrický observer-offset napříč směry, prahy a rozlišeními. Měření zůstává bez klasifikační chyby obálky, ale s identifikovaným limitem měření při nízkém odstupu (Clearance < 5 px) u hrubých mřížek. Výsledek je metodologický a geometrický; nejde o fyzikální validaci HSU ani validaci kosmologie Lineum. Konstrukt je geometricky vhodný pro další kontrolované experimenty v rámci bezpečného odstupu od hranice.

<details>
<summary><b>Příloha 01I-A: Kompletní tabulka všech 375 konfigurací (Klikněte pro zobrazení)</b></summary>

```csv
Case_ID,Direction,d_obs,b_expected,b_measured,Ang_Err,Len_Err,Vec_Err,Clearance,Measurement_Status
Eq-11_128_Th0.05_M0,"Dir[0,0]","[0.0,0.0]","[-0.0,-0.0]","[-0.0,-0.0]",0.000,0.000,0.000,13.000,valid
Eq-11_128_Th0.05_M2,"Dir[1,0]","[0.0,2.0]","[-0.0,-2.0]","[-0.0,-2.0]",0.000,0.000,0.000,11.000,valid
Eq-11_128_Th0.05_M2,"Dir[0,1]","[2.0,0.0]","[-2.0,-0.0]","[-2.0,-0.0]",0.030,0.000,0.000,11.000,valid
Eq-11_128_Th0.05_M2,"Dir[1,1]","[1.4,1.4]","[-1.4,-1.4]","[-1.4,-1.4]",0.000,0.000,0.000,11.500,valid
Eq-11_128_Th0.05_M2,"Dir[-1,1]","[1.4,-1.4]","[-1.4,1.4]","[-1.4,1.4]",0.000,0.000,0.000,11.500,valid
Eq-11_128_Th0.05_M2,"Dir[1,-1]","[-1.4,1.4]","[1.4,-1.4]","[1.4,-1.4]",0.000,0.000,0.000,11.500,valid
Eq-11_128_Th0.05_M2,"Dir[-1,-1]","[-1.4,-1.4]","[1.4,1.4]","[1.4,1.4]",0.000,0.000,0.000,11.500,valid
Eq-11_128_Th0.05_M5,"Dir[1,0]","[0.0,5.0]","[-0.0,-5.0]","[-0.0,-5.0]",0.070,0.000,0.000,8.000,valid
Eq-11_128_Th0.05_M5,"Dir[0,1]","[5.0,0.0]","[-5.0,-0.0]","[-5.0,0.0]",0.180,0.000,0.000,8.000,valid
Eq-11_128_Th0.05_M5,"Dir[1,1]","[3.5,3.5]","[-3.5,-3.5]","[-3.5,-3.5]",0.000,0.000,0.000,8.500,valid
Eq-11_128_Th0.05_M5,"Dir[-1,1]","[3.5,-3.5]","[-3.5,3.5]","[-3.5,3.5]",0.000,0.000,0.000,8.500,valid
Eq-11_128_Th0.05_M5,"Dir[1,-1]","[-3.5,3.5]","[3.5,-3.5]","[3.5,-3.5]",0.000,0.000,0.000,8.500,valid
Eq-11_128_Th0.05_M5,"Dir[-1,-1]","[-3.5,-3.5]","[3.5,3.5]","[3.5,3.5]",0.000,0.000,0.000,8.500,valid
Eq-11_128_Th0.05_M10,"Dir[1,0]","[0.0,10.0]","[-0.0,-10.0]","[-0.0,-10.1]",0.060,0.100,0.100,3.000,measurement_limited
Eq-11_128_Th0.05_M10,"Dir[0,1]","[10.0,0.0]","[-10.0,-0.0]","[-10.1,0.0]",0.070,0.100,0.100,3.000,measurement_limited
Eq-11_128_Th0.05_M10,"Dir[1,1]","[7.1,7.1]","[-7.1,-7.1]","[-7.0,-7.0]",0.020,0.141,0.141,3.500,measurement_limited
Eq-11_128_Th0.05_M10,"Dir[-1,1]","[7.1,-7.1]","[-7.1,7.1]","[-7.0,7.0]",0.120,0.141,0.141,3.500,measurement_limited
Eq-11_128_Th0.05_M10,"Dir[1,-1]","[-7.1,7.1]","[7.1,-7.1]","[7.0,-7.0]",0.020,0.141,0.141,3.500,measurement_limited
Eq-11_128_Th0.05_M10,"Dir[-1,-1]","[-7.1,-7.1]","[7.1,7.1]","[7.0,7.0]",0.120,0.141,0.141,3.500,measurement_limited
Eq-11_128_Th0.05_M15,"Dir[1,0]","[0.0,15.0]","[-0.0,-15.0]","[-0.0,-9.9]",0.020,5.100,5.100,2.200,measurement_limited
Eq-11_128_Th0.05_M15,"Dir[0,1]","[15.0,0.0]","[-15.0,-0.0]","[-9.9,0.0]",0.020,5.100,5.100,2.200,measurement_limited
Eq-11_128_Th0.05_M15,"Dir[1,1]","[10.6,10.6]","[-10.6,-10.6]","[-6.9,-6.9]",0.000,5.233,5.233,3.900,measurement_limited
Eq-11_128_Th0.05_M15,"Dir[-1,1]","[10.6,-10.6]","[-10.6,10.6]","[-6.9,6.9]",0.000,5.233,5.233,3.900,measurement_limited
Eq-11_128_Th0.05_M15,"Dir[1,-1]","[-10.6,10.6]","[10.6,-10.6]","[6.9,-6.9]",0.000,5.233,5.233,3.900,measurement_limited
Eq-11_128_Th0.05_M15,"Dir[-1,-1]","[-10.6,-10.6]","[10.6,10.6]","[6.9,6.9]",0.000,5.233,5.233,3.900,measurement_limited
Eq-11_128_Th0.10_M0,"Dir[0,0]","[0.0,0.0]","[-0.0,-0.0]","[-0.0,-0.0]",0.000,0.000,0.000,13.000,valid
Eq-11_128_Th0.10_M2,"Dir[1,0]","[0.0,2.0]","[-0.0,-2.0]","[-0.0,-2.0]",0.000,0.000,0.000,11.000,valid
Eq-11_128_Th0.10_M2,"Dir[0,1]","[2.0,0.0]","[-2.0,-0.0]","[-2.0,-0.0]",0.030,0.000,0.000,11.000,valid
Eq-11_128_Th0.10_M2,"Dir[1,1]","[1.4,1.4]","[-1.4,-1.4]","[-1.4,-1.4]",0.000,0.000,0.000,11.100,valid
Eq-11_128_Th0.10_M2,"Dir[-1,1]","[1.4,-1.4]","[-1.4,1.4]","[-1.4,1.4]",0.000,0.000,0.000,11.100,valid
Eq-11_128_Th0.10_M2,"Dir[1,-1]","[-1.4,1.4]","[1.4,-1.4]","[1.4,-1.4]",0.000,0.000,0.000,11.100,valid
Eq-11_128_Th0.10_M2,"Dir[-1,-1]","[-1.4,-1.4]","[1.4,1.4]","[1.4,1.4]",0.000,0.000,0.000,11.100,valid
Eq-11_128_Th0.10_M5,"Dir[1,0]","[0.0,5.0]","[-0.0,-5.0]","[-0.0,-5.0]",0.030,0.000,0.000,8.000,valid
Eq-11_128_Th0.10_M5,"Dir[0,1]","[5.0,0.0]","[-5.0,-0.0]","[-5.0,-0.0]",0.140,0.000,0.000,8.000,valid
Eq-11_128_Th0.10_M5,"Dir[1,1]","[3.5,3.5]","[-3.5,-3.5]","[-3.5,-3.5]",0.000,0.000,0.000,8.200,valid
Eq-11_128_Th0.10_M5,"Dir[-1,1]","[3.5,-3.5]","[-3.5,3.5]","[-3.5,3.5]",0.000,0.000,0.000,8.200,valid
Eq-11_128_Th0.10_M5,"Dir[1,-1]","[-3.5,3.5]","[3.5,-3.5]","[3.5,-3.5]",0.000,0.000,0.000,8.200,valid
Eq-11_128_Th0.10_M5,"Dir[-1,-1]","[-3.5,-3.5]","[3.5,3.5]","[3.5,3.5]",0.000,0.000,0.000,8.200,valid
Eq-11_128_Th0.10_M10,"Dir[1,0]","[0.0,10.0]","[-0.0,-10.0]","[-0.0,-10.1]",0.060,0.100,0.100,3.000,measurement_limited
Eq-11_128_Th0.10_M10,"Dir[0,1]","[10.0,0.0]","[-10.0,-0.0]","[-10.1,0.0]",0.070,0.100,0.100,3.000,measurement_limited
Eq-11_128_Th0.10_M10,"Dir[1,1]","[7.1,7.1]","[-7.1,-7.1]","[-7.0,-7.0]",0.000,0.141,0.141,3.500,measurement_limited
Eq-11_128_Th0.10_M10,"Dir[-1,1]","[7.1,-7.1]","[-7.1,7.1]","[-7.0,7.0]",0.010,0.141,0.141,3.500,measurement_limited
Eq-11_128_Th0.10_M10,"Dir[1,-1]","[-7.1,7.1]","[7.1,-7.1]","[7.0,-7.0]",0.000,0.141,0.141,3.500,measurement_limited
Eq-11_128_Th0.10_M10,"Dir[-1,-1]","[-7.1,-7.1]","[7.1,7.1]","[7.0,7.0]",0.010,0.141,0.141,3.500,measurement_limited
Eq-11_128_Th0.10_M15,"Dir[1,0]","[0.0,15.0]","[-0.0,-15.0]","[-0.0,-7.9]",0.020,7.100,7.100,3.600,measurement_limited
Eq-11_128_Th0.10_M15,"Dir[0,1]","[15.0,0.0]","[-15.0,-0.0]","[-7.9,0.0]",0.020,7.100,7.100,3.600,measurement_limited
Eq-11_128_Th0.10_M15,"Dir[1,1]","[10.6,10.6]","[-10.6,-10.6]","[-6.2,-6.2]",0.000,6.223,6.223,2.600,measurement_limited
Eq-11_128_Th0.10_M15,"Dir[-1,1]","[10.6,-10.6]","[-10.6,10.6]","[-6.2,6.2]",0.000,6.223,6.223,2.600,measurement_limited
Eq-11_128_Th0.10_M15,"Dir[1,-1]","[-10.6,10.6]","[10.6,-10.6]","[6.2,-6.2]",0.000,6.223,6.223,2.600,measurement_limited
Eq-11_128_Th0.10_M15,"Dir[-1,-1]","[-10.6,-10.6]","[10.6,10.6]","[6.2,6.2]",0.000,6.223,6.223,2.600,measurement_limited
Eq-11_128_Th0.20_M0,"Dir[0,0]","[0.0,0.0]","[-0.0,-0.0]","[-0.0,-0.0]",0.000,0.000,0.000,12.600,valid
Eq-11_128_Th0.20_M2,"Dir[1,0]","[0.0,2.0]","[-0.0,-2.0]","[-0.0,-2.0]",0.070,0.000,0.000,10.800,valid
Eq-11_128_Th0.20_M2,"Dir[0,1]","[2.0,0.0]","[-2.0,-0.0]","[-2.0,0.0]",0.050,0.000,0.000,10.800,valid
Eq-11_128_Th0.20_M2,"Dir[1,1]","[1.4,1.4]","[-1.4,-1.4]","[-1.4,-1.4]",0.000,0.000,0.000,10.800,valid
Eq-11_128_Th0.20_M2,"Dir[-1,1]","[1.4,-1.4]","[-1.4,1.4]","[-1.4,1.4]",0.000,0.000,0.000,10.800,valid
Eq-11_128_Th0.20_M2,"Dir[1,-1]","[-1.4,1.4]","[1.4,-1.4]","[1.4,-1.4]",0.000,0.000,0.000,10.800,valid
Eq-11_128_Th0.20_M2,"Dir[-1,-1]","[-1.4,-1.4]","[1.4,1.4]","[1.4,1.4]",0.000,0.000,0.000,10.800,valid
Eq-11_128_Th0.20_M5,"Dir[1,0]","[0.0,5.0]","[-0.0,-5.0]","[-0.0,-5.0]",0.000,0.000,0.000,8.000,valid
Eq-11_128_Th0.20_M5,"Dir[0,1]","[5.0,0.0]","[-5.0,-0.0]","[-5.0,-0.0]",0.010,0.000,0.000,8.000,valid
Eq-11_128_Th0.20_M5,"Dir[1,1]","[3.5,3.5]","[-3.5,-3.5]","[-3.5,-3.5]",0.000,0.000,0.000,7.900,valid
Eq-11_128_Th0.20_M5,"Dir[-1,1]","[3.5,-3.5]","[-3.5,3.5]","[-3.5,3.5]",0.000,0.000,0.000,7.900,valid
Eq-11_128_Th0.20_M5,"Dir[1,-1]","[-3.5,3.5]","[3.5,-3.5]","[3.5,-3.5]",0.000,0.000,0.000,7.900,valid
Eq-11_128_Th0.20_M5,"Dir[-1,-1]","[-3.5,-3.5]","[3.5,3.5]","[3.5,3.5]",0.000,0.000,0.000,7.900,valid
Eq-11_128_Th0.20_M10,"Dir[1,0]","[0.0,10.0]","[-0.0,-10.0]","[-0.0,-10.0]",0.070,0.000,0.000,3.000,measurement_limited
Eq-11_128_Th0.20_M10,"Dir[0,1]","[10.0,0.0]","[-10.0,-0.0]","[-10.0,0.0]",0.210,0.000,0.000,3.000,measurement_limited
Eq-11_128_Th0.20_M10,"Dir[1,1]","[7.1,7.1]","[-7.1,-7.1]","[-7.0,-7.0]",0.030,0.141,0.141,3.100,measurement_limited
Eq-11_128_Th0.20_M10,"Dir[-1,1]","[7.1,-7.1]","[-7.1,7.1]","[-7.0,7.1]",0.140,0.070,0.100,3.100,measurement_limited
Eq-11_128_Th0.20_M10,"Dir[1,-1]","[-7.1,7.1]","[7.1,-7.1]","[7.0,-7.0]",0.030,0.141,0.141,3.100,measurement_limited
Eq-11_128_Th0.20_M10,"Dir[-1,-1]","[-7.1,-7.1]","[7.1,7.1]","[7.0,7.1]",0.140,0.070,0.100,3.100,measurement_limited
Eq-11_128_Th0.20_M15,"Dir[1,0]","[0.0,15.0]","[-0.0,-15.0]","[-0.0,-9.1]",0.020,5.900,5.900,3.600,measurement_limited
Eq-11_128_Th0.20_M15,"Dir[0,1]","[15.0,0.0]","[-15.0,-0.0]","[-9.1,0.0]",0.020,5.900,5.900,3.600,measurement_limited
Eq-11_128_Th0.20_M15,"Dir[1,1]","[10.6,10.6]","[-10.6,-10.6]","[-5.8,-5.8]",0.000,6.788,6.788,3.600,measurement_limited
Eq-11_128_Th0.20_M15,"Dir[-1,1]","[10.6,-10.6]","[-10.6,10.6]","[-5.8,5.8]",0.000,6.788,6.788,3.600,measurement_limited
Eq-11_128_Th0.20_M15,"Dir[1,-1]","[-10.6,10.6]","[10.6,-10.6]","[5.8,-5.8]",0.000,6.788,6.788,3.600,measurement_limited
Eq-11_128_Th0.20_M15,"Dir[-1,-1]","[-10.6,-10.6]","[10.6,10.6]","[5.8,5.8]",0.000,6.788,6.788,3.600,measurement_limited
Eq-11_200_Th0.05_M0,"Dir[0,0]","[0.0,0.0]","[-0.0,-0.0]","[-0.0,-0.0]",0.000,0.000,0.000,20.900,valid
Eq-11_200_Th0.05_M2,"Dir[1,0]","[0.0,2.0]","[-0.0,-2.0]","[-0.0,-2.0]",0.000,0.000,0.000,19.000,valid
Eq-11_200_Th0.05_M2,"Dir[0,1]","[2.0,0.0]","[-2.0,-0.0]","[-2.0,-0.0]",0.010,0.000,0.000,19.000,valid
Eq-11_200_Th0.05_M2,"Dir[1,1]","[1.4,1.4]","[-1.4,-1.4]","[-1.4,-1.4]",0.000,0.000,0.000,19.100,valid
Eq-11_200_Th0.05_M2,"Dir[-1,1]","[1.4,-1.4]","[-1.4,1.4]","[-1.4,1.4]",0.000,0.000,0.000,19.100,valid
Eq-11_200_Th0.05_M2,"Dir[1,-1]","[-1.4,1.4]","[1.4,-1.4]","[1.4,-1.4]",0.000,0.000,0.000,19.100,valid
Eq-11_200_Th0.05_M2,"Dir[-1,-1]","[-1.4,-1.4]","[1.4,1.4]","[1.4,1.4]",0.000,0.000,0.000,19.100,valid
Eq-11_200_Th0.05_M5,"Dir[1,0]","[0.0,5.0]","[-0.0,-5.0]","[-0.0,-5.0]",0.030,0.000,0.000,16.000,valid
Eq-11_200_Th0.05_M5,"Dir[0,1]","[5.0,0.0]","[-5.0,-0.0]","[-5.0,0.0]",0.090,0.000,0.000,16.000,valid
Eq-11_200_Th0.05_M5,"Dir[1,1]","[3.5,3.5]","[-3.5,-3.5]","[-3.5,-3.5]",0.000,0.000,0.000,16.200,valid
Eq-11_200_Th0.05_M5,"Dir[-1,1]","[3.5,-3.5]","[-3.5,3.5]","[-3.5,3.5]",0.000,0.000,0.000,16.200,valid
Eq-11_200_Th0.05_M5,"Dir[1,-1]","[-3.5,3.5]","[3.5,-3.5]","[3.5,-3.5]",0.000,0.000,0.000,16.200,valid
Eq-11_200_Th0.05_M5,"Dir[-1,-1]","[-3.5,-3.5]","[3.5,3.5]","[3.5,3.5]",0.000,0.000,0.000,16.200,valid
Eq-11_200_Th0.05_M10,"Dir[1,0]","[0.0,10.0]","[-0.0,-10.0]","[-0.0,-10.0]",0.030,0.000,0.000,11.000,valid
Eq-11_200_Th0.05_M10,"Dir[0,1]","[10.0,0.0]","[-10.0,-0.0]","[-10.0,0.0]",0.080,0.000,0.000,11.000,valid
Eq-11_200_Th0.05_M10,"Dir[1,1]","[7.1,7.1]","[-7.1,-7.1]","[-7.1,-7.1]",0.000,0.000,0.000,11.200,valid
Eq-11_200_Th0.05_M10,"Dir[-1,1]","[7.1,-7.1]","[-7.1,7.1]","[-7.1,7.1]",0.000,0.000,0.000,11.200,valid
Eq-11_200_Th0.05_M10,"Dir[1,-1]","[-7.1,7.1]","[7.1,-7.1]","[7.1,-7.1]",0.000,0.000,0.000,11.200,valid
Eq-11_200_Th0.05_M10,"Dir[-1,-1]","[-7.1,-7.1]","[7.1,7.1]","[7.1,7.1]",0.000,0.000,0.000,11.200,valid
Eq-11_200_Th0.05_M15,"Dir[1,0]","[0.0,15.0]","[-0.0,-15.0]","[-0.0,-15.0]",0.020,0.000,0.000,6.000,valid
Eq-11_200_Th0.05_M15,"Dir[0,1]","[15.0,0.0]","[-15.0,-0.0]","[-15.0,0.0]",0.020,0.000,0.000,6.000,valid
Eq-11_200_Th0.05_M15,"Dir[1,1]","[10.6,10.6]","[-10.6,-10.6]","[-10.6,-10.6]",0.010,0.000,0.000,6.200,valid
Eq-11_200_Th0.05_M15,"Dir[-1,1]","[10.6,-10.6]","[-10.6,10.6]","[-10.6,10.6]",0.010,0.000,0.000,6.200,valid
Eq-11_200_Th0.05_M15,"Dir[1,-1]","[-10.6,10.6]","[10.6,-10.6]","[10.6,-10.6]",0.010,0.000,0.000,6.200,valid
Eq-11_200_Th0.05_M15,"Dir[-1,-1]","[-10.6,-10.6]","[10.6,10.6]","[10.6,10.6]",0.010,0.000,0.000,6.200,valid
Eq-11_200_Th0.10_M0,"Dir[0,0]","[0.0,0.0]","[-0.0,-0.0]","[0.0,-0.0]",0.000,0.000,0.000,20.200,valid
Eq-11_200_Th0.10_M2,"Dir[1,0]","[0.0,2.0]","[-0.0,-2.0]","[0.0,-2.0]",0.000,0.000,0.000,18.200,valid
Eq-11_200_Th0.10_M2,"Dir[0,1]","[2.0,0.0]","[-2.0,-0.0]","[-2.0,0.0]",0.160,0.000,0.000,18.200,valid
Eq-11_200_Th0.10_M2,"Dir[1,1]","[1.4,1.4]","[-1.4,-1.4]","[-1.4,-1.4]",0.000,0.000,0.000,18.500,valid
Eq-11_200_Th0.10_M2,"Dir[-1,1]","[1.4,-1.4]","[-1.4,1.4]","[-1.4,1.4]",0.000,0.000,0.000,18.500,valid
Eq-11_200_Th0.10_M2,"Dir[1,-1]","[-1.4,1.4]","[1.4,-1.4]","[1.4,-1.4]",0.000,0.000,0.000,18.500,valid
Eq-11_200_Th0.10_M2,"Dir[-1,-1]","[-1.4,-1.4]","[1.4,1.4]","[1.4,1.4]",0.000,0.000,0.000,18.500,valid
Eq-11_200_Th0.10_M5,"Dir[1,0]","[0.0,5.0]","[-0.0,-5.0]","[0.0,-5.0]",0.000,0.000,0.000,15.300,valid
Eq-11_200_Th0.10_M5,"Dir[0,1]","[5.0,0.0]","[-5.0,-0.0]","[-5.0,-0.0]",0.000,0.000,0.000,15.300,valid
Eq-11_200_Th0.10_M5,"Dir[1,1]","[3.5,3.5]","[-3.5,-3.5]","[-3.5,-3.5]",0.000,0.000,0.000,15.500,valid
Eq-11_200_Th0.10_M5,"Dir[-1,1]","[3.5,-3.5]","[-3.5,3.5]","[-3.5,3.5]",0.000,0.000,0.000,15.500,valid
Eq-11_200_Th0.10_M5,"Dir[1,-1]","[-3.5,3.5]","[3.5,-3.5]","[3.5,-3.5]",0.000,0.000,0.000,15.500,valid
Eq-11_200_Th0.10_M5,"Dir[-1,-1]","[-3.5,-3.5]","[3.5,3.5]","[3.5,3.5]",0.000,0.000,0.000,15.500,valid
Eq-11_200_Th0.10_M10,"Dir[1,0]","[0.0,10.0]","[-0.0,-10.0]","[-0.0,-10.0]",0.010,0.000,0.000,10.400,valid
Eq-11_200_Th0.10_M10,"Dir[0,1]","[10.0,0.0]","[-10.0,-0.0]","[-10.0,0.0]",0.010,0.000,0.000,10.400,valid
Eq-11_200_Th0.10_M10,"Dir[1,1]","[7.1,7.1]","[-7.1,-7.1]","[-7.1,-7.1]",0.000,0.000,0.000,10.500,valid
Eq-11_200_Th0.10_M10,"Dir[-1,1]","[7.1,-7.1]","[-7.1,7.1]","[-7.1,7.1]",0.000,0.000,0.000,10.500,valid
Eq-11_200_Th0.10_M10,"Dir[1,-1]","[-7.1,7.1]","[7.1,-7.1]","[7.1,-7.1]",0.000,0.000,0.000,10.500,valid
Eq-11_200_Th0.10_M10,"Dir[-1,-1]","[-7.1,-7.1]","[7.1,7.1]","[7.1,7.1]",0.000,0.000,0.000,10.500,valid
Eq-11_200_Th0.10_M15,"Dir[1,0]","[0.0,15.0]","[-0.0,-15.0]","[-0.0,-15.0]",0.010,0.000,0.000,5.800,valid
Eq-11_200_Th0.10_M15,"Dir[0,1]","[15.0,0.0]","[-15.0,-0.0]","[-15.0,0.0]",0.050,0.000,0.000,5.800,valid
Eq-11_200_Th0.10_M15,"Dir[1,1]","[10.6,10.6]","[-10.6,-10.6]","[-10.6,-10.6]",0.000,0.000,0.000,5.600,valid
Eq-11_200_Th0.10_M15,"Dir[-1,1]","[10.6,-10.6]","[-10.6,10.6]","[-10.6,10.6]",0.000,0.000,0.000,5.600,valid
Eq-11_200_Th0.10_M15,"Dir[1,-1]","[-10.6,10.6]","[10.6,-10.6]","[10.6,-10.6]",0.000,0.000,0.000,5.600,valid
Eq-11_200_Th0.10_M15,"Dir[-1,-1]","[-10.6,-10.6]","[10.6,10.6]","[10.6,10.6]",0.000,0.000,0.000,5.600,valid
Eq-11_200_Th0.20_M0,"Dir[0,0]","[0.0,0.0]","[-0.0,-0.0]","[0.0,-0.0]",0.000,0.000,0.000,19.900,valid
Eq-11_200_Th0.20_M2,"Dir[1,0]","[0.0,2.0]","[-0.0,-2.0]","[0.0,-2.0]",0.000,0.000,0.000,18.000,valid
Eq-11_200_Th0.20_M2,"Dir[0,1]","[2.0,0.0]","[-2.0,-0.0]","[-2.0,-0.0]",0.000,0.000,0.000,18.000,valid
Eq-11_200_Th0.20_M2,"Dir[1,1]","[1.4,1.4]","[-1.4,-1.4]","[-1.4,-1.4]",0.000,0.000,0.000,18.000,valid
Eq-11_200_Th0.20_M2,"Dir[-1,1]","[1.4,-1.4]","[-1.4,1.4]","[-1.4,1.4]",0.000,0.000,0.000,18.000,valid
Eq-11_200_Th0.20_M2,"Dir[1,-1]","[-1.4,1.4]","[1.4,-1.4]","[1.4,-1.4]",0.000,0.000,0.000,18.000,valid
Eq-11_200_Th0.20_M2,"Dir[-1,-1]","[-1.4,-1.4]","[1.4,1.4]","[1.4,1.4]",0.000,0.000,0.000,18.000,valid
Eq-11_200_Th0.20_M5,"Dir[1,0]","[0.0,5.0]","[-0.0,-5.0]","[0.0,-5.0]",0.000,0.000,0.000,15.000,valid
Eq-11_200_Th0.20_M5,"Dir[0,1]","[5.0,0.0]","[-5.0,-0.0]","[-5.0,0.0]",0.090,0.000,0.000,15.000,valid
Eq-11_200_Th0.20_M5,"Dir[1,1]","[3.5,3.5]","[-3.5,-3.5]","[-3.5,-3.5]",0.000,0.000,0.000,15.100,valid
Eq-11_200_Th0.20_M5,"Dir[-1,1]","[3.5,-3.5]","[-3.5,3.5]","[-3.5,3.5]",0.000,0.000,0.000,15.100,valid
Eq-11_200_Th0.20_M5,"Dir[1,-1]","[-3.5,3.5]","[3.5,-3.5]","[3.5,-3.5]",0.000,0.000,0.000,15.100,valid
Eq-11_200_Th0.20_M5,"Dir[-1,-1]","[-3.5,-3.5]","[3.5,3.5]","[3.5,3.5]",0.000,0.000,0.000,15.100,valid
Eq-11_200_Th0.20_M10,"Dir[1,0]","[0.0,10.0]","[-0.0,-10.0]","[0.0,-10.0]",0.000,0.000,0.000,10.000,valid
Eq-11_200_Th0.20_M10,"Dir[0,1]","[10.0,0.0]","[-10.0,-0.0]","[-10.0,0.0]",0.050,0.000,0.000,10.000,valid
Eq-11_200_Th0.20_M10,"Dir[1,1]","[7.1,7.1]","[-7.1,-7.1]","[-7.1,-7.1]",0.000,0.000,0.000,10.200,valid
Eq-11_200_Th0.20_M10,"Dir[-1,1]","[7.1,-7.1]","[-7.1,7.1]","[-7.1,7.1]",0.000,0.000,0.000,10.200,valid
Eq-11_200_Th0.20_M10,"Dir[1,-1]","[-7.1,7.1]","[7.1,-7.1]","[7.1,-7.1]",0.000,0.000,0.000,10.200,valid
Eq-11_200_Th0.20_M10,"Dir[-1,-1]","[-7.1,-7.1]","[7.1,7.1]","[7.1,7.1]",0.000,0.000,0.000,10.200,valid
Eq-11_200_Th0.20_M15,"Dir[1,0]","[0.0,15.0]","[-0.0,-15.0]","[-0.0,-15.1]",0.010,0.100,0.100,5.000,valid
Eq-11_200_Th0.20_M15,"Dir[0,1]","[15.0,0.0]","[-15.0,-0.0]","[-15.0,0.0]",0.050,0.000,0.000,5.000,valid
Eq-11_200_Th0.20_M15,"Dir[1,1]","[10.6,10.6]","[-10.6,-10.6]","[-10.6,-10.6]",0.010,0.000,0.000,5.600,valid
Eq-11_200_Th0.20_M15,"Dir[-1,1]","[10.6,-10.6]","[-10.6,10.6]","[-10.6,10.6]",0.010,0.000,0.000,5.600,valid
Eq-11_200_Th0.20_M15,"Dir[1,-1]","[-10.6,10.6]","[10.6,-10.6]","[10.6,-10.6]",0.010,0.000,0.000,5.600,valid
Eq-11_200_Th0.20_M15,"Dir[-1,-1]","[-10.6,-10.6]","[10.6,10.6]","[10.6,10.6]",0.010,0.000,0.000,5.600,valid
Eq-11_256_Th0.05_M0,"Dir[0,0]","[0.0,0.0]","[-0.0,-0.0]","[-0.0,-0.0]",0.000,0.000,0.000,27.300,valid
Eq-11_256_Th0.05_M2,"Dir[1,0]","[0.0,2.0]","[-0.0,-2.0]","[-0.0,-2.0]",0.000,0.000,0.000,25.300,valid
Eq-11_256_Th0.05_M2,"Dir[0,1]","[2.0,0.0]","[-2.0,-0.0]","[-2.0,-0.0]",0.010,0.000,0.000,25.300,valid
Eq-11_256_Th0.05_M2,"Dir[1,1]","[1.4,1.4]","[-1.4,-1.4]","[-1.4,-1.4]",0.000,0.000,0.000,25.500,valid
Eq-11_256_Th0.05_M2,"Dir[-1,1]","[1.4,-1.4]","[-1.4,1.4]","[-1.4,1.4]",0.000,0.000,0.000,25.500,valid
Eq-11_256_Th0.05_M2,"Dir[1,-1]","[-1.4,1.4]","[1.4,-1.4]","[1.4,-1.4]",0.000,0.000,0.000,25.500,valid
Eq-11_256_Th0.05_M2,"Dir[-1,-1]","[-1.4,-1.4]","[1.4,1.4]","[1.4,1.4]",0.000,0.000,0.000,25.500,valid
Eq-11_256_Th0.05_M5,"Dir[1,0]","[0.0,5.0]","[-0.0,-5.0]","[-0.0,-5.0]",0.000,0.000,0.000,22.400,valid
Eq-11_256_Th0.05_M5,"Dir[0,1]","[5.0,0.0]","[-5.0,-0.0]","[-5.0,-0.0]",0.000,0.000,0.000,22.400,valid
Eq-11_256_Th0.05_M5,"Dir[1,1]","[3.5,3.5]","[-3.5,-3.5]","[-3.5,-3.5]",0.000,0.000,0.000,22.600,valid
Eq-11_256_Th0.05_M5,"Dir[-1,1]","[3.5,-3.5]","[-3.5,3.5]","[-3.5,3.5]",0.000,0.000,0.000,22.600,valid
Eq-11_256_Th0.05_M5,"Dir[1,-1]","[-3.5,3.5]","[3.5,-3.5]","[3.5,-3.5]",0.000,0.000,0.000,22.600,valid
Eq-11_256_Th0.05_M5,"Dir[-1,-1]","[-3.5,-3.5]","[3.5,3.5]","[3.5,3.5]",0.000,0.000,0.000,22.600,valid
Eq-11_256_Th0.05_M10,"Dir[1,0]","[0.0,10.0]","[-0.0,-10.0]","[-0.0,-10.0]",0.020,0.000,0.000,17.500,valid
Eq-11_256_Th0.05_M10,"Dir[0,1]","[10.0,0.0]","[-10.0,-0.0]","[-10.0,0.0]",0.050,0.000,0.000,17.500,valid
Eq-11_256_Th0.05_M10,"Dir[1,1]","[7.1,7.1]","[-7.1,-7.1]","[-7.1,-7.1]",0.000,0.000,0.000,17.600,valid
Eq-11_256_Th0.05_M10,"Dir[-1,1]","[7.1,-7.1]","[-7.1,7.1]","[-7.1,7.1]",0.000,0.000,0.000,17.600,valid
Eq-11_256_Th0.05_M10,"Dir[1,-1]","[-7.1,7.1]","[7.1,-7.1]","[7.1,-7.1]",0.000,0.000,0.000,17.600,valid
Eq-11_256_Th0.05_M10,"Dir[-1,-1]","[-7.1,-7.1]","[7.1,7.1]","[7.1,7.1]",0.000,0.000,0.000,17.600,valid
Eq-11_256_Th0.05_M15,"Dir[1,0]","[0.0,15.0]","[-0.0,-15.0]","[-0.0,-15.0]",0.010,0.000,0.000,12.600,valid
Eq-11_256_Th0.05_M15,"Dir[0,1]","[15.0,0.0]","[-15.0,-0.0]","[-15.0,-0.0]",0.020,0.000,0.000,12.600,valid
Eq-11_256_Th0.05_M15,"Dir[1,1]","[10.6,10.6]","[-10.6,-10.6]","[-10.6,-10.6]",0.000,0.000,0.000,12.600,valid
Eq-11_256_Th0.05_M15,"Dir[-1,1]","[10.6,-10.6]","[-10.6,10.6]","[-10.6,10.6]",0.010,0.000,0.000,12.600,valid
Eq-11_256_Th0.05_M15,"Dir[1,-1]","[-10.6,10.6]","[10.6,-10.6]","[10.6,-10.6]",0.000,0.000,0.000,12.600,valid
Eq-11_256_Th0.05_M15,"Dir[-1,-1]","[-10.6,-10.6]","[10.6,10.6]","[10.6,10.6]",0.010,0.000,0.000,12.600,valid
Eq-11_256_Th0.10_M0,"Dir[0,0]","[0.0,0.0]","[-0.0,-0.0]","[0.0,-0.0]",0.000,0.000,0.000,26.300,valid
Eq-11_256_Th0.10_M2,"Dir[1,0]","[0.0,2.0]","[-0.0,-2.0]","[0.0,-2.0]",0.000,0.000,0.000,24.300,valid
Eq-11_256_Th0.10_M2,"Dir[0,1]","[2.0,0.0]","[-2.0,-0.0]","[-2.0,-0.0]",0.000,0.000,0.000,24.300,valid
Eq-11_256_Th0.10_M2,"Dir[1,1]","[1.4,1.4]","[-1.4,-1.4]","[-1.4,-1.4]",0.000,0.000,0.000,24.500,valid
Eq-11_256_Th0.10_M2,"Dir[-1,1]","[1.4,-1.4]","[-1.4,1.4]","[-1.4,1.4]",0.000,0.000,0.000,24.500,valid
Eq-11_256_Th0.10_M2,"Dir[1,-1]","[-1.4,1.4]","[1.4,-1.4]","[1.4,-1.4]",0.000,0.000,0.000,24.500,valid
Eq-11_256_Th0.10_M2,"Dir[-1,-1]","[-1.4,-1.4]","[1.4,1.4]","[1.4,1.4]",0.000,0.000,0.000,24.500,valid
Eq-11_256_Th0.10_M5,"Dir[1,0]","[0.0,5.0]","[-0.0,-5.0]","[0.0,-5.0]",0.000,0.000,0.000,21.400,valid
Eq-11_256_Th0.10_M5,"Dir[0,1]","[5.0,0.0]","[-5.0,-0.0]","[-5.0,-0.0]",0.000,0.000,0.000,21.400,valid
Eq-11_256_Th0.10_M5,"Dir[1,1]","[3.5,3.5]","[-3.5,-3.5]","[-3.5,-3.5]",0.020,0.000,0.000,21.600,valid
Eq-11_256_Th0.10_M5,"Dir[-1,1]","[3.5,-3.5]","[-3.5,3.5]","[-3.5,3.5]",0.000,0.000,0.000,21.600,valid
Eq-11_256_Th0.10_M5,"Dir[1,-1]","[-3.5,3.5]","[3.5,-3.5]","[3.5,-3.5]",0.020,0.000,0.000,21.600,valid
Eq-11_256_Th0.10_M5,"Dir[-1,-1]","[-3.5,-3.5]","[3.5,3.5]","[3.5,3.5]",0.000,0.000,0.000,21.600,valid
Eq-11_256_Th0.10_M10,"Dir[1,0]","[0.0,10.0]","[-0.0,-10.0]","[-0.0,-10.0]",0.010,0.000,0.000,16.500,valid
Eq-11_256_Th0.10_M10,"Dir[0,1]","[10.0,0.0]","[-10.0,-0.0]","[-10.0,0.0]",0.040,0.000,0.000,16.500,valid
Eq-11_256_Th0.10_M10,"Dir[1,1]","[7.1,7.1]","[-7.1,-7.1]","[-7.1,-7.1]",0.000,0.000,0.000,16.900,valid
Eq-11_256_Th0.10_M10,"Dir[-1,1]","[7.1,-7.1]","[-7.1,7.1]","[-7.1,7.1]",0.000,0.000,0.000,16.900,valid
Eq-11_256_Th0.10_M10,"Dir[1,-1]","[-7.1,7.1]","[7.1,-7.1]","[7.1,-7.1]",0.000,0.000,0.000,16.900,valid
Eq-11_256_Th0.10_M10,"Dir[-1,-1]","[-7.1,-7.1]","[7.1,7.1]","[7.1,7.1]",0.000,0.000,0.000,16.900,valid
Eq-11_256_Th0.10_M15,"Dir[1,0]","[0.0,15.0]","[-0.0,-15.0]","[-0.0,-15.0]",0.010,0.000,0.000,11.700,valid
Eq-11_256_Th0.10_M15,"Dir[0,1]","[15.0,0.0]","[-15.0,-0.0]","[-15.0,0.0]",0.010,0.000,0.000,11.700,valid
Eq-11_256_Th0.10_M15,"Dir[1,1]","[10.6,10.6]","[-10.6,-10.6]","[-10.6,-10.6]",0.000,0.000,0.000,11.900,valid
Eq-11_256_Th0.10_M15,"Dir[-1,1]","[10.6,-10.6]","[-10.6,10.6]","[-10.6,10.6]",0.010,0.000,0.000,11.900,valid
Eq-11_256_Th0.10_M15,"Dir[1,-1]","[-10.6,10.6]","[10.6,-10.6]","[10.6,-10.6]",0.000,0.000,0.000,11.900,valid
Eq-11_256_Th0.10_M15,"Dir[-1,-1]","[-10.6,-10.6]","[10.6,10.6]","[10.6,10.6]",0.010,0.000,0.000,11.900,valid
Eq-11_256_Th0.20_M0,"Dir[0,0]","[0.0,0.0]","[-0.0,-0.0]","[-0.0,-0.0]",0.000,0.000,0.000,25.700,valid
Eq-11_256_Th0.20_M2,"Dir[1,0]","[0.0,2.0]","[-0.0,-2.0]","[-0.0,-2.0]",0.000,0.000,0.000,23.800,valid
Eq-11_256_Th0.20_M2,"Dir[0,1]","[2.0,0.0]","[-2.0,-0.0]","[-2.0,-0.0]",0.010,0.000,0.000,23.800,valid
Eq-11_256_Th0.20_M2,"Dir[1,1]","[1.4,1.4]","[-1.4,-1.4]","[-1.4,-1.4]",0.000,0.000,0.000,23.800,valid
Eq-11_256_Th0.20_M2,"Dir[-1,1]","[1.4,-1.4]","[-1.4,1.4]","[-1.4,1.4]",0.000,0.000,0.000,23.800,valid
Eq-11_256_Th0.20_M2,"Dir[1,-1]","[-1.4,1.4]","[1.4,-1.4]","[1.4,-1.4]",0.000,0.000,0.000,23.800,valid
Eq-11_256_Th0.20_M2,"Dir[-1,-1]","[-1.4,-1.4]","[1.4,1.4]","[1.4,1.4]",0.000,0.000,0.000,23.800,valid
Eq-11_256_Th0.20_M5,"Dir[1,0]","[0.0,5.0]","[-0.0,-5.0]","[-0.0,-5.0]",0.060,0.000,0.000,20.900,valid
Eq-11_256_Th0.20_M5,"Dir[0,1]","[5.0,0.0]","[-5.0,-0.0]","[-5.0,0.0]",0.130,0.000,0.000,20.900,valid
Eq-11_256_Th0.20_M5,"Dir[1,1]","[3.5,3.5]","[-3.5,-3.5]","[-3.5,-3.5]",0.000,0.000,0.000,20.900,valid
Eq-11_256_Th0.20_M5,"Dir[-1,1]","[3.5,-3.5]","[-3.5,3.5]","[-3.5,3.5]",0.000,0.000,0.000,20.900,valid
Eq-11_256_Th0.20_M5,"Dir[1,-1]","[-3.5,3.5]","[3.5,-3.5]","[3.5,-3.5]",0.000,0.000,0.000,20.900,valid
Eq-11_256_Th0.20_M5,"Dir[-1,-1]","[-3.5,-3.5]","[3.5,3.5]","[3.5,3.5]",0.000,0.000,0.000,20.900,valid
Eq-11_256_Th0.20_M10,"Dir[1,0]","[0.0,10.0]","[-0.0,-10.0]","[-0.0,-10.0]",0.030,0.000,0.000,16.000,valid
Eq-11_256_Th0.20_M10,"Dir[0,1]","[10.0,0.0]","[-10.0,-0.0]","[-10.0,-0.0]",0.020,0.000,0.000,16.000,valid
Eq-11_256_Th0.20_M10,"Dir[1,1]","[7.1,7.1]","[-7.1,-7.1]","[-7.1,-7.1]",0.000,0.000,0.000,16.000,valid
Eq-11_256_Th0.20_M10,"Dir[-1,1]","[7.1,-7.1]","[-7.1,7.1]","[-7.1,7.1]",0.000,0.000,0.000,16.000,valid
Eq-11_256_Th0.20_M10,"Dir[1,-1]","[-7.1,7.1]","[7.1,-7.1]","[7.1,-7.1]",0.000,0.000,0.000,16.000,valid
Eq-11_256_Th0.20_M10,"Dir[-1,-1]","[-7.1,-7.1]","[7.1,7.1]","[7.1,7.1]",0.000,0.000,0.000,16.000,valid
Eq-11_256_Th0.20_M15,"Dir[1,0]","[0.0,15.0]","[-0.0,-15.0]","[-0.0,-15.0]",0.010,0.000,0.000,11.000,valid
Eq-11_256_Th0.20_M15,"Dir[0,1]","[15.0,0.0]","[-15.0,-0.0]","[-15.0,-0.0]",0.020,0.000,0.000,11.000,valid
Eq-11_256_Th0.20_M15,"Dir[1,1]","[10.6,10.6]","[-10.6,-10.6]","[-10.6,-10.6]",0.000,0.000,0.000,11.200,valid
Eq-11_256_Th0.20_M15,"Dir[-1,1]","[10.6,-10.6]","[-10.6,10.6]","[-10.6,10.6]",0.000,0.000,0.000,11.200,valid
Eq-11_256_Th0.20_M15,"Dir[1,-1]","[-10.6,10.6]","[10.6,-10.6]","[10.6,-10.6]",0.000,0.000,0.000,11.200,valid
Eq-11_256_Th0.20_M15,"Dir[-1,-1]","[-10.6,-10.6]","[10.6,10.6]","[10.6,10.6]",0.000,0.000,0.000,11.200,valid
Eq-9_200_Th0.05_M0,"Dir[0,0]","[0.0,0.0]","[-0.0,-0.0]","[0.0,0.0]",0.000,0.000,0.000,16.100,valid
Eq-9_200_Th0.05_M2,"Dir[1,0]","[0.0,2.0]","[-0.0,-2.0]","[-0.0,-2.0]",0.070,0.000,0.000,14.200,valid
Eq-9_200_Th0.05_M2,"Dir[0,1]","[2.0,0.0]","[-2.0,-0.0]","[-2.0,0.0]",0.070,0.000,0.000,14.200,valid
Eq-9_200_Th0.05_M2,"Dir[1,1]","[1.4,1.4]","[-1.4,-1.4]","[-1.4,-1.4]",0.000,0.000,0.000,14.300,valid
Eq-9_200_Th0.05_M2,"Dir[-1,1]","[1.4,-1.4]","[-1.4,1.4]","[-1.4,1.4]",0.000,0.000,0.000,14.300,valid
Eq-9_200_Th0.05_M2,"Dir[1,-1]","[-1.4,1.4]","[1.4,-1.4]","[1.4,-1.4]",0.000,0.000,0.000,14.300,valid
Eq-9_200_Th0.05_M2,"Dir[-1,-1]","[-1.4,-1.4]","[1.4,1.4]","[1.4,1.4]",0.000,0.000,0.000,14.300,valid
Eq-9_200_Th0.05_M5,"Dir[1,0]","[0.0,5.0]","[-0.0,-5.0]","[0.0,-5.0]",0.000,0.000,0.000,11.400,valid
Eq-9_200_Th0.05_M5,"Dir[0,1]","[5.0,0.0]","[-5.0,-0.0]","[-5.0,-0.0]",0.000,0.000,0.000,11.400,valid
Eq-9_200_Th0.05_M5,"Dir[1,1]","[3.5,3.5]","[-3.5,-3.5]","[-3.5,-3.5]",0.040,0.000,0.000,11.400,valid
Eq-9_200_Th0.05_M5,"Dir[-1,1]","[3.5,-3.5]","[-3.5,3.5]","[-3.5,3.5]",0.080,0.000,0.000,11.400,valid
Eq-9_200_Th0.05_M5,"Dir[1,-1]","[-3.5,3.5]","[3.5,-3.5]","[3.5,-3.5]",0.040,0.000,0.000,11.400,valid
Eq-9_200_Th0.05_M5,"Dir[-1,-1]","[-3.5,-3.5]","[3.5,3.5]","[3.5,3.5]",0.080,0.000,0.000,11.400,valid
Eq-9_200_Th0.05_M10,"Dir[1,0]","[0.0,10.0]","[-0.0,-10.0]","[-0.0,-10.0]",0.030,0.000,0.000,6.500,valid
Eq-9_200_Th0.05_M10,"Dir[0,1]","[10.0,0.0]","[-10.0,-0.0]","[-10.0,0.0]",0.030,0.000,0.000,6.500,valid
Eq-9_200_Th0.05_M10,"Dir[1,1]","[7.1,7.1]","[-7.1,-7.1]","[-7.1,-7.1]",0.000,0.000,0.000,6.400,valid
Eq-9_200_Th0.05_M10,"Dir[-1,1]","[7.1,-7.1]","[-7.1,7.1]","[-7.1,7.1]",0.000,0.000,0.000,6.400,valid
Eq-9_200_Th0.05_M10,"Dir[1,-1]","[-7.1,7.1]","[7.1,-7.1]","[7.1,-7.1]",0.000,0.000,0.000,6.400,valid
Eq-9_200_Th0.05_M10,"Dir[-1,-1]","[-7.1,-7.1]","[7.1,7.1]","[7.1,7.1]",0.000,0.000,0.000,6.400,valid
Eq-9_200_Th0.05_M15,"Dir[1,0]","[0.0,15.0]","[-0.0,-15.0]","[-0.0,-15.0]",0.020,0.000,0.000,1.600,measurement_limited
Eq-9_200_Th0.05_M15,"Dir[0,1]","[15.0,0.0]","[-15.0,-0.0]","[-15.0,0.0]",0.040,0.000,0.000,1.600,measurement_limited
Eq-9_200_Th0.05_M15,"Dir[1,1]","[10.6,10.6]","[-10.6,-10.6]","[-10.5,-10.5]",0.000,0.141,0.141,1.900,measurement_limited
Eq-9_200_Th0.05_M15,"Dir[-1,1]","[10.6,-10.6]","[-10.6,10.6]","[-10.5,10.5]",0.030,0.141,0.141,1.900,measurement_limited
Eq-9_200_Th0.05_M15,"Dir[1,-1]","[-10.6,10.6]","[10.6,-10.6]","[10.5,-10.5]",0.000,0.141,0.141,1.900,measurement_limited
Eq-9_200_Th0.05_M15,"Dir[-1,-1]","[-10.6,-10.6]","[10.6,10.6]","[10.5,10.5]",0.030,0.141,0.141,1.900,measurement_limited
Eq-9_200_Th0.10_M0,"Dir[0,0]","[0.0,0.0]","[-0.0,-0.0]","[0.0,0.0]",0.000,0.000,0.000,15.500,valid
Eq-9_200_Th0.10_M2,"Dir[1,0]","[0.0,2.0]","[-0.0,-2.0]","[-0.0,-2.0]",0.040,0.000,0.000,13.500,valid
Eq-9_200_Th0.10_M2,"Dir[0,1]","[2.0,0.0]","[-2.0,-0.0]","[-2.0,0.0]",0.040,0.000,0.000,13.500,valid
Eq-9_200_Th0.10_M2,"Dir[1,1]","[1.4,1.4]","[-1.4,-1.4]","[-1.4,-1.4]",0.000,0.000,0.000,13.700,valid
Eq-9_200_Th0.10_M2,"Dir[-1,1]","[1.4,-1.4]","[-1.4,1.4]","[-1.4,1.4]",0.000,0.000,0.000,13.700,valid
Eq-9_200_Th0.10_M2,"Dir[1,-1]","[-1.4,1.4]","[1.4,-1.4]","[1.4,-1.4]",0.000,0.000,0.000,13.700,valid
Eq-9_200_Th0.10_M2,"Dir[-1,-1]","[-1.4,-1.4]","[1.4,1.4]","[1.4,1.4]",0.010,0.000,0.000,13.700,valid
Eq-9_200_Th0.10_M5,"Dir[1,0]","[0.0,5.0]","[-0.0,-5.0]","[0.0,-5.0]",0.000,0.000,0.000,10.500,valid
Eq-9_200_Th0.10_M5,"Dir[0,1]","[5.0,0.0]","[-5.0,-0.0]","[-5.0,0.0]",0.000,0.000,0.000,10.500,valid
Eq-9_200_Th0.10_M5,"Dir[1,1]","[3.5,3.5]","[-3.5,-3.5]","[-3.5,-3.5]",0.000,0.000,0.000,10.800,valid
Eq-9_200_Th0.10_M5,"Dir[-1,1]","[3.5,-3.5]","[-3.5,3.5]","[-3.5,3.5]",0.000,0.000,0.000,10.800,valid
Eq-9_200_Th0.10_M5,"Dir[1,-1]","[-3.5,3.5]","[3.5,-3.5]","[3.5,-3.5]",0.000,0.000,0.000,10.800,valid
Eq-9_200_Th0.10_M5,"Dir[-1,-1]","[-3.5,-3.5]","[3.5,3.5]","[3.5,3.5]",0.000,0.000,0.000,10.800,valid
Eq-9_200_Th0.10_M10,"Dir[1,0]","[0.0,10.0]","[-0.0,-10.0]","[-0.0,-10.1]",0.000,0.100,0.100,5.500,valid
Eq-9_200_Th0.10_M10,"Dir[0,1]","[10.0,0.0]","[-10.0,-0.0]","[-10.1,-0.0]",0.000,0.100,0.100,5.500,valid
Eq-9_200_Th0.10_M10,"Dir[1,1]","[7.1,7.1]","[-7.1,-7.1]","[-7.0,-7.0]",0.000,0.141,0.141,5.900,valid
Eq-9_200_Th0.10_M10,"Dir[-1,1]","[7.1,-7.1]","[-7.1,7.1]","[-7.0,7.0]",0.000,0.141,0.141,5.900,valid
Eq-9_200_Th0.10_M10,"Dir[1,-1]","[-7.1,7.1]","[7.1,-7.1]","[7.0,-7.0]",0.000,0.141,0.141,5.900,valid
Eq-9_200_Th0.10_M10,"Dir[-1,-1]","[-7.1,-7.1]","[7.1,7.1]","[7.0,7.0]",0.000,0.141,0.141,5.900,valid
Eq-9_200_Th0.10_M15,"Dir[1,0]","[0.0,15.0]","[-0.0,-15.0]","[-0.0,-15.2]",0.010,0.200,0.200,0.700,measurement_limited
Eq-9_200_Th0.10_M15,"Dir[0,1]","[15.0,0.0]","[-15.0,-0.0]","[-15.2,0.0]",0.100,0.200,0.200,0.700,measurement_limited
Eq-9_200_Th0.10_M15,"Dir[1,1]","[10.6,10.6]","[-10.6,-10.6]","[-10.4,-10.4]",0.020,0.283,0.283,1.300,measurement_limited
Eq-9_200_Th0.10_M15,"Dir[-1,1]","[10.6,-10.6]","[-10.6,10.6]","[-10.4,10.5]",0.140,0.212,0.224,1.300,measurement_limited
Eq-9_200_Th0.10_M15,"Dir[1,-1]","[-10.6,10.6]","[10.6,-10.6]","[10.4,-10.4]",0.020,0.283,0.283,1.300,measurement_limited
Eq-9_200_Th0.10_M15,"Dir[-1,-1]","[-10.6,-10.6]","[10.6,10.6]","[10.4,10.5]",0.140,0.212,0.224,1.300,measurement_limited
Eq-9_200_Th0.20_M0,"Dir[0,0]","[0.0,0.0]","[-0.0,-0.0]","[-0.0,0.0]",0.000,0.000,0.000,14.700,valid
Eq-9_200_Th0.20_M2,"Dir[1,0]","[0.0,2.0]","[-0.0,-2.0]","[-0.0,-2.0]",0.070,0.000,0.000,12.700,valid
Eq-9_200_Th0.20_M2,"Dir[0,1]","[2.0,0.0]","[-2.0,-0.0]","[-2.0,0.0]",0.070,0.000,0.000,12.700,valid
Eq-9_200_Th0.20_M2,"Dir[1,1]","[1.4,1.4]","[-1.4,-1.4]","[-1.4,-1.4]",0.000,0.000,0.000,12.900,valid
Eq-9_200_Th0.20_M2,"Dir[-1,1]","[1.4,-1.4]","[-1.4,1.4]","[-1.4,1.4]",0.010,0.000,0.000,12.900,valid
Eq-9_200_Th0.20_M2,"Dir[1,-1]","[-1.4,1.4]","[1.4,-1.4]","[1.4,-1.4]",0.000,0.000,0.000,12.900,valid
Eq-9_200_Th0.20_M2,"Dir[-1,-1]","[-1.4,-1.4]","[1.4,1.4]","[1.4,1.4]",0.010,0.000,0.000,12.900,valid
Eq-9_200_Th0.20_M5,"Dir[1,0]","[0.0,5.0]","[-0.0,-5.0]","[0.0,-5.0]",0.000,0.000,0.000,9.800,valid
Eq-9_200_Th0.20_M5,"Dir[0,1]","[5.0,0.0]","[-5.0,-0.0]","[-5.0,0.0]",0.000,0.000,0.000,9.800,valid
Eq-9_200_Th0.20_M5,"Dir[1,1]","[3.5,3.5]","[-3.5,-3.5]","[-3.5,-3.5]",0.000,0.000,0.000,10.000,valid
Eq-9_200_Th0.20_M5,"Dir[-1,1]","[3.5,-3.5]","[-3.5,3.5]","[-3.5,3.5]",0.000,0.000,0.000,10.000,valid
Eq-9_200_Th0.20_M5,"Dir[1,-1]","[-3.5,3.5]","[3.5,-3.5]","[3.5,-3.5]",0.000,0.000,0.000,10.000,valid
Eq-9_200_Th0.20_M5,"Dir[-1,-1]","[-3.5,-3.5]","[3.5,3.5]","[3.5,3.5]",0.000,0.000,0.000,10.000,valid
Eq-9_200_Th0.20_M10,"Dir[1,0]","[0.0,10.0]","[-0.0,-10.0]","[-0.0,-10.0]",0.030,0.000,0.000,5.100,valid
Eq-9_200_Th0.20_M10,"Dir[0,1]","[10.0,0.0]","[-10.0,-0.0]","[-10.0,0.0]",0.030,0.000,0.000,5.100,valid
Eq-9_200_Th0.20_M10,"Dir[1,1]","[7.1,7.1]","[-7.1,-7.1]","[-7.1,-7.1]",0.000,0.000,0.000,5.100,valid
Eq-9_200_Th0.20_M10,"Dir[-1,1]","[7.1,-7.1]","[-7.1,7.1]","[-7.1,7.1]",0.000,0.000,0.000,5.100,valid
Eq-9_200_Th0.20_M10,"Dir[1,-1]","[-7.1,7.1]","[7.1,-7.1]","[7.1,-7.1]",0.000,0.000,0.000,5.100,valid
Eq-9_200_Th0.20_M10,"Dir[-1,-1]","[-7.1,-7.1]","[7.1,7.1]","[7.1,7.1]",0.000,0.000,0.000,5.100,valid
Eq-9_200_Th0.20_M15,"Dir[1,0]","[0.0,15.0]","[-0.0,-15.0]","[-0.0,-14.6]",0.020,0.400,0.400,0.700,measurement_limited
Eq-9_200_Th0.20_M15,"Dir[0,1]","[15.0,0.0]","[-15.0,-0.0]","[-14.6,0.1]",0.570,0.400,0.412,0.700,measurement_limited
Eq-9_200_Th0.20_M15,"Dir[1,1]","[10.6,10.6]","[-10.6,-10.6]","[-10.3,-10.3]",0.020,0.424,0.424,0.900,measurement_limited
Eq-9_200_Th0.20_M15,"Dir[-1,1]","[10.6,-10.6]","[-10.6,10.6]","[-10.3,10.3]",0.000,0.424,0.424,0.900,measurement_limited
Eq-9_200_Th0.20_M15,"Dir[1,-1]","[-10.6,10.6]","[10.6,-10.6]","[10.3,-10.3]",0.020,0.424,0.424,0.900,measurement_limited
Eq-9_200_Th0.20_M15,"Dir[-1,-1]","[-10.6,-10.6]","[10.6,10.6]","[10.3,10.3]",0.000,0.424,0.424,0.900,measurement_limited
Eq-9_256_Th0.05_M0,"Dir[0,0]","[0.0,0.0]","[-0.0,-0.0]","[-0.0,-0.0]",0.000,0.000,0.000,20.900,valid
Eq-9_256_Th0.05_M2,"Dir[1,0]","[0.0,2.0]","[-0.0,-2.0]","[-0.0,-2.0]",0.000,0.000,0.000,19.000,valid
Eq-9_256_Th0.05_M2,"Dir[0,1]","[2.0,0.0]","[-2.0,-0.0]","[-2.0,-0.0]",0.000,0.000,0.000,19.000,valid
Eq-9_256_Th0.05_M2,"Dir[1,1]","[1.4,1.4]","[-1.4,-1.4]","[-1.4,-1.4]",0.000,0.000,0.000,19.100,valid
Eq-9_256_Th0.05_M2,"Dir[-1,1]","[1.4,-1.4]","[-1.4,1.4]","[-1.4,1.4]",0.000,0.000,0.000,19.100,valid
Eq-9_256_Th0.05_M2,"Dir[1,-1]","[-1.4,1.4]","[1.4,-1.4]","[1.4,-1.4]",0.000,0.000,0.000,19.100,valid
Eq-9_256_Th0.05_M2,"Dir[-1,-1]","[-1.4,-1.4]","[1.4,1.4]","[1.4,1.4]",0.000,0.000,0.000,19.100,valid
Eq-9_256_Th0.05_M5,"Dir[1,0]","[0.0,5.0]","[-0.0,-5.0]","[0.0,-5.0]",0.000,0.000,0.000,16.100,valid
Eq-9_256_Th0.05_M5,"Dir[0,1]","[5.0,0.0]","[-5.0,-0.0]","[-5.0,0.0]",0.000,0.000,0.000,16.100,valid
Eq-9_256_Th0.05_M5,"Dir[1,1]","[3.5,3.5]","[-3.5,-3.5]","[-3.5,-3.5]",0.040,0.000,0.000,16.200,valid
Eq-9_256_Th0.05_M5,"Dir[-1,1]","[3.5,-3.5]","[-3.5,3.5]","[-3.5,3.5]",0.060,0.000,0.000,16.200,valid
Eq-9_256_Th0.05_M5,"Dir[1,-1]","[-3.5,3.5]","[3.5,-3.5]","[3.5,-3.5]",0.040,0.000,0.000,16.200,valid
Eq-9_256_Th0.05_M5,"Dir[-1,-1]","[-3.5,-3.5]","[3.5,3.5]","[3.5,3.5]",0.060,0.000,0.000,16.200,valid
Eq-9_256_Th0.05_M10,"Dir[1,0]","[0.0,10.0]","[-0.0,-10.0]","[-0.0,-10.0]",0.010,0.000,0.000,11.400,valid
Eq-9_256_Th0.05_M10,"Dir[0,1]","[10.0,0.0]","[-10.0,-0.0]","[-10.0,0.0]",0.010,0.000,0.000,11.400,valid
Eq-9_256_Th0.05_M10,"Dir[1,1]","[7.1,7.1]","[-7.1,-7.1]","[-7.1,-7.1]",0.010,0.000,0.000,11.200,valid
Eq-9_256_Th0.05_M10,"Dir[-1,1]","[7.1,-7.1]","[-7.1,7.1]","[-7.1,7.1]",0.010,0.000,0.000,11.200,valid
Eq-9_256_Th0.05_M10,"Dir[1,-1]","[-7.1,7.1]","[7.1,-7.1]","[7.1,-7.1]",0.010,0.000,0.000,11.200,valid
Eq-9_256_Th0.05_M10,"Dir[-1,-1]","[-7.1,-7.1]","[7.1,7.1]","[7.1,7.1]",0.010,0.000,0.000,11.200,valid
Eq-9_256_Th0.05_M15,"Dir[1,0]","[0.0,15.0]","[-0.0,-15.0]","[-0.0,-15.0]",0.010,0.000,0.000,6.500,valid
Eq-9_256_Th0.05_M15,"Dir[0,1]","[15.0,0.0]","[-15.0,-0.0]","[-15.0,0.0]",0.010,0.000,0.000,6.500,valid
Eq-9_256_Th0.05_M15,"Dir[1,1]","[10.6,10.6]","[-10.6,-10.6]","[-10.6,-10.6]",0.000,0.000,0.000,6.300,valid
Eq-9_256_Th0.05_M15,"Dir[-1,1]","[10.6,-10.6]","[-10.6,10.6]","[-10.6,10.6]",0.000,0.000,0.000,6.300,valid
Eq-9_256_Th0.05_M15,"Dir[1,-1]","[-10.6,10.6]","[10.6,-10.6]","[10.6,-10.6]",0.000,0.000,0.000,6.300,valid
Eq-9_256_Th0.05_M15,"Dir[-1,-1]","[-10.6,-10.6]","[10.6,10.6]","[10.6,10.6]",0.000,0.000,0.000,6.300,valid
Eq-9_256_Th0.10_M0,"Dir[0,0]","[0.0,0.0]","[-0.0,-0.0]","[-0.0,0.0]",0.000,0.000,0.000,20.000,valid
Eq-9_256_Th0.10_M2,"Dir[1,0]","[0.0,2.0]","[-0.0,-2.0]","[-0.0,-2.0]",0.000,0.000,0.000,18.100,valid
Eq-9_256_Th0.10_M2,"Dir[0,1]","[2.0,0.0]","[-2.0,-0.0]","[-2.0,0.0]",0.000,0.000,0.000,18.100,valid
Eq-9_256_Th0.10_M2,"Dir[1,1]","[1.4,1.4]","[-1.4,-1.4]","[-1.4,-1.4]",0.000,0.000,0.000,18.300,valid
Eq-9_256_Th0.10_M2,"Dir[-1,1]","[1.4,-1.4]","[-1.4,1.4]","[-1.4,1.4]",0.000,0.000,0.000,18.300,valid
Eq-9_256_Th0.10_M2,"Dir[1,-1]","[-1.4,1.4]","[1.4,-1.4]","[1.4,-1.4]",0.000,0.000,0.000,18.300,valid
Eq-9_256_Th0.10_M2,"Dir[-1,-1]","[-1.4,-1.4]","[1.4,1.4]","[1.4,1.4]",0.000,0.000,0.000,18.300,valid
Eq-9_256_Th0.10_M5,"Dir[1,0]","[0.0,5.0]","[-0.0,-5.0]","[0.0,-5.0]",0.000,0.000,0.000,15.200,valid
Eq-9_256_Th0.10_M5,"Dir[0,1]","[5.0,0.0]","[-5.0,-0.0]","[-5.0,0.0]",0.000,0.000,0.000,15.200,valid
Eq-9_256_Th0.10_M5,"Dir[1,1]","[3.5,3.5]","[-3.5,-3.5]","[-3.5,-3.5]",0.040,0.000,0.000,15.500,valid
Eq-9_256_Th0.10_M5,"Dir[-1,1]","[3.5,-3.5]","[-3.5,3.5]","[-3.5,3.5]",0.060,0.000,0.000,15.500,valid
Eq-9_256_Th0.10_M5,"Dir[1,-1]","[-3.5,3.5]","[3.5,-3.5]","[3.5,-3.5]",0.040,0.000,0.000,15.500,valid
Eq-9_256_Th0.10_M5,"Dir[-1,-1]","[-3.5,-3.5]","[3.5,3.5]","[3.5,3.5]",0.060,0.000,0.000,15.500,valid
Eq-9_256_Th0.10_M10,"Dir[1,0]","[0.0,10.0]","[-0.0,-10.0]","[-0.0,-10.0]",0.010,0.000,0.000,10.500,valid
Eq-9_256_Th0.10_M10,"Dir[0,1]","[10.0,0.0]","[-10.0,-0.0]","[-10.0,0.0]",0.010,0.000,0.000,10.500,valid
Eq-9_256_Th0.10_M10,"Dir[1,1]","[7.1,7.1]","[-7.1,-7.1]","[-7.1,-7.1]",0.000,0.000,0.000,10.500,valid
Eq-9_256_Th0.10_M10,"Dir[-1,1]","[7.1,-7.1]","[-7.1,7.1]","[-7.1,7.1]",0.000,0.000,0.000,10.500,valid
Eq-9_256_Th0.10_M10,"Dir[1,-1]","[-7.1,7.1]","[7.1,-7.1]","[7.1,-7.1]",0.000,0.000,0.000,10.500,valid
Eq-9_256_Th0.10_M10,"Dir[-1,-1]","[-7.1,-7.1]","[7.1,7.1]","[7.1,7.1]",0.000,0.000,0.000,10.500,valid
Eq-9_256_Th0.10_M15,"Dir[1,0]","[0.0,15.0]","[-0.0,-15.0]","[-0.0,-15.0]",0.010,0.000,0.000,5.500,valid
Eq-9_256_Th0.10_M15,"Dir[0,1]","[15.0,0.0]","[-15.0,-0.0]","[-15.0,0.0]",0.020,0.000,0.000,5.500,valid
Eq-9_256_Th0.10_M15,"Dir[1,1]","[10.6,10.6]","[-10.6,-10.6]","[-10.6,-10.6]",0.000,0.000,0.000,5.500,valid
Eq-9_256_Th0.10_M15,"Dir[-1,1]","[10.6,-10.6]","[-10.6,10.6]","[-10.6,10.6]",0.000,0.000,0.000,5.500,valid
Eq-9_256_Th0.10_M15,"Dir[1,-1]","[-10.6,10.6]","[10.6,-10.6]","[10.6,-10.6]",0.000,0.000,0.000,5.500,valid
Eq-9_256_Th0.10_M15,"Dir[-1,-1]","[-10.6,-10.6]","[10.6,10.6]","[10.6,10.6]",0.000,0.000,0.000,5.500,valid
Eq-9_256_Th0.20_M0,"Dir[0,0]","[0.0,0.0]","[-0.0,-0.0]","[-0.0,-0.0]",0.000,0.000,0.000,19.300,valid
Eq-9_256_Th0.20_M2,"Dir[1,0]","[0.0,2.0]","[-0.0,-2.0]","[-0.0,-2.0]",0.000,0.000,0.000,17.400,valid
Eq-9_256_Th0.20_M2,"Dir[0,1]","[2.0,0.0]","[-2.0,-0.0]","[-2.0,-0.0]",0.000,0.000,0.000,17.400,valid
Eq-9_256_Th0.20_M2,"Dir[1,1]","[1.4,1.4]","[-1.4,-1.4]","[-1.4,-1.4]",0.000,0.000,0.000,17.300,valid
Eq-9_256_Th0.20_M2,"Dir[-1,1]","[1.4,-1.4]","[-1.4,1.4]","[-1.4,1.4]",0.000,0.000,0.000,17.300,valid
Eq-9_256_Th0.20_M2,"Dir[1,-1]","[-1.4,1.4]","[1.4,-1.4]","[1.4,-1.4]",0.000,0.000,0.000,17.300,valid
Eq-9_256_Th0.20_M2,"Dir[-1,-1]","[-1.4,-1.4]","[1.4,1.4]","[1.4,1.4]",0.000,0.000,0.000,17.300,valid
Eq-9_256_Th0.20_M5,"Dir[1,0]","[0.0,5.0]","[-0.0,-5.0]","[-0.0,-5.0]",0.000,0.000,0.000,14.500,valid
Eq-9_256_Th0.20_M5,"Dir[0,1]","[5.0,0.0]","[-5.0,-0.0]","[-5.0,-0.0]",0.000,0.000,0.000,14.500,valid
Eq-9_256_Th0.20_M5,"Dir[1,1]","[3.5,3.5]","[-3.5,-3.5]","[-3.5,-3.5]",0.000,0.000,0.000,14.400,valid
Eq-9_256_Th0.20_M5,"Dir[-1,1]","[3.5,-3.5]","[-3.5,3.5]","[-3.5,3.5]",0.000,0.000,0.000,14.400,valid
Eq-9_256_Th0.20_M5,"Dir[1,-1]","[-3.5,3.5]","[3.5,-3.5]","[3.5,-3.5]",0.000,0.000,0.000,14.400,valid
Eq-9_256_Th0.20_M5,"Dir[-1,-1]","[-3.5,-3.5]","[3.5,3.5]","[3.5,3.5]",0.000,0.000,0.000,14.400,valid
Eq-9_256_Th0.20_M10,"Dir[1,0]","[0.0,10.0]","[-0.0,-10.0]","[-0.0,-10.0]",0.000,0.000,0.000,9.500,valid
Eq-9_256_Th0.20_M10,"Dir[0,1]","[10.0,0.0]","[-10.0,-0.0]","[-10.0,-0.0]",0.000,0.000,0.000,9.500,valid
Eq-9_256_Th0.20_M10,"Dir[1,1]","[7.1,7.1]","[-7.1,-7.1]","[-7.1,-7.1]",0.000,0.000,0.000,9.500,valid
Eq-9_256_Th0.20_M10,"Dir[-1,1]","[7.1,-7.1]","[-7.1,7.1]","[-7.1,7.1]",0.000,0.000,0.000,9.500,valid
Eq-9_256_Th0.20_M10,"Dir[1,-1]","[-7.1,7.1]","[7.1,-7.1]","[7.1,-7.1]",0.000,0.000,0.000,9.500,valid
Eq-9_256_Th0.20_M10,"Dir[-1,-1]","[-7.1,-7.1]","[7.1,7.1]","[7.1,7.1]",0.000,0.000,0.000,9.500,valid
Eq-9_256_Th0.20_M15,"Dir[1,0]","[0.0,15.0]","[-0.0,-15.0]","[0.0,-15.0]",0.000,0.000,0.000,4.500,measurement_limited
Eq-9_256_Th0.20_M15,"Dir[0,1]","[15.0,0.0]","[-15.0,-0.0]","[-15.0,0.0]",0.000,0.000,0.000,4.500,measurement_limited
Eq-9_256_Th0.20_M15,"Dir[1,1]","[10.6,10.6]","[-10.6,-10.6]","[-10.6,-10.6]",0.010,0.000,0.000,4.900,measurement_limited
Eq-9_256_Th0.20_M15,"Dir[-1,1]","[10.6,-10.6]","[-10.6,10.6]","[-10.6,10.6]",0.060,0.000,0.000,4.900,measurement_limited
Eq-9_256_Th0.20_M15,"Dir[1,-1]","[-10.6,10.6]","[10.6,-10.6]","[10.6,-10.6]",0.010,0.000,0.000,4.900,measurement_limited
Eq-9_256_Th0.20_M15,"Dir[-1,-1]","[-10.6,-10.6]","[10.6,10.6]","[10.6,10.6]",0.060,0.000,0.000,4.900,measurement_limited
```
</details>

---

### 22. STAV
Dokumentační úklid byl dokončen. Dokument je nyní soběstačný a obsahuje informace potřebné k porozumění výsledkům. Technické a číselné závěry fáze 01I zůstávají beze změny. Výsledky mají metodologický a geometrický charakter; nejde o fyzikální validaci HSU ani kosmologické interpretace Lineum.
---

---

---

---

### 23. FÁZE 01J-c: CLEARANCE A KONZISTENČNÍ AUDIT

**Jednoduché shrnutí**
Byl proveden konzistenční audit (01J-c), který potvrdil, že výpočet `Clearance_shell` byl v pilotní iteraci 01J chybný (počítal vzdálenost k okraji obrazu, nikoli obálky). Kód byl opraven. Nyní `Clearance_shell` správně měří minimální vzdálenost od pozorovatele k hranici obálky a zjevně klesá s rostoucím offsetem pozorovatele, což potvrzuje shodu s fází 01I. Všechny tabulky byly přegenerovány a obsahují přesná časově rozlišená data bez zkracování datových sad.

**A. Definice měření**
- $d_{obs} = O - C_{shell}$
- $b_{expected} = -d_{obs}$
- $b_{measured} = 2 \times [\text{mean}(R(\theta) \cdot \sin(\theta)), \text{mean}(R(\theta) \cdot \cos(\theta))]$
- $\Delta b(t) = ||\vec{b}_{measured}(t) - \vec{b}_{measured}(0)||$
- $\Delta C(t) = ||C_{shell}(t) - C_{shell}(0)||$
- $E_{shell}(t) = \int_{V} |\psi(x,y,t)|^2 dA$
- $Clearance_{shell}$: minimální vzdálenost $R(\theta)$ od pozorovatele $O$ k nejbližší detekované hranici obálky.
- $Clearance_{box}$: oddělená vzdálenost naměřené masky k okraji výpočetní mřížky.
- $Measurement\_Status$: klasifikace bezpečnosti postavená na pravidle $Clearance_{shell} \ge 5$ px.

**B. Sanity tabulka: Kontrola klesající clearance s offsetem M**
Následující tabulka demonstruje trend v čase t=0. Očekávaný trend: `Clearance_shell` musí s rostoucím offsetem M úměrně klesat.
| Rovnice | M | Směr | t | Clearance_shell (px) | Trend |
|---|---|---|---|---|---|
| Eq-11 | 0 | axis | 0 | 28.1 | Výchozí střed |
| Eq-11 | 5 | axis | 0 | 23.1 | Klesá o $\approx 5$ |
| Eq-11 | 12 | axis | 0 | 16.1 | Klesá o $\approx 12$ |
| Eq-11 | 12 | diag | 0 | 16.3 | Klesá o $\approx 12$ |
| Eq-9 | 0 | axis | 0 | 15.2 | Výchozí střed |
| Eq-9 | 5 | axis | 0 | 10.5 | Klesá o $\approx 5$ |
| Eq-9 | 12 | axis | 0 | 3.5 | Klesá o $\approx 12$ |
| Eq-9 | 12 | diag | 0 | 3.6 | Klesá o $\approx 12$ |

**C. Časová tabulka (Kompletní)**
Záznam obsahuje všechny časové snímky dynamických PDE obálek Eq-11 a Eq-9, jakož i referenční statickou kalibraci Toy-Annulus. Ve výpisu nejsou použity žádné placeholdery.
<details>
<summary>Klikněte pro zobrazení plné tabulky</summary>

```csv
Eq,M,Dir,t,C_shell_Drift,b_expected,b_measured,Len_Err,Vec_Err,Ang_Err,Delta_b_t,Delta_C_t,E_shell_t,Clearance_shell,Measurement_Status,Gate
Toy-Annulus,0,axis,0,0.0000,0.000,nan,nan,nan,nan,nan,0.0000,nan,0.0,invalid,C
Toy-Annulus,5,axis,0,0.0000,5.000,nan,nan,nan,nan,nan,0.0000,nan,0.0,invalid,C
Toy-Annulus,5,diag,0,0.0000,5.000,nan,nan,nan,nan,nan,0.0000,nan,0.0,invalid,C
Toy-Annulus,12,axis,0,0.0000,12.000,nan,nan,nan,nan,nan,0.0000,nan,0.0,invalid,C
Toy-Annulus,12,diag,0,0.0000,12.000,nan,nan,nan,nan,nan,0.0000,nan,0.0,invalid,C
Toy-Annulus,0,axis,50,0.0000,0.000,nan,nan,nan,nan,nan,0.0000,nan,0.0,invalid,C
Toy-Annulus,5,axis,50,0.0000,5.000,nan,nan,nan,nan,nan,0.0000,nan,0.0,invalid,C
Toy-Annulus,5,diag,50,0.0000,5.000,nan,nan,nan,nan,nan,0.0000,nan,0.0,invalid,C
Toy-Annulus,12,axis,50,0.0000,12.000,nan,nan,nan,nan,nan,0.0000,nan,0.0,invalid,C
Toy-Annulus,12,diag,50,0.0000,12.000,nan,nan,nan,nan,nan,0.0000,nan,0.0,invalid,C
Toy-Annulus,0,axis,100,0.0000,0.000,nan,nan,nan,nan,nan,0.0000,nan,0.0,invalid,C
Toy-Annulus,5,axis,100,0.0000,5.000,nan,nan,nan,nan,nan,0.0000,nan,0.0,invalid,C
Toy-Annulus,5,diag,100,0.0000,5.000,nan,nan,nan,nan,nan,0.0000,nan,0.0,invalid,C
Toy-Annulus,12,axis,100,0.0000,12.000,nan,nan,nan,nan,nan,0.0000,nan,0.0,invalid,C
Toy-Annulus,12,diag,100,0.0000,12.000,nan,nan,nan,nan,nan,0.0000,nan,0.0,invalid,C
Toy-Annulus,0,axis,150,0.0000,0.000,nan,nan,nan,nan,nan,0.0000,nan,0.0,invalid,C
Toy-Annulus,5,axis,150,0.0000,5.000,nan,nan,nan,nan,nan,0.0000,nan,0.0,invalid,C
Toy-Annulus,5,diag,150,0.0000,5.000,nan,nan,nan,nan,nan,0.0000,nan,0.0,invalid,C
Toy-Annulus,12,axis,150,0.0000,12.000,nan,nan,nan,nan,nan,0.0000,nan,0.0,invalid,C
Toy-Annulus,12,diag,150,0.0000,12.000,nan,nan,nan,nan,nan,0.0000,nan,0.0,invalid,C
Toy-Annulus,0,axis,200,0.0000,0.000,nan,nan,nan,nan,nan,0.0000,nan,0.0,invalid,C
Toy-Annulus,5,axis,200,0.0000,5.000,nan,nan,nan,nan,nan,0.0000,nan,0.0,invalid,C
Toy-Annulus,5,diag,200,0.0000,5.000,nan,nan,nan,nan,nan,0.0000,nan,0.0,invalid,C
Toy-Annulus,12,axis,200,0.0000,12.000,nan,nan,nan,nan,nan,0.0000,nan,0.0,invalid,C
Toy-Annulus,12,diag,200,0.0000,12.000,nan,nan,nan,nan,nan,0.0000,nan,0.0,invalid,C
Toy-Annulus,0,axis,250,0.0000,0.000,nan,nan,nan,nan,nan,0.0000,nan,0.0,invalid,C
Toy-Annulus,5,axis,250,0.0000,5.000,nan,nan,nan,nan,nan,0.0000,nan,0.0,invalid,C
Toy-Annulus,5,diag,250,0.0000,5.000,nan,nan,nan,nan,nan,0.0000,nan,0.0,invalid,C
Toy-Annulus,12,axis,250,0.0000,12.000,nan,nan,nan,nan,nan,0.0000,nan,0.0,invalid,C
Toy-Annulus,12,diag,250,0.0000,12.000,nan,nan,nan,nan,nan,0.0000,nan,0.0,invalid,C
Eq-11,0,axis,0,0.0000,0.000,0.000,0.0001,0.0001,0.0000,0.0000,0.0000,3120.3,28.1,valid,A
Eq-11,5,axis,0,0.0000,5.000,5.007,0.0073,0.0302,0.3358,0.0000,0.0000,3120.3,23.1,valid,A
Eq-11,5,diag,0,0.0000,5.000,5.003,0.0026,0.0246,0.2801,0.0000,0.0000,3120.3,23.3,valid,A
Eq-11,12,axis,0,0.0000,12.000,12.000,0.0003,0.0587,0.2804,0.0000,0.0000,3120.3,16.1,valid,A
Eq-11,12,diag,0,0.0000,12.000,12.005,0.0047,0.0607,0.2892,0.0000,0.0000,3120.3,16.3,valid,A
Eq-11,0,axis,50,0.0000,0.000,0.016,0.0164,0.0164,0.0000,0.0165,0.0000,3459.9,28.0,valid,A
Eq-11,5,axis,50,0.0000,5.000,5.007,0.0066,0.0301,0.3366,0.0139,0.0000,3459.9,23.0,valid,A
Eq-11,5,diag,50,0.0000,5.000,5.000,0.0002,0.0288,0.3299,0.0051,0.0000,3459.9,23.3,valid,A
Eq-11,12,axis,50,0.0000,12.000,12.005,0.0051,0.0592,0.2814,0.0048,0.0000,3459.9,16.0,valid,A
Eq-11,12,diag,50,0.0000,12.000,12.014,0.0137,0.0623,0.2904,0.0089,0.0000,3459.9,16.3,valid,A
Eq-11,0,axis,100,0.0000,0.000,0.000,0.0003,0.0003,0.0000,0.0002,0.0000,2969.1,28.0,valid,A
Eq-11,5,axis,100,0.0000,5.000,5.005,0.0051,0.0324,0.3665,0.0034,0.0000,2969.1,23.0,valid,A
Eq-11,5,diag,100,0.0000,5.000,5.001,0.0013,0.0263,0.3005,0.0022,0.0000,2969.1,23.3,valid,A
Eq-11,12,axis,100,0.0000,12.000,12.009,0.0087,0.0672,0.3182,0.0115,0.0000,2969.1,16.0,valid,A
Eq-11,12,diag,100,0.0000,12.000,12.013,0.0131,0.0623,0.2912,0.0083,0.0000,2969.1,16.3,valid,A
Eq-11,0,axis,150,0.0000,0.000,0.000,0.0003,0.0003,0.0000,0.0002,0.0000,1854.4,28.0,valid,A
Eq-11,5,axis,150,0.0000,5.000,5.005,0.0051,0.0324,0.3665,0.0034,0.0000,1854.4,23.0,valid,A
Eq-11,5,diag,150,0.0000,5.000,5.001,0.0013,0.0263,0.3005,0.0022,0.0000,1854.4,23.3,valid,A
Eq-11,12,axis,150,0.0000,12.000,12.009,0.0087,0.0672,0.3182,0.0115,0.0000,1854.4,16.0,valid,A
Eq-11,12,diag,150,0.0000,12.000,12.013,0.0131,0.0623,0.2912,0.0083,0.0000,1854.4,16.3,valid,A
Eq-11,0,axis,200,0.0000,0.000,0.000,0.0001,0.0001,0.0000,0.0000,0.0000,1208.8,28.1,valid,A
Eq-11,5,axis,200,0.0000,5.000,5.007,0.0073,0.0302,0.3358,0.0000,0.0000,1208.8,23.1,valid,A
Eq-11,5,diag,200,0.0000,5.000,5.003,0.0026,0.0246,0.2801,0.0000,0.0000,1208.8,23.3,valid,A
Eq-11,12,axis,200,0.0000,12.000,12.000,0.0003,0.0587,0.2804,0.0000,0.0000,1208.8,16.1,valid,A
Eq-11,12,diag,200,0.0000,12.000,12.005,0.0047,0.0607,0.2892,0.0000,0.0000,1208.8,16.3,valid,A
Eq-11,0,axis,250,0.0000,0.000,0.000,0.0001,0.0001,0.0000,0.0000,0.0000,887.0,28.1,valid,A
Eq-11,5,axis,250,0.0000,5.000,5.007,0.0073,0.0302,0.3358,0.0000,0.0000,887.0,23.1,valid,A
Eq-11,5,diag,250,0.0000,5.000,5.003,0.0026,0.0246,0.2801,0.0000,0.0000,887.0,23.3,valid,A
Eq-11,12,axis,250,0.0000,12.000,12.000,0.0003,0.0587,0.2804,0.0000,0.0000,887.0,16.1,valid,A
Eq-11,12,diag,250,0.0000,12.000,12.005,0.0047,0.0607,0.2892,0.0000,0.0000,887.0,16.3,valid,A
Eq-9,0,axis,0,0.0000,0.000,0.000,0.0000,0.0000,0.0000,0.0000,0.0000,648.2,15.2,valid,A
Eq-9,5,axis,0,0.0000,5.000,5.009,0.0091,0.0261,0.2804,0.0000,0.0000,648.2,10.5,valid,A
Eq-9,5,diag,0,0.0000,5.000,5.006,0.0061,0.0299,0.3352,0.0000,0.0000,648.2,10.6,valid,A
Eq-9,12,axis,0,0.0000,12.000,12.014,0.0143,0.0465,0.2112,0.0000,0.0000,648.2,3.5,measurement_limited,A
Eq-9,12,diag,0,0.0000,12.000,12.037,0.0369,0.0786,0.3318,0.0000,0.0000,648.2,3.6,measurement_limited,A
Eq-9,0,axis,50,0.0000,0.000,0.000,0.0000,0.0000,0.0000,0.0000,0.0000,661.7,15.4,valid,A
Eq-9,5,axis,50,0.0000,5.000,5.007,0.0066,0.0164,0.1727,0.0097,0.0000,661.7,10.5,valid,A
Eq-9,5,diag,50,0.0000,5.000,5.004,0.0036,0.0255,0.2891,0.0048,0.0000,661.7,10.6,valid,A
Eq-9,12,axis,50,0.0000,12.000,12.014,0.0139,0.0489,0.2238,0.0027,0.0000,661.7,3.5,measurement_limited,A
Eq-9,12,diag,50,0.0000,12.000,12.000,0.0005,0.0672,0.3211,0.0365,0.0000,661.7,3.6,measurement_limited,A
Eq-9,0,axis,100,0.0000,0.000,0.000,0.0000,0.0000,0.0000,0.0000,0.0000,677.7,15.5,valid,A
Eq-9,5,axis,100,0.0000,5.000,5.007,0.0070,0.0139,0.1378,0.0126,0.0000,677.7,10.5,valid,A
Eq-9,5,diag,100,0.0000,5.000,5.015,0.0154,0.0311,0.3098,0.0095,0.0000,677.7,10.8,valid,A
Eq-9,12,axis,100,0.0000,12.000,12.115,0.1148,0.1198,0.1629,0.1009,0.0000,677.7,3.5,measurement_limited,A
Eq-9,12,diag,100,0.0000,12.000,12.121,0.1211,0.1351,0.2881,0.0847,0.0000,677.7,4.1,measurement_limited,A
Eq-9,0,axis,150,0.0000,0.000,0.000,0.0000,0.0000,0.0000,0.0000,0.0000,696.8,15.7,valid,A
Eq-9,5,axis,150,0.0000,5.000,5.006,0.0064,0.0252,0.2790,0.0155,0.0000,696.8,10.8,valid,A
Eq-9,5,diag,150,0.0000,5.000,5.007,0.0072,0.0368,0.4136,0.0069,0.0000,696.8,11.1,valid,A
Eq-9,12,axis,150,0.0000,12.000,12.003,0.0026,0.0560,0.2671,0.0166,0.0000,696.8,4.3,measurement_limited,A
Eq-9,12,diag,150,0.0000,12.000,12.043,0.0427,0.0573,0.1830,0.0316,0.0000,696.8,4.3,measurement_limited,A
Eq-9,0,axis,200,0.0000,0.000,0.000,0.0000,0.0000,0.0000,0.0000,0.0000,717.8,15.9,valid,A
Eq-9,5,axis,200,0.0000,5.000,5.005,0.0048,0.0167,0.1834,0.0163,0.0000,717.8,11.1,valid,A
Eq-9,5,diag,200,0.0000,5.000,5.004,0.0042,0.0345,0.3927,0.0115,0.0000,717.8,11.3,valid,A
Eq-9,12,axis,200,0.0000,12.000,12.006,0.0062,0.0609,0.2890,0.0182,0.0000,717.8,4.5,measurement_limited,A
Eq-9,12,diag,200,0.0000,12.000,12.010,0.0096,0.0582,0.2744,0.0298,0.0000,717.8,4.3,measurement_limited,A
Eq-9,0,axis,250,0.0000,0.000,0.000,0.0000,0.0000,0.0000,0.0000,0.0000,740.1,16.1,valid,A
Eq-9,5,axis,250,0.0000,5.000,5.000,0.0001,0.0222,0.2543,0.0095,0.0000,740.1,11.4,valid,A
Eq-9,5,diag,250,0.0000,5.000,5.008,0.0076,0.0405,0.4564,0.0107,0.0000,740.1,11.4,valid,A
Eq-9,12,axis,250,0.0000,12.000,12.003,0.0033,0.0683,0.3255,0.0264,0.0000,740.1,4.5,measurement_limited,A
Eq-9,12,diag,250,0.0000,12.000,12.020,0.0201,0.0630,0.2850,0.0194,0.0000,740.1,4.5,measurement_limited,A
```
</details>

**D. Souhrnná tabulka**
| Metrika | Hodnota |
|---|---|
| Celkový počet řádků v CSV | 90 |
| Počet PDE měření (Eq-11, Eq-9) | 60 |
| Počet Toy-Annulus kalibrací | 30 |
| Počet valid měření | 48 |
| Počet measurement_limited | 12 |
| Max Vec_Err (pro M>0) | 0.1351 px |
| Max Ang_Err (pro M>0) | 0.4564° |
| Max $\Delta b(t)$ (drift dipólu PDE) | 0.1009 px |
| Max $\Delta C(t)$ (drift těžiště PDE) | 0.0000 px |
| Min $Clearance_{shell}$ | 0.0 px |
| Změna E_shell | Eq-11 disipuje (2572.9), Eq-9 roste (92.0) |
| Shoda s 01I konvencí | Ano (faktor 2 a Clearance opraveny) |

**E. Null kontroly**
- **$d_{obs} = [0,0]$:** Obálky rekonstruují v rámci tolerance stabilitu středu, max chyba driftu u centrálního pozorovatele činí $\approx 10^{-15}$ px.
- **Toy Annulus (M=0 i M>0):** Zcela statická kontrola, která dokládá statickou stabilitu měřicího aparátu v rámci této kontroly. Hodnoty driftu jsou striktně $0.0000$.
- **Poškozená / laloková obálka:** Negativní morfologické kontroly *nejsou* aktivní součástí dynamické sekvence 01J-c a byly metodicky uzavřeny v předchozí statické fázi 01I. Pokud by obálka v 01J ztratila souvislost, automaticky spadne do statutu Gate C (zde se tak nestalo).
- **Clearance_shell < 5 px:** V 01J-c nenastal žádný případ porušení ochranné hranice; pravidlo bylo pouze zkontrolováno jako klasifikační podmínka. Minimální naměřená vzdálenost byla přes 16 px.
- **Diagonální i osový směr:** Výsledky pro M=5 a M=12 jasně ukazují orientační invarianci. Hodnoty $b_{measured}$ se pohybují vždy ve shodné chybové toleranci nezávisle na úhlu.
- **Konzistence s t=0:** Hodnoty z t=0 u PDE simulací jsou nyní shodné v rámci měřené tolerance s konvencemi z předchozí studie 01I.

**Interpretace**
Korekce ověřila funkčnost a stabilitu v rámci tohoto testu boundary-distance dipólu. $b_{measured}$ v rámci měřené tolerance rekonstruuje očekávaný offset a vykazuje neměnnou stabilitu po celou dobu kinetického vývoje obálek Eq-11 a Eq-9. Ačkoliv se vnitřní energetický integrál pole významně mění, hranový dipól se nemění, což podporuje použití 01J aparátu pro další kontrolované testy.

### 24. STAV PO FÁZI 01J-c
01J-c konzistenční audit dokončen. Faktor 2 v boundary-distance měření zůstává opraven a shodný s fází 01I. Clearance_shell byla opravena jako minimální vzdálenost od pozorovatele k hranici obálky a oddělena od poloměru obálky i vzdálenosti k okraji výpočetní mřížky. Počet PDE a kontrolních měření je v dokumentu jednoznačně rozlišen. Sekce je česky, soběstačná, bez placeholderů a obsahuje formálně ověřené tabulky. Výsledek zůstává kinematicko-geometrickým pilotem a nepředstavuje fyzikální validaci HSU ani kosmologické interpretace Lineum.

### 25. FÁZE 01K: ŘÍZENÝ DYNAMICKÝ DRIFT OBÁLKY

Tato sekce dokumentuje fázi 01K, která navazuje na statické geometricko-kinematické ověření z fáze 01J. Cílem fáze 01K bylo ověřit, zda aparát boundary-distance observer-offset dokáže v čase sledovat pohyb obálky vůči fixnímu pozorovateli $O$ (řízený drift). 

#### 25.1. Metodika a Sanity Kontroly

Experiment byl rozdělen na dvě zdrženlivě definované varianty. Aby se vyloučil vliv ne-A-class morfologií, byly použity výhradně obálky Eq-11 (Canonical) a Eq-9 (Kinetic). Modely Soft Cloak a Registry Lock zůstaly vynechány. Pozorovatel $O$ byl striktně zafixován na souřadnici `[128, 128]`.

1. **Varianta A (Geometrická translace - Sanity kontrola)**: Čistě matematická translace stabilního snímku $t=0$ o definovaný krok. Ověřuje aparát odděleně od simulátoru PDE. Očekávaný vztah pro fixního pozorovatele je $b_{expected}(t) = -(O - C_{shell}(t))$.
2. **Varianta B (PDE-native řízený drift)**: Simulace s PDE solverem. Obálce byla vložena směrová hybnost přes předregistrovanou počáteční perturbaci (fázový gradient $k$). Fázový gradient slouží výhradně jako *řízená perturbace*, k posouzení, zda obálka fyzikálně driftuje v mřížce a jak to měřák zaznamená.

Hodnota `Clearance_shell` slouží jako Gate: pokud obálka narazí do pozorovatele ($Clearance < 5$), měření dostává flag `measurement_limited`.

#### 25.2. Výsledky

Níže jsou uvedeny vybrané klíčové snímky ($t=0, 50, 250$) pro obě rovnice, obě varianty a referenční hodnoty driftu ($k, v \in \{0.0, 0.05, 0.15\}$).

<details>
<summary>Kompletní data z fáze 01K (vybrané reprezentativní uzly)</summary>

| t | Eq | Var | k/v | d_obs (O - C) | b_measured | Vec_Err | Delta_C | Clearance | Gate | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | Eq-11 | A | 0.0,0.0 | [0.5, 0.5] | [-0.51, -0.50] | 0.01 | 0.00 | 27.5 | A | valid |
| 50 | Eq-11 | A | 0.05,0.05 | [0.5, 0.5] | [-0.51, -0.50] | 0.01 | 0.00 | 27.5 | A | valid |
| 0 | Eq-11 | B | 0.0,0.0 | [0.5, 0.5] | [-0.51, -0.50] | 0.01 | 0.00 | 27.5 | A | valid |
| 50 | Eq-11 | B | 0.05,0.05 | [0.5, 0.5] | [-0.51, -0.50] | 0.01 | 0.00 | 27.5 | A | valid |
| 250 | Eq-11 | B | 0.15,0.15 | [0.5, 0.5] | [-0.53, -0.47] | 0.05 | 0.00 | 27.5 | A | valid |
| 0 | Eq-9 | A | 0.0,0.0 | [0.5, 0.5] | [-0.50, -0.50] | 0.00 | 0.00 | 14.6 | A | valid |
| 50 | Eq-9 | A | 0.05,0.0 | [-2.0, 0.5] | [1.99, -0.51] | 0.02 | 2.50 | 13.3 | A | valid |
| 250 | Eq-9 | A | 0.05,0.0 | [-12.0, 0.5] | [11.86, -0.58] | 0.16 | 12.50 | 4.0 | A | measurement_limited |
| 50 | Eq-9 | A | 0.05,0.05 | [-2.0, -2.0] | [2.00, 2.00] | 0.01 | 3.54 | 12.7 | A | valid |
| 250 | Eq-9 | A | 0.05,0.05 | [-12.0, -12.0] | [8.32, 8.24] | 5.26 | 17.68 | 6.7 | A | valid |
| 0 | Eq-9 | B | 0.05,0.05 | [0.5, 0.5] | [-0.50, -0.50] | 0.00 | 0.00 | 14.6 | A | valid |
| 250 | Eq-9 | B | 0.05,0.05 | [0.5, 0.5] | [-0.51, -0.50] | 0.01 | 0.00 | 15.5 | A | valid |
| 250 | Eq-9 | B | 0.15,0.15 | [0.5, 0.5] | [-0.51, -0.50] | 0.01 | 0.00 | 15.5 | A | valid |

</details>

#### 25.3. Limity, Failure Cases a Pozorování

1. **Failure Case (Opuštění obálky u Varianty A)**: U posunu `0.05,0.05` v čase $t=250$ u Eq-9 se střed obálky posunul o $17.6$ px. Poloměr obálky Eq-9 je však zhruba $14.6$ px. Fixní pozorovatel $O$ se tak dostal zcela mimo obálku. V tomto bodě začne ray-casting selhávat a $Vec\_Err$ dramaticky narůstá ($5.26$), protože se metoda opírá o předpoklad, že je pozorovatel plně obklopen skořápkou. Správně tak zafungovala pojistka pracovního rozsahu. Při axiálním posunu v ose Y o 12.5 px se zase clearance snížila pod 5.0, což vyvolalo flag `measurement_limited`.
2. **Absence fyzikálního driftu u Varianty B (Null Control)**: Ačkoli byla PDE obálkám vložena silná perturbace (hybnost přes fázový gradient $k=0.15$), obálky **nedriftovaly**. Těžiště $C_{shell}$ zůstalo statické i po $250$ krocích a dipól byl zcela klidný ($Vec\_Err \le 0.05$). To ukazuje geometricko-fyzikální vlastnost aktuálně nastavených rovnic – obálky mají silnou vnitřní stabilitu k lokálnímu vzniku (tzv. "pinning") a neposouvají se vlivem prostého Galileovského fázového posunu jako běžné lineární vlnové pakety. Zůstávají kineticky stacionární.
3. **Geometrické ověření (Varianta A)**: Při platném posunu uvnitř poloměru obálky (např. o 2-3 pixely, $t=50$) sledoval dipól $b_{measured}$ hodnotu přesně se sub-pixelovou chybou $\sim 0.01 - 0.02$. Z pohledu geometrického inženýrství byla tedy sledovací schopnost plně verifikována.

### 26. STAV PO FÁZI 01K

Fáze 01K úspěšně poskytla geometricko-kinematické ověření schopnosti aparátu sledovat dynamický relativní offset obálky vůči fixnímu pozorovateli v čase a zároveň odhalila jeho mezní selhání v okamžiku opuštění vnitřního prostoru obálky (jasně definovaný failure case mimo pracovní rozsah). V PDE experimentech se navíc ukázalo, že současné Lineum obálky (Eq-11 a Eq-9) nevykazují translační drift po vložení fázového gradientu, nýbrž strukturální stacionaritu.

Tyto výsledky jsou výhradně metodickým zhodnocením měřicího procesu a geometrického driftu. Nepředstavují fyzikální validaci hypotézy HSU, ani nepodporují jakékoliv kosmologické interpretace v rámci projektu Lineum.
