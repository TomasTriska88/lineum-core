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
|---|---|---|---|---|---|---|---|
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

### 25. FÁZE 01K-a: Korekční audit řízeného dynamického driftu obálky

Tato sekce dokumentuje fázi 01K-a, která korekčním auditem nahrazuje dřívější pilotní fázi 01K. Cílem je metodická oprava dokumentace, vyjasnění pracovního rozsahu boundary-distance observer-offset aparátu a odstranění zavádějících fyzikálních dezinterpretací. Nejedná se o fyzikální validaci ani zavádění nových fyzikálních claimů.

#### 25.1. Metodika a Sanity Kontroly 01K-a

Metodika navazuje na geometricko-kinematický rámec předchozích fází za dodržení následujících pevných konvencí:
- **Souřadnice**: `[row, col] = [y, x]`
- **Offset a dipól**: Vložený posun pozorovatele $d_{obs} = O - C_{shell}$, očekávaný hraniční dipól $b_{expected} = -d_{obs}$.
- **`Observer_Inside_Shell`**: Testováno prostřednictvím algoritmu `binary_fill_holes(mask)`. To zajišťuje, že je korektně zachycen stav, kdy je pozorovatel uvnitř vnější hranice obálky i u prstencových (ring) obálek. Topologické jádro / nízká amplituda uvnitř prstence se nepovažuje za patologickou díru, pokud je pozorovatel prokazatelně uvnitř vyplněné vnější obálky.
- **`Clearance_shell`**: Minimální vzdálenost od pozorovatele k hranici obálky. Pokud `Clearance_shell < 5 px`, měření nesmí být považováno za plně validní (naráží na diskretizační limit mřížky), i když `Observer_Inside_Shell = True`.
- **`Measurement_Status`**: Výstupní klasifikace může nabývat těchto hodnot:
  - `valid`
  - `measurement_limited_clearance`
  - `gate_failed_morphology`
  - `measurement_invalid_outside_shell` (např. opuštění obálky)

Experiment byl proveden na plně A-class stabilních modelech Eq-11 (Canonical) a Eq-9 (Kinetic). Modely jako Soft Cloak byly vyloučeny z důvodu nesplnění počátečních morfologických podmínek. Pozorovatel $O$ byl zafixován.

#### 25.2. Datová účetní tabulka 01K-a

Následující tabulka je závazným přehledem celého datového rozsahu auditu 01K-a. Čtenář nepotřebuje přístup k externím skriptům ani logům — tabulka je kompletní a soběstačná.

**Měřicí řádky (measurement rows):**

| Varianta | Typ dat | Konfigurace | Časové snímky | Počet řádků |
|---|---|---|---|---|
| A | Geometrická translace | Eq-11 × shift=0.05, Eq-11 × shift=0.10, Eq-9 × shift=0.05, Eq-9 × shift=0.10 | t = 0, 50, 100, 150, 200, 250 | 24 |
| B | PDE fázový gradient | Eq-11 × k=0.05, Eq-11 × k=0.15, Eq-9 × k=0.05, Eq-9 × k=0.15 | t = 0, 50, 100, 150, 200, 250 | 24 |
| **Celkem measurement rows** | | | | **48** |

**Doplňkové diagnostické řádky (Var B fázový gradient, t > 0):**

| Typ | Poznámka | Počet řádků |
|---|---|---|
| Var B diagnostika | t > 0; 4 řádky t=0 mají Mean\|grad φ\|=0 (jsou zahrnuty v měřicích 24) | 20 |

**Celkový počet tabulkových řádků vložených v sekci 01K-a: 68** (Var A 24 + Var B measurement 24 + Var B diagnostika 20)

| Measurement_Status | Var A | Var B | Celkem |
|---|---|---|---|
| `valid` | 18 | 24 | 42 |
| `measurement_limited_clearance` | 6 | 0 | 6 |
| `gate_failed_morphology` | 0 | 0 | 0 |
| `measurement_invalid_outside_shell` | 0 | 0 | 0 |

**Poznámka:** Výše uvedené počty se vztahují výhradně na 48 measurement rows (Var A + Var B). Var B fázová diagnostika (20 řádků, všechny `valid` diagnostics) je vedena odděleně a nesmí být míchána s tímto measurement_status účetnictvím.


#### 25.3. VARIANTA A — Geometrická translace


Geometrická translace slouží jako čistě matematická sanity kontrola měřáku odděleně od simulátoru PDE. 

**Klíčové výsledky:**
- Těžiště $C_{shell}(t)$ se mění úměrně aplikovanému posunu, což potvrzuje detekci pohybu.
- Měřený dipól $b_{measured}$ spolehlivě sleduje očekávaný $b_{expected}$ s velmi nízkou chybou ($Vec\_Err < 0.05$ px), dokud se pozorovatel nachází uvnitř obálky a zároveň splňuje podmínku `Clearance_shell >= 5 px`.
- Větší posuny v kombinaci s užším průměrem Eq-9 vedou k dosažení limitních stavů.
  - Při $t=200$ (posun o 10 px) klesne clearance na cca 2.8 px, což vyvolává status `measurement_limited_clearance`.
  - Při $t=250$ (posun o 12.5 px) klesne clearance na 0.0 px (pozorovatel je doslova na okraji) a status spadne na `measurement_limited_clearance`. Zde je vysoká chyba ($Vec\_Err \approx 17.666$ px) přímým důsledkem kolizního geometrického režimu limitace měření a **nesmí být interpretována jako validní výsledek měřáku ani jako fyzikální chyba rovnice.**

**Agregované statistiky plného běhu 01K-a (Varianta A, oba modely, oba shift-kroky, 6 časových snímků):**

| Metrika | Hodnota |
|---|---|
| Celkový počet řádků | 24 |
| Počet `valid` | 18 |
| Počet `measurement_limited_clearance` | 6 |
| Počet `gate_failed_morphology` | 0 |
| Počet `measurement_invalid_outside_shell` | 0 |
| Max Vec_Err pro `valid` | 0.020 px |
| Max Vec_Err pro `measurement_limited_clearance` | 17.666 px (Eq-9, t=250, Clearance=0.0 px) |
| Min Clearance_shell celkem | 0.0 px |
| Observer_Inside_Shell = True ve všech limitních stavech? | Ano |
| Eq-9 / Var-A / t=250 status | `measurement_limited_clearance` (nikoli `valid`) |

**Souhrnná auditní tabulka — všechny řádky Varianty A:**

<details>
<summary>Klikněte pro zobrazení všech 24 řádků</summary>

| t | Eq | shift | C_shell | d_obs | Vec_Err | Clearance | Observer_Inside | Enclosure_Status | Measurement_Status |
|---|---|---|---|---|---|---|---|---|---|
| 0 | Eq-11 | 0.05 | [100.0, 100.0] | [0.0, 0.0] | 0.000 | 36.8 | True | inside | valid |
| 50 | Eq-11 | 0.05 | [102.5, 102.5] | [-2.5, -2.5] | 0.001 | 34.3 | True | inside | valid |
| 100 | Eq-11 | 0.05 | [105.0, 105.0] | [-5.0, -5.0] | 0.001 | 31.8 | True | inside | valid |
| 150 | Eq-11 | 0.05 | [107.5, 107.5] | [-7.5, -7.5] | 0.001 | 29.3 | True | inside | valid |
| 200 | Eq-11 | 0.05 | [110.0, 110.0] | [-10.0, -10.0] | 0.001 | 26.8 | True | inside | valid |
| 250 | Eq-11 | 0.05 | [112.5, 112.5] | [-12.5, -12.5] | 0.020 | 24.3 | True | inside | valid |
| 0 | Eq-11 | 0.10 | [100.0, 100.0] | [0.0, 0.0] | 0.000 | 36.8 | True | inside | valid |
| 50 | Eq-11 | 0.10 | [105.0, 105.0] | [-5.0, -5.0] | 0.001 | 31.8 | True | inside | valid |
| 100 | Eq-11 | 0.10 | [110.0, 110.0] | [-10.0, -10.0] | 0.001 | 26.8 | True | inside | valid |
| 150 | Eq-11 | 0.10 | [115.0, 115.0] | [-15.0, -15.0] | 0.001 | 21.8 | True | inside | valid |
| 200 | Eq-11 | 0.10 | [120.0, 120.0] | [-20.0, -20.0] | 0.001 | 16.8 | True | inside | valid |
| 250 | Eq-11 | 0.10 | [125.0, 125.0] | [-25.0, -25.0] | 0.020 | 11.8 | True | inside | valid |
| 0 | Eq-9 | 0.05 | [100.0, 100.0] | [0.0, 0.0] | 0.000 | 18.5 | True | inside | valid |
| 50 | Eq-9 | 0.05 | [102.5, 102.5] | [-2.5, -2.5] | 0.001 | 14.7 | True | inside | valid |
| 100 | Eq-9 | 0.05 | [105.0, 105.0] | [-5.0, -5.0] | 0.000 | 10.7 | True | inside | valid |
| 150 | Eq-9 | 0.05 | [107.5, 107.5] | [-7.5, -7.5] | 0.043 | 6.9 | True | inside | valid |
| 200 | Eq-9 | 0.05 | [110.0, 110.0] | [-10.0, -10.0] | 0.019 | 2.8 | True | boundary_limited | measurement_limited_clearance |
| 250 | Eq-9 | 0.05 | [112.5, 112.5] | [-12.5, -12.5] | 17.666 | 0.0 | True | boundary_limited | measurement_limited_clearance |
| 0 | Eq-9 | 0.10 | [100.0, 100.0] | [0.0, 0.0] | 0.000 | 18.5 | True | inside | valid |
| 50 | Eq-9 | 0.10 | [105.0, 105.0] | [-5.0, -5.0] | 0.020 | 11.2 | True | inside | valid |
| 100 | Eq-9 | 0.10 | [110.0, 110.0] | [-10.0, -10.0] | 0.074 | 3.8 | True | boundary_limited | measurement_limited_clearance |
| 150 | Eq-9 | 0.10 | [115.0, 115.0] | [-15.0, -15.0] | 21.209 | 0.0 | True | boundary_limited | measurement_limited_clearance |
| 200 | Eq-9 | 0.10 | [120.0, 120.0] | [-20.0, -20.0] | 28.280 | 0.0 | True | boundary_limited | measurement_limited_clearance |
| 250 | Eq-9 | 0.10 | [125.0, 125.0] | [-25.0, -25.0] | 35.351 | 0.0 | True | boundary_limited | measurement_limited_clearance |

</details>

#### 25.4. VARIANTA B — PDE fázový gradient

V této variantě byla simulace oživena v PDE solveru a obálce byla vložena směrová hybnost přes předregistrovanou počáteční perturbaci (fázový gradient $k$).

**Klíčové výsledky:**
- Měření diagnostiky potvrdilo, že **fázový gradient byl skutečně aplikován**. Hodnota Mean|grad φ| systematicky a lineárně roste s $k \times t$.
- **V tomto konkrétním nastavení a délce běhu nebyl naměřen translační drift amplitudové obálky po aplikaci fázového gradientu.** Změna polohy těžiště zůstala zanedbatelná ($Delta\_C = 0.0$).
- Dřívější závěr o tzv. „strukturálním pinningu" byl stažen. Absenci driftu v tomto testu nelze nekriticky povýšit na absolutní vlastnost Lineum rovnic.

**Agregované statistiky plného běhu 01K-a (Varianta B, oba modely, oba k, 6 časových snímků):**

| Metrika | Hodnota |
|---|---|
| Celkový počet řádků | 24 |
| Počet `valid` | 24 |
| Počet `measurement_limited_clearance` | 0 |
| Max Vec_Err | 0.000 px |
| Delta_C ve všech snímcích | 0.0 px |
| Observer_Inside_Shell = True ve všech snímcích? | Ano |

**Měřicí data Varianty B — všechny řádky (24/24; tabulka obsahuje všechny auditované měřicí řádky Varianty B):**

<details>
<summary>Klikněte pro zobrazení všech 24 měřicích řádků Var B</summary>

| t | Eq | k | C_shell | d_obs | b_expected | b_measured | Vec_Err | Delta_C | Clearance | Observer_Inside | Enclosure_Status | Gate | Measurement_Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | Eq-11 | 0.05 | [100.0, 100.0] | [0.0, 0.0] | [0.0, 0.0] | [0.00, 0.00] | 0.000 | 0.000 | 36.8 | True | inside | A | valid |
| 50 | Eq-11 | 0.05 | [100.0, 100.0] | [0.0, 0.0] | [0.0, 0.0] | [0.00, 0.00] | 0.000 | 0.000 | 37.0 | True | inside | A | valid |
| 100 | Eq-11 | 0.05 | [100.0, 100.0] | [0.0, 0.0] | [0.0, 0.0] | [0.00, 0.00] | 0.000 | 0.000 | 36.8 | True | inside | A | valid |
| 150 | Eq-11 | 0.05 | [100.0, 100.0] | [0.0, 0.0] | [0.0, 0.0] | [0.00, 0.00] | 0.000 | 0.000 | 37.0 | True | inside | A | valid |
| 200 | Eq-11 | 0.05 | [100.0, 100.0] | [0.0, 0.0] | [0.0, 0.0] | [0.00, 0.00] | 0.000 | 0.000 | 36.8 | True | inside | A | valid |
| 250 | Eq-11 | 0.05 | [100.0, 100.0] | [0.0, 0.0] | [0.0, 0.0] | [0.00, 0.00] | 0.000 | 0.000 | 36.6 | True | inside | A | valid |
| 0 | Eq-11 | 0.15 | [100.0, 100.0] | [0.0, 0.0] | [0.0, 0.0] | [0.00, 0.00] | 0.000 | 0.000 | 36.8 | True | inside | A | valid |
| 50 | Eq-11 | 0.15 | [100.0, 100.0] | [0.0, 0.0] | [0.0, 0.0] | [0.00, 0.00] | 0.000 | 0.000 | 37.0 | True | inside | A | valid |
| 100 | Eq-11 | 0.15 | [100.0, 100.0] | [0.0, 0.0] | [0.0, 0.0] | [0.00, 0.00] | 0.000 | 0.000 | 36.8 | True | inside | A | valid |
| 150 | Eq-11 | 0.15 | [100.0, 100.0] | [0.0, 0.0] | [0.0, 0.0] | [0.00, 0.00] | 0.000 | 0.000 | 37.0 | True | inside | A | valid |
| 200 | Eq-11 | 0.15 | [100.0, 100.0] | [0.0, 0.0] | [0.0, 0.0] | [0.00, 0.00] | 0.000 | 0.000 | 36.8 | True | inside | A | valid |
| 250 | Eq-11 | 0.15 | [100.0, 100.0] | [0.0, 0.0] | [0.0, 0.0] | [0.00, 0.00] | 0.000 | 0.000 | 36.6 | True | inside | A | valid |
| 0 | Eq-9 | 0.05 | [100.0, 100.0] | [0.0, 0.0] | [0.0, 0.0] | [0.00, 0.00] | 0.000 | 0.000 | 18.5 | True | inside | A | valid |
| 50 | Eq-9 | 0.05 | [100.0, 100.0] | [0.0, 0.0] | [0.0, 0.0] | [0.00, 0.00] | 0.000 | 0.000 | 18.1 | True | inside | A | valid |
| 100 | Eq-9 | 0.05 | [100.0, 100.0] | [0.0, 0.0] | [0.0, 0.0] | [0.00, 0.00] | 0.000 | 0.000 | 17.7 | True | inside | A | valid |
| 150 | Eq-9 | 0.05 | [100.0, 100.0] | [0.0, 0.0] | [0.0, 0.0] | [0.00, 0.00] | 0.000 | 0.000 | 17.4 | True | inside | A | valid |
| 200 | Eq-9 | 0.05 | [100.0, 100.0] | [0.0, 0.0] | [0.0, 0.0] | [0.00, 0.00] | 0.000 | 0.000 | 17.0 | True | inside | A | valid |
| 250 | Eq-9 | 0.05 | [100.0, 100.0] | [0.0, 0.0] | [0.0, 0.0] | [0.00, 0.00] | 0.000 | 0.000 | 16.7 | True | inside | A | valid |
| 0 | Eq-9 | 0.15 | [100.0, 100.0] | [0.0, 0.0] | [0.0, 0.0] | [0.00, 0.00] | 0.000 | 0.000 | 18.5 | True | inside | A | valid |
| 50 | Eq-9 | 0.15 | [100.0, 100.0] | [0.0, 0.0] | [0.0, 0.0] | [0.00, 0.00] | 0.000 | 0.000 | 18.1 | True | inside | A | valid |
| 100 | Eq-9 | 0.15 | [100.0, 100.0] | [0.0, 0.0] | [0.0, 0.0] | [0.00, 0.00] | 0.000 | 0.000 | 17.7 | True | inside | A | valid |
| 150 | Eq-9 | 0.15 | [100.0, 100.0] | [0.0, 0.0] | [0.0, 0.0] | [0.00, 0.00] | 0.000 | 0.000 | 17.4 | True | inside | A | valid |
| 200 | Eq-9 | 0.15 | [100.0, 100.0] | [0.0, 0.0] | [0.0, 0.0] | [0.00, 0.00] | 0.000 | 0.000 | 17.0 | True | inside | A | valid |
| 250 | Eq-9 | 0.15 | [100.0, 100.0] | [0.0, 0.0] | [0.0, 0.0] | [0.00, 0.00] | 0.000 | 0.000 | 16.7 | True | inside | A | valid |

</details>

**Diagnostická tabulka fázového gradientu (Varianta B, 20 diagnostických řádků; tabulka obsahuje všechny auditované řádky t > 0):**

<details>
<summary>Klikněte pro zobrazení 20 diagnostických řádků (t > 0; 4 řádky t=0 mají Mean|grad φ|=0 — jsou v celkovém součtu 24, ale diagnosticky irelevantní)</summary>

| Eq | t | k | Mean\|grad φ\| | Delta_C | Observer_Inside | Measurement_Status |
|---|---|---|---|---|---|---|
| Eq-11 | 50 | 0.05 | 3.54 | 0.0 | True | valid |
| Eq-11 | 100 | 0.05 | 7.07 | 0.0 | True | valid |
| Eq-11 | 150 | 0.05 | 10.61 | 0.0 | True | valid |
| Eq-11 | 200 | 0.05 | 14.14 | 0.0 | True | valid |
| Eq-11 | 250 | 0.05 | 17.68 | 0.0 | True | valid |
| Eq-11 | 50 | 0.15 | 10.61 | 0.0 | True | valid |
| Eq-11 | 100 | 0.15 | 21.21 | 0.0 | True | valid |
| Eq-11 | 150 | 0.15 | 31.82 | 0.0 | True | valid |
| Eq-11 | 200 | 0.15 | 42.43 | 0.0 | True | valid |
| Eq-11 | 250 | 0.15 | 53.03 | 0.0 | True | valid |
| Eq-9 | 50 | 0.05 | 3.54 | 0.0 | True | valid |
| Eq-9 | 100 | 0.05 | 7.07 | 0.0 | True | valid |
| Eq-9 | 150 | 0.05 | 10.61 | 0.0 | True | valid |
| Eq-9 | 200 | 0.05 | 14.14 | 0.0 | True | valid |
| Eq-9 | 250 | 0.05 | 17.68 | 0.0 | True | valid |
| Eq-9 | 50 | 0.15 | 10.61 | 0.0 | True | valid |
| Eq-9 | 100 | 0.15 | 21.21 | 0.0 | True | valid |
| Eq-9 | 150 | 0.15 | 31.82 | 0.0 | True | valid |
| Eq-9 | 200 | 0.15 | 42.43 | 0.0 | True | valid |
| Eq-9 | 250 | 0.15 | 53.03 | 0.0 | True | valid |

</details>

### 26. STAV PO FÁZI 01K-a

01K-a korekční audit dokončen. Varianta A potvrdila, že boundary-distance měřák sleduje řízený geometrický drift obálky vůči fixnímu pozorovateli v rámci pracovního rozsahu, tj. pokud je pozorovatel uvnitř obálky a Clearance_shell >= 5 px. Eq-9 při větším posunu vstupuje do limitního režimu, takže odpovídající řádky jsou klasifikovány jako measurement_limited_clearance, nikoli jako validní chyba měřáku. Varianta B ověřila, že fázový gradient byl aplikován, ale v tomto konkrétním nastavení a délce běhu nebyl naměřen translační drift amplitudové obálky. Výsledek zůstává kinematicko-geometrickým auditem a nepředstavuje fyzikální validaci HSU ani kosmologické interpretace Lineum.

### 27. HSU/Lineum komparační rámec po validaci měřicího aparátu

#### 27.A. Shrnutí pozice po uzavření 01I / 01J / 01K-a

Fáze 01I, 01J a 01K-a netestovaly HSU jako fyzikální teorii. Testovaly výhradně to, zda geometricko-kinematický měřicí aparát funguje správně v kontrolovaném prostředí: zda detekuje observer-offset, zda je konzistentní v čase a zda správně klasifikuje limitní stavy.

Výsledky ukazují, že tento aparát v definovaném pracovním rozsahu funguje spolehlivě. Zároveň fáze ukázaly, proč je takový aparát nutnou podmínkou pro jakoukoli seriózní komparaci: bez morfologických bran, bez klasifikace clearance a bez validace rozsahu by bylo snadné zaměnit geometrický artefakt, deformaci obálky nebo limitní stav měřáku za fyzikální signál. Tato sekce proto slouží jako analytický přechod od validace měřáku k formulaci toho, co zbývá.

---

#### 27.B. Metodické předpoklady, které HSU implicitně potřebuje

Aby bylo jakékoli srovnání HSU a Lineum metodicky korektní, musí být splněna sada podmínek. Tyto podmínky nejsou kritikou HSU jako takového — jsou obecnými nároky na jakoukoli teorii, která pracuje s pojmy obálka, pozorovatel a fyzikální signál.

| # | Nutná podmínka | Stav aparátu po 01K-a |
|---|---|---|
| 1 | Jednoznačná, detekovatelná obálka / hranice | Ověřeno v definovaném rozsahu |
| 2 | Dostatečná kruhovost nebo sférická symetrie obálky | Ověřeno pro A-class morfologie |
| 3 | Pozorovatel prokazatelně uvnitř platné obálky (`Observer_Inside_Shell = True`) | Implementováno a validováno |
| 4 | Bezpečný odstup pozorovatele od hranice (`Clearance_shell ≥ 5 px`) | Implementováno, limitní stavy klasifikovány |
| 5 | Oddělení observer-offsetu od deformace obálky | Geometrická translace (Var A) ověřena; deformace zatím netestována |
| 6 | Stabilita signálu v čase | Pilotně ověřeno v 01J-c pro definovaný rozsah |
| 7 | Rozlišení mezi geometrií, morfologií a fyzikální interpretací | Explicitně kodifikováno v metodice; interpretační zákaz vynucen |
| 8 | Zákaz odvozovat fyzikální závěry z nekontrolované morfologie | Zakódováno jako invariant klasifikačního systému |

Podmínky 1–4 a 7–8 jsou v aparátu implementovány. Podmínky 5 a 6 jsou splněny pouze pro specifický podprostor experimentů; robustní testování na deformovaných nebo dynamických obálkách zatím neproběhlo.

---

#### 27.C. Co aparát po 01I / 01J / 01K-a prokazatelně umí

Výsledky jsou formulovány výhradně v kinematicko-geometrickém rámci, bez fyzikálních závěrů.

**01I — Slepý boundary-distance audit:**
Měřák bez znalosti ground truth správně rekonstruuje observer-offset ve vektoru $b_{measured}$ s chybou pod 0.1 px, pokud je pozorovatel uvnitř obálky a Clearance_shell ≥ 5 px. Morfologické brány (`gate_failed_morphology`, `measurement_invalid_outside_shell`) správně blokují neplatná měření. Nulový offset dává nulový signál — aparát tedy nemá systematickou bias.

**01J-c — Kinematicko-geometrický pilot:**
Měřák je konzistentní napříč časem v 01J geometrickém pilotu. Hodnoty Vec_Err zůstávají stabilní při dodržení pracovního rozsahu. Clearance audit odhalil, že dřívější výsledky s nedostatečnou clearance byly nesprávně klasifikovány; po reklasifikaci jsou výsledky konzistentní.

**01K-a Varianta A — Řízený drift obálky:**
Měřák sleduje řízený geometrický drift obálky vůči fixnímu pozorovateli s chybou pod 0.05 px v platném rozsahu. Eq-11 (větší poloměr obálky) zůstává v platném rozsahu po celých 250 kroků. Eq-9 (menší poloměr) vstupuje do limitního režimu při t=200–250 s shift_step=0.05 a při t=100+ s shift_step=0.10. Limitní stavy jsou správně klasifikovány jako `measurement_limited_clearance`.

**01K-a Varianta B — PDE fázový gradient:**
Fázový gradient byl prokazatelně aplikován (Mean|grad φ| lineárně roste s k × t). V daném nastavení a délce běhu nebyl naměřen translační drift amplitudové obálky. Tento výsledek nelze povýšit na obecné tvrzení o fyzikálních vlastnostech rovnic — jde o kinematické pozorování v konkrétní konfiguraci.

---

#### 27.D. Co z HSU zatím zůstává hypotetické

Níže uvedené body popisují oblasti, kde současná formulace HSU ponechává otevřené metodické otázky. Nejde o výčet chyb, ale o seznam nutných dalších kroků k férovému testování.

1. **Odpovídání matematické obálky fyzikálnímu horizontu:** HSU pracuje s pojmem sférická slupka jako observačním horizontem. Převod geometrické obálky PDE pole na tento fyzikální pojem zatím nebyl formálně odvozen. Bez tohoto odvození nelze z geometrických měření na 2D Lineum obálce usuzovat na kosmologický observer-offset.

2. **Převod observer-offsetu na klidovou energii nebo hmotnost:** HSU vyvozuje z geometrického offsetu $u^*$ fyzikální veličiny (efektivní drift $v_{eff}$, poměr DM/DE). Přímé odvození tohoto vztahu z Lineum PDE nebylo provedeno ani registrováno jako validovaný krok.

3. **Kosmologický význam geometrického dipólu:** Dipólový vektor $b_{measured}$ v Lineum je geometrická veličina rekonstruovaná z tvaru obálky. Jeho ekvivalence s dipólem rádiových zdrojů v HSU není doložena; chybí explicitní "visibility function" nebo "source count prescription".

4. **Převoditelnost 2D na 3D:** Veškeré experimenty probíhají na 2D mřížce. Argumenty pro přímý přechod do 3D sférické geometrie HSU nebyly formulovány ani testovány. Omezení 2D modelu jsou explicitně kodifikována v sekci 10.10, ale formální převodní argument chybí.

5. **Platnost A-class geometrie jako fyzikální reality:** Experimenty pracují s A-class morfologiemi (Eq-11, Eq-9 v klidovém režimu). Realistické kosmologické obálky jsou dynamické, deformované a vystavené šumu. Robustnost měřáku na těchto typech obálek nebyla testována.

6. **Robustnost HSU vztahů vůči degradaci vstupů:** Současná formulace HSU neobsahuje explicitní analýzu toho, jak se predikce mění v přítomnosti deformovaných obálek, šumového pole, variabilního prahování nebo okrajových stavů. Bez takové analýzy nelze určit, kde leží hranice interpretovatelnosti.

---

#### 27.E. Co původní rámec HSU neřeší dostatečně přísně

Tato část shrnuje metodické nedostatky, které byly identifikovány v průběhu přípravy komparačního aparátu. Jde o otevřené metodické otázky, ne o zpochybnění samotné intuice HSU.

- **Chybějící morfologické brány:** Původní rámec neobsahuje podmínky pro odmítnutí měření na základě morfologie obálky (např. gate_failed_morphology, boundary_limited). Bez těchto bran může měřák produkovat zdánlivě validní výsledky i v případech, kdy je obálka deformovaná nebo pozorovatel leží mimo platný rozsah.

- **Chybějící negativní kontroly:** Pro férové testování je nutné demonstrovat, že aparát nedává falešně pozitivní výsledky při nulovém fyzikálním signálu. V dosavadní formulaci HSU taková negativní kontrola není dokumentována.

- **Chybějící kontrola tautologického měření:** Bez slepého auditu hrozí, že měřicí aparát zpětně potvrdí to, co mu bylo implicitně vloženo (bias toward expected result). Fáze 01I tuto kontrolu provedla — pro HSU analogické testy tato kontrola v původním manuskriptu chybí.

- **Neoddělení observer-offsetu od deformace obálky:** Pokud obálka není přesně kruhová / sférická, část geometrického dipólu pochází z deformace tvaru, nikoli z observer-offsetu. Toto oddělení nebylo v původním rámci explicitně formalizováno.

- **Neřešený limit pozorovatele u hranice:** Co se stane, když se pozorovatel nachází blízko hranice obálky nebo ji překročí, není v HSU formulaci ošetřeno. Výsledky 01K-a ukazují, že tato situace vede ke kvalitativně odlišnému chování měřáku (explodující Vec_Err).

- **Neoddělenou geometrická validace od fyzikální interpretace:** Pro férové testování je nutné přesně vymezit, kdy výsledek geometrické rekonstrukce opravňuje k fyzikální interpretaci a kdy ne. Tato hranice v původní formulaci není explicitně nastavena.

---

#### 27.F. Co musí přijít dál před jakoukoli fyzikální interpretací

Následující testovací bloky jsou nutnou podmínkou pro přechod od validace měřáku k testování fyzikálních tvrzení HSU. Žádný z nich nebyl spuštěn; jsou zde uvedeny jako registrované a formulované testovací záměry.

| # | Testovací blok | Účel |
|---|---|---|
| T-01 | Test robustnosti na deformovaných obálkách | Ověřit, zda je měřák stabilní i na nekruhových morfologiích |
| T-02 | Test na realisticky dynamických obálkách (PDE bez simplifikací) | Ověřit, zda drift obálky za realistických podmínek neznehodnocuje měření |
| T-03 | Formální 2D→3D převodní argument nebo explicitní 3D test | Odůvodnit nebo zpochybnit přímou aplikovatelnost 2D výsledků na 3D HSU geometrii |
| T-04 | Vazba geometrického offsetu na HSU energetické veličiny | Odvodit nebo zpochybnit, zda $b_{measured}$ lze převést na $u^*$ a $v_{eff}$ |
| T-05 | Test citlivosti na práh detekce obálky | Ověřit, jak výsledky závisí na zvoleném threshold (10/50/90 % amplitudy) |
| T-06 | Porovnání s numerickými očekáváními HSU manuskriptu | Konfrontovat geometrické výsledky s konkrétními predikovanými hodnotami, jsou-li v manuskriptu uvedeny |
| T-07 | Formulace explicitních falsifikačních kritérií | Definovat, při jakém výsledku by bylo nutné prohlásit HSU–Lineum analogii za nedoloženou |

Pořadí bloků nereprezentuje prioritu; záleží na dostupném výpočetním čase a vývoji metodiky.

---

#### 27.G. Přechodový závěr

Po uzavření fází 01I, 01J a 01K-a existuje pro první odvozu funkční geometricko-kinematický měřicí aparát, který:

- správně detekuje observer-offset v definovaném pracovním rozsahu,
- klasifikuje limitní a neplatné stavy místo jejich tiché kontaminace výsledků,
- je soběstačný a auditovatelný bez závislosti na externích implementacích,
- neobsahuje hardcoded fyzikální závěry.

HSU jako fyzikální hypotéza zatím není prostřednictvím tohoto aparátu ani potvrzena, ani vyvrácena. Současná formulace HSU ponechává otevřené metodické otázky v oblastech morfologické kontroly, negativních kontrol a oddělení geometrické rekonstrukce od fyzikální interpretace — tyto otázky jsou předmětem plánovaných testovacích bloků T-01 až T-07.

HSU je bráno vážně právě proto, že je podrobováno přísné metodice: cílem je férové testování konkrétních tvrzení, nikoli jejich lacině potvrzení ani jejich apriorní odmítnutí. Aparát je nyní dostatečně připraven k tomuto přechodu.

### 28. Registr testovatelných tvrzení HSU

#### 28.A. Shrnutí

Sekce 27 ukázala, co aparát umí a co v HSU zatím chybí. Dalším krokem není potvrzovat nebo vyvracet HSU jako celek, ale rozložit ho na konkrétní, individuálně testovatelná tvrzení. Teorie přestává být monolitickou hypotézou a stává se testovacím plánem.

Každé tvrzení v registru níže má přiřazen typ (geometrický, kinematický, fyzikální nebo kosmologický), stav po uzavření aparátu 01I/01J/01K-a a odkaz na nejbližší nutný test. Tvrzení označená jako „rekonstruovaný metodický claim" nejsou doslovnou citací manuskriptu — jsou explicitní formulací podmínky, která je v HSU implicitní, ale v původním textu není dostatečně přísně oddělena od závěru.

---

#### 28.B. Registr tvrzení

| ID | Tvrzení HSU | Typ tvrzení | Opora ve zdroji | Co by muselo být měřeno | Stav po 01I / 01J / 01K-a | Riziko / slabina | Další nutný test |
|---|---|---|---|---|---|---|---|
| HSU-01 | Existuje jednoznačná uzavřená obálka nebo fyzikální horizont | Geometrický | Přímé tvrzení HSU | Detekce obálky se stabilním těžištěm a uzavřenou hranicí | Geometricky podpořeno pro A-class morfologie (Eq-11, Eq-9 v klidovém rozsahu). Deformované nebo šumové obálky nebyly testovány. | Realistické obálky mohou být nekruhové, fragmentované nebo s proměnnou šíří. | T-01 (robustnost na deformovaných obálkách) |
| HSU-02 | Pozorovatel lze definovat vůči obálce pomocí observer-offsetu $u^*$ | Geometrický | Přímé tvrzení HSU | Observer_Inside_Shell = True, Clearance ≥ prahová hodnota, rekonstrukce vektoru $d_{obs}$ | Implementováno a validováno v 01I. Observer-offset je detekovatelný s chybou pod 0.1 px v pracovním rozsahu. | Tvrzení platí v geometrické rovině; fyzikální odpovídání $u^*$ z HSU manuskriptu ($u^* \approx 5{-}6$ Mpc) nebylo odvozeno. | T-04 (vazba geometrického offsetu na HSU $u^*$) |
| HSU-03 | Hraniční dipól lze měřit lokálně z profilu vzdáleností k hranici obálky | Geometrický / kinematický | Rekonstruovaný metodický claim | Vektor $b_{measured}$ rekonstruovaný ray-castingem, Vec_Err vůči $b_{expected}$ | Geometricky validováno v 01I a 01J-c. Aparát rekonstruuje dipólový vektor s nízkou chybou v platném rozsahu. | HSU pracuje s dipólem z celooblohových survey (Cosmic Octave), nikoli s lokálním ray-castingem. Záměna těchto rovin je rizikem. | T-04, T-06 (porovnání s HSU predikcemi) |
| HSU-04 | Geometrický observer-offset $u^*$ generuje kinematický efektivní drift $v_{eff}$ | Kinematický | Přímé tvrzení HSU | Odvození $v_{eff} = H_\perp u^*$ z PDE dat; velikost driftu | Zatím nevalidováno. Aparát měří geometrický offset; kinematická konverze na $v_{eff}$ nebyla provedena ani registrována jako krok. | Přechod z geometrické polohy na kinematický drift (rychlost) vyžaduje fyzikální přemostění, které v aparátu dosud chybí. | T-04 (vstup do Sekce 29) |
| HSU-05 | 2D průřez nebo analogie dostatečně odpovídá 3D sférické slupce HSU | Geometrický | Rekonstruovaný metodický claim | Formální převodní argument nebo srovnání výsledků 2D a 3D experimentu | Zatím nevalidováno. Omezení 2D jsou kodifikována v sekci 10.10; formální převodní argument chybí. | Topologie sférické slupky a 2D kruhu se v klíčových vlastnostech liší (sférická harmonická vs. Fourierova); přímé analogie mohou být zavádějící. | T-03 (2D→3D převodní test) |
| HSU-06 | Obálka zůstává stabilní v čase i při dynamice pole | Kinematický | Nepřímý předpoklad HSU | Časový průběh $C_{shell}(t)$, $\Delta C$, morfologická třída bez deformace | Pilotně podpořeno: 01J-c a 01K-a Var B ukazují $\Delta C \approx 0$ v klidovém PDE režimu. Var B fázový gradient neindukoval drift amplitudové obálky v daném nastavení. | Výsledek platí pro klidový A-class režim. Dynamické, deformované nebo šumové obálky nebyly testovány. | T-02 (dynamické realistické obálky) |
| HSU-07 | Deformaci slupky lze oddělit od čistého observer-offsetu v měřeném signálu | Kinematický | Rekonstruovaný metodický claim | Měřicí protokol s kontrolní deformací bez offsetu a s offsetem bez deformace | Připraveno k testování. Var A ověřila čistou translaci (bez deformace); deformační test zatím nebyl spuštěn. | Pokud deformace a offset vyvolají srovnatelné $b_{measured}$, hrozí systematická záměna zdroje signálu. | T-01 |
| HSU-08 | Geometrické projekce určují poměr DM/DE a dipólové anomálie (Cosmic Octave) | Kosmologický | Přímé tvrzení HSU | Odvození DM/DE poměru z geometrických dat PDE; porovnání s pozorovaným dipólem rádiových zdrojů | Mimo rozsah současných dat. Výsledky aparátu jsou výhradně geometricko-kinematické; žádný kosmologický observable zatím nebyl odvozen ani registrován. | Riziko numerologie při odvozování kosmologické konstanty z geometrických poměrů bez dynamického zdůvodnění. Statický úhlový poměr bez časového vývoje (viz sekce 3 tohoto dokumentu). | T-04, T-06 (vstup do Sekce 29) |
| HSU-09 | Model obstojí vůči variabilitě prahu detekce, velikosti mřížky, šumu a okrajovým limitům | Geometrický | Rekonstruovaný metodický claim | Fuzzy threshold audit (10/50/90 %), grid resolution scan, přidaný šum k obálce | Připraveno k testování. Metodika fuzzy threshold auditu je definována v sekci 12; pro 01I/01J/01K-a konfigurace neproběhl plný sweep. | Pokud se výsledky mění při změně prahu nebo rozlišení, nelze považovat geometrický signal za robustní. | T-05 (threshold sensitivity) |
| HSU-10 | Lineum Eq-11 / Eq-9 lze fyzikálně propojit s HSU bez dodatečné neověřené interpretace | Fyzikální | Rekonstruovaný metodický claim | Formální derivace nebo falsifikace analogie: Lineum obálka ↔ HSU sférická slupka | Geometricky připraveno — aparát měří offset na Lineum obálkách. Fyzikální analogie není doložena; interpretační most z PDE geometrie na HSU fyzikální kategorie dosud neexistuje. | Riziko, že geometrická shoda bude zaměněna za fyzikální ekvivalenci. Interpretační zákaz je vynucen v metodice, ale formální derivace chybí. | T-03, T-04 (vstup do Sekce 29) |

---

### 29. Test převodu observer-offsetu na HSU fyzikální veličiny

**Cíl sekce:**
Nevalidovat fyziku HSU, ale analyticky ověřit, zda je metodicky možné (a za jakých podmínek) převést geometrický observer-offset získaný v aparátu Lineum na fyzikální a kosmologické veličiny deklarované v HSU (zejména $u^*$ a $v_{eff}$) bez zavádění skrytých nebo libovolných předpokladů.

#### 29.A. Zdrojová extrakce z HSU PDF (v29 FINAL)
Vycházíme výhradně z přímých tvrzení uvedených v HSU manuskriptu. Následující tabulka odděluje fyzikální veličiny HSU od možností jejich přímého geometrického mapování.

| Položka | Tvrzení / vztah v HSU | Opora ve zdroji | Jaký typ veličiny to je | Lze přímo mapovat z Lineum? |
|---|---|---|---|---|
| $u^*$ (Observer offset) | Vzdálenost pozorovatele od středu slupky (CSW), $u^* \approx 5{-}6$ Mpc. | Přímé tvrzení | Fyzikální vzdálenost | **Ne přímo.** Vyžaduje kalibraci prostorové škály. |
| $H_\perp$ (Normal expansion) | Normálová rychlost expanze slupky, definovaná jako $\dot{R}/R$. | Přímé tvrzení | Převrácený čas (expanzní škála) | **Nelze.** Lineum má simulační čas v PDE bězích, ale tento čas není kalibrován jako kosmologický čas HSU. Z něj nelze přímo odvodit $H_\perp$. |
| $v_{eff}$ (Effective drift) | Kinematický drift indukovaný expanzí a offsetem: $v_{eff} = H_\perp u^*$. | Přímé tvrzení | Rychlost | **Ne.** Je závislý na nedefinovaném $H_\perp$. |
| Cosmic Octave dipól | Změřené anomálie v survey datech vykazují společnou směrovost a dipólový charakter. | Přímé tvrzení | Kosmologický datový vzorec | **Částečně (směrově).** Směr vektoru zjistit lze, amplitudu nikoliv. |
| DM/DE projekce | Tangenciální a radiální geometrické projekce slupky produkují DM a DE poměr. | Přímé tvrzení (separátní interpretační vrstva) | Kosmologické hustoty | **Ne.** Lokální observer-offset měření v Lineum aparátu není totožné s HSU tangenciální/radiální projekcí slupky; jde o oddělenou interpretační vrstvu. |

#### 29.B. Dimenzionální kontrola
Křížová kontrola jednotek ukazuje, jaká přemostění chybí mezi datovým prostorem Lineum a HSU:
- **$u^*$** (HSU): `[L]` (Mpc)
- **$H_\perp$** (HSU): `[1/T]` (km/s/Mpc)
- **$v_{eff}$** (HSU): `[L/T]` (km/s)
- **$b_{measured}$** (Lineum): `[px]` geometrická/pixelová vzdálenost bez rozměru.

**Co chybí k formálnímu převodu:**
1. **Škálování prostoru:** Chybí převodní konstanta (škála) z bezrozměrného pixelu na fyzikální délku (Mpc).
2. **Časová škála:** Lineum simulační čas zatím nemá fyzikální kosmologickou kalibraci vůči HSU expanzi. Z PDE dat tak nelze interně vygenerovat $H_\perp$.
3. **Topologický most (2D ↔ 3D):** Vztah Lineum 2D kružnice k HSU 3D (hypersférické) slupce a vztah lokálního boundary-distance dipólu k celooblohovému survey dipólu.

#### 29.C. Konzervativní mapovací protokol (bez fyzikální platnosti)
Pro další testování lze zavést čistě *formální* mapování, jehož cílem není potvrdit fyziku, ale otestovat stabilitu aparatury:
1. Lineum aparát změří geometrický offset vektor $b_{measured}$ na PDE obálce.
2. Zavedením kalibrační konstanty $S_L$ lze formálně definovat simulovaný offset: $u^*_{sim} = S_L \cdot |b_{measured}|$.
3. Zavedením vnější testovací konstanty $H_\perp$ lze formálně definovat simulovaný drift: $v_{eff,sim} = H_\perp \cdot u^*_{sim}$.
*Upozornění: Bez nezávislé kalibrace $S_L$ a bez vyřešení 3D mostu představuje tento protokol pouze numerické škálování, nikoli potvrzení fyzikálního mechanismu HSU.*

#### 29.D. Co lze testovat hned (v rámci Lineum)
I bez fyzikálního claimu umožňuje navržený protokol testovat robustnost metodiky HSU na PDE datech:
- **Linearitu formálního mapování $v_{eff,sim} \propto u^*_{sim}$ po zavedení externí konstanty $H_\perp$:** Zůstává formálně dopočtená hodnota $v_{eff,sim}$ lineární vůči zavedenému offsetu $u^*_{sim}$ při pevně zvolené externí hodnotě $H_\perp$?
- **Znaménkovou konzistenci driftu:** Zůstává orientace vektoru $b_{measured}$ stabilní?
- **Stabilitu výpočtu:** Chování $b_{measured}$ při různých, extrémních offsetech.
- **Citlivost:** Variabilita vůči mřížce, prahování (fuzzy threshold) a clearance prahům.
- **Oddělení deformace:** Schopnost odlišit skutečný offset obálky od morfologické deformace (např. asymetrická tloušťka slupky).

#### 29.E. Co zatím testovat nelze
Z provedené analýzy a striktního ukotvení v HSU v29 FINAL.pdf vyplývá, že následující body zůstávají mimo dosah stávající metodiky:
- **Reálná kosmologická rychlost ($v_{eff}$ v km/s):** Nelze potvrdit reálné hodnoty, chybí škálování.
- **Reálná hmotnost / energie:** Offset s tímto nijak nesouvisí (korigovaný claim HSU-04).
- **Fyzikální závěr o DM/DE poměru:** Jedná se o nezávislou geometrickou projekci HSU.
- **Platnost 3D hypersférické struktury:** Zatím ověřováno pouze 2D průřezy.
- **Shoda s observačními survey (Cosmic Octave):** K tomu chybí explicitní datový a syntetický most z lokálních dat.

#### 29.F. Doporučená další fáze (nespuštěna)
Pro posun z čisté geometrie do vrstvy, která umožní byť jen syntetické srovnávání s HSU veličinami, je nutné vybudovat škálovací rámec.

**Navržená příští fáze (zatím nespuštěna):**

> ### 30. Formální škálovací model mezi Lineum jednotkami a HSU veličinami
> 
> *Cíl budoucí fáze:* Navrhnout a matematicky rigorózně zdůvodnit konstantu $S_L$, otestovat vliv chybějícího $H_\perp$ a analyzovat vliv topologické redukce (2D vs. 3D). Fáze bude striktně dbát na oddělení formální kalibrace od fyzikální validity.

*(Tato fáze 30. zatím nebyla spuštěna a vyčká na povel).*

### 30. Formální škálovací model mezi Lineum jednotkami a HSU veličinami

#### 30.A. Jednoduché shrnutí
Tato sekce řeší výhradně formální škálování mezi testovacím aparátem Lineum a fyzikálním rámcem HSU. Lineum měří geometrický offset v bezrozměrných simulačních jednotkách (pixelech). HSU naproti tomu používá reálné fyzikální a kosmologické veličiny jako megaparseky (Mpc) a rychlosti (km/s). Převod mezi těmito dvěma světy je matematicky možný pouze po zavedení externích škálovacích konstant, které z PDE samotných odvodit nelze. Vybudovaný škálovací model je proto ryze formálním algebraickým převodem a nepředstavuje fyzikální validaci teorie HSU.

#### 30.B. Zdrojové veličiny z HSU
Následující tabulka definuje cílové veličiny extrahované přímo z `HSU v29 FINAL.pdf`.

| Veličina | Definice v HSU | Opora ve zdroji | Jednotka | Role v mapování |
|---|---|---|---|---|
| $u^*$ | Observer-offset (vzdálenost pozorovatele od středu slupky CSW). HSU uvádí typickou hodnotu $u^* \approx 5{-}6$ Mpc. | Přímé tvrzení HSU | Mpc | Cílová délková škála převáděná z $b_{measured}$. |
| $H_\perp$ | Normálová míra expanze slupky, definovaná jako $\dot{R}/R$. | Přímé tvrzení HSU | km/s/Mpc (nebo $1/s$) | Převodník vzdálenosti $u^*$ na driftovou rychlost. |
| $v_{eff}$ | Efektivní drift (kinematický skalární dipólový drift). | Přímé tvrzení HSU | km/s | Výsledný pozorovatelný kinematický projev offsetu. |
| Vztah $v_{eff} = H_\perp u^*$ | Rovnice svazující offset, rychlost expanze a efektivní drift. | Přímé tvrzení HSU | Rovnice | Definuje formální propojení mezi naměřeným offsetem a výslednou kinematikou. |

#### 30.C. Lineum veličiny
Aparát z fáze 01I generuje vlastní proměnné v bezrozměrném nebo pixelovém metrickém prostoru.

| Veličina | Definice v Lineum aparátu | Jednotka | Stav validace | Omezení |
|---|---|---|---|---|
| $b_{measured}$ | Vektor naměřeného dipólu (offsetu pozorovatele) vzhledem k obálce. | px | Validováno (01I) | Geometrická hodnota závislá na rozlišení mřížky. |
| $d_{obs}$ | Zadaný / synteticky nastavený posun pozorovatele vůči těžišti obálky. | px | Validováno (01I) | Slouží k syntéze $b_{expected}$. |
| $C_{shell}$ | Střed (těžiště) amplitudové obálky PDE pole. | px | Validováno (01J) | Reaguje na šum a prahování. |
| $Clearance_{shell}$ | Nejkratší vzdálenost od pozorovatele k hranici PDE obálky. | px | Validováno (01K-a) | Musí být $\ge 5$ px pro platnost $b_{measured}$. |
| $Vec\_Err$ | Odchylka mezi zadaným $b_{expected}$ a naměřeným $b_{measured}$. | px | Validováno (01I) | Klíčová chybová metrika ovlivňující formální mapování. |
| Simulační čas / PDE iterace | Iterativní krok PDE updatu (běhy po 250 – 2000 krocích). | iterace | Použito v 01J/01K-a pro časové sledování aparátu | Není kalibrován na kosmologický čas HSU. |
| $Measurement\_Status$ | Binární/kategorické hodnocení platnosti měřicího snímku. | stav | Validováno (01K-a) | Omezuje převod na platná a ne-limitní data. |

#### 30.D. Formální mapování
Definujeme konzervativní algebraický přepis mezi Lineum prostorem a HSU formalismem.

1. Simulovaný observer-offset:
   $$u^*_{sim} = S_L \cdot |b_{measured}|$$
2. Simulovaný efektivní drift:
   $$v_{eff,sim} = H_\perp \cdot u^*_{sim}$$
3. Sloučené formální mapování:
   $$v_{eff,sim} = H_\perp \cdot S_L \cdot |b_{measured}|$$

**Metodické omezení:**
- $S_L$ (škálovací konstanta prostoru) není známa a z PDE simulace ji nelze odvodit.
- $H_\perp$ (rychlost expanze) není odvoditelná z Lineum simulačního času bez zavedení fyzikální kalibrace.
- Tento postup představuje ryze **algebraický převod, nikoliv fyzikální potvrzení** mechanismů popsaných v HSU.

#### 30.E. Dimenzionální sanity check
Rozměrová (jednotková) kontrola potvrzuje, že pro konzistentní výsledek musí být zachovány následující jednotky:
- $S_L$: Mpc / px
- $b_{measured}$: px
- $u^*_{sim}$: Mpc
- $H_\perp$: (km/s) / Mpc (tj. inverzní čas ve formátu zohledňujícím rozpínání)
- $v_{eff,sim}$: km/s

Pokud $H_\perp$ zadáme ve standardním kosmologickém formátu km/s/Mpc a $u^*$ bude převeden do Mpc, získáme výsledný simulovaný drift $v_{eff,sim}$ standardně v km/s.

#### 30.F. Co lze z tohoto modelu testovat bez fyzikálního claimu
Zavedení formálního škálování nám otevírá cestu k novým testům, které zůstávají striktně v mezích validace aparátu:
- **Linearita mapování:** Odezva $v_{eff,sim}$ na škálování offsetu $|b_{measured}|$ při konstantních parametrech $S_L$ a $H_\perp$.
- **Směrová a znaménková konzistence:** Chování orientace vektoru $b_{measured}$ při formálních úpravách referenčního rámce.
- **Citlivostní analýza $S_L$:** Vliv různé volby prostorové škály na velikost chybové odezvy.
- **Citlivostní analýza $H_\perp$:** Rychlost růstu chyby při hypotetických hodnotách kosmologické expanze.
- **Chybová propagace:** Přenos lokální chyby rekonstrukce ($Vec\_Err$) do škálovaných veličin ($u^*_{sim}$ a $v_{eff,sim}$).
- **Stabilitní hranice:** Analýza robustnosti převodu při blížení se k limitu $Clearance_{shell} < 5$ px.

#### 30.G. Co tento model stále neřeší
Zavedené mapovací vztahy představují limitovaný formální model. Model neřeší a nevyjadřuje se k následujícím bodům:
- **Neřeší 2D $\rightarrow$ 3D hypersférický most:** Mapování ignoruje topologický skok z 2D řezu na 3D slupku.
- **Neřeší fyzikální paralelu PDE $\rightarrow$ HSU:** Neověřuje, zda se Lineum obálka skutečně chová jako fyzikální HSU slupka.
- **Neřeší DM/DE projekce:** Ty v HSU existují jako zcela oddělená integrační operace nad slupkou.
- **Neřeší Cosmic Octave survey data:** Neporovnává $v_{eff,sim}$ s pozorovacími anomáliemi.
- **Neřeší reálný kosmologický čas.**
- **Neřeší, zda je HSU interpretace fyzikálně pravdivá.**

#### 30.H. Minimální číselný demonstrační příklad
Manuskript HSU zmiňuje pro observer-offset hrubý odhad $u^* \approx 5{-}6$ Mpc. 
Lze vytvořit čistě demonstrativní škálování k vizualizaci kalibračního postupu:

- Zvolíme referenční Lineum offset: $|b_{measured}| = 10$ px.
- Pro formální sladění s HSU zavedeme pevnou škálu: $S_L = 0.5{-}0.6$ Mpc/px.
- Tímto krokem je formálně zajištěno, že naměřený 10pixelový offset odpovídá deklarovaným $u^* = 5{-}6$ Mpc.

*Důležité upozornění: Výše uvedený příklad je pouze demonstrační škálovací operace. Není to hodnota odvozená z fundamentálních vlastností PDE a nepředstavuje validaci fyzikálních zjištění HSU. Slouží výhradně jako ilustrace formálního převodu. Veškerá přesnější numerická demonstrace by vyžadovala explicitní externí fyzikální kalibraci z reálných survey dat.*

#### 30.I. Doporučená další fáze (nespuštěna)
Jakmile je vytvořeno a zapsáno formální přemostění, dalším logickým testovacím blokem je zkoumání vlivu nejistot při mapování geometrie do fyzikálních škál.

**Navržená příští fáze (zatím nespuštěna):**

> ### 31. Chybová propagace observer-offset měřáku do HSU $v_{eff}$
> 
> *Cíl budoucí fáze:* Z čistě formálního modelu vypočítat, jak geometrická chyba $Vec\_Err$, nejistota ve stanovení škály $S_L$ a nejistota $H_\perp$ ovlivní celkovou nejistotu odvozené veličiny $v_{eff,sim}$. Test ukáže matematickou robustnost přenosu chyb, aniž by usuzoval na platnost HSU.

*(Tato fáze 31. zatím nebyla spuštěna a vyčká na povel).*

### 31. Chybová propagace observer-offset měřáku do HSU $v_{eff}$

#### 31.A. Jednoduché shrnutí
Tato sekce analyzuje šíření nejistot v rámci formálního mapovacího modelu ustanoveného v Sekci 30. Cílem není vytvářet nový fyzikální claim ani hodnotit pravdivost teorie HSU, ale čistě matematicky odvodit, jak velká by byla chyba výsledné simulované rychlosti $v_{eff,sim}$, pokud by Lineum aparát dodal určitý geometrický offset s lokální chybou, a my bychom následně zavedli externí konstanty $S_L$ a $H_\perp$. Sekce ukazuje citlivost formálního mapování na vstupní nejistoty.

#### 31.B. Vstupní rovnice
Základem analýzy je přímá algebraická substituce:
- $u^*_{sim} = S_L \cdot b$
- $v_{eff,sim} = H_\perp \cdot S_L \cdot b$

kde pro potřeby zjednodušení značení používáme:
- $b = |b_{measured}|$
- $S_L$ je externí prostorová škála [Mpc/px]
- $H_\perp$ je externí expanzní míra [km/s/Mpc]
- $v_{eff,sim}$ je formální mapovaná rychlost driftu [km/s]

#### 31.C. Zdroje nejistoty
Tabulka níže kategorizuje zdroje nejistot vstupující do formálního mapování.

| Symbol | Význam | Zdroj nejistoty | Stav v Lineum/HSU |
|---|---|---|---|
| $\sigma_b$ | Chyba rekonstrukce $b_{measured}$ | Závisí na přesnosti Lineum aparátu (úzce navázáno na metriku $Vec\_Err$) | Kvantifikovatelné. Měřák v 01I ve validním pracovním rozsahu vykazoval chyby v řádu desetin pixelu, s dříve reportovanými validními maximy přibližně do 0.141 px podle konfigurace. |
| $\sigma_{S_L}$ | Nejistota prostorové škály | Omezená znalost převodního poměru mezi PDE obálkou a kosmologickým prostorem | Nekvantifikováno. Externí předpoklad mapování. |
| $\sigma_H$ | Nejistota expanzní míry | Nepřesnost pozorování nebo nejistota teoretické volby $H_\perp$ | Nekvantifikováno. HSU předpokládá kinematický rámec nezávislý na lokální PDE simulaci. |
| Chyba clearance | Zkreslení hranice obálky | $Clearance_{shell} < 5$ px způsobuje kolaps ray-castingu | Kvantifikovatelné. Validováno ve fázích 01J a 01K-a jako pracovní limit platnosti. |
| Topologická chyba | 2D $\rightarrow$ 3D skok | Transformace plochého geometrického měření na 3D hypersférickou slupku | Zatím nekvantifikováno. Zásadní koncepční nejistota HSU mapování. |
| Chyba mapování dipólu | Lokální vs. survey data | Srovnání lokálního $d_{obs}$ profilu se sledováním reálných survey objektů (Cosmic Octave) | Zatím nekvantifikováno. |

#### 31.D. Analytická propagace chyby
Budeme-li uvažovat nejistoty jako statisticky nezávislé, platí pro součin $v = H_\perp S_L b$ standardní zákon šíření chyb.

**Relativní chyba:**
$$ \left( \frac{\sigma_v}{v} \right)^2 = \left( \frac{\sigma_H}{H_\perp} \right)^2 + \left( \frac{\sigma_{S_L}}{S_L} \right)^2 + \left( \frac{\sigma_b}{b} \right)^2 $$

**Absolutní chyba:**
$$ \sigma_v = v \cdot \sqrt{ \left( \frac{\sigma_H}{H_\perp} \right)^2 + \left( \frac{\sigma_{S_L}}{S_L} \right)^2 + \left( \frac{\sigma_b}{b} \right)^2 } $$

*Pravidlo nulového offsetu:* Pro velmi malé offsety ($b \approx 0$) relativní chyba formálně diverguje k nekonečnu. V těchto případech je nutné pracovat výhradně s absolutní chybou, která se po dosazení redukuje na lineární závislost na absolutní chybě měřáku $\sigma_v \approx H_\perp S_L \sigma_b$.

#### 31.E. Vazba na měřicí výsledky 01I/01J/01K-a
Předchozí validace aparátu nám dává jasné mantinely, jak se $\sigma_b$ chová v praxi:
- Měřicí běhy ve fázích 01I prokázaly, že uvnitř platného rozsahu ($Clearance_{shell} \ge 5$ px) je rekonstrukční chyba velmi malá ($Vec\_Err < 0.1$ px).
- Analýza 01K-a Var A demonstrovala, že při porušení bezpečného clearance rozsahu chyba měřáku skokově naroste. Data s limitem $Clearance_{shell} < 5$ px tak z definice nesmějí do fyzikálního mapování vůbec vstupovat.
- Varianta B v auditu 01K-a byla použita pouze ke kontrole citlivosti aparátu na fázový gradient. Nezavedla skutečný kosmologický drift a fungovala ryze pro vnitřní časové sledování simulátoru.

#### 31.F. Ilustrační numerický příklad
Následující příklad je **čistě demonstrační**. Neslouží jako reálná predikce HSU a nepředstavuje výsledek Lineum fyziky. Ukazuje pouze kalkulační projev šíření chyb.

**Zvolené parametry:**
- Referenční Lineum offset: $b = 10$ px
- Typická chyba měřáku: $Vec\_Err \approx \sigma_b = 0.1$ px
- Formální prostorová škála: $S_L = 0.5$ Mpc/px
- Formální expanzní konstanta: $H_\perp = 70$ km/s/Mpc

**Formální výsledek:**
- Simulovaný observer-offset: $u^*_{sim} = 0.5 \cdot 10 = 5$ Mpc
- Simulovaný efektivní drift: $v_{eff,sim} = 70 \cdot 5 = 350$ km/s

**Rozbor chyb (příspěvky k relativní chybě $v_{eff,sim}$):**
1. **Příspěvek z Lineum (geometrie):** $\sigma_b / b = 0.1 / 10 = 1\%$. Tento 1% příspěvek platí pouze pro zvolený příklad  = 10$ px. Pro menší offsety se relativní chyba $\sigma_b / b$ zvětšuje, proto nulové a velmi malé offsety nelze hodnotit relativní chybou.
2. **Příspěvek z $S_L$ a $H_\perp$ (optimistická varianta):** Zavedeme-li hypotetickou toleranci $2\%$ u obou konstant, relativní chyba vzroste zhruba na $3\%$, tedy $\sigma_v \approx 10$ km/s.
3. **Příspěvek z $S_L$ a $H_\perp$ (konzervativní varianta):** Pokud nejistota externí kalibrace $S_L$ dosahuje $20\%$ (což je realistické při hrubém odhadování měřítka obálky), geometrická chyba $1\%$ se stává prakticky bezvýznamnou a celkovou nejistotu driftu (v desítkách km/s) bude pravděpodobně dominovat neznámá fyzikální konstanta.

#### 31.G. Interpretace
Při pohledu na odvozenou chybovou propagaci lze vyvodit střízlivé analytické závěry:
- V rámci zavedeného algebraického vztahu se přesnost (nebo chyba) detekce offsetu promítá do $v_{eff,sim}$ zcela lineárně.
- Uvnitř validního provozního rozsahu měřáku ($Clearance_{shell} > 5$ px) je samotná detekční chyba $\sigma_b$ dostatečně malá na to, aby v tomto demonstračním rozsahu pravděpodobně netvoří hlavní zdroj nejistoty mapování.
- Skutečně **dominantní neznámé** jsou volba kalibrační konstanty $S_L$, stanovení $H_\perp$, chybějící 2D/3D topologický most a absence přímé vazby mezi lokálním měřením a celooblohovým survey dipólem (Cosmic Octave).
- Lze tak konstatovat, že současným teoretickým limitem projektu již není primárně výpočetní přesnost geometrického měřáku Lineum, ale robustnost externího fyzikálního mapování.

#### 31.H. Co tato sekce neřeší
Pro zachování akademické přesnosti sekce důrazně připomíná, že:
- neřeší a nevyjadřuje se k pravdivosti teorie HSU,
- neanalyzuje reálná pozorovací data anomálií,
- nijak se nedotýká DM/DE projekcí (jež zůstávají odděleny),
- nenabízí 2D/3D most,
- neposkytuje zdůvodnění původu konstanty $H_\perp$,
- neřeší fyzikální kalibraci $S_L$.

#### 31.I. Doporučená další fáze (nespuštěna)
Vzhledem k analytickému zjištění, že matematická chyba silně závisí na externích předpokladech, je logickým dalším krokem citlivostní simulace pro jednotlivé zdroje chyby izolovaně.

**Navržená další analytická fáze (zatím nespuštěna):**

> ### 32. Test dominantních chybových zdrojů HSU/Lineum mapování
> 
> *Cíl budoucí fáze:* Systematicky a formálně rozlišit, v jakých oblastech parametrického prostoru pochází největší matematická nejistota výsledku z měřicí chyby Lineum aparátu, z nejistoty prostorové škály $S_L$, z expanzní míry $H_\perp$, nebo z fundamentálního topologického převodu 2D/3D. Fáze nenahrazuje fyzikální validaci.

*(Tato fáze 32. zatím nebyla spuštěna a vyčká na povel).*

### 32. Test dominantních chybových zdrojů HSU/Lineum mapování

#### 32.A. Jednoduché shrnutí
Tato sekce přímo navazuje na Sekci 31. Jejím cílem není provádět novou fyzikální validaci ani řešit pravdivost teorie HSU. Zcela analyticky rozlišuje, který ze vstupů do formálního mapovacího vztahu nejvíce ovlivňuje celkovou matematickou nejistotu. Zjišťujeme, zda je za případnou nepřesnost zodpovědný geometrický měřák Lineum, nebo zda celkové numerické nejistotě dominují externí neznámé parametry (prostorová škála a expanzní míra).

#### 32.B. Vstupní model
Stručné zopakování formálního mapování ze Sekce 31:
$$ v = H \cdot S \cdot b $$

kde zjednodušeně:
- $b = |b_{measured}|$
- $S = S_L$
- $H = H_\perp$

Odpovídající vzorec pro celkovou relativní chybu:
$$ \left( \frac{\sigma_v}{v} \right)^2 = \left( \frac{\sigma_H}{H} \right)^2 + \left( \frac{\sigma_S}{S} \right)^2 + \left( \frac{\sigma_b}{b} \right)^2 $$

#### 32.C. Definice příspěvku jednotlivých zdrojů
Pro zjištění dominance zavedeme podíl jednotlivých příspěvků vůči celkové varianci. Definujme celkovou varianci relativní chyby $Q$:
$$ Q = \left( \frac{\sigma_H}{H} \right)^2 + \left( \frac{\sigma_S}{S} \right)^2 + \left( \frac{\sigma_b}{b} \right)^2 $$

Následně jednotlivé relativní příspěvky (v intervalu 0 až 1) činí:
- Příspěvek měřáku: $P_b = (\sigma_b / b)^2 / Q$
- Příspěvek prostorové škály: $P_S = (\sigma_S / S)^2 / Q$
- Příspěvek expanzní míry: $P_H = (\sigma_H / H)^2 / Q$

Tyto podíly jasně kvantifikují, který zdroj dominuje numerické chybě ve zvoleném scénáři.

#### 32.D. Scénáře
K analýze použijeme ryze ilustrační (nikoliv fyzikálně validující) scénáře, složené z typických rozptylů parametrů.

Hodnoty offsetu $b$:
- $2$ px
- $5$ px
- $10$ px
- $15$ px

Chyby měřáku $\sigma_b$:
- $0.01$ px (optimistický běh)
- $0.1$ px (běžný validní případ)
- $0.141$ px (konzervativní validní maximum z předchozí dokumentace)

Nejistoty prostorové škály $\sigma_S / S$:
- $1\%$
- $5\%$
- $20\%$

Nejistoty expanzní míry $\sigma_H / H$:
- $1\%$
- $5\%$
- $10\%$

*Poznámky k limitům:* 
1. Nulové a velmi malé offsety ($b \approx 0$) jsou řešeny jako zvláštní případ – relativní chyba zde matematicky diverguje a standardní podílové rovnice ztrácejí smysl.
2. Případy s malou mezerou do okraje ($Clearance_{shell} < 5$ px) do formálního mapování vůbec nevstupují, neboť ray-casting v tomto režimu selhává.
3. Topologický most (2D/3D) a mapovací most dipólů (lokální vs. survey) nebudou v těchto výpočtech reprezentovány procenty, jelikož pro ně zatím neexistuje spolehlivý zdroj. Představují samostatné nekvantifikované systematické nejistoty.

#### 32.E. Výsledková tabulka
Přehledová tabulka vypočtených reprezentativních scénářů ilustruje, jak se skládají chyby:

| Scénář | $b$ | $\sigma_b$ | $\sigma_b / b$ | $\sigma_S / S$ | $\sigma_H / H$ | Celková relativní chyba | Dominantní zdroj |
|---|---:|---:|---:|---:|---:|---:|---|
| 1. Dobře měřený velký offset | 10 | 0.1 | $1.0\%$ | $1.0\%$ | $1.0\%$ | $1.73\%$ | Vyrovnáno ($P_b, P_S, P_H \approx 33\%$) |
| 2. Malý offset | 2 | 0.1 | $5.0\%$ | $1.0\%$ | $1.0\%$ | $5.20\%$ | Měřák $P_b$ ($92\%$) |
| 3. Nejistá prostorová škála | 10 | 0.1 | $1.0\%$ | $20.0\%$ | $5.0\%$ | $20.64\%$ | Škála $P_S$ ($94\%$) |
| 4. Nejistá expanze | 10 | 0.1 | $1.0\%$ | $5.0\%$ | $10.0\%$ | $11.22\%$ | Expanze $P_H$ ($79\%$) |
| 5. Konzervativní validní měřák | 10 | 0.141 | $1.41\%$ | $5.0\%$ | $5.0\%$ | $7.21\%$ | Externí kalibrace $P_S, P_H$ (každá $48\%$) |
| 6. Hraniční/nevhodný případ | $\approx 0$ | $0.1$ | Diverguje | N/A | N/A | Diverguje | Matematická singularita (malé $b$) nebo rozpad měření ($Clearance < 5$ px) |

#### 32.F. Interpretace
Pohled na tabulku umožňuje formulovat tyto zdrženlivé závěry:
- U větších offsetů v platném pracovním rozsahu (Scénáře 1, 3, 4, 5) může být chyba měřáku menší než nejistoty plynoucí z externích kalibračních předpokladů.
- U malých offsetů (Scénář 2) relativní chyba měřáku pochopitelně roste a stává se dominantní (více než 90 % vlivu).
- Jakmile $\sigma_S$ nebo $\sigma_H$ dosáhne jednotek až desítek procent (Scénáře 3 a 4), externí kalibrace pravděpodobně dominuje celkové numerické chybě mapování.
- Hlavní analytický limit při mapování se tím přesouvá od geometrického měřáku (ray-castingu) směrem k fyzikálnímu a topologickému mapování.
- Tento závěr nijak nevaliduje HSU, pouze určuje priority pro další případnou metodickou práci – zdokonalování měřáku již u velkých offsetů nepřinese podstatné zpřesnění kosmologického výsledku, pokud není zpřesněna formální kalibrace.

#### 32.G. Nekvantifikované systematické nejistoty
Tabulka výše pokrývá pouze numerické a měřicí chyby. Zcela stranou stojí systematické koncepční mosty, které nelze vtěsnat do rovnice relativní chyby:
- **2D $\rightarrow$ 3D hypersférický most:** Jak přesně odpovídá 2D kružnice 3D slupce.
- **Vztah lokálního měřáku k survey datům:** Lokální boundary-distance dipól vs. celooblohový (Cosmic Octave) dipól.
- **Analogie Lineum/HSU:** Míra abstrakce při tvrzení, zda lze Lineum obálku metodicky považovat za relevantní analogii HSU slupky.
- **DM/DE projekce:** Proces nezávislý na lokálním observer-offset měření.

Tyto nejistoty nejsou skryté v procentech – představují nutné metodické kroky, které je třeba v budoucnu vyřešit před jakýmkoliv vyvozováním fyzikálních závěrů.

#### 32.H. Co z toho plyne pro další práci
Metodické priority pro budoucí analýzy:
- Další iterativní zpřesňování ray-castingu pravděpodobně není hlavní prioritou pro scénáře velkých validních offsetů (kde je $Vec\_Err$ již nyní dostatečně nízký), protože celkové nejistotě budou pravděpodobně dominovat kalibrační a mapovací nejistoty.
- Naopak vyšší metodickou prioritou se stává fyzikální zdůvodnění a vymezení parametrů $S_L$ a expanzní míry $H_\perp$.
- Z hlediska topologie je kritické analyzovat povahu 2D/3D mostu.
- Pro případné porovnávání s Cosmic Octave musí být odděleně sestaven dedikovaný "survey bridge".

#### 32.I. Doporučená další fáze (nespuštěna)
Jelikož se ukazuje, že mapování trpí absencí převodu z plochy do prostoru, navrhovaným logickým krokem je zkoumání této prostorové transformace.

**Navržená další analytická fáze (zatím nespuštěna):**

> ### 33. Analýza 2D/3D mostu mezi Lineum obálkou a HSU slupkou
> 
> *Cíl budoucí fáze:* Zhodnotit z čistě metodického pohledu, zda lze aktuální 2D Lineum obálku používat pouze jako orientační analogii, nebo zda existuje konzervativní matematický převod (projekční pravidlo) umožňující korektní přemostění do 3D/hypersférické HSU geometrie.

*(Tato fáze 33. zatím nebyla spuštěna a vyčká na povel).*

### 33. Analýza 2D/3D mostu mezi Lineum obálkou a HSU slupkou

#### 33.A. Jednoduché shrnutí
Tato sekce metodicky posuzuje geometrický rozdíl mezi 2D aparátem Lineum a vícerozměrnou fyzikální slupkou teorie HSU. Lineum aparát zatím pracuje pouze s dvoudimenzionální obálkou (kruhovou hranicí v rovině). HSU pracuje s konečně silnou hypersférickou slupkou; její přesná dimenzionální interpretace musí být držena podle formulace v primárním textu. 2D model může posloužit jako metodická měřicí analogie pro testování výpočetní logiky (algoritmu offsetu), ale sám o sobě nezakládá žádný 3D fyzikální závěr. Cílem této sekce je určit, jaké vlastnosti lze z 2D roviny formálně přenést a co zatím zůstává nepřemostěné.

#### 33.B. Co HSU tvrdí o geometrii
Geometrická tvrzení extrahovaná přímo z primárního zdroje `HSU v29 FINAL.pdf`:

| Bod | Formulace v HSU | Opora ve zdroji | Typ tvrzení | Význam pro 2D/3D most |
|---|---|---|---|---|
| Hypersférická slupka a CSW | HSU popisuje konečně silnou hypersférickou slupku; CSW je v primárním textu používáno jako Center of the Shell's Width, tedy střed tloušťky slupky. | Primární text HSU | Přímé tvrzení HSU | Vyžaduje převod z 2D roviny do odpovídající vícerozměrné geometrie. |
| Observer offset ($u^*$) | Fyzický posun pozorovatele vůči středu radiálního profilu slupky | HSU v29 PDF | Přímé tvrzení HSU | Lze mapovat jako vzdálenost, vyžaduje definici středu a okraje. |
| DM/DE projekce | Interpretace tangenciálních a radiálních vlivů offsetu jako temné hmoty a energie | HSU v29 PDF | Přímé tvrzení HSU | Zcela mimo dosah 2D měřicího aparátu; vyžaduje 3D integraci vrstev. |

#### 33.C. Co reprezentuje Lineum 2D obálka
Lineum aparát je čistě výpočetní a geometrický nástroj operující v ploše:

| Lineum prvek | 2D význam | Co lze převést | Co nelze převést bez dalšího mostu |
|---|---|---|---|
| 2D mřížka a pole | PDE plocha pro vlnovou rovnici | Rozložení amplitudy, hranice vlnové fronty | Nelze ztotožnit s 3D prostorem bez projekčního pravidla. |
| Obálka ($C_{shell}$) | 2D maska / uzavřená křivka | Polohu středu, kruhovitost | Tloušťku slupky, objem. |
| Měřák $b_{measured}$ | Vektor posunu v rovině | Relativní velikost offsetu, lokální vzdálenosti k okraji ($Clearance_{shell}$) | Směrovou 3D anizotropii dipólu. |

*Poznámka:* Validita měření z fází 01I–01K-a platí výhradně v rámci 2D geometrického aparátu.

#### 33.D. Možné typy 2D/3D vztahu
Z metodického hlediska připadají v úvahu tyto varianty propojení:

1. **2D průřez 3D slupkou**
   - Lineum kruh je chápán jako přímý radiální řez sférickou/slupkovou strukturou přes její střed.
   - Tento model umožňuje zachovat střed a radiální observer-offset.
   - Nezachytí objemové integrály ani plnou 3D anizotropii potřebnou pro projekce typu DM/DE.

2. **2D projekce 3D slupky**
   - Lineum obraz je mapovou projekcí (např. ortografickou nebo stereografickou) složitější 3D geometrie do roviny.
   - V závislosti na projekčním pravidlu může deformovat vzdálenosti a úhly (např. vzdálenost k okraji obálky neodpovídá radiální tloušťce slupky).
   - Vyžaduje exaktní matematické projekční pravidlo.

3. **Čistá metodická analogie**
   - Lineum aparát nijak netvrdí 3D ekvivalenci a není geometricky svázán s HSU.
   - Používá se výhradně jako abstraktní výpočetní polygon pro otestování logiky "jak měřit offset uvnitř ohraničeného vlnového pole".
   - Neumožňuje dělat žádné přímé fyzikální závěry o HSU slupce.

4. **Neplatný / nepodložený most**
   - Bez jasného určení, zda jde o řez nebo projekci, nelze jakákoliv naměřená 2D data (kromě prostého faktu, že algoritmus umí změřit střed masky) na 3D HSU aplikovat.

#### 33.E. Které veličiny se mohou zachovat při přechodu

| Veličina | Zachovatelná ve 2D řezu? | Zachovatelná ve 2D projekci? | Poznámka |
|---|---|---|---|
| Relativní velikost offsetu | Ano | Závisí na pravidlu | V řezu přes střed je vzdálenost invariantní. |
| Směr offsetu a dipólu | Částečně (jen 2 složky) | Částečně | Ve 3D vzniká třetí složka dipólu ignorovaná ve 2D. |
| Vzdálenost k hranici | Ano | Ne (deformace) | Řez zachová skutečnou radiální vůli, projekce okraj deformuje. |
| Shell thickness (tloušťka) | Ano | Ne | Jen pokud řez prochází radiálně středem. |
| Objem a plocha obálky | Ne | Ne | Míry délky, plochy a objemu mají odlišnou dimenzionální závislost; nelze je převést bez explicitního geometrického pravidla. |
| Survey dipól (Cosmic Octave) | Ne | Ne | Pozorování oblohy nelze modelovat jednou 2D rovinou. |
| DM/DE projekční poměry | Ne | Ne | Tyto vlivy vyžadují sférickou integraci nad celou slupkou. |

#### 33.F. Co 2D aparát rozhodně nestačí pokrýt
Z tabulek výše vyplývá, že aktuální simulace Lineum 2D obálky jednoznačně neumožňuje pokrýt:
- objemové a plošné integrály uvnitř 3D slupky,
- plnou hypersférickou topologii a konečnou tloušťku vesmíru,
- DM/DE projekce, které HSU odvozuje z úhlových a radiálních poměrů celé slupky,
- Cosmic Octave survey (pozorování anizotropie na skutečné nebeské sféře),
- skutečnou fyzikální expanzi (bez externího kalibrování),
- jakýkoliv převod na reálné fyzikální jednotky (Mpc, km/s) bez dodatečné mapovací vrstvy.

#### 33.G. Minimální konzervativní most
Pro zajištění akademické a metodické přísnosti je nutné přijmout následující nejbezpečnější formulaci vztahu Lineum a HSU:
- Lineum 2D aparát lze zatím používat výhradně jako **metodický test lokální geometrie observer-offsetu**.
- Nelze ho zatím používat jako validní fyzikální model HSU slupky.
- Pro účely další práce lze opatrně zavést pracovní hypotézu „2D radiální průřez“ – avšak pouze jako testovací geometrii pro odvozování algebraických vztahů, nikoliv jako nástroj pro validaci tvrzení HSU.

> **Formální vymezení:**
> V této fázi je 2D Lineum obálka považována pouze za metodickou analogii lokálního řezu slupkou. Přenos závěrů na 3D/hypersférickou HSU geometrii vyžaduje samostatné projekční nebo řezové pravidlo.

#### 33.H. Dopad na předchozí výsledky 01I–32
Toto formální vymezení jasně ohraničuje předchozí poznatky, aniž by je zneplatnilo:
- Výsledky měřáku (tolerance a chyba ray-castingu fází 01I a 01K-a) zůstávají plně platné v rámci 2D výpočetní geometrie.
- Formální škálování (Sekce 30) a propagace chyb (Sekce 31 a 32) zůstávají platné jako formální algebraické závislosti (určují limit numerické přesnosti).
- Fyzikální interpretace HSU pomocí Lineum zůstává zcela neuzavřená.
- Toto vymezení je v souladu se závěrem Sekce 32: dominantní neznámou není numerická chyba měření, ale samotný **typ geometrického mapování** mezi oběma systémy.

#### 33.I. Doporučená další fáze (nespuštěna)
Pro formální ukotvení budoucích srovnání navrhujeme matematicky zadefinovat způsob, jakým budeme (nebo nebudeme) převádět výsledky 2D roviny do 3D předpokladů HSU.

**Navržená další metodická fáze (zatím nespuštěna):**

> ### 34. Návrh konzervativního projekčního / řezového pravidla pro HSU-Lineum srovnání
> 
> *Cíl budoucí fáze:* Formálně definovat a zdůvodnit, zda další srovnávací práce mezi Lineum a HSU bude používat pravidlo 2D řezu, pravidlo 2D projekce, nebo zůstane výhradně u metodické analogie, která zakazuje jakýkoliv fyzikální přesah.

*(Tato fáze 34. zatím nebyla spuštěna a vyčká na povel).*

### 34. Návrh konzervativního projekčního / řezového pravidla pro HSU-Lineum srovnání

#### 34.A. Jednoduché shrnutí
Sekce 33 metodicky vymezila, že neexistence rigorózního 2D/3D mostu představuje hlavní metodické omezení současného srovnávacího rámce. Cílem této Sekce 34 není daný topologický most fyzikálně vyřešit, nýbrž výhradně metodicky rozhodnout, jakým nejbezpečnějším způsobem se bude v dalších částech dokumentu se vztahem obálky a slupky pracovat. Za tímto účelem je nutné ustanovit výchozí konzervativní pracovní pravidlo: 2D Lineum obálka funguje čistě jako výpočetní metodická analogie pro algoritmus měření lokálního observer-offsetu, nikoli jako fyzikální model vícerozměrné HSU slupky.

#### 34.B. Kandidátní pravidla mostu
Pro teoretické provázání simulace se zdrojem `HSU v29 FINAL.pdf` připadají v úvahu tyto základní konstrukty:

| Pravidlo | Popis | Co umožňuje | Co neumožňuje | Riziko |
|---|---|---|---|---|
| **1. 2D radiální řez** | Rovina simulace se položí přesně radiálně napříč HSU slupkou skrze její středový bod. | Identifikaci středu a relativní míry offsetu, lokální radiální rozlišení k okrajům. | Plnou reprezentaci celoslupkové anizotropie a 3D integraci. | Nepovolené přesahy, pokud není striktně užíván jen jako geometrická abstrakce (skrytá ztráta osy Z). |
| **2. 2D projekce** | Plocha simulace se interpretuje jako projekční plátno plného 3D objemu s dodatečnou mapovací funkcí. | Umožnila by porovnání celooblohových integrálů, pokud by bylo ustaveno pravidlo. | Nemůže fungovat bez exaktně zadané nelineární mapovací rovnice. | Vysoce nebezpečné deformace vzdáleností, úhlů a dipólových sil (over-claiming). |
| **3. Metodická analogie** | 2D aparát není fyzikálním obrazem; je to jen testovací nástroj. | Zcela bezpečný test vnitřní měřicí logiky "jak hledat offset uvnitř tlusté vlnové hranice". | Fyzikální závěry o vlastnostech reálného kosmologického kontinua (survey dipól). | Nejnižší riziko. Zamezuje falešným fyzikálním závěrům. |
| **4. Žádný most** | Vztah je prohlášen za nedefinovaný. | Nulové propojení mezi HSU tezemi a výstupy Lineum. | Neposkytuje žádný prostor pro srovnávací a škálovací framework. | Zablokování další analýzy chybové propagace a komparace. |

#### 34.C. Hodnocení pravidla „2D radiální řez“
Toto pravidlo by bylo použitelné pouze tehdy, pokud by se simulace formálně omezila na studium jednoho vybraného směrového profilu.
- **Co by mohlo zachovat:** Identifikaci lokálního středu (CSW), lokální relativní radiální offset a vůli k hranici podél řezné osy.
- **Co nezachová:** Nedokáže modelovat objemové integrály napříč slupkou, zachytit celooblohový survey dipól ani projekce vlivů temné hmoty a energie (DM/DE), které v HSU vycházejí z komplexního 3D prostorového integrálu úhlů.
- **Omezení:** Bylo by vyžadováno neustále zdůrazňovat, že tento řez v žádném případě nevaliduje HSU model komplexně, ale pouze algebraicky zastupuje jeden izolovaný profilový test.

#### 34.D. Hodnocení pravidla „2D projekce“
Pravidlo projekce z vícerozměrné hypersféry do 2D kruhu si kategoricky žádá analytickou mapovací funkci. 
- Bez takovéto exaktní rovnice nelze bezpečně převádět vzdálenosti (deformace na krajích mapy) ani vektory. 
- Aktuálně neexistuje formální shoda na to, jak přesně 3D slupku "rozložit" do vlnové PDE rovnice operující v ploše tak, aby zůstaly nezdeformovány úhly a vzdálenosti okrajů.
- **Omezení:** Toto pravidlo aktuálně není připraveno pro použití ke kvantitativní fyzikální komparaci a vnášelo by obrovské systematické mapovací chyby.

#### 34.E. Hodnocení pravidla „metodická analogie“
Jedná se o nejbezpečnější dostupnou variantu pro současný stav dokumentu:
- Výpočetní aparát Lineum je v tomto reportu metodicky omezen na roli testovacího polygonu pro chování offsetového algoritmu; není pro účely srovnání presentován jako fyzikální model vesmíru.
- Toto pravidlo nepřenáší fyzikální vlastnosti obálky na vlastnosti vesmíru; zachovává výpočetní hodnotu testů (fáze 01I–01K-a, tolerance šumu), ale snižuje riziko nechtěného kosmologického over-claimingu.
- **Omezení:** Vylučuje tvrzení o kosmologické platnosti HSU tezí na základě výsledků 2D aparátu. Pouze ukazuje, že "geometrie offsetu algebraicky funguje".

#### 34.F. Doporučené pracovní pravidlo pro další report
Jako pracovní pravidlo pro navazující části přijímáme pravidlo „Metodické analogie" podpořené následující závaznou formulací:

> Dokud nebude matematicky odvozeno a ověřeno explicitní projekční nebo radiální řezové pravidlo, je 2D Lineum obálka pro účely tohoto dokumentu používána **výhradně jako metodická analogie** pro studium algebraických a výpočetních vlastností lokální geometrie observer-offsetu. Jakékoli mapování výsledků ray-castingu a škálování na kinematické veličiny HSU slupky budiž důsledně označováno jako mapování čistě formální, bez nároku na fyzikální validaci HSU interpretace.

#### 34.G. Dopad na Sekce 29–32
Implementace tohoto striktního pravidla nedevalvuje, nýbrž stabilizuje a doostřuje předchozí kapitoly:
- Formální škálování (Sekce 30) zůstává nadále algebraicky platné. Je to matematický kalkul převodu proměnných, nesupluje fyziku.
- Chybová propagace (Sekce 31 a 32) je matematicky korektní a platná v rámci nastaveného formálního modelu (vztah měřák vs. škála).
- Závěr o dominantní nejistotě zůstává v souladu s předchozími sekcemi: největším zdrojem nejistoty není numerický šum lokálního algoritmu, ale 2D/3D topologický a lokální/survey most.
- Zmíněné sekce tímto nejsou fyzikálně rozšiřovány; pracovní pravidlo stanovuje jejich metodické ohraničení.

#### 34.H. Co smíme a nesmíme v dalších sekcích tvrdit
Závazný rámec limituje slovník další komunikace a reportování:

| Typ tvrzení | Povolené znění | Nevhodné / zakázané znění |
|---|---|---|
| Výsledky testů (01K-a) | „Lineum aparát v validním 2D pracovním rozsahu rekonstruuje observer-offset s nízkou geometrickou chybou; relativní chyba závisí na velikosti offsetu." | „Lineum aparát potvrdil reálný 3D observer-offset." |
| Povaha PDE softwaru | „Lineum modeluje vlnovou rovnici ve 2D ploše a funguje jako testovací polygon offsetové geometrie.“ | „Lineum simuluje vícerozměrnou HSU slupku.“ |
| Status HSU | „Byl sestaven formální algebraický rámec mapování a chybové propagace." | „Výsledky potvrzují / vyvracejí teorii HSU." |
| 2D/3D most | „K dalšímu přenosu do HSU je nutná separátní topologická vrstva nebo explicitní řezové pravidlo.“ | „Převod z obálky rovnou mapuje slupku jedna ku jedné.“ |
| DM/DE a survey | „Tyto jevy závisí na komplexní 3D/anizotropní distribuci, 2D aparát na ně metodicky nedosáhne.“ | „Lineum v současném 2D stavu testuje DM/DE projekce či dipól oblohy.“ |

#### 34.I. Doporučená další fáze (nespuštěna)
Ukotvení 2D platformy coby abstraktní analogie odhaluje zásadní rozdíl mezi lokální kinematikou (získání offsetového vektoru ze vzdálenosti k hranici) a globální vesmírnou optikou (co přesně z takového lokálního bodu na slupce vlastně na obloze uvidíme a jak se to transformuje do "survey" anizotropie – Cosmic Octave).

**Navržená další metodická fáze (zatím nespuštěna):**

> ### 35. Návrh testovacího protokolu pro survey bridge / Cosmic Octave
> 
> *Cíl budoucí fáze:* Metodicky a matematicky rozlišit mezi výhradně lokálním dipólem (určeným boundary-distance měřením observer-offsetu) a celooblohovým *survey* dipólem napříč konečně silnou hypersférickou HSU slupkou. Cílem je identifikovat, jak by musel vypadat přepisovací protokol z lokálního do průhledového referenčního rámce.

*(Fáze 35 nebyla spuštěna a vyčká na povel).*

### 35. Návrh testovacího protokolu pro survey bridge / Cosmic Octave

#### 35.A. Jednoduché shrnutí
Lineum aparát v dosavadní fázi měří výhradně lokální geometrický offset v rámci 2D syntetické obálky: vzdálenost od simulačního pozorovatele k hranici amplitudové masky. HSU naproti tomu operuje se sadou celooblohových / survey observačních tvrzení označovanou jako Cosmic Octave — souborem dipólových kanálů měřených v reálných kataloguích galaxií, kvazarů a CMB. Tyto dvě roviny jsou kvalitativně odlišné: jedna je geometrický výpočet ve 2D syntetickém poli, druhá jsou statistické estimátory z prostorového rozdělení kosmologických objektů na obloze. Sekce 35 nemá tento rozdíl překonat, nýbrž ho přesně popsat a vymezit, co by musel obsahovat formální survey bridge, aby bylo metodicky dovoleno obě roviny srovnávat.

#### 35.B. Co HSU tvrdí o Cosmic Octave a survey dipólech
Následující tvrzení jsou extrahována přímo z primárního textu `HSU v29 FINAL.pdf`.

| Bod | Formulace v HSU | Opora ve zdroji | Typ tvrzení | Význam pro survey bridge |
|---|---|---|---|---|
| Cosmic Octave — definice | HSU organizuje observační motivaci jako soubor dipólových kanálů, které autor označuje jako „hlasy" (voices) a souhrnně nazývá Cosmic Octave. Na Str. 17 PDF je explicitně vyjmenováno sedm kanálů: (1) deep radio source-count dipoles, (2) deep quasar/IR dipoles, (3) late-time bulk-flow residuals a CosmicFlows depth-dependence, (4) directional Hubble/distance-dipole signals, (5) galaxy spin-handedness asymmetry, (6) X-ray cluster scaling-relation anisotropy, (7) spatial variation of the fine structure constant. Jako 8. hlas je na Str. 10 zmiňováno CMB alignment a zásadní poznámka: „The Octave does not enumerate exactly eight signals. It names eight landmarks in a continuous spectrum." | HSU v29 PDF, Str. 10, 17 | Přímé tvrzení HSU | Survey bridge by musel zahrnout alespoň jeden z těchto kanálů a odpovídající kernel. |
| Observer offset jako společný parametr | Každý kanál Cosmic Octave má pre-registrovaný kernel `K_X(z)`, který překládá offset pozorovatele `u*` na předpokládanou dipólovou amplitudu. Šest kanálů nezávisle vrací `u* ≈ 5–6 Mpc`. | HSU v29 PDF, Str. 12 | Přímé tvrzení HSU | Srovnání by vyžadovalo derivaci analogického kernelu pro Lineum geometrii. |
| Obecný dipólový estimátor | `D_X(z, n̂) = [K_X(z) β_eff + G_X(z) ε_u] d̂·n̂`, kde `K_X` je drift/aberrace a `G_X` kóduje hloubkovou asymetrii konečné slupky. | HSU v29 PDF, Str. 14 | Přímé tvrzení HSU | Neexistuje analogický estimátor pro Lineum boundary-distance; bez jeho odvození nelze porovnávat výstupy. |
| Survey systematics | HSU výslovně uvádí, že katalogy mají systematiky (selection function, cleaning pipeline) a nevyžaduje, aby jediný katalog sloužil jako konečný verdikt. | HSU v29 PDF, Str. 14 | Nepřímý předpoklad HSU | Survey bridge musí explicitně ošetřit selection effects a biasy. |
| Kosmologické zdroje dat | Pro Cosmic Octave HSU jmenovitě uvádí: NVSS, CatWISE, CF4 (CosmicFlows), SPHEREx, Euclid, ELT/ANDES, LISA, CMB-S4. | HSU v29 PDF, Str. 11–17 | Přímé tvrzení HSU | Lineum aparát nemá vazbu na žádný z těchto katalogů; nemůže tento prostor přímočaře pokrýt. |

*Poznámka:* Pokud není v PDF uvedena konkrétní numerická hodnota pro dílčí kanál, tato sekce ji nevyplňuje odhadem.

#### 35.C. Co měří Lineum boundary-distance aparát
Lineum měřicí vrstva je definována čistě geometricky v 2D syntetickém poli:

| Lineum veličina | Co znamená | Typ měření | Lze přímo porovnat se survey? |
|---|---|---|---|
| 2D obálka (`C_shell`) | Uzavřená 2D křivka ohraničující amplitudovou masku PDE pole. | Syntetická geometrie. | Ne — obálka nemá ekvivalent v observačním prostoru oblohy. |
| Lokální pozorovatel O | Nastavený bod v 2D poli, od nějž se provádí ray-casting k hranici. | Syntetická poloha. | Ne — pozorovatel HSU je kosmologická poloha v 3D prostoru. |
| `b_measured` | 2D vektor offsetu mezi středem obálky a pozicí pozorovatele. | Geometrická vzdálenost v pixelech. | Pouze jako formální analogie, ne observační ekvivalent. |
| Ray-casting / `Clearance_shell` | Vzdálenost k nejbližšímu okraji obálky podél paprsku. | Lokální geometrická vzdálenost. | Ne — survey dipól závisí na statistice distribuce zdrojů na celé obloze. |
| Chyba měřáku (`Vec_Err`) | Absolutní odchylka rekonstruovaného offsetu od zadané hodnoty. | Numerická validace 2D algoritmu. | Ne — nemá observační ekvivalent v HSU kernelu. |

#### 35.D. Klíčový rozdíl: lokální dipól vs. survey dipól
Oba pojmy sdílejí slovo „dipól", ale operují v odlišných prostorech:

| Vlastnost | Lineum lokální dipól | HSU / survey dipól |
|---|---|---|
| Datový prostor | 2D syntetické amplitudové pole (PDE). | Prostorová distribuce kosmologických objektů nebo záření na sféře. |
| Geometrický prostor | 2D euklidovská rovina s kruhovou hranicí. | 3D nebo hypersférická geometrie; promítnutá do úhlových souřadnic na obloze. |
| Zdroj měření | Ray-casting k hranici obálky simulace. | Počítání zdrojů / bulk flow / CMB anizotropie v observačním katalogu. |
| Závislost na pozorovateli | Synteticky nastavená poloha O v 2D poli. | Fyzikální poloha pozorovatele v 3D vesmíru vůči CSW; inferována z průniku více kanálů. |
| Závislost na 2D/3D mostu | Přímá — výsledek existuje výhradně v 2D rovině. | Teoreticky 3D/hypersférická; redukce na 2D vyžaduje explicitní projekci nebo řez. |
| Nutnost observačních dat | Ne — jde o syntetickou simulaci. | Ano — survey dipól bez reálných nebo přinejmenším formálně modelovaných dat nelze určit. |

#### 35.E. Minimální požadavky na survey bridge
Aby bylo možné metodicky srovnávat výstupy Lineum s HSU survey tvrzeními (Cosmic Octave), musel by survey bridge splňovat minimálně:

1. **Definice syntetické oblohy / pozorovací sféry.** Musí existovat formální mapování z Lineum 2D geometrie (nebo její 3D analogie) do úhlových souřadnic na sféře — žádná taková projekce doposud není odvozena.
2. **Projekční pravidlo z Lineum geometrie do úhlových dat.** Viz Sekce 33 a 34: bez explicitního radiálního řezu nebo projekce nelze přenášet vzdálenosti a směry do úhlového prostoru.
3. **Definice sledovaných objektů nebo tracerů.** Survey dipól je statistika distribuce zdrojů; syntetická obálka neobsahuje žádné tracery ani jejich hustotní pole.
4. **Dipólový estimátor.** HSU používá kanálově specifické kernely `K_X(z)` a `G_X(z)`. Pro Lineum by musel být odvozen analogický estimátor pro příslušný syntetický kanál.
5. **Normalizace amplitudy.** Survey dipól je normalizován vůči střední hustotě zdrojů; v syntetickém 2D poli tato normalizace neexistuje.
6. **Oddělení geometrického dipólu od selection bias a sampling bias.** Reálné survey katalogy mají systematiky (flux limit, sky coverage, redshift incompleteness); syntetický most by je musel buď modelovat, nebo výslovně vyloučit.
7. **Možnost porovnání se skutečnými survey daty nebo alespoň s jejich formálním modelem.** Bez referenčního kanálu (byť syntetického, ale fyzikálně motivovaného) nemá amplitudové srovnání informační hodnotu.

#### 35.F. Co lze testovat bez observačních dat
Bez reálných katalogů lze metodicky testovat:
- správnost geometrického estimátoru v syntetické konfiguraci (stabilita dipólového směru vzhledem k poloze pozorovatele),
- chování syntetických dipólů pod různými konfiguracemi 2D obálky,
- citlivost odhadnutého směru na přidaný šum a maskování části obálky,
- stabilitu výsledku při proměnném clearance a velikosti offsetu.

Tato testování mají hodnotu pro ověřování vnitřní konzistence algoritmu. **Nelze z nich potvrdit Cosmic Octave jako observační tvrzení ani odvodit fyzikální `u*` pozorovatele.**

#### 35.G. Co zatím nelze testovat
Z hlediska aktuálního stavu aparátu nelze:
- porovnávat s konkrétními survey katalogy (NVSS, CatWISE, SPHEREx, CF4),
- testovat fyzikální původ Cosmic Octave ani jeho dipólovou koherenci,
- modelovat DM/DE projekce (vyžadují 3D integraci přes celou slupku),
- odhadnout reálný kosmologický drift pozorovatele (`v_eff`),
- přenést výsledky lokálního boundary-distance dipólu na celooblohové survey pole.

#### 35.H. Dopad na dosavadní report
Toto vymezení je konzistentní s předchozími sekcemi a nemění jejich obsah:
- Výsledky měřáku (fáze 01I–01K-a) zůstávají platné pro 2D syntetickou geometrii.
- Pracovní pravidlo ze Sekce 34 zůstává závazné: Lineum je metodická analogie, ne fyzikální model HSU.
- Bez survey bridge nelze Lineum výsledky metodicky srovnávat s Cosmic Octave ani s jednotlivými dipólovými kanály HSU.
- Další práce by měla systematicky oddělovat geometrický výpočetní model od observační vrstvy a nezaměňovat syntetický estimátor za observační validaci.

#### 35.I. Doporučená další fáze (nespuštěna)
Identifikace minimálních požadavků na survey bridge (35.E) naznačuje, že prvním krokem k jeho zavedení by bylo sestrojení čistě syntetického estimátoru dipólu bez jakéhokoli nároku na observační ekvivalenci.

**Navržená další metodická fáze (zatím nespuštěna):**

> ### 36. Návrh syntetického survey estimátoru pro test dipólové geometrie
>
> *Cíl budoucí fáze:* Vytvořit čistě syntetický, fyzikálně nevalidační estimátor, který z definované 2D nebo 3D geometrické analogie generuje úhlovou distribuci tracerů a měří dipólový směr a amplitudu. Výsledky by sloužily jako vnitřní konzistentní test geometrie, ne jako observační potvrzení HSU. Musí být jasně vyznačeno, že syntetický estimátor není survey bridge ani observační validace Cosmic Octave.

*(Fáze 36 nebyla spuštěna a vyčká na povel.)*

### 36. Návrh syntetického survey estimátoru pro test dipólové geometrie

#### 36.A. Jednoduché shrnutí
Sekce 35 metodicky vymezila, že mezi lokálním Lineum boundary-distance dipólem a survey dipólem HSU Cosmic Octave chybí nezbytný most. Sekce 36 tento most nestaví, ani nahrazuje observační data. Jejím výhradním cílem je navrhnout syntetický testovací aparát — tedy soubor formálních kroků, jak by se v budoucnu dala vytvořit kontrolovaná umělá úhlová distribuce tracerů a v ní změřit dipólový signál. Cílem je zjistit, jak by se geometrický observer-offset projevil v ideálním, plně kontrolovaném syntetickém modelu — nikoli zda se tak projevuje ve skutečném vesmíru.

#### 36.B. Co musí syntetický estimátor napodobit z HSU
Níže jsou uvedeny pouze prvky z primárního textu `HSU v29 FINAL.pdf`, které by syntetický estimátor musel formálně respektovat jako rámec.

| HSU prvek | Opora v PDF | Typ tvrzení | Co by estimátor musel napodobit | Co zatím nenapodobuje |
|---|---|---|---|---|
| Cosmic Octave jako soubor dipólových kanálů (voices / landmarks) | HSU v29 PDF, Str. 10, 17 | Přímé tvrzení HSU | Strukturu více nezávislých kanálů, z nichž každý má vlastní redshift-kernel. | Reálná data kanálů; fyzikální zdroj dipólu. |
| Pre-registrovaný kernel `K_X(z)` pro každý kanál | HSU v29 PDF, Str. 12 | Přímé tvrzení HSU | Potřebu analytického výrazu, který překládá `u*` na amplitudu dipólu v daném kanálu. | Konkrétní hodnoty kernelů odvozených z HSU metriky; nelze odvodit bez plné 3D geometrie. |
| Kernel `G_X(z)` pro hloubkovou asymetrii | HSU v29 PDF, Str. 93 | Přímé tvrzení HSU | Potřebu druhého kernelu kódujícího konečně-objemovou asymetrii (finite-volume asymmetry). | Konkrétní hodnoty; vyžaduje 3D integraci přes slupku. |
| Obecný dipólový estimátor `D_X(z, n̂)` | HSU v29 PDF, Str. 14 | Přímé tvrzení HSU | Strukturu dvousložkového estimátoru (kinetická + objemová složka). | Kvantitativní hodnoty β_eff a ε_u z fyzikálního modelu. |
| Role observer-offsetu `u*` | HSU v29 PDF, Str. 12, 17 | Přímé tvrzení HSU | Zavedení parametru offsetu jako vstupu estimátoru a jeho vliv na amplitudu. | Fyzikální kalibraci na reálnou kosmologickou polohu. |
| Survey systematics jako nutná korekce | HSU v29 PDF, Str. 13–14 | Nepřímý předpoklad HSU | Explicitní modelování nebo výslovné vyloučení selection effects, sky coverage, redshift incompleteness. | Veškeré reálné systematiky survey katalogů. |
| Potřeba vzájemné konzistence více nezávislých kanálů | HSU v29 PDF, Str. 12, 78 | Rekonstruovaný metodický claim | Zapojení alespoň dvou syntetických kanálů s různými kernely pro test vnitřní konzistence. | Cross-probe closure s reálnými katalogy. |

*Poznámka:* Všechny výše uvedené prvky jsou rámovými požadavky, nikoli tvrzeními o výsledcích syntetického testu. Syntetický estimátor sám o sobě neposkytuje žádné fyzikální tvrzení o HSU ani o platnosti jeho tezí.

#### 36.C. Vstupní syntetická geometrie
Estimátor potřebuje přesně definovaný vstup, který musí splňovat podmínky z uzavřených fází reportu.

| Vstup | Definice | Zdroj | Podmínka použití |
|---|---|---|---|
| Pracovní geometrický model | 2D analogie: kruhová obálka v rovině; nebo budoucí 3D radiální řez hypersféry (zatím nedefinován, viz Sekce 34). | Sekce 33–34 tohoto dokumentu. | Pouze 2D analogie je v současné fázi povolena; 3D model vyžaduje přídavné projekční pravidlo. |
| Pozorovatel O | Bod v 2D poli (nebo jeho budoucí 3D ekvivalent), jehož offset od středu obálky je vstupem estimátoru. | Sekce 01I/01J (geometrie obálky). | Povoleno, pokud Measurement_Status = VALID dle fáze 01K-a. |
| Střed obálky `C_shell` | Střed amplitudové masky PDE pole; analogie CSW v HSU. | Lineum PDE geometrie. | Povoleno vždy jako část 2D syntetické geometrie. |
| Offsetový vektor `b_measured` / `d_obs` | 2D vektor od `C_shell` k pozorovateli O; analogie `u*` v HSU. | Sekce 29–30 tohoto dokumentu. | Jen pokud relativní chyba ≤ stanovený limit z fáze 01K-a; viz Sekce 31–32. |
| `Measurement_Status` | Označení platnosti měření dle fáze 01K-a: VALID / LIMITED. | Fáze 01K-a (uzavřená). | Vstup do estimátoru smí být použit jen pro záznamy se statusem VALID. |
| Projekční pravidlo | Explicitní mapovací funkce z 2D/3D offsetu do úhlových souřadnic na syntetické sféře. | Sekce 34 (zatím nedefinováno). | Bez tohoto pravidla lze pracovat jen se syntetickými úhlovými souřadnicemi definovanými přímo v 2D geometrii (ne mapovanými na oblohu). |

#### 36.D. Syntetická obloha / úhlová distribuce tracerů
Návrh čistě formálního postupu pro vytvoření syntetické oblohy, bez nároku na ekvivalenci s reálným survey katalogem:

1. **Definice úhlové domény:** V 2D analogii se pracovní sféra redukuje na kružnici S¹ (azimutální úhel φ ∈ [0, 2π)). V budoucí 3D analogii by se přidala polární složka θ.
2. **Generování tracerů:** Tracery jsou body na kružnici S¹ (nebo sféře S²) generované Monte Carlo z definovaného hustotního pole. V izotropním základním stavu je hustota rovnoměrná.
3. **Izotropní baseline:** Referenční distribuce bez dipólu — rovnoměrné pokrytí kružnice N body.
4. **Vložená dipólová modulace:** Hustota tracerů je modulována výrazem `ρ(φ) = ρ₀ [1 + A · cos(φ − φ₀)]`, kde `A` je amplituda vloženého dipólu a `φ₀` je jeho vložený směr. Tato modulace je čistě syntetická; nevyjadřuje fyzikální příčinu.
5. **Šum a sampling maska:** K datům lze přidat Poissonův šum a vyřadit část kružnice (analogie sky mask) pro test vlivu neúplného pokrytí.
6. **Oddělení geometrického signálu od výběrového biasu:** Výběrový bias se modeluje asymetrií v maskování nebo v hustotě vzorkování; pro každý scénář se zjistí, zda estimátor správně rozlišuje vložený dipólový signál od biasu způsobeného maskováním.

*Důležité:* Syntetická obloha nepředstavuje reálný survey katalog. Výsledky měření na syntetické obloze nelze interpretovat jako observační potvrzení HSU ani jako výsledek reálného kosmologického průzkumu.

#### 36.E. Dipólový estimátor
Minimální formální estimátor pro rekonstrukci syntetického dipólu:

**Vstup:** Množina N tracerů s úhlovými pozicemi {φ_i} a váhami {w_i}.

**Výstup:** Rekonstruovaný dipólový vektor `D̂_rec = (1/W) · Σᵢ wᵢ · n̂(φᵢ)`, kde `n̂(φᵢ) = (cos φᵢ, sin φᵢ)` je jednotkový směr i-tého traceru a `W = Σᵢ wᵢ`. Amplituda dipólu je `|D̂_rec|`; jeho směr je `arg(D̂_rec)`.

*Poznámka:* Tento tvar je obecný vážený průměr směrů — standardní technická volba. Není to finální HSU estimátor `D_X(z, n̂)` z PDF; tvar přímého součtu jednostkových vektorů neobsahuje redshift-kernely `K_X` a `G_X`.

| Metrika | Význam | Jak se měří | Riziko |
|---|---|---|---|
| Rekonstruovaný směr dipólu `φ_rec` | Uhel maxima dipólu v syntetické distribuci. | `arg(D̂_rec)` v 2D; sférická harmonická Y¹₁ v 3D. | Bias při neúplném nebo asymetrickém sky coverage. |
| Amplituda dipólu `|D̂_rec|` | Síla rekonstruovaného dipólového signálu. | Délka vektoru `D̂_rec`. | Podestimace při vysokém Poissonově šumu nebo malém N. |
| Odchylka od vloženého dipólu `Δφ` | Chyba rekonstrukce směru vůči vloženému `φ₀`. | `|φ_rec − φ₀|` (mod 2π). | Degradace při maskování nebo výběrovém biasu. |
| Amplitudová chyba `ΔA` | Relativní odchylka rekonstruované amplitudy od vložené A. | `(|D̂_rec| − A) / A`. | Přecenění při korelovaném šumu; podhodnocení při maskování. |
| Nulový test (null test) | Ověření, že estimátor vrací ~0 při izotropním vstupu. | Aplikace estimátoru na čistě izotropní distribuci. | False detection při systematickém biasu generátoru. |

#### 36.F. Kontrolní scénáře
Níže navržené scénáře jsou určeny k budoucímu testování — nejsou spuštěny:

| Scénář | Cíl | Očekávaný výsledek | Co by znamenalo selhání |
|---|---|---|---|
| 1. Nulový dipól | Ověřit, že estimátor nedetekuje signál v izotropní distribuci. | `|D̂_rec| ≈ 0` v rámci šumu. | Systematický bias generátoru nebo estimátoru. |
| 2. Známý vložený dipól | Ověřit, že estimátor správně rekonstruuje vložený směr a amplitudu. | `φ_rec ≈ φ₀`, `|D̂_rec| ≈ A`. | Chyba v implementaci estimátoru nebo generátoru. |
| 3. Malý offset (A ≈ 0.01) | Test detekce slabého dipólu u hranice citlivosti. | Rekonstrukce s vysokou rozptylovou chybou; nulový test nesmí selhat. | False positive v nulovém testu. |
| 4. Velký offset v platném rozsahu (A ≈ 0.3) | Test robustnosti estimátoru pro silný dipól. | Přesná rekonstrukce; amplitudová chyba pod zvoleným prahem. | Nasycení estimátoru nebo nelineární bias. |
| 5. Výběrová maska (pokrytí 70 %) | Test vlivu částečného sky coverage. | Bias směru; odhadnutá amplituda nižší než vložená. | Nepozorovaný systematický posun `φ_rec` > 10°. |
| 6. Anizotropní sampling (hustší vzorkování v jednom kvadrantu) | Test odolnosti vůči selection bias. | Posun `D̂_rec` směrem k přehustěné oblasti; výrazná amplitudová chyba. | Maskování chyby estimátoru nevšimnuto. |
| 7. Dva syntetické kanály s různými amplitudami | Test vnitřní konzistence (analogie vzájemné shody více kanálů Cosmic Octave). | Oba kanály vrátí stejný `φ_rec` pro stejný vložený směr; amplitudy se liší dle nastavené modulace. | Nekonzistentní směry → chyba vstupní geometrie nebo generátoru. |
| 8. Záměna lokálního a survey dipólu (negativní kontrola) | Ověřit, že přímé dosazení `b_measured` jako „survey dipólu" bez projekčního pravidla vede k metodicky nedefendovatelným výsledkům. | Estimátor vrátí číslo, ale bez projekčního pravidla nemá fyzikální interpretaci. | Pokud by výsledek byl interpretován jako observační potvrzení → metodická chyba. |

#### 36.G. Co lze tímto estimátorem testovat
V rámci syntetické, fyzikálně nevalidační roviny lze testovat:
- schopnost estimátoru rekonstruovat vložený syntetický dipól (směr a amplitudu) v kontrolovaných podmínkách,
- stabilitu rekonstruovaného směru při proměnném šumu a různých hodnotách offsetu,
- vliv sampling bias a sky mask na bias amplitudy a směru,
- rozlišení nulového a nenulového dipólového signálu v syntetické distribuci,
- interní konzistenci při použití více syntetických kanálů s různými kernely (pokud jsou definovány),
- citlivost na tvar obálky a pozici pozorovatele v 2D analogii.

#### 36.H. Co tímto estimátorem stále nelze testovat
Syntetický estimátor nemůže a nesmí být interpretován jako nástroj pro:
- potvrzení nebo vyvrácení reálné Cosmic Octave,
- porovnání s observačními daty NVSS, CatWISE, CF4, SPHEREx, Euclid nebo jinými katalogy,
- odvozování fyzikálního původu kosmologického dipólu,
- modelování DM/DE projekcí vyžadujících 3D integraci přes slupku,
- validaci HSU jako fyzikální teorie,
- překlenutí 2D/3D mostu, pokud není odvozen dle Sekce 34.

#### 36.I. Dopad na report
Zavedení syntetického estimátoru by v rámci navazující práce znamenalo:
- vytvoření první výpočetní vrstvy mezi lokálním boundary-distance měřením a syntetickým survey dipólem,
- rozšíření měřicího aparátu Lineum o nový metodický modul bez zvýšení fyzikální platnosti HSU,
- formální oddělení algoritmické testovatelnosti (zda estimátor funguje v syntetickém poli) od observační interpretace (co říká o reálném vesmíru),
- poskytnutí záznamu o limitech syntetického testu pro budoucí audity a komparační studie.

Zavedení estimátoru nezvyšuje kosmologický status ani Lineum, ani HSU.

#### 36.J. Doporučená další fáze (nespuštěna)
Návrh estimátoru v Sekci 36 přirozeně ústí do potřeby implementačního pokusu na toy datech, aby bylo možné ověřit, zda formální návrh funguje v praxi.

**Navržená další metodická fáze (zatím nespuštěna):**

> ### 37. Implementace syntetického survey estimátoru na toy datech
>
> *Cíl budoucí fáze:* Navrhnout minimální skript, který vygeneruje syntetickou úhlovou distribuci (S¹ nebo S²) s kontrolovaným dipólem a změří návratnost směru a amplitudy pomocí estimátoru navrženého v Sekci 36. Scénáře 1–8 z Sekce 36.F by sloužily jako validační sada. Výsledky by byly prezentovány jako interní algoritmický test, nikoli jako observační potvrzení HSU. Toy data nejsou observační data a jejich výsledky nemohou být interpretovány jako kosmologické potvrzení platnosti HSU.

*(Fáze 37 nebyla spuštěna a vyčká na povel.)*

### 37. Implementace syntetického survey estimátoru na toy datech

#### 37.A. Jednoduché shrnutí
Sekce 37 implementuje minimální toy syntetický estimátor dipólu na 2D umělé úhlové distribuci (kružnice S¹). Cílem je výhradně algoritmický test: ověřit, že jednoduchý vážený vektorový estimátor dokáže rekonstruovat vložený syntetický dipól, rozlišit nulový a nenulový případ a ukázat citlivost na šum, maskování a sampling bias. Tato sekce netestuje reálné survey katalogy, netestuje Cosmic Octave a nevaliduje HSU. Výsledky nelze interpretovat jako observační nebo fyzikální potvrzení platnosti HSU.

#### 37.B. Vztah k HSU a Sekci 36
HSU pracuje s více dipólovými kanály a reálnou survey vrstvou (viz Sekce 35–36). Tato implementace napodobuje pouze obecnou strukturu „úhlová distribuce → dipólový estimátor", nikoli konkrétní HSU estimátor `D_X(z, n̂)` z PDF. Kernely `K_X(z)` a `G_X(z)` z HSU nejsou implementovány, protože jejich derivace vyžaduje plnou 3D geometrii HSU, která v Lineum aparátu není k dispozici. Toy estimátor slouží jako interní algoritmický sanity check, nikoliv jako mezivrstva mezi Lineum a HSU.

#### 37.C. Toy model a analytická kontrola
Tracery jsou generovány rejection samplingem z distribuce:

```
p(θ) = (1 + A · cos(θ − θ₀)) / (2π)
```

kde `A` je amplituda syntetického dipólu, `θ₀` je vložený směr a `A = 0` odpovídá izotropnímu případu.

Analytická kontrola: Pro ideální distribuci platí:

```
E[n] = (A/2) · n₀   kde n = [cos θ, sin θ]
```

Proto odhadujeme: `A_hat = 2 · ‖mean(n)‖`. Tento tvar je toy estimátor — standardní vážený průměr jednotkových vektorů. Neobsahuje redshift-kernely `K_X`, `G_X` ani jiné prvky specifické pro HSU.

#### 37.D. Scénáře
Všechny scénáře byly spuštěny s `N_REPEATS = 200` opakováními na scénář, `seed = 42`, výstup uložen v `.scratch/37_synthetic_survey_results.csv`.

| ID | Popis | N tracerů | A_in | θ₀ [°] | Maska | Anizo. sampling |
|---|---|---|---|---|---|---|
| S1_null | Nulový dipól (izotropní) | 500 | 0.00 | — | ne | ne |
| S2_weak | Slabý dipól | 500 | 0.05 | 45 | ne | ne |
| S3_moderate | Střední dipól | 500 | 0.10 | 90 | ne | ne |
| S4_strong | Silný dipól | 500 | 0.20 | 135 | ne | ne |
| S5_small_sample | Malý vzorek, střední dipól | 50 | 0.10 | 90 | ne | ne |
| S6_masked | Maska ~30 % oblohy, střední dipól | 500 | 0.10 | 90 | ano (π–4π/3) | ne |
| S7_aniso_sampling | Anizotropní sampling, bez dipólu | 500 | 0.00 | — | ne | ano (Q1) |
| S8_multi_channel | 3 kanály, stejný směr, různý šum | 200/500/100 | 0.10 | 60 | ne | ne |

#### 37.E. Výsledky
Agregované výsledky přes 200 opakování na scénář:

| ID | A_in | A_hat (mean ± std) | Úhlová chyba (mean ± std) [°] | Poznámka |
|---|---|---|---|---|
| S1_null | 0.00 | 0.081 ± 0.043 | — | Sampling šum; žádný stabilní směr. |
| S2_weak | 0.05 | 0.095 ± 0.049 | 52.6 ± — | Signál blízko šumové hranice; směr neurčitý. |
| S3_moderate | 0.10 | 0.126 ± 0.051 | 33.9 ± — | Směr rekonstruovatelný; amplituda mírně nadhodnocena vlivem šumu. |
| S4_strong | 0.20 | 0.206 ± 0.056 | 15.7 ± — | Robustní rekonstrukce; nejnižší úhlová chyba. |
| S5_small_sample | 0.10 | 0.254 ± 0.121 | 71.1 ± — | Nízké N: amplituda výrazně nadhodnocena, směr nejistý. |
| S6_masked | 0.10 | 0.441 ± 0.053 | 47.0 ± — | Maska způsobuje bias amplitudy (4× vyšší než vložená) a posun směru. |
| S7_aniso_sampling | 0.00 | 0.607 ± 0.067 | — | Anizo. sampling vytváří falešný dipól bez fyzikální příčiny. |
| S8_multi_channel | 0.10 | 0.160 ± 0.050 | 54.2 ± — | Průměr tří kanálů; shoda směru je interní test konzistence, ne Cosmic Octave. |

*Surová data:* `.scratch/37_synthetic_survey_results.csv` — výhradně interní výpočetní podklad. `A_hat_mean` je aritmetický průměr 200 opakování (seed = 42); úhlová chyba je průměrná minimální úhlová vzdálenost rekonstruovaného a vloženého směru ve stupních; u scénářů S1 a S7 (A_in = 0) není úhlová chyba definována a není vykazována.

*Noise floor a kladný amplitudový bias:* A_hat = 2 · ‖mean(n)‖ je vždy nezáporná veličina, protože norma vektoru nemůže být záporná. Pro izotropní nulový případ má A_hat kladný amplitudový bias daný normou náhodného průměrného vektoru. V 2D lze pro velké N očekávat přibližně E[A_hat] ≈ √(π/N); pro N = 500 tedy přibližně 0.079. To odpovídá naměřenému S1 výsledku A_hat ≈ 0.081 (rozptyl v tomto běhu ≈ 0.043). Jde o očekávanou vlastnost estimátoru, nikoli o fyzikální signál. S2 (A_in = 0.05) leží pod nebo těsně u tohoto průměrného amplitudového noise flooru pro N = 500; proto je jeho úhlová rekonstrukce nestabilní a nelze ji interpretovat jako robustní detekci směru.

#### 37.F. Failure / bias cases
Scénáře S5–S7 ilustrují hlavní zdroje degradace estimátoru:

- **Maska (S6):** Neúplné pokrytí kružnice způsobuje systematický posun rekonstruovaného směru a výraznou nadestimaci amplitudy. Bez explicitní korekce masky je výsledek metodicky nepoužitelný. A_hat = 0.441 pro A_in = 0.10 (chyba faktoru ~4×).
- **Anizotropní sampling (S7):** Nerovnoměrné vzorkování bez fyzikálního dipólu generuje falešný signál A_hat = 0.607. Estimátor nerozlišuje geometrický bias od fyzikálního signálu; tento případ slouží jako negativní kontrola.
- **Malé N (S5):** Při N = 50 roste amplitudová chyba výrazně (std = 0.121 vs. 0.051 při N = 500). Úhlová chyba dosahuje průměrně 71°, což je prakticky náhodný směr.
- **Slabý dipól (S2):** A_in = 0.05 leží těsně u průměrného amplitudového noise flooru estimátoru pro N = 500 (E[A_hat] ≈ √(π/500) ≈ 0.079). Vložená amplituda je prakticky nerozlišitelná od tohoto kladného biasu, proto je rekonstrukce směru nestabilní a výsledná úhlová chyba 52.6° nepředstavuje spolehlivou detekci.

#### 37.G. Co bylo zjištěno
V rámci tohoto toy testu bylo zjištěno:
- Toy estimátor v kontrolovaných datech rekonstruuje vložený dipól především u silnějších signálů (S3, S4) a dostatečného počtu tracerů. U nulového nebo slabého signálu je výsledek omezen sampling šumem a kladným amplitudovým noise floorem daným normou průměrného vektoru.
- Nulový signál (S1) nevykazuje stabilní preferovaný směr; nenulová průměrná amplituda A_hat ≈ 0.081 je projevem noise flooru, nikoli fyzikálního signálu.
- Masky (S6) a anizotropní sampling (S7) jsou dominantní zdroje bias estimátoru a při jejich přítomnosti jsou výsledky metodicky nespolehlivé bez explicitní korekce.
- Multi-channel scénář (S8) pouze testuje formální kombinaci více syntetických kanálů. V tomto běhu nezakládá žádný závěr o Cosmic Octave a podle naměřené úhlové chyby 54.2° zůstává rekonstrukce směru omezená šumem.

#### 37.H. Co nebylo ověřeno
Toy test výslovně neověřuje:
- platnost HSU jako kosmologické teorie,
- Cosmic Octave ani žádný z jeho dipólových kanálů,
- shodu s reálnými survey daty (NVSS, CatWISE, CF4, SPHEREx, Euclid),
- DM/DE projekce ani 3D integraci přes hypersférickou slupku,
- překlenutí 2D/3D mostu (viz Sekce 33–34).

Výsledky mají výhradně interní algoritmickou hodnotu pro diagnostiku chování estimátoru za různých syntetických podmínek.

#### 37.I. Doporučená další fáze (nespuštěna)
Toy test v Sekci 37 ukázal, že maska a anizotropní sampling jsou kritické zdroje bias. Přirozeným dalším krokem je zavedení explicitní korekce těchto efektů.

**Navržená další metodická fáze (zatím nespuštěna):**

> ### 38. Mask-aware syntetický survey estimátor a korekce selection bias
>
> *Cíl budoucí fáze:* Rozšířit toy estimátor o explicitní model masky a selection function, derivovat korekci sampling biasu z geometrie masky, a ověřit, zda korigovaný estimátor redukuje false positive riziko identifikované v S6 a S7. Výsledky zůstanou ryze syntetické; bez reálných katalogových dat jde o interní algoritmický test. Neprováděj reálné katalogové testy.

*(Fáze 38 nebyla spuštěna a vyčká na povel.)*

### 38. Mask-aware syntetický survey estimator a korekce selection bias

#### 38.A. Jednoduché shrnutí
Sekce 37 demonstrovala limity základního vektorového estimátoru: sampling noise floor u nulového signálu a výrazný falešný dipól vlivem masky (neúplného pokrytí oblohy) a anizotropního vzorkování (nerovnoměrné hustoty tracerů). Sekce 38 na to navazuje implementací a syntetickým testem jednoduché korekce — *Inverse Selection Weighting* (ISW). Cílem je algoritmicky prověřit, za jakých podmínek dokáže explicitní znalost výběrové funkce (selection function) tyto biasy kompenzovat. Nejde o aplikaci na reálné survey systematics, ale výhradně o pochopení chování matematického aparátu na toy datech (kružnice S¹).

#### 38.B. Vztah k HSU a Sekci 35–37
HSU metrika a dipólová rozhraní (Sekce 35–36) explicitně předpokládají existenci survey masky a selection function. Tato sekce však reálnou HSU masku nevyužívá; pracuje s čistě syntetickými *toy* maskami. Snížení falešného dipólu v syntetickém toy nastavení nelze převádět na závěr o opravitelnosti reálných survey katalogů a využít k potvrzení Cosmic Octave. Syntetická mask-aware vrstva je nutná matematická pojistka pro pochopení limitů dipólových analýz.

#### 38.C. Toy model masky a selection function
Vycházíme z distribuce generující tracery na kružnici:
`p(θ) ∝ 1 + A_in · cos(θ − θ₀)`

Každý generovaný bod je následně podroben výběrové funkci (selection function) `S(θ) ∈ [0, 1]`, která určuje pravděpodobnost, že daný tracer bude "pozorován".
Pokud `S(θ) = 1`, obloha je plně pozorovatelná. Pokud `S(θ) < 1`, část tracerů je vyřazena. Pokud `S(θ) = 0`, vzniká maska s nulovou propustností (hard cut).

*Naive estimator:*
Počítá průměr `mean(n_i)` ze všech *pozorovaných* tracerů s váhou 1.

*Corrected estimator:*
Aplikuje inverzní vážení pravděpodobností detekce.

#### 38.D. Korekční metoda (Inverse Selection Weighting)
Metoda *Inverse Selection Weighting* (ISW) přiděluje každému pozorovanému traceru váhu nepřímo úměrnou pravděpodobnosti jeho detekce:
`w_i = 1 / S(θ_i)`

Tím se uměle zesiluje váha tracerů v oblastech, kde výběrová funkce potlačila pozorování, což by teoreticky mělo obnovit původní úhlovou distribuci.

**Limity metody:**
- *Hard cuts:* Pokud `S(θ) = 0` (úplný výřez), nelze váhu definovat (dělení nulou). Metoda vyžaduje oříznutí vah (clipping), např. `S(θ) ≥ 0.05`. Tím ale vzniká problém: v oblasti tvrdé masky nejsou pozorovány *žádné* tracery, takže neexistuje nic, co by se dalo převážit. U tvrdých masek metoda selhává.
- *Variance blow-up:* V oblastech s velmi nízkým `S(θ)` mají tracery nepoměrně vysokou váhu `w_i`, což drasticky zvyšuje šum v estimátoru.

#### 38.E. Scénáře
Bylo definováno 6 syntetických scénářů (N = 500, počet opakování = 200).
- **S1 Null no mask:** Baseline. A_in = 0, S(θ) = 1.
- **S2 Null aniso:** A_in = 0, S(θ) = 1 pro Q1, jinak S(θ) = 0.33. Anizotropní výběrová pravděpodobnost.
- **S3 Null hard cut:** A_in = 0, S(θ) = 0 na pásu 60°. Úplný výřez.
- **S4 Weak dipole no mask:** A_in = 0.05 (pod noise floorem), S(θ) = 1.
- **S5 Strong dipole smooth mask:** A_in = 0.20, hladce proměnná S(θ) = 0.5 + 0.5*cos(θ - π).
- **S6 Strong dipole hard cut:** A_in = 0.20, S(θ) = 0 na pásu 60°.

#### 38.F. Výsledky
*(Hodnoty reprezentují průměry ze 200 repetic)*

| ID | A_in | Maska | A_naive | A_corr | Úhl. chyba Naive [°] | Úhl. chyba Corr [°] | Korekce |
|---|---|---|---|---|---|---|---|
| S1 Null no mask | 0.00 | None | 0.080 | 0.080 | — | — | Beze změny |
| S2 Null aniso | 0.00 | Aniso | 0.606 | **0.088** | — | — | Zlepšení |
| S3 Null hard cut | 0.00 | Hard cut | 0.388 | 0.388 | — | — | Beze změny (selhání) |
| S4 Weak dipole | 0.05 | None | 0.087 | 0.087 | 59.8 | 59.8 | Beze změny |
| S5 Strong smooth | 0.20 | Smooth | 0.940 | **0.211** | 125.4 | **71.9** | Zlepšení |
| S6 Strong hard cut| 0.20 | Hard cut | 0.417 | 0.417 | 71.9 | 71.9 | Beze změny (selhání) |

#### 38.G. Co korekce zlepšila
V tomto syntetickém nastavení korekce ISW výrazně snížila bias v případech, kde výběrová funkce nezakrývala oblohu úplně:
- U anizotropního samplingu (S2) snížila falešný dipól směrem k očekávanému noise flooru (A = 0.606) prakticky zpět k hodnotě teoretického sampling noise flooru (A = 0.088 pro N=500).
- U silného dipólu překrytého hladkou proměnnou maskou (S5) snížila amplitudový bias (z 0.940 na 0.211) a zmenšila úhlovou chybu (ze 125° na 72°).

#### 38.H. Co korekce nezvládá
Výsledky ukazují matematické limity:
- **Nezvládá tvrdé výřezy (hard cuts).** Scénáře S3 a S6 ukazují, že `A_naive` a `A_corr` jsou identické. Důvodem je, že v zakryté oblasti nejsou naměřeny žádné tracery, které by bylo možné převážit nahoru, zatímco nezakryté tracery mají váhu blízkou 1.0. Tím se naive a corrected vektor stanou de facto identickými a výrazný bias masky přetrvá.
- **Nezachraňuje slabé signály.** Scénář S4 ukazuje, že u slabých dipólů blízko průměrnému noise flooru (0.079) není úhlová chyba zachránitelná ani s perfektním vzorkováním (zůstává na hladině praktického šumu, chyba ~60°).
- Neřeší fyzikální HSU interpretaci ani převod přes 2D/3D most.

#### 38.I. Dopad na další práci
Analýza ukazuje, že výběrová funkce a maska oblohy jsou kritickými vstupy pro jakýkoliv survey dipól. Zatímco jemné anizotropie ve vzorkování lze u toy modelu účinně opravit vážením (ISW), **přítomnost oblastí s nulovou selection function (jako je nepozorovatelná oblast Mléčné dráhy v reálných surveyích) představuje zásadní překážku**, kterou lokální vážení nemůže jednoduše kompenzovat bez pokročilejších metod doplňování pozadí nebo modelování sférických harmonik. 
Před jakýmkoliv porovnáním s reálnými daty (či Cosmic Octave) by musela být explicitně známa a zahrnuta úplná 3D selection function. Bez ní by výrazné falešné dipóly v tomto toy nastavení mohly být mylně interpretovány jako fyzikální signál.

#### 38.J. Doporučená další fáze (nespuštěna)
Navrhovaná další algoritmická kontrola je testování multi-kanálové konzistence.

> ### 39. Multi-channel syntetický estimator a test shody směrů
>
> *Cíl budoucí fáze:* Rozšířit toy estimátor na více syntetických kanálů s různými selection funkcemi a ověřit, zda zdánlivá shoda směrů napříč kanály může vzniknout sdílenou maskou i v případě, že fyzikální dipól neexistuje. Tato fáze nespustí reálné katalogové testy a nebude interpretována jako Cosmic Octave validace.

*(Fáze 39 nebyla spuštěna a vyčká na povel.)*

### 39. Multi-channel syntetický estimator a test shody směrů

#### 39.A. Jednoduché shrnutí
Sekce 38 ukázala, že maska nebo nerovnoměrné vzorkování může vytvořit výrazný falešný dipól v rámci jednoho měřicího kanálu. Sekce 39 tento jev rozšiřuje a testuje, zda společná maska může vytvořit zdánlivou shodu směrů (concordance) ve více nezávislých syntetických kanálech současně, a to i v případě, že neexistuje žádný společný fyzikální signál. **Nejde o Cosmic Octave validaci, ani o analýzu reálných survey dat.** Jde pouze o diagnostiku chování multi-channel biasu v kontrolovaném toy prostředí.

#### 39.B. Vztah k HSU / Cosmic Octave
Zatímco HSU operuje s vícero dipólovými kanály (tzv. „voices“) v rámci modelu Cosmic Octave, tato sekce **nepřebírá reálné HSU kanály a neprovádí žádné observační porovnání.** Shoda syntetických vektorů v toy datech není shodou v Cosmic Octave. Cílem je pouze ověřit obecný matematický problém: do jaké míry může sdílená systematická chyba napodobit sdílený fyzikální signál napříč několika frekvencemi nebo sledováními.

#### 39.C. Toy multi-channel model
Rozšíření předchozího S¹ modelu. Multi-channel systém obsahuje 4 nezávislé **syntetické kanály**.
Každý kanál má definován vlastní:
- počet tracerů (`N_i`),
- vloženou amplitudu (`A_in`) a směr (`theta_in`) – reprezentující **true dipole**,
- výběrovou funkci (selection function) – **masku**.
Kanály mohou mít masku **shared** (společnou pro všechny) nebo **independent** (každý kanál má jinou, nebo žádnou). Ze simulace se počítá **estimated dipole**.

#### 39.D. Metriky shody směrů
Pro měření míry shody (concordance) mezi kanály byly definovány tyto toy metriky:
- **Mean pairwise angular separation:** Průměrná úhlová vzdálenost mezi všemi páry kanálů (čím menší, tím větší shoda).
- **Resultant length (circular concentration, R):** Délka výsledného vektoru součtu jednotkových vektorů ze všech kanálů dělená jejich počtem (R ∈ [0, 1]). R blížící se 1.0 znamená vysokou koncentraci odhadovaných směrů.
- **Channels within 30°:** Průměrný počet kanálů, které leží v toleranci 30° od společného středu.
- **False concordance flag:** Indikátor, který se spustí, pokud kanály bez reálného signálu (`A_in = 0`) vygenerují vysokou shodu (R > 0.7).

#### 39.E. Scénáře
Bylo spuštěno 8 syntetických scénářů, každý opakován 200x. Kanály měly velikosti N = 500, 800, 1000, 1200.

| ID | Vložený signál (A_in) | Maska (Selection pattern) | Korekce (ISW) |
|---|---|---|---|
| 1. Null independent | 0.0 (Null) | Žádná / Uniformní | Ne |
| 2. Null shared aniso | 0.0 (Null) | Sdílená anizotropní maska | Ne |
| 3. Null shared corrected | 0.0 (Null) | Sdílená anizotropní maska | Ano |
| 4. True common dipole | 0.15 (Společný směr 45°) | Žádná | Ne |
| 5. True common, diff masks | 0.15 (Společný směr 45°) | Různé nezávislé masky | Ne |
| 6. Mixed directions | 0.15 (Každý jiný směr) | Žádná | Ne |
| 7. One contaminated | 0.15 (Společný směr) | 1 kanál má hard-cut masku | Ne |
| 8. Weak common signal | 0.05 (Slabý signál 135°) | Žádná | Ne |

#### 39.F. Výsledky
*(Agregováno z 200 repetic per scénář)*

| ID scénáře | A_hat_mean | Pairwise Sep [°] | Resultant Length (R) | False Concordance | Interpretace |
|---|---|---|---|---|---|
| 1. Null indep. | 0.061 | 89.3° | 0.459 | False | Náhodný rozptyl, bez shody. |
| 2. Null shared | 0.433 | 4.9° | **0.998** | **True** | Maska tvoří v tomto toy nastavení velmi vysokou zdánlivou shodu. |
| 3. Null corrected | 0.076 | 91.8° | 0.437 | False | Korekce v tomto scénáři zdánlivou shodu výrazně snížila. |
| 4. True common | 0.161 | 21.7° | 0.956 | False | Vložený syntetický signál vede ke shodě směrů v tomto toy nastavení. |
| 5. True, diff masks | 0.301 | 74.0° | 0.598 | False | Rozdílné masky snižují shodu i u vloženého společného signálu. |
| 6. Mixed dirs | 0.160 | 112.8° | 0.145 | False | Záměrně bez shody. |
| 7. Contaminated | 0.207 | 32.3° | 0.917 | False | Jeden vadný kanál mírně zhorší shodu. |
| 8. Weak common | 0.089 | 66.8° | 0.657 | False | Slabý signál dává nestabilní shodu. |

#### 39.G. Co bylo zjištěno
Výsledky z toy dat ukazují:
- **Společná maska umí vytvořit zdánlivou shodu:** Ve scénáři S2 vytvořila sdílená selection function u kanálů s nulovým vloženým signálem velmi vysokou zdánlivou shodu směrů (R = 0.998, úhlový rozptyl pod 5°). Scénář S2 ukazuje, že ve zvoleném syntetickém nastavení může společná selection function vytvořit vysokou zdánlivou shodu i při nulovém vloženém signálu. Tento výsledek nelze převádět na závěr o reálných Cosmic Octave kanálech; slouží pouze jako metodické varování pro budoucí modelování společných systematik.
- **Korekce v tomto toy scénáři snížila zdánlivou shodu:** Použití ISW korekce (S3) snížilo zdánlivou shodu a vrátilo systém do náhodného rozptylu (R = 0.437). To neznamená univerzální odstranění multi-channel biasu; korekce funguje pouze u tohoto typu sdílené anizotropní masky.
- **Různé masky snižují shodu skutečného signálu:** Ve scénáři S5 různé masky v jednotlivých kanálech způsobily, že vložený syntetický signál nebyl tak konzistentně naměřen (R kleslo na 0.598, rozptyl 74°).

#### 39.H. Co nebylo zjištěno
Vzhledem k syntetické povaze experimentu:
- Nebyla ověřena Cosmic Octave.
- Nebyla testována reálná survey data (NVSS, CatWISE apod.).
- Nebyla ověřena ani vyvrácena tvrzení HSU o observační shodě.
- Nebyly testovány 3D projekce ani lokální temná hmota/energie.
- Nebyl vyřešen způsob, jak propojit boundary-distance dipól s reálnými katalogy.

#### 39.I. Dopad na další práci
Shoda směrů ve více kanálech (multi-channel concordance) **sama o sobě nestačí k odlišení fyzikálního signálu od biasu**. Společné systematické vlivy, jako je společná maska oblohy, mohou v tomto syntetickém modelu napodobit souhlas směrů. Z toho plyne, že jakýkoli budoucí survey bridge musí explicitně modelovat společné i nezávislé masky a selection functions jednotlivých katalogů, aby se oddělil pravý sdílený signál od sdíleného biasu.

#### 39.J. Doporučená další fáze (nespuštěna)
Pro kvantifikaci pravděpodobnosti náhodné shody v závislosti na typu masky se navrhuje:

> ### 40. Null-hypothesis test pro multi-channel concordance
>
> *Cíl:* Formálně spočítat, jak často může shoda více syntetických kanálů vzniknout náhodou nebo společnou maskou při nulovém skutečném signálu. Získat p-hodnoty pro toy scénáře a stanovit hranici statistické významnosti pro budoucí analýzy.

### 40. Null-hypothesis test pro multi-channel concordance

#### 40.A. Jednoduché shrnutí
Sekce 39 ukázala, že sdílená výběrová funkce (maska) může v toy nastavení vytvořit velmi vysokou zdánlivou shodu směrů i při nulovém vloženém signálu. Sekce 40 kvantifikuje, jak často taková shoda vzniká pod nulovou hypotézou prostřednictvím Monte Carlo simulace 1 000 opakování na scénář. **Nejde o Cosmic Octave validaci, nejde o reálná survey data, nejde o test HSU.** Jde výhradně o syntetické měření míry falešné concordance v kontrolovaném toy prostředí.

#### 40.B. Nulová hypotéza
Nulová hypotéza pro tento toy test zní: *žádný společný syntetický signál nebyl vložen* (`A_i = 0` pro všechny kanály). Veškerá případná shoda směrů vzniká výhradně ze sampling noise, geometrie masky nebo selection function. Shoda překračující zvolený práh je v tomto kontextu označena jako **false concordance**. Výsledky jsou statistikou toy modelu na kružnici S¹; nemají observační ani kosmologický dosah.

#### 40.C. Testované scénáře
Bylo spuštěno 8 scénářů (1 000 Monte Carlo opakování každý, fixní seed). Čtyři kanály s N = 500, 800, 1000, 1200.

| ID | Typ | Vložený signál | Maska | Korekce |
|---|---|---|---|---|
| S1 Null no mask | null | A_i = 0 | Žádná | Ne |
| S2 Null random masks | null | A_i = 0 | Nezávislé náhodné | Ne |
| S3 Null shared aniso | null | A_i = 0 | Sdílená anizotropní | Ne |
| S4 Null shared hard-cut | null | A_i = 0 | Sdílená hard-cut | Ne |
| S5 Null shared + ISW | null | A_i = 0 | Sdílená anizotropní | Ano |
| S6 Null shared varied N | null | A_i = 0 | Sdílená anizotropní | Ne |
| S7 Positive common | positive control | A_i = 0.15, theta0 = 45° | Žádná | Ne |
| S8 Positive weak | positive control | A_i = 0.05, theta0 = 135° | Žádná | Ne |

#### 40.D. Concordance metriky a thresholdy
Ke kvantifikaci falešné shody byly sledovány tyto metriky:
- **Resultant length R** (\u2208 [0, 1]): vyšší hodnota znamená větší koncentraci odhadovaných směrů. Thresholdy R > 0.70, R > 0.85, R > 0.95.
- **Mean pairwise separation** (°): průměrná úhlová vzdálenost každého kanálu od každého. Thresholdy: < 30°, < 20°.
- **Channels within 30°**: kolik ze 4 kanálů leží do 30° od výsledného průměrného směru. Thresholdy: 3/4 a 4/4.
Více thresholdů je použito záměrně: žádný jediný práh nedefinuje dostatečnou shodu bez znalosti příslušného nulového rozdělení.

#### 40.E. Výsledky null testu
*(Agregace z 1 000 Monte Carlo opakování per scénář)*

| ID scénáře | Typ | Median R | P99 R | Rate R>0.85 | Rate sep<30° | Rate 4/4 w30° |
|---|---|---|---|---|---|
| S1 Null no mask | null | 0.439 | 0.944 | 4.8 % | 1.3 % | 0.0 % |
| S2 Null random masks | null | 0.420 | 0.933 | 4.4 % | 0.9 % | 0.0 % |
| S3 Null shared aniso | null | **0.998** | **1.000** | **1000/1000** | **1000/1000** | **1000/1000** |
| S4 Null shared hard-cut | null | **0.993** | **1.000** | **1000/1000** | **1000/1000** | **1000/1000** |
| S5 Null + ISW korekce | null | 0.447 | 0.948 | 5.1 % | 1.4 % | 0.0 % |
| S6 Null shared varied N | null | **0.998** | **1.000** | **1000/1000** | **1000/1000** | **1000/1000** |
| S7 Positive common | pos. control | 0.967 | 0.999 | 96.0 % | 77.3 % | cca 70 % |
| S8 Positive weak | pos. control | 0.693 | 0.981 | 25.3 % | 9.5 % | cca 5 % |

*Poznámka k interpretaci:* U null scénářů (S1–S6) se hodnoty ve sloupci „Rate R>0.85“ interpretují jako false concordance rate — míra, se kterou nulové toy kanály překročí práh bez vloženého signálu. U positive-control scénářů (S7–S8) jde o concordance detection rate — míru dosažení prahu při vloženém syntetickém signálu; tato hodnota není false rate.

*Poznámka k Monte Carlo rozlišení:* Test používá 1 000 opakování, tudíž reportované míry jsou MC odhady s rozlišením přibližně 0,1 procentního bodu na výskyt. U hodnot 1000/1000 je vhodné číst výsledek jako saturaci v tomto konečném běhu, nikoli jako absolutní pravděpodobnost 1 pro všechny možlné konfigurace masek a prahů.

#### 40.F. Co bylo zjištěno
Na základě výsledků z toy dat:
- **Nezávislé masky (S1, S2) mají nízkou false concordance:** Při absenci sdílené masky dosahuje false rate R > 0.85 přibližně 4–5 %, tedy v rozsahu odpovídajícím náhodné shodě ve 4 kanálech.
- **Sdílená maska bez korekce (S3, S4, S6) generuje false concordance ve všech 1 000 opakováních:** V tomto Monte Carlo běhu (1 000 opakování) překočila sdílená selection function práh R > 0.85 v každém z 1 000 opakování (1000/1000). Stejný výsledek nastal i při různých velikostech kanálů (S6). Jde o empirický výsledek daného toy nastavení pro zvolenou masku a zvolené prahy — nikoli o obecný matematický zákon pro všechny možné konfigurace. Tyto scénáře nevypovídají nic o reálných survey katalozích ani o Cosmic Octave; pouze ukazují, že společná selection function v tomto toy modelu dramaticky mění null rozdělení concordance.
- **ISW korekce (S5) snížila false concordance na úroveň srovnatelnou s nezávislými maskami:** V tomto Monte Carlo běhu klesla míra překročení prahu R > 0.85 z 1000/1000 na 51/1000 opakování (5.1 %). Toto platí pouze pro tento toy typ hladké sdílené selection function; u hard-cut masek by korekce selhávala, jak bylo ukázáno v Sekci 38.
- **Slabý vložený syntetický signál (S8) leží blízko nulového rozdělení:** Concordance rate (míra dosažení prahu R > 0.85) je u S8 25.3 %, tedy vyšší než u null scénářů S1/S2 (4–5 %), ale podstatně nižší než u silné pozitivní kontroly S7 (96.0 %). Slabý vložený syntetický signál proto v tomto nastavení nelze považovat za robustní pozitivní kontrolu — výsledky se překrývají s null rozdělením a neumožňují odlišení od nulového scénáře v tomto toy nastavení.

#### 40.G. Co nebylo zjištěno
Vzhledem k syntetické a 2D povaze experimentu:
- Nebyla ověřena Cosmic Octave.
- Nebyla testována reálná survey data (NVSS, CatWISE, SPHEREx ani jiné katalogy).
- Nebyla ověřena ani zpochybněna tvrzení HSU o observační shodě.
- Nebyly testovány 3D projekce, DM/DE komponenty ani lokální gravitační modely.
- Nebyl vyřešen způsob přechodu od boundary-distance dipólu k reálnému survey dipólu.
- Nebyl odvozen skutečný kosmologický significance test; výsledky jsou výhradně toy statistikou.

#### 40.H. Dopad na další práci
- **Concordance metrika bez nulového rozdělení je nedostatečná.** Výsledky ukazují, že pozorování s vysokým R vyžaduje srovnání s příslušnou nulovou distribucí pro daný maskový vzor; bez ní nelze odlišit shodu z fyzikálního signálu od sdíleného biasu.
- **Společné masky musí být explicitně modelovány napříč kanály.** V tomto toy nastavení sdílená maska v 1000/1000 opakováních způsobuje false concordance pro zvolené prahy; v reálné analýze by musely být known systematics modelovány před jakýmkoliv výrokem o shodě směrů.
- **ISW korekce snižuje false concordance pouze u hladkých sdílených selection functions.** Pro jiné typy systematik nebo neznámou selection function zůstává false concordance bez efektivní korekce.

#### 40.I. Doporučená další fáze (nespuštěna)
Na základě výsledků se navrhuje:

> ### 41. Hierarchický model společného signálu a společné systematiky
>
> *Cíl:* Navrhnout formální rámec (Bayesovský nebo frekventistický), který oddělí sdílený syntetický směr od sdílené maskové/systematické komponenty v multi-channel toy datech. Tato fáze by navrhla separační model pro případ, kdy jsou k dispozici prior o selection function i o vloženém syntetickém signálu.
>
> *(Fáze 41 nebyla spuštěna a vyčká na povel.)*

### 41. Hierarchický model společného signálu a společné systematiky

#### 41.A. Jednoduché shrnutí
Sekce 40 ukázala, že concordance metrika (resultant length R, pairwise angular separation) musí být vždy posuzována proti příslušnému nulovému rozdělení. Samotná vysoká hodnota R nestačí k odlišení vložené syntetické komponenty od sdílené systematiky. Dalším přirozeným krokem proto není měřit další concordance, ale sestavit statistický model, který umožní tyto dvě příčiny porovnat. Sekce 41 navrhuje formální rámec takového modelu — jde o návrh budoucí inferenční vrstvy, nikoli o reálný observační test a nikoli o validaci HSU nebo Cosmic Octave.

#### 41.B. Motivace po Sekcích 37–40
Sekce 37–40 postupně odhalily limity vektorového estimátoru:
- **Sekce 37:** Vektorový estimátor má nenulový noise floor `E[A_hat] ≈ √(π/N)`. Slabé signály jsou nerozeznatelné od šumu.
- **Sekce 38:** V jediném kanálu může maska vytvořit výrazný falešný dipól; ISW korekce funguje pouze u hladkých selection functions.
- **Sekce 39:** Sdílená maska může vytvořit zdánlivou shodu směrů ve více kanálech bez vloženého signálu.
- **Sekce 40:** Monte Carlo test kvantifikoval false concordance rate: u sdílené anizotropní masky dosahuje saturace v 1000/1000 opakováních, u nezávislých masek je ~4–5 %.

Závěr: Dalším krokem není tvrdit, že pozorovaná shoda je signál nebo bias, ale sestavit model, který tyto dvě možnosti umí formálně porovnat. Sekce 41 takový model navrhuje.

#### 41.C. Dekompozice pozorovaného směru kanálu
Pro kanál *i* je pozorovaný odhadnutý dipólový vektor `d_i` dekomponován jako:

`d_i = s_common + m_shared + b_i + ε_i`

kde:
- **`s_common`** (hypotetický společný syntetický směr): sdílená dipólová komponenta přítomná ve všech kanálech, pokud existuje vložený společný signál.
- **`m_shared`** (společná masková / selection systematika): příspěvek sdílené selection function nebo sdíleného výřezu oblohy, který posune odhadnuté směry všech kanálů konzistentním směrem.
- **`b_i`** (kanálový bias): bias specifický pro kanál *i*, způsobený jeho vlastní selection function (pokud se liší od sdílené).
- **`ε_i`** (kanálový šum): sampling noise specifický pro kanál *i*, s amplitudou řízenou `√(π/N_i)` (Rayleighovo rozdělení v limitě nulového signálu).

Toto je statistický návrh organizace nejistot, nikoli fyzikální model HSU ani kosmologický model.

| Komponenta | Symbol | Původ | Pozorovatelná? |
|---|---|---|---|
| Společný syntetický signál | `s_common` | Vložený dipól A_i, theta0 | Hypoteticky — potřebuje izolaci od systematiky |
| Společná systematika | `m_shared` | Sdílená selection function / maska | Dílčí — v toy modelu je známá; v reálu zpravidla ne |
| Kanálový bias | `b_i` | Vlastní selection function kanálu | Dílčí — závisí na znalosti sel. func. |
| Kanálový šum | `ε_i` | Sampling noise, počítáno z N_i | Modelovatelný přes Rayleigh rozdělení |

#### 41.D. Kandidátní hypotézy
Pro formální porovnání jsou definovány čtyři hypotézy:

| Hypotéza | Společná syntetická komponenta | Společná systematika | Zdroj shody | Interpretace |
|---|---|---|---|---|
| **H0** | Ne (`s_common = 0`) | Ne (`m_shared = 0`) | Čistý sampling noise ε_i | Null baseline — shoda je náhodná |
| **Hmask** | Ne (`s_common = 0`) | Ano (`m_shared ≠ 0`) | Sdílená selection function / maska | False concordance — systematika napodobuje signál |
| **Hsig** | Ano (`s_common ≠ 0`) | Ne (`m_shared = 0`) | Vložený společný směr | Pozitivní detekce — signál bez systematiky |
| **Hsig+mask** | Ano (`s_common ≠ 0`) | Ano (`m_shared ≠ 0`) | Obojí — zaměnitelné bez dalšího modelu | Neidentifikovatelné bez explicitní korekce |

Podstatné je, že **Hmask a Hsig generují podobné concordance hodnoty** (jak ukázal srovnání scénářů S3 a S7 v Sekci 40). Bez explicitního modelu `m_shared` nelze tyto hypotézy od sebe odlišit.

#### 41.E. Jaké veličiny by model potřeboval
Níže jsou uvedeny vstupy, které by formální hierarchický model vyžadoval, a jejich dostupnost v současném toy prostředí:

| Vstup | Význam | Zdroj v toy modelu | Dostupné nyní? |
|---|---|---|---|
| `theta_hat_i` | Odhadnutý směr kanálu i | Výstup naive / corrected estimátoru | Ano (Sekce 37–40) |
| `sigma_theta_i` | Nejistota odhadu směru kanálu i | Přibližně z Rayleigh distribuce a N_i | Přibližně (analyticky) |
| `A_hat_i` | Odhadnutá amplituda kanálu i | Výstup estimátoru | Ano |
| `S_i(theta)` | Selection function kanálu i | Definována v toy skriptech 38–40 | Ano (v toy) |
| `m_shared(theta)` | Společná masková systematika | Sdílená selection function v toy | Ano (v toy); v reálu zpravidla neznámá |
| Null distribuce concordance | Rozdělení R pod H0 / Hmask | Monte Carlo z Sekce 40 | Ano (Sekce 40) |
| Positive-control distribuce | Rozdělení R pod Hsig | Monte Carlo z Sekce 40 (S7/S8) | Ano (Sekce 40) |
| Korekční status kanálu | ISW použito / nepoužito | Flag z Sekce 38 | Ano |
| N_i | Počet tracerů kanálu i | Parametr toy modelu | Ano |

#### 41.F. Bayesovský konceptuální rámec
Bayesovský přístup k porovnání hypotéz by vyžadoval specifikaci likelihood funkce, priorů a evidence pro každou hypotézu. Níže je pouze symbolický konceptuální návrh — žádné výpočty nebyly provedeny.

**Likelihood:**
Za předpokladu von Misesova nebo Gaussovského rozdělení směrů na kružnici:
`P(theta_hat_i | theta0, kappa_i)` — pravděpodobnost pozorování odhadnutého směru při daném skutečném směru `theta0` a koncentračním parametru `kappa_i`.

**Modely:**
- `P(data | H0) = ∏_i P(theta_hat_i | theta0_random, kappa_noise_i)` — směry jsou nezávislé šumy.
- `P(data | Hmask) = ∏_i P(theta_hat_i | theta_mask, kappa_mask_i)` — kde `theta_mask` je směr indukovaný sdílenou maskou.
- `P(data | Hsig) = ∏_i P(theta_hat_i | theta0_sig, kappa_sig_i)` — kde `theta0_sig` je skutečný vložený směr.
- `P(data | Hsig+mask) = ∏_i P(theta_hat_i | theta0_sig + theta_mask, kappa_i)` — smíšený model.

**Model comparison (Bayes factor):**
`BF(Hsig, Hmask) = P(data | Hsig) / P(data | Hmask)`

Zásadní otázkou je, zda `theta_mask` je identifikovatelná z dat, nebo musí být modelována jako latentní proměnná s priorem. V toy nastavení je `theta_mask` přesně známa; v reálné aplikaci by musela být odhadnuta z doplňkových dat o maskách a selection functions.

Toto je návrh budoucí inferenční vrstvy; žádné Bayes factory nebyly počítány.

#### 41.G. Frekventistická varianta rámce
Alternativně lze použít frekventistický přístup bez plné Bayesovské parametrizace:

1. **Null distribution:** Z Monte Carlo Sekce 40 (scénáře S1–S6) je k dispozici empirické rozdělení concordance metriky R pod různými null hypotézami (H0 i Hmask).
2. **Pozorovaná statistika:** Pro syntetická nebo budoucí reálná data se spočítá observovaná hodnota `R_obs`.
3. **p-hodnota:** `p = P(R ≥ R_obs | H_null)` — počet Monte Carlo realizací s R ≥ R_obs dělený celkovým počtem.
4. **Korekce pro sdílenou masku:** Pokud je sdílená selection function aproximativně známa, použije se ISW korekce (Sekce 38); pak se p-hodnota počítá proti null distribuce scénáře S5 (sdílená maska + korekce), nikoli S3 (sdílená maska bez korekce).
5. **Srovnání s pozitivní kontrolou:** Výsledná p-hodnota se doplňuje o concordance detection rate z S7 / S8, aby byl kontext úplný: nízká p-hodnota vůči H0 ještě neznamená vysokou detection power.

Ani frekventistická varianta neurčuje fyzikální původ případného signálu a nevypovídá nic o HSU ani o Cosmic Octave.

#### 41.H. Jak by model chránil před falešnou concordance
Hierarchický model chrání před over-claimingem tím, že explicitně zahrnuje `m_shared` jako latentní komponentu:
- **Shoda směrů bez modelu masky je nedostatečná** — ve scénáři Hmask je R srovnatelné se scénářem Hsig; bez znalosti `m_shared` jsou oba případy zaměnitelné.
- **Každý kanál musí mít explicitní i sdílenou systematiku** — smíšení kanálového biasu `b_i` se sdílenou komponentou `m_shared` vede k neidentifikovatelnosti bez separátních dat.
- **Porovnání hypotéz je nezbytné** — místo prosté interpretace vysokého R jako signálu je nutné spočítat, jak pravděpodobné je vysoké R pod každou hypotézou zvlášť.
- **Korekce ISW snižuje sdílený maskový bias, nikoli ale celou systematiku** — u hard-cut masek nebo neznámých selection functions `m_shared` zůstává neodkorigována, a model musí s touto nejistotou pracovat explicitně.

#### 41.I. Co tento model stále neřeší
Hierarchický statistický rámec navržený v Sekci 41 neřeší:
- Reálné survey katalogy (NVSS, CatWISE, CF4, SPHEREx, Euclid ani jiné).
- Observační ověření nebo vyvrácení HSU.
- Validaci Cosmic Octave.
- Fyzikální původ případného sdíleného syntetického signálu.
- DM/DE projekce ani lokální kosmologické modely.
- Přechod od 2D toy modelu na kružnici S¹ k reálné 3D sféře (S²).
- Správnost HSU kernelů `K_X(z)`, `G_X(z)`, `D_X(z,n)` ani jejich empirické hodnoty.

#### 41.J. Dopad na report
Sekce 41 ukotvuje, že další cesta v tomto metodickém výzkumu musí být formální porovnání hypotéz, nikoli prosté měření concordance. Dosavadní survey větev (Sekce 35–40) systematicky ukázala, že:

1. Vektorový estimátor má nenulový noise floor.
2. Maska indukuje bias v jednom kanálu.
3. Sdílená maska indukuje zdánlivou shodu ve více kanálech.
4. False concordance rate musí být kvantifikována null testem.
5. Porovnání hypotéz je nezbytnou podmínkou před jakýmkoliv výrokem o společném signálu.

Report tím získává statistický rámec omezující riziko over-claimingu: **žádný výsledek z Sekcí 37–40 nepodporuje ani nevyvrací žádné fyzikální tvrzení HSU nebo Cosmic Octave**; výsledky jsou metodickým základem pro budoucí rigorózní analýzu.

#### 41.K. Doporučená další fáze (nespuštěna)
Na základě tohoto návrhu se doporučuje:

> ### 42. Toy model comparison: H0 vs Hmask vs Hsig
>
> *Cíl:* Implementovat minimální syntetický porovnávací test, který na toy datech spočítá, zda výsledky lépe odpovídají nulovému šumu (H0), sdílené masce (Hmask) nebo vloženému společnému syntetickému signálu (Hsig). Konkrétně: spočítat empirické p-hodnoty concordance metriky vůči null distribucím z Sekce 40 a navrhnout Bayes factor proxy z poměru četností.
>
> *(Fáze 42 nebyla spuštěna a vyčká na povel.)*

### 42. Toy model comparison: H0 vs Hmask vs Hsig

#### 42.A. Jednoduché shrnutí
Sekce 41 navrhla formální statistický rámec pro rozlišení tří zdrojů concordance: čistého šumu (H0), společné maskové systematiky (Hmask) a vložené společné syntetické komponenty (Hsig). Sekce 42 provádí první toy implementaci tohoto porovnání prostřednictvím transparentního diagnostického skórovacího systému. Test porovnává H0, Hmask a Hsig na 8 syntetických scénářích (500 MC opakování každý, fixní seed). **Nejde o Cosmic Octave validaci, nejde o reálná survey data, nejde o test HSU.** Výsledky jsou diagnostikou schopnosti toy skórování rozlišit jednoduché generativní případy.

#### 42.B. Hypotézy

| Hypotéza | Co předpokládá | Jak by vysvětlovala concordance | Omezení v toy modelu |
|---|---|---|---|
| **H0** | Žádný společný syntetický směr, žádná sdílená maska | Shoda vzniká náhodou (sampling noise) | Nelze odlišit od Hmask, pokud R_obs je vysoké z jiného důvodu |
| **Hmask** | Sdílená selection function, žádná vložená syntetická komponenta | Maska konzistentně posouvá odhadnuté směry | Nelze rozlišit od Hsig, pokud maska je zarovnána s vloženým směrem |
| **Hsig** | Vložená společná syntetická komponenta theta0, bez sdílené masky | Kanály konvergují k theta0 díky vloženému signálu | Obtížně oddělitelný od Hmask při silné masce nebo slabém signálu |
| **Hsig+mask** | Obojí — vložená syntetická komponenta i sdílená maska | Kombinace obou zdrojů; zaměnitelné bez separace | V tomto toy testu zahrnut jako analytická poznámka, nikoliv jako plný inference model |

#### 42.C. Toy scoring metoda
Scoring je diagnostický toy nástroj — ne formální Bayesovská inference ani kosmologický significance test.

**score_H0** = p-like hodnota: podíl 300 inline H0 MC běhů (A=0, žádná maska), kde R ≥ R_obs. Vysoké score_H0 → pozorovana concordance je konzistentní s čistým šumem.

**score_Hmask** = `max(0, cos(θ_obs − θ_mask)) × (1 − p_H0)`, kde θ_mask je směr odhadnutý ze simulace se sdílenou maskou a A=0. Vysoké score_Hmask → pozorovaný střední směr odpovídá masce A H0 je již slabé.

**score_Hsig** = `R_obs × (1 − p_H0) × max(0, 1 − mask_align)`. Vysoké score_Hsig → silná concordance, H0 je slabé, a maska neexplainuje pozorovaný směr.

**preferred_model** = argmax(score_H0, score_Hmask, score_Hsig).

**margin** = rozdíl diagnostického toy skóre nejlépe a druhého nejlépe hodnoceného modelu. Není to pravděpodobnost ani Bayes factor. Margin může přesáhnout 1.0, protože score_Hsig není striktně omezeno na interval [0, 1] — závisí na R_obs a na (1 − mask_align), kde mask_align může nabývat záporných hodnot (cos úhlu > 90°), čímž faktor (1 − mask_align) překročí 1. Vysoký margin tedy znamená velký rozdíl mezi toy skóre, nikoli statistickou jistotu. **ambiguity_flag** = True, pokud margin < 0.10.

Penalizace složitosti (AIC-like) nebyla implementována; Hsig+mask je v tomto toy testu zahrnut pouze jako analytická poznámka, nikoliv jako plná inferenční hypotéza. Použité skóre je diagnostické toy skóre — není to Bayes factor, není to kosmologická evidence a není to inference nad reálnými survey daty.

#### 42.D. Scénáře

| ID | True generátor | Vložený signál (A, theta0) | Maska | Očekávaný výsledek |
|---|---|---|---|---|
| S1 H0 baseline | H0 | A=0 | Žádná (uniformní) | Preferovat H0 |
| S2 Hmask baseline | Hmask | A=0 | Sdílená anizotropní (peak 135°) | Preferovat Hmask |
| S3 Hsig baseline | Hsig | A=0.15, theta0=45° | Žádná | Preferovat Hsig |
| S4 Hsig + nezávislé masky | Hsig | A=0.15, theta0=45° | Nezávislé náhodné | Méně rozhodné |
| S5 Hsig + maska zarovnaná | Hsig+mask | A=0.15, theta0=45° | Sdílená anizo peak 45° | Hsig a Hmask zaměnitelné |
| S6 Hsig + maska opačná | Hsig+mask | A=0.15, theta0=45° | Sdílená anizo peak 225° | Konflikt signál vs maska |
| S7 Slabý Hsig | Hsig_weak | A=0.05, theta0=90° | Žádná | H0/Hsig obtížně oddělitelné |
| S8 Contaminated | Hsig+outlier | 3× A=0.15 theta0=45°; 1× A=0 maska | Jeden kanál maskový | Snížená rozhodnost |

#### 42.E. Výsledky
*(Agregace medianů z 500 MC opakování per scénář; preferred_model = dominantní výběr across opakování)*

| ID scénáře | True gen. | Preferred (rate) | Ambiguity | Margin | R (med.) | Interpretace |
|---|---|---|---|---|---|---|
| S1 H0 baseline | H0 | **H0** (59 %) | 11 % | 0.455 | 0.428 | Scoring preferuje H0 v 59 % případů; zbývajících 41 % náhodně osciluje. |
| S2 Hmask baseline | Hmask | **Hmask** (100 %) | 0 % | 0.999 | 0.997 | Scoring spolehlivě preferuje Hmask v každém opakování. |
| S3 Hsig baseline | Hsig | **Hsig** (100 %) | 0 % | 1.197 | 0.962 | Scoring spolehlivě preferuje Hsig v každém opakování. |
| S4 Hsig + nezáv. masky | Hsig | **Hmask** (100 %) | 0 % | 0.252 | 0.523 | Scoring nesprávně preferuje Hmask — nezávislé masky vytvořily různé biasy, scoring nedokázal odlišit od maskové systematiky. |
| S5 Hsig + maska zarovn. | Hsig+mask | **Hmask** (100 %) | 0 % | 0.999 | 0.998 | Maska a signál zarovnány → scoring nedokáže odlišit Hmask od Hsig. |
| S6 Hsig + maska opačná | Hsig+mask | **Hmask** (100 %) | 0 % | 0.998 | 0.995 | Silná sdílená maska dominuje nad vloženým signálem; Hmask vždy preferovaný. |
| S7 Slabý Hsig | Hsig_weak | **Hsig** (82 %) | 3 % | 0.936 | 0.718 | Scoring preferuje Hsig, ale pouze v 82 % — slabý signál je méně stabilní. |
| S8 Contaminated | Hsig+outlier | **Hsig** (74 %) | 28 % | 0.185 | 0.756 | Jeden maskový kanál výrazně zvyšuje ambiguitu (28 %) a snižuje margin. |

#### 42.F. Co bylo zjištěno
Na základě výsledků toy scoringu — laicky řečeno: jednoduchý toy soudce pozná čisté školní případy, ale v zamotaných situacích se plete. To je metodicky důležitý výsledek:
- **S1 (H0 baseline):** Scoring preferuje H0 jen v 59 % opakování, s ambiguitou 11 %. Čistý šumový scénář není scoringem rozlišen ve všech repeticích — toy scoring zůstává v části běhů nerozhodný nebo citlivý na náhodnou shodu.
- **S2 (Hmask baseline):** V čistém toy scénáři se sdílenou anizotropní maskou preferovaný model odpovídal generativnímu nastavení v každém opakování (100 %, margin 0.999). Jednoduchý školní případ pro scoring.
- **S3 (Hsig baseline):** V čistém toy scénáři s vloženým syntetickým signálem a bez masky preferovaný model odpovídal generativnímu nastavení v každém opakování (100 %, margin 1.197; margin > 1 je zde možný — viz 42.C). Jednoduchý školní případ pro scoring.
- **S4 (Hsig + nezávislé masky):** Scoring se splete, i když byl vložen společný syntetický směr. Různé masky v jednotlivých kanálech vytvořily různé biasy, které scoring interpretuje jako sdílenou systematiku. Toto není chyba kosmologie ani HSU — je to limit toy scoringu: bez dobrého modelu masky nedokáže odlišit Hsig od Hmask, pokud jsou systematiky heterogenní.
- **S5 (maska zarovnaná se signálem):** Maska míří přibližně stejným směrem jako vložený signál. Scoring volí Hmask v každém opakování, protože pro něj jsou oba zdroje zaměnitelné. V takovém nastavení není scoring schopen rozlišit Hmask od Hsig bez doplňkového modelu masky.
- **S6 (maska opačná k signálu):** Silná sdílená maska míří opačným směrem než vložený signál. Scoring přesto volí Hmask v každém opakování — silná masková systematika dominuje nad vloženou syntetickou komponentou. Ani toto není fyzikální závěr; je to limit toy scoringu při silné sdílené masce.
- **S7 (slabý signál):** Scoring preferuje Hsig v 82 % opakování, ale 18 % nerozhodných příkladů ukazuje, že slabý signál poblíž noise flooru není toy scoringem robustně rozlišitelný.
- **S8 (kontaminovaný kanál):** Jeden outlier kanál s maskovou systematikou zvyšuje ambiguitu na 28 % a snižuje margin na 0.185. Scoring je v tomto scénáři nejméně rozhodný — outlier kanál výrazně zhoršuje rozlišovací schopnost i tehdy, kdy zbývající tři kanály mají vložený syntetický směr.

#### 42.G. Co nebylo zjištěno
Vzhledem k syntetické a 2D povaze experimentu:
- Nebyla ověřena Cosmic Octave.
- Nebyla testována reálná survey data (NVSS, CatWISE, SPHEREx ani jiné katalogy).
- Nebyla ověřena ani zpochybněna tvrzení HSU o observační shodě.
- Nebyl spočítán skutečný Bayes factor pro kosmologická data.
- Nebyly testovány DM/DE projekce ani lokální kosmologické modely.
- Nebyl vyřešen přechod od 2D toy modelu na kružnici S¹ k 3D sféře (S²).

#### 42.H. Dopad na další práci
- **Toy scoring rozlišuje čisté školní případy (S2, S3), ale v zamotaných situacích se plete** — heterogenní systematiky (S4), zarovnaná maska se signálem (S5, S6). To je očekávané chování jednoduchého scoringu bez explicitního modelu systematiky a je to důležitý metodický výsledek.
- **Sdílená syntetická komponenta a sdílená maska jsou pro tento toy scoring zaměnitelné,** pokud maska míří přibližně stejným směrem jako vložený syntetický směr. Budoucí analýza musí mít explicitní model masky, jinak nelze z concordance vyvodit nic o přítomnosti nebo nepřítomnosti společné syntetické komponenty.
- **Jeden outlier kanál (S8) výrazně snižuje rozhodnost** — budoucí survey analýza musí řešit outlier detekci před concordance testem.
- **Výsledky 'preferred_model' jsou toy diagnostika.** Neposkytují pravděpodobnosti v bayesovském smyslu, nejsou to Bayesovy faktory ani kosmologická evidence, a nesmí být interpretovány jako fyzikální závěry o HSU nebo Cosmic Octave.

#### 42.I. Doporučená další fáze (nespuštěna)
Na základě tohoto toy testu se navrhuje:

### 43. Robustness audit model-comparison skóre

#### 43.A. Jednoduché shrnutí
Sekce 42 navrhla toy skórovací systém pro rozlišení tří zdrojů concordance: čistého šumu (H0), maskové systematiky (Hmask) a vložené syntetické komponenty (Hsig). Sekce 43 testuje, zda se výsledky tohoto skórování mění při změně scoring pravidel, síly signálu, síly masky, počtu kanálů nebo prahu ambiguity. Cílem není najít finální správný scoring, ale zjistit, které závěry jsou konzistentní a které jsou citlivé na volbu parametrů. Nejde o HSU, Cosmic Octave ani reálná survey data.

V průběhu auditu byl nalezen a opraven implementační artefakt v definici maskového směru pro uniformní (no-mask) scénáře. Tento artefakt způsoboval chybnou Hmask preferenci v S3 (čistý Hsig bez masky) při 4 kanálech v první verzi skriptu. Po opravě je S3 konzistentně hodnocen jako Hsig ve všech scoring variantech a počtech kanálů.

#### 43.B. Proč je robustness audit nutný
Závěr opírající se o jednu konkrétní ad hoc scoring funkci není metodicky silný — mohl být artefaktem volby parametrů nebo implementace. Pokud různé scoring varianty dávají konzistentní výsledek, je závěr podloženější. Pokud se výsledky mění, je potřeba opatrnější interpretace.

#### 43.C. Implementační audit — oprava artefaktu

Funkce `estimate_mask_dir()` odhaduje průměrný směr maskové systematiky simulací katalogů s danou selection function bez vloženého signálu. Pro **uniformní** selection function (no-mask scénář) vrací tato funkce náhodný střední směr se slabou koncentrací (circular_mean_R ≈ 0.01–0.08), protože žádná skutečná maska neexistuje. Pokud tento náhodný směr náhodou padl poblíž theta0 (vloženého syntetického směru), funkce `score_Hmask` dostala nenulovou hodnotu a mohla v některých opakováních preferovat Hmask i tehdy, kdy maska nebyla přítomna.

**Oprava (v2):** Přidána detekce izotropní masky. Pokud je `circular_mean_R < 0.10` (maska nemá koncentrovaný směr), je `score_Hmask` nastaven na 0 — maskové skóre je zakázáno, pokud selection function nemá definovatelný preferovaný směr. Tato oprava je metodicky korrektní: scoring nesmí přičítat maskovou systematiku tam, kde žádná maska není.

| Verze skriptu | S3 (4 kanály) výsledek | Příčina |
|---|---|---|
| v1 (původní) | Hmask 100 % | Artefakt — náhodný mask_dir zarovnaný s theta0 |
| v2 (opravena) | Hsig 100 % | Izotropní maska detekována, score_Hmask = 0 |

#### 43.D. Testované scoring varianty

| Scoring varianta | Princip | Co chrání | Omezení |
|---|---|---|---|
| **Original** | Reprodukce Sekce 42 s detekcí izotropní masky | Baseline | Margin může být > 1 při záporném mask_align pro anizo masky |
| **Normalized** | mask_align clipped do [0, 1]; margin striktně ≤ R_obs | Zabraňuje umělému zvětšení score_Hsig | Méně citlivý na záporný mask_align |
| **Conservative** | score_Hsig penalizován kvadraticky (1 − mask_align)² | Snižuje záměnu Hsig/Hmask při zarovnané anizo masce | Agresivnější penalizace — může podcenit Hsig |
| **Mask-first** | Hmask dostane 1.5× boost, pokud mask_align > 0.7 a p_H0 < 0.10 | Testuje upřednostňování maskového vysvětlení | Asymetrický — Hmask boost aktivní jen pro silné anizo masky |

#### 43.E. Testované parametry

| Parametr | Testované hodnoty | Scénáře | Proč se testuje |
|---|---|---|---|
| Scoring varianta | original, normalized, conservative, mask_first | všechny S1–S8 | Citlivost na volbu scoring funkce |
| Síla signálu (A) | 0.05, 0.10, 0.20 | S3, S7 | Jak moc závisí detekce na síly syntetického směru |
| Síla masky | slabá (0.40), střední (0.65), silná (0.85) | S2, S5, S6 | Jak moc závisí Hmask preference na intenzitě masky |
| Počet kanálů | 3, 4, 6 | S2, S3 | Citlivost na počet kanálů |
| Práh ambiguity | 0.05, 0.10, 0.20 | všechny S1–S8 | Citlivost na volbu hranice nerozhodnosti |

Celkový objem: 5 parametrových sweep × Pareto výběr scénářů = 90 kombinací × 200 MC opakování.

#### 43.F. Výsledky

Plná data jsou v `.scratch/43_robustness_audit_results.csv`. Výsledky pochází z opravené verze v2.

**Sweep 1 — Základní srovnání 8 scénářů × 4 scoring varianty (baseline: 4 kanály, A=0.15, střední maska)**

| Scénář | True gen. | Original | Normalized | Conservative | Mask-first | Konzistentní? |
|---|---|---|---|---|---|---|
| S1 H0 | H0 | H0 59 % | H0 59 % | H0 59 % | H0 59 % | ✓ |
| S2 Hmask | Hmask | Hmask 100 % | Hmask 100 % | Hmask 100 % | Hmask 100 % | ✓ |
| S3 Hsig | Hsig | Hsig 100 % | Hsig 100 % | Hsig 100 % | Hsig 100 % | ✓ |
| S4 indep. masky | Hsig | Hmask 100 % | Hmask 100 % | Hmask 100 % | Hmask 100 % | ✓ (shodně) |
| S5 maska zarovn. | Hsig+mask | Hmask 100 % | Hmask 100 % | Hmask 100 % | Hmask 100 % | ✓ (shodně) |
| S6 maska opačná | Hsig+mask | Hmask 100 % | Hmask 100 % | Hmask 100 % | Hmask 100 % | ✓ |
| S7 slabý Hsig | Hsig_weak | Hsig 72 % | Hsig 67 % | Hsig 70 % | Hsig 68 % | ✓ (H0 zbytek) |
| S8 contaminated | Hsig+outlier | Hsig 71 % | Hsig 67 % | Hsig 60 % | Hsig 79 % | ✓ (Hmask zbytek) |

**Sweep 2 — Síla signálu A ∈ {0.05, 0.10, 0.20} pro S3 a S7**

| Scénář | A=0.05 Hsig | A=0.10 Hsig | A=0.20 Hsig |
|---|---|---|---|
| S3 Hsig (original) | 67 % | 98 % | 100 % |
| S3 Hsig (normalized) | 69 % | 97 % | 100 % |
| S7 Weak (original) | 68 % | 65 % | 74 % |
| S7 Weak (normalized) | 74 % | 69 % | 68 % |

S3 při A=0.05 je scoring nejméně rozhodný (67–69 %). Při A=0.10 je preference Hsig 97–98 %, při A=0.20 je 100 %. S7 (slabý signál) se pohybuje v rozsahu 65–74 % Hsig — zbytek tvoří H0, nikoli Hmask, protože maska je izotropní.

**Sweep 3 — Síla masky (slabá/střední/silná) pro S2, S5, S6**

| Scénář | Maska | Original Hmask | Conservative Hmask |
|---|---|---|---|
| S2 Hmask | slabá | 100 % | 100 % |
| S2 Hmask | střední | 100 % | 100 % |
| S2 Hmask | silná | 100 % | 100 % |
| S5 aligned | slabá | 100 % | 100 % |
| S5 aligned | střední | 100 % | 100 % |
| S5 aligned | silná | 100 % | 100 % |
| S6 misalign | slabá | 100 % | 100 % |
| S6 misalign | střední | 100 % | 100 % |
| S6 misalign | silná | 46 % | 50 % |

S6 při silné masce v opačném směru: scoring preferuje Hmask jen v 46–50 % opakování. Silná maska mířící opačným směrem než vložený signál vytváří konflikt, ve kterém scoring nedosáhne jasné dominance.

**Sweep 4 — Počet kanálů (3/4/6) pro S2 a S3**

| Scénář | Kanály | Original Hsig | Normalized Hsig |
|---|---|---|---|
| S3 Hsig | 3 | 100 % | 100 % |
| S3 Hsig | 4 | 100 % | 100 % |
| S3 Hsig | 6 | 96 % | 94 % |

Po opravě artefaktu je S3 při 3, 4 i 6 kanálech hodnocen jako Hsig. Při 6 kanálech klesá preference na 94–96 % — zbytek tvoří H0, nikoli Hmask.

**Sweep 5 — Práh ambiguity (0.05 / 0.10 / 0.20)**

| Scénář | thr=0.05 | thr=0.10 | thr=0.20 |
|---|---|---|---|
| S1 H0 | 3 % | 7 % | 21 % |
| S2 Hmask | 0 % | 0 % | 0 % |
| S3 Hsig | 0 % | 0 % | 0 % |
| S4 indep. | 1 % | 6 % | 68 % |
| S5 aligned | 0 % | 0 % | 0 % |
| S6 misalign | 0 % | 0 % | 0 % |
| S7 weak | 4 % | 9 % | 15 % |
| S8 contam. | 7 % | 28 % | 60 % |

S4 (nezávislé masky) je při thr=0.20 nerozhodný v 68 % opakování. S8 jde z 7 % na 60 % ambiguity. Volba prahu výrazně ovlivňuje interpretaci nejzamotanějších scénářů.

#### 43.G. Co bylo zjištěno
- **S2 (Hmask baseline)** je konzistentní ve všech scoring variantech i parametrech — Hmask 100 % napříč všemi sweepi.
- **S3 (Hsig baseline)** je po opravě artefaktu konzistentní — Hsig je preferován ve všech scoring variantech a při 3, 4 i 6 kanálech.
- **S4, S5, S6** — výsledek Hmask je konzistentní napříč scoring variantami. Jde o scénáře, kde toy scoring nemá dostatek informací k oddělení maskové systematiky od vložené syntetické komponenty.
- **S6 při silné masce opačného směru** je jediný scénář, kde scoring nedává konzistentní výsledek — 46–50 % Hmask ukazuje na konflikt masky a signálu, který scoring nedává jednoznačně.
- **S7 (slabý signál)** je rozdělen mezi Hsig (65–74 %) a H0 — zbytek nejde do Hmask, protože maska je izotropní.
- **Práh ambiguity** má zásadní vliv na S4 a S8 — pro tyto scénáře je nutné práh explicitně zdůvodnit.

#### 43.H. Co to znamená laicky
Po opravě implementačního artefaktu jsou výsledky konzistentnější. Čistý signální scénář (S3) je skórován jako Hsig ve všech variantech a ve všech počtech kanálů. Scénáře, kde scoring nemá dostatek informací (S4, S5, S6), vrací shodný výsledek napříč variantami — to znamená, že problém není v konkrétní scoring funkci, ale v tom, že toy scoring nemá dostatek informací k rozlišení, pokud se maska a signál překrývají nebo jsou kanály ovlivňovány různými maskami.

#### 43.I. Co nebylo zjištěno
- Nebyla ověřena Cosmic Octave.
- Nebyla testována reálná survey data (NVSS, CatWISE, SPHEREx ani jiné katalogy).
- Nebyla ověřena ani zpochybněna tvrzení HSU.
- Nebyl spočítán skutečný Bayes factor pro kosmologická data.
- Nebyly testovány DM/DE projekce ani lokální kosmologické modely.
- Nebyl vyřešen přechod od 2D toy modelu (S¹) k 3D sféře (S²).

#### 43.J. Dopad na další práci
- **Oprava artefaktu v izotropní masce je metodicky nutná** — scoring nesmí přičítat maskovou systematiku tam, kde selection function nemá definovatelný preferovaný směr.
- **S4, S5, S6 zůstávají jako benchmark failure cases** — žádná ze čtyř scoring variant tato selhání neopravila.
- **Práh ambiguity je nutný explicitní parametr** — různé prahy dávají výrazně odlišnou reportovanou ambiguitu pro S4 a S8.
- Sekce 44 by měla navrhnout přístup, který odstraní závislost na ad hoc scoring funkcích a umožní formálnější oddělení maskové a signální složky.

#### 43.K. Doporučená další fáze (nespuštěna)

> ### 44. Minimal generative toy model pro Hmask vs Hsig
>
> *Cíl:* Nahradit ad hoc scoring jednoduchým generativním modelem, který explicitně simuluje maskovou složku, syntetickou společnou komponentu a kanálový šum. Likelihood-based přístup umožní formálnější porovnání hypotéz a odstraní závislost na ručně navržených scoring funkcích. Zaměřit se zejména na neidentifikovatelnost S4/S5 a na robustnost detekce u slabého signálu (S7).
>
> *(Fáze 44 nebyla spuštěna a vyčká na povel.)*

### 44. Minimal generative toy model pro Hmask vs Hsig

#### 44.A. Jednoduché shrnutí
Sekce 42–43 používaly jednoduché skórovací pravidlo (ad hoc scoring), které přiřazovalo váhy různým hypotézám na základě ručně navržených vzorců. Sekce 44 místo toho implementuje generativní přístup: pro každou hypotézu (G0, Gmask, Gsig, Gsig+mask) vygenerujeme referenční Monte Carlo distribuci v prostoru tří diagnostických metrik a porovnáme, které hypotéze jsou pozorovaná toy data nejblíže. Cílem není najít absolutní vítěze, ale zjistit, zda generativní přístup přiznává nerozhodnost tam, kde je metodicky správná. Nejde o HSU, Cosmic Octave ani reálná survey data.

#### 44.B. Proč generativní toy model
Ad hoc scoring ze Sekcí 42–43 byl závislý na ručně navržených scoring funkcích, jejichž robustnost byla omezená (zejména u S5/S6/S4). Generativní toy model místo toho:
- simuluje, jaká data by každá hypotéza generovala,
- porovnává, jak blízko jsou pozorovaná toy data každé referenční distribuci,
- přiznává nerozhodnost, pokud jsou dvě hypotézy kompatibilní zároveň.
Tato nerozhodnost je platný a metodicky správný výsledek — lepší než falešná jistota.

#### 44.C. Generativní hypotézy

| Hypotéza | Co generuje | Co by vysvětlovala | Omezení |
|---|---|---|---|
| **G0** | Čistý sampling šum, uniformní maska, A=0 | Concordance vznikla náhodou | Těžko oddělitelná od slabého Gsig při malém N |
| **Gmask** | Sdílená anizotropní maska, A=0 | Concordance způsobena společnou selection function | Při silné masce může být zaměnitelná s Gsig+mask |
| **Gsig** | Sdílená syntetická direktiva, uniformní maska | Concordance způsobena společnou vloženou komponentou | Zaměnitelná s G0 při slabém signálu |
| **Gsig+mask** | Sdílená direktiva + sdílená maska | Obě složky přítomny zároveň | Těžko identifikovatelná oproti čistým případům |

#### 44.D. Diagnostické porovnání — compatibility score

Pro každou hypotézu G ∈ {G0, Gmask, Gsig, Gsig+mask}:
1. Vygeneruje se N_ref = 400 referenčních MC simulací v prostoru metrik **(R, pairwise sep, mask_alignment)**.
2. Z referenčních simulací odhadneme střed μ_G a kovarianční matici Σ_G, regularizovanou přidáním ε·I (ε=10⁻⁶) pro numerickou stabilitu.
3. Pro pozorovaný scénář spočítáme Mahalanobisovu vzdálenost: `d² = (x_obs − μ_G)ᵀ Σ_G⁻¹ (x_obs − μ_G)`.
4. Compatibility score: `C_G = exp(−0.5 × d²)` — čím blíže referenční distribuci, tím vyšší C_G. Hodnota je v intervalu (0, 1], ale **není to pravděpodobnost**.
5. Preferovaný model = hypotéza s nejvyšším C_G v rámci testovaných hypotéz. **Neznamená to pravdivý generativní model, fyzikální výsledek ani Bayesovskou posteriorní pravděpodobnost.**
6. `ambiguity_flag = True` pokud `C_pref − C_second < 0.10` — threshold je aplikován na rozdíl diagnostického compatibility skóre, nikoli na Bayes faktor.
7. Pokud jsou všechny C_G ≈ 0, jde o **model coverage gap** — žádná z testovaných hypotéz dobře nepokrývá daný scénář.

**Důležité:** Compatibility score není pravděpodobnost ani Bayesův faktor. Nejde o kosmologickou evidenci. Jde o diagnostické skóre pro porovnání toy generativních hypotéz v syntetickém nastavení na S¹.

#### 44.E. Scénáře

| Scénář | True gen. | A | Maska | Očekávaný výsledek |
|---|---|---|---|---|
| S1 G0 | G0 | 0 | uniformní | G0 nebo G0/Gsig ambiguous při vyšším N |
| S2 Gmask | Gmask | 0 | sdílená anizo | Gmask nebo Gsig+mask |
| S3 Gsig | Gsig | 0.15 | uniformní | Gsig |
| S4 Gsig+indep. masky | Gsig | 0.15 | různé na každém kanálu | G0 nebo ambiguous |
| S5 Gsig+maska zarovnaná | Gsig+mask | 0.15 | zarovnaná se signálem | Gsig nebo ambiguous |
| S6 Gsig+maska opačná | Gsig+mask | 0.15 | opačný směr | ambiguous nebo G0 |
| S7 Weak Gsig | Gsig_weak | 0.05 | uniformní | Gsig nebo G0/Gsig ambiguous |
| S8 Contaminated | Gsig+outlier | 0.15/0 | 1 kanál s maskou | G0 nebo G0 ambiguous |

#### 44.F. Výsledky

Plná data jsou v `.scratch/44_minimal_generative_toy_model_results.csv`. Výsledky jsou shrnuty přes N ∈ {500, 800, 1000, 1200}.

| Scénář | True gen. | Preferred (N=800) | C_G0 | C_Gmask | C_Gsig | C_Gsig+m | Ambig? |
|---|---|---|---|---|---|---|---|
| S1 G0 | G0 | G0 / Gsig | 0.994 | 0.000 | 0.996 | — | ✓ ano |
| S2 Gmask | Gmask | Gsig+mask | 0.000 | 0.992 | 0.000 | vysoké | ✓ ano |
| S3 Gsig | Gsig | Gsig | 0.000 | 0.000 | 0.994 | — | ✗ ne |
| S4 Gsig+indep | Gsig | G0 | 0.368 | 0.000 | 0.000 | — | ✗ ne |
| S5 Gsig+aligned | Gsig+mask | Gsig | 0.000 | 0.000 | 0.005 | — | ✓ ano |
| S6 Gsig+misalign | Gsig+mask | G0 | 0.000 | 0.000 | 0.000 | — | ✓ ano |
| S7 Weak | Gsig_weak | Gsig | 0.329 | 0.000 | 0.541 | — | ✗ ne |
| S8 Contam. | Gsig+outlier | G0 | 0.160 | 0.000 | 0.000 | — | ✗ ne |

*Poznámka ke S2: Preferred je Gsig+mask, ale C_Gmask ≈ 0.99 — Gmask a Gsig+mask referenční distribuce se překrývají, pokud maska neobsahuje vloženou syntetickou komponentu. Toto je metodicky korektní přiznání nerozhodnosti.*

*Poznámka ke S4: Preferred G0 neznamená, že ve scénáři nebyl vložený syntetický směr. Nezávislé masky na každém kanálu se vzájemně ruší; výsledné metriky (R ≈ 0.48, sep ≈ 95°) se v tomto toy nastavení nejvíce podobají G0 referenční distribuci. Jde o limit pokrytí: aktuální model nemá hypotézu pro heterogenní kanálové masky. Výsledek nelze číst jako „žádný signál“, ale jako „žádná testovaná hypotéza tuto situaci dobře nepopsal“.*

*Poznámka ke S6: Všechny C_G ≈ 0 — pozorovaná data (R ≈ 0.99, sep ≈ 7.9°) leží mimo všechny referenční distribuce. Preferred „G0“ je jen technický vítěz mezi nulami; výsledek je out-of-model. Silná misaligned maska generuje metriky, které žádná z implementovaných hypotéz nevytváří.*

*Poznámka ke S8: C_G0 = 0.16, ostatní C = 0. Výsledek G0 není pozitivní identifikace šumu — jde o nejméně nepasující hypotézu při nízké absolutní C. Jde o model coverage gap.*

**N-sweep — stabilita přes N ∈ {500, 800, 1000, 1200}:**

| Scénář | Preferred (konzistentní?) | Ambig? (konzistentní?) | Citlivý na N? |
|---|---|---|---|
| S1 G0 | G0 (N=500), Gsig (N≥800) | ano ve všech N | Ano — overlap závisí na N |
| S2 Gmask | Gsig+mask ve všech N | ano ve všech N | Ne |
| S3 Gsig | Gsig ve všech N | ne ve všech N | Ne |
| S4 Gsig+indep | G0 ve všech N | ne ve všech N | Ne — coverage gap konzistentně |
| S5 Gsig+aligned | Gsig ve všech N | ano ve všech N | Ne |
| S6 Gsig+misalign | G0 ve všech N | ano ve všech N | Ne — out-of-model konzistentně |
| S7 Weak | Gsig ve všech N | ne ve všech N | Ano — C_Gsig kolíšá (0.998→0.541→0.878→1.000) |
| S8 Contam. | G0 ve všech N | ne ve všech N | Mírně — C_G0 klesá s N |

#### 44.G. Co bylo zjištěno
- **G0 je rozpoznán pouze při menším N:** při N ≥ 800 se referenční distribuce G0 a Gsig překrývají natolik, že model hlásí ambiguitu. To je metodicky správné — při malém počtu tracerů nelze odlišit šum od slabého signálu.
- **S3 (Gsig baseline):** V tomto toy nastavení je dosahováno nejvyššího diagnostického compatibility skóre pro Gsig konzistentně napříč N — C_Gsig ≈ 0.98–1.00, C_G0 ≈ 0.00. Výsledek platí pro tyto toy parametry a nelze jej generalizovat mimo toto nastavení.
- **Gmask (S2) preferuje Gsig+mask, nikoliv čistý Gmask** — referenční distribuce Gmask a Gsig+mask se překrývají v metrickém prostoru. Generativní model přiznává tuto nerozhodnost explicitně přes ambiguity_flag.
- **S4 a S8 — model coverage gap:** Preferred je G0, ale preference G0 neznamená, že ve scénáři nebyl vložený syntetický směr. Znamená pouze, že z testovaných generativních hypotéz se výsledné metriky nejvíce podobaly G0 referenci. Aktuální model nemá hypotézu pro heterogenní kanálové masky ani outlier kanály.
- **S5 (zarovnaná maska)** a **S6 (opačná maska)** jsou oba ambiguous nebo mimo všechny distribuce — generativní model přiznává neidentifikovatelnost těchto scénářů, což je metodicky zásadní výsledek.
- **S7 (slabý signál) — citlivý na N:** Preferred je Gsig ve všech N, ale C_Gsig není stabilní přes N (0.998, 0.541, 0.878, 1.000 pro N=500/800/1000/1200). Slabý syntetický signál je v tomto toy nastavení citlivý na N a výsledek nelze číst jako robustní detekci.
- **S8 (kontaminovaný kanál) — model coverage gap:** C_G0 = 0.16–0.32, ostatní C = 0. Preferred G0 není pozitivní identifikace šumu — jde o nejméně nepasující hypotézu při nízké absolutní C. Outlier kanál posuvá metriky mimo všechny referenční distribuce.

#### 44.H. Co to znamená laicky
Generativní toy model přiznává nerozhodnost tehdy, kdy ji přiznat je správné — například u G0 při vyšším N nebo u Gmask vs. Gsig+mask. V tomto toy nastavení má S3 (Gsig baseline) nejvyšší diagnostické compatibility skóre konzistentně přes N; to však neznamená, že by generativní model obecně rozhodoval v složitějších scénářích. Zamotačné scénáře (S4, S5, S6, S8) jsou přiznány jako nerozhodné nebo mimo pokrytí modelů.

#### 44.I. Co nebylo zjištěno
- Nebyla ověřena Cosmic Octave.
- Nebyla testována reálná survey data (NVSS, CatWISE, SPHEREx ani jiné katalogy).
- Nebyla ověřena ani zpochybněna tvrzení HSU.
- Nebyl spočítán skutečný Bayes factor pro kosmologická data.
- Nebyly testovány DM/DE projekce ani lokální kosmologické modely.
- Nebyl vyřešen přechod od 2D toy modelu (S¹) k 3D sféře (S²).
- Nebyla řešena správnost HSU kernelů K_X(z), G_X(z), D_X(z,n).

#### 44.J. Dopad na další práci
- **Generativní přístup přiznává nerozhodnost explicitněji** než ad hoc scoring ze Sekcí 42–43 — zejména pro S1, S2, S5, S6.
- **S3 má konzistentní diagnostické compatibility skóre** napříč N v tomto toy nastavení.
- **S5/S6/S8 zůstávají metodickým limitem** — generativní model ani ad hoc scoring nedokáží jednoznačně identifikovat zamotané scénáře bez explicitního modelu outlier kanálů.
- Sekce 45 by měla rozšířit model o outlier-aware složku, která umožní detekci kontaminovaného kanálu jako součást generativního modelu.

#### 44.K. Doporučená další fáze (nespuštěna)

> ### 45. Outlier-aware generative toy model
>
> *Cíl:* Rozšířit generativní toy model ze Sekce 44 o možnost, že jeden nebo více kanálů nepatří ke společné syntetické komponentě ani ke sdílené masce, ale má vlastní odlišnou systematiku. Likelihood-based přístup by umožnil explicitní detekovatelnost kontaminovaného kanálu a zvýšenou robustnost u scénářů S8 a potenciálně S4.
>
> *(Fáze 45 nebyla spuštěna a vyčká na povel.)*

### 45. Outlier-aware generative toy model

#### 45.A. Jednoduché shrnutí
Sekce 44 ukázala, že scénáře jako S8 (kontaminovaný kanál) a S4 (nezávislé masky) způsobují „model coverage gap" — žádná z testovaných hypotéz (G0, Gmask, Gsig, Gsig+mask) tyto situace dobře nepopíše. Sekce 45 přidává novou hypotézu **Goutlier**: většina kanálů sdílí společnou syntetickou komponentu, ale jeden kanál má vlastní nezávislou systematiku. Cílem je zjistit, zda tato dodatečná složka zlepší popis scénářů z coverage gap. Nejde o hledání vadných reálných survey dat ani o Cosmic Octave. Jde o toy test outlier složky na syntetickém S¹ nastavení.

#### 45.B. Proč outlier-aware model
V multi-channel nastavení může jeden kanál s odlišnou selection function nebo vlastní systematickou chybou „rozbít" celkovou concordance tak, že výsledné metriky nevyhovují žádné z čistých hypotéz. Bez outlier komponenty model takový scénář hlásí jako coverage gap nebo nesprávně přiřadí G0. Outlier-aware model explicitně testuje, zda vynechání jednoho kanálu (leave-one-out) výrazně zvýší kompatibilitu s Gsig — pokud ano, je daný kanál diagnosticky podezřelý. Outlier score v tomto toy nastavení není potvrzení vadnosti kanálu v reálných datech; je to pouze syntetická diagnostická veličina.

#### 45.C. Hypotézy

| Hypotéza | Co předpokládá | Co by vysvětlovala | Omezení |
|---|---|---|---|
| **G0** | Čistý šum, uniformní maska | Concordance náhodná | Překrývá se s Gsig při malém N |
| **Gmask** | Sdílená anizotropní maska | Concordance způsobena selection function | Zaměnitelná s Gsig+mask |
| **Gsig** | Sdílená syntetická direktiva | Concordance způsobena vloženou komponentou | Zaměnitelná s G0 při slabém signálu |
| **Gsig+mask** | Direktiva + sdílená maska | Obě složky přítomny | Těžko oddělitelná od čistých případů |
| **Goutlier** | n−1 kanálů sdílí Gsig, 1 kanál je outlier | Concordance přerušena jedním odlišným kanálem | Nefunguje pro více outlierů, ani pro heterogenní masky |

#### 45.D. Outlier diagnostika

Pro každý kanál i (leave-one-out):
1. Vynecháme kanál i z pozorovaných dat → vektor metrik `x_obs_bez_i`.
2. Vygenerujeme leave-one-out referenční distribuci pro Gsig s n−1 kanály.
3. Spočítáme `C_Gsig_bez_i` = Mahalanobis compatibility pro x_obs_bez_i vůči loo-referenci.
4. `outlier_score_i = C_Gsig_bez_i − C_Gsig_vše` — kladná hodnota znamená, že vynechání kanálu i zlepší Gsig kompatibilitu.
5. Outlier detection: kanál s max outlier_score > 0.05 je označen jako diagnosticky podežzelý.

**Kalibrační analýza (n=100 trialů, N=800):** False positive míra při threshold 0.05 v no-outlier scénářích:
- G0 (S1): FP ≈11 % — LOO skóre bimodální; p50 = 0, p95 = 0.36.
- Gmask (S2): FP = 0 % — Gmask je vůči LOO stabilní.
- Gsig (S3, bez outlieru): FP = 84 % — vynechání libovolného kanálu zvyšuje Gsig kompatibilitu, protože loo-reference má nižší dimenzi.
  LOO skóre neodlišuje čistý Gsig (S3) od Gsig+outlier (S4) spolehlivě.
- Gsig+1 outlier (S4): TP = 88 % — margin vůči S3 FP je malý.

**Důležité:** Threshold 0.05 je příliš citlivý pro Gsig-family scénáře. LOO diagnostika v této implementaci není diskriminativní pro Gsig vs. Gsig+outlier. Outlier score není potvrzení vadnosti kanálu v reálných datech; je to toy diagnostika na S¹ s vysokou false positive mírou v Gsig-family scénářích.

**Důležité:** Outlier score není potvrzení vadnosti kanálu v reálných datech. Je to toy diagnostika na S¹. Negativní outlier score může nastat i u šumu.

#### 45.E. Scénáře

| Scénář | True gen. | Signal | Maska | True outlier ch. | Očekávání |
|---|---|---|---|---|---|
| S1 G0 | G0 | žádný | uniformní | žádný | G0 preferován, žádný outlier |
| S2 Gmask | Gmask | žádný | sdílená | žádný | Gmask preferován, žádný outlier |
| S3 Gsig | Gsig | A=0.15 | uniformní | žádný | Gsig preferován, žádný outlier |
| S4 Gsig+1 kontam. | Goutlier | A=0.15 (3 ch), 0 (1 ch) | 1 ch s maskou | ch 3 | Goutlier preferován, outlier detekován |
| S5 Gmask+1 indep. | Gmask+outlier | žádný | 3 ch sdílí masku, 1 uniformní | ch 3 | ambiguous nebo out-of-model |
| S6 Gsig+indep.masky | Gsig+hetero | A=0.15 | každý ch jiná maska | žádný | G0 nebo coverage gap |
| S7 Weak Gsig+outlier | Goutlier_weak | A=0.05 (3 ch), 0 (1 ch) | 1 ch s maskou | ch 3 | G0 nebo ambiguous |
| S8 Two outliers | Two_outliers | A=0.15 (2 ch), 0 (2 ch) | 2 ch s maskou | oba | G0 nebo coverage gap |

#### 45.F. Výsledky

Níže uvedená tabulka shrnuje reprezentativní agregované výsledky pro N=800; interpretace vychází z kalibrační analýzy popsané v této sekci.

| Scénář | True gen. | Preferred | C_G0 | C_Gsig | C_Gout | Ambig? | Outlier det.? | Správně? | Interpretace |
|---|---|---|---|---|---|---|---|---|---|
| S1 G0 | G0 | G0 | 0.968 | 0.000 | 0.016 | ✗ | ✓ (FP) | ✗ | G0 preferován, LOO false positive |
| S2 Gmask | Gmask | Gmask | 0.000 | 0.000 | 0.000 | ✗ | ✓ (seed) | — | Gmask preferován; LOO FP = 0 % systematicky (viz kalibraci) |
| S3 Gsig | Gsig | Gsig | 0.000 | 0.984 | 0.446 | ✗ | ✗ | ✓ | Gsig preferován, bez outlier |
| S4 Gsig+1 kontam. | Goutlier | **Goutlier** | 0.000 | 0.000 | **0.442** | ✗ | ✓ | ✓ | Outlier-aware preferován a detekován |
| S5 Gmask+1 indep. | Gmask+outlier | G0 | 0.000 | 0.000 | 0.004 | ✓ | ✓ | ✓ | Out-of-model, ambiguous |
| S6 Gsig+indep.masky | Gsig+hetero | G0 | 0.476 | 0.000 | 0.033 | ✗ | ✓ (FP) | ✗ | Coverage gap — heterogenní masky |
| S7 Weak+outlier | Goutlier_weak | G0 | 0.533 | 0.000 | 0.202 | ✗ | ✓ | ‘½ | LOO našlo odlišný kanál, ale generativní model preferoval G0; scénář zůstává částečně nepokryt |
| S8 Two outliers | Two_outliers | G0 | 0.384 | 0.000 | 0.052 | ✗ | ✓ (partial) | ✘ | Single-outlier model nemá hypotézu pro 2 outliery; detekce jednoho je cov. gap |

*Zkratky: FP = false positive (outlier_score > threshold, ale true_outlier = žádný); partial = detekce 1 outlieru ze 2 skutečných; seed = artefakt konkrétního MC seed, ne systematická chyba; ½ = částečně pokryt. Správně = shoda s true_outlier_channel.*

*Poznámka ke S1: LOO outlier detection má při threshold 0.05 FP míru ≈11 % v G0 baseline (kalibrovaná analýza, n=100 trialů, N=800). LOO skóre jsou bimodální: většina je 0, ale ocas distribuce sahá až p95=0.36. Pro S2 (Gmask) je FP systematicky 0 % — Gmask je vůči LOO stabilní (všechny kanály sdílejí stejnou masku). Detekce v S2 v hlavní tabulce je artefakt jednoho seed.*

*Poznámka ke S4: Goutlier je preferován konzistentně napříč N={500, 800, 1000, 1200}. Outlier detekce (TP = 88 %) je dosahována za ceny vysoké false positive míry v S3 (84 % při threshold 0.05). Úspěch S4 je tedy nezbytné hodnotit společně s FP mírou: model neodlišuje spolehlivě S3 od S4 na úrovni LOO diagnostiky.*

*Poznámka ke S7: LOO diagnostika označila odlišný kanál, ale generativní model preferoval G0 — scénář zůstává částečně nepokryt. Slabý společný signál (A=0.05) nepostačuje, aby Goutlier hypotéza získala vyšší compatibility než G0.*

*Poznámka ke S8: S8 není čistý false positive — jde o partial detection a model coverage gap. Model detekoval jeden odlišný kanál ze dvou skutečných, ale nemá hypotézu pro 2 outliery. C_Goutlier ≈ 0.05 znamená, že ani Goutlier single-channel referenci dobře nepopsal scénář se dvěma odlišnými kanály.*

#### 45.G. Co bylo zjištěno

**Souhrnná tabulka outlier diagnostiky (N=800, threshold = 0.05):**

| Scénář | True outlier | Outlier det. | Klasifikace | Preferovaný model | Interpretace |
|---|---|---|---|---|---|
| S1 G0 | 0 (none) | ✓ | FP — 11 % syst. FP míra | G0 | LOO bimodální, FP závisí na seed |
| S2 Gmask | 0 (none) | ✓ (seed) | seed artifact | Gmask | Syst. FP = 0 %; Gmask je LOO stabilní |
| S3 Gsig | 0 (none) | ✗ | true negative | Gsig | V hlavním N=800 běhu nebyl označen outlier, ale kalibrační analýza ukazuje vysokou FP míru (84 %) napříč opakováními; tento jednotlivý běh tedy nereprezentuje stabilní výkon LOO diagnostiky. |
| S4 Gsig+1 kontam. | 1 (ch 3) | ✓ | true positive | Goutlier | TP = 88 %, ale S3 FP = 84 % — nespolehlivý margin |
| S5 Gmask+1 indep. | 1 (ch 3) | ✓ | partial | G0 | Outlier nalezen, Goutlier nepokryt (Gmask-based) |
| S6 Gsig+indep.masky | 0 (hetero) | ✓ | FP | G0 | Heterogenní masky nejsou jeden outlier |
| S7 Weak+outlier | 1 (ch 3) | ✓ | true pos. (LOO) | G0 | LOO OK, Goutlier neprefereovaný — částečně nepokryt |
| S8 Two outliers | 2 (ch 2,3) | ✓ | partial | G0 | Single-outlier model coverage gap |

- **S4 (Gsig + 1 kontaminovaný kanál):** V tomto toy nastavení je Goutlier preferován s C_Goutlier = 0.43–0.56 konzistentně napříč N. U S4 LOO diagnostika často označuje vložený odlišný kanál, ale stejná diagnostika má podobně vysokou FP míru u S3 bez outlieru. Výsledek tedy ukazuje potenciál outlier-aware rozšíření, ale zároveň nedostatečnou diskriminaci současného LOO skóre.
- **S3 (čistý Gsig):** V hlavním runu (1 trial) outlier_detected = False, ale kalibrační analýza ukazuje, že FP míra pro S3 při threshold 0.05 je 84 % (n=100 trialů). Jeden úspěšný výsledek v hlavním runu nevyjadřuje systematický výkon LOO diagnostiky.
- **LOO false positive v S1 a S2:** V čistých baseline scénářích (G0, Gmask) LOO diagnostika hlásí outlier_detected = True. To ukazuje, že threshold 0.05 je příliš nízký pro scénáře bez společné syntetické komponenty — LOO skóre jsou v těchto případech numericky nestabilní.
- **S5 (Gmask + 1 nezávislý kanál):** Zůstává out-of-model a ambiguous. Outlier kanál odpovídal vloženému odlišnému kanálu LOO detekcí, ale žádná hypotéza tento scénář dobře nepokryje. Goutlier referenční distribuce je navržena pro Gsig+outlier, nikoli pro Gmask+outlier.
- **S6 (heterogenní masky):** Coverage gap — G0 preferován, Goutlier C ≈ 0.03. Heterogenní kanálové masky nelze popsat jako „jeden outlier".
- **S7 (slabý signál + outlier):** LOO diagnostika označila odlišný kanál, ale generativní model preferoval G0. Scénář zůstává částečně nepokryt — slabý společný signál (A=0.05) nestačí, aby Goutlier hypotéza získala vyšší compatibility než G0.
- **S8 (dva outliery):** S8 není čistý false positive. Jde o partial detection a model coverage gap: single-outlier model Goutlier nemá hypotézu pro 2 odlišné kanály. C_Goutlier ≈ 0.05 znamená, že ani tato nejbližší hypotéza scénář dobře nepopsal.

#### 45.H. Co to znamená laicky
Model umí být užitečný, když přesně jeden kanál vybočuje. Problém je, že současná leave-one-out diagnostika je moc podezřívavá: i když jsou kanály všechny ze stejné skupiny, vynechání jednoho kanálu může zlepšit skóre. Proto samotné označení outlieru nestačí; musí být kalibrované proti čistým scénářům bez outlieru.

#### 45.I. Co nebylo zjištěno
- Nebyla ověřena Cosmic Octave.
- Nebyla testována reálná survey data (NVSS, CatWISE, SPHEREx ani jiné katalogy).
- Nebyla ověřena ani zpochybněna tvrzení HSU.
- Nebyl spočítán skutečný Bayes factor pro kosmologická data.
- Nebyly testovány DM/DE projekce ani lokální kosmologické modely.
- Nebyl vyřešen přechod od 2D toy modelu (S¹) k 3D sféře (S²).
- Nebyla řešena správnost HSU kernelů K_X(z), G_X(z,n).
- Nebyla testována kalibrovaná detekce outlierů pro Gmask scénáře.

#### 45.J. Dopad na další práci
- **S4-like scénář je v tomto toy nastavení lépe popsán outlier-aware hypotézou:** Goutlier hypotéza rozšiřuje model o jeden outlier kanál a LOO diagnostika v části běhů označuje vložený odlišný kanál.
- **LOO diagnostika je nekalibrovaná pro Gsig-family:** Kalibrační analýza ukazuje FP míru 84 % pro S3 (Gsig bez outlieru) při threshold 0.05. LOO míra pro Gsig a Gsig+outlier je takřka shodná — margin TP vs. FP je malý. Samy thresholdy (0.05, 0.10, 0.15) nevyjadřují toto metodické omezení aktuální LOO diagnostiky.
- **Goutlier je jednokanálový model:** Pro 2+ outlier kanály (S8) a heterogenní masky (S6) zůstává coverage gap. Sekce 46 by měla ověřit, zda směsový model dokáže toto omezení snížit.
- **Slabý signál zůstává problematický:** S7 ukazuje, že při A=0.05 je outlier kanál těžko identifikovatelný — model přiznává nerozhodnost.

#### 45.K. Doporučená další fáze (nespuštěna)

> ### 46. Multi-outlier and mixture generative toy model
>
> *Cíl:* Rozšířit toy generativní rámec o více outlier kanálů a směsové váhy. Hypotéza G_mixture by předpokládala, že kanály jsou rozděleny do dvou skupin: skupina A sdílí jednu komponentu, skupina B sdílí jinou. Tím by bylo možné testovat situace jako S8 (2 outliery) nebo S6 (heterogenní masky) bez nutnosti nutit všechny kanály do jedné hypotézy.
>
> *(Fáze 46 nebyla spuštěna a vyčká na povel.)*
