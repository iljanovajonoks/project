<h2 align="center">Kriptovalūtu Portfeļa Analizētājs</h2>              

**Apraksts**</br>
Šis projekts ir kriptovalūtu portfeļa analīzes rīks. Lai sāktu, jums ir Excel fails ar datiem par jūsu kriptovalūtu portfeli, tostarp kriptovalūtas nosaukumu, summu un iegādātās vienības cenu. Projekta mērķis ir izmantot tīmekļa automatizāciju, lai no CoinMarketCap iegūtu aktuālās kriptovalūtas cenas un procentuālās cenu izmaiņas (1 dienai, 7 dienām un 1 mēnesim) un aprēķinātu peļņu vai zaudējumus no sākotnējā ieguldījuma, sākotnējā ieguldījuma summu un pašreizējo investīciju summu.

**Projekta uzdevums**</br>

Uzdevums ir izveidot risinājumu, kas ļautu viegli iegūt un analizēt datus par kriptovalūtu ieguldījumiem. Projekts ietver vairākus soļus:

1. Datu lasīšana: Portfeļa dati tiek lasīti no sākotnējā Excel faila, kurā ir informācija par kriptovalūtu nosaukumu, daudzumu un iegādes cenu.
2. Aktuālu cenu un cenas izmaiņas procentu iegūšana: Izmantojot tīmekļa automatizāciju un Selenium, tiek iegūtas aktuālās kriptovalūtu cenas un cenas izmaiņas procenti no CoinMarketCap.
3. Peļņas/Zaudējumu aprēķins: Tiek aprēķināta peļņa vai zaudējumi, salīdzinot sākotnējo ieguldījumu ar pašreizējo vērtību procentos.
4. Datu izvadīšana Excel failā: Rezultāti tiek saglabāti atpakaļ Excel failā, ļaujot viegli sekot līdzi izmaiņām un saglabāt analīzes vēsturi.

**Izmantotās python bibliotēkas**

1. **Selenium**: Izmantoju Selenium kā galveno automātizācijas rīku, kas nodrošina pārlūkošanas funkcionalitāti un datu iegūšanu. Tāpat plaši izmantoju:</br>
Keys - Izmantoju, lai simulētu "ENTER" pogas darbību un veiktu tīmekļa lapas darbības, piemēram, ievades lauka apstiprināšanu.</br>
By - Izmantoju, lai identificētu un meklētu HTML elementus pēc to atribūtiem, piemēram, pēc klases vai id.</br>
WEbDriverWait - Izmantoju, lai gaidītu, kad paradīsies konkrēts elements lapā.</br>
EC - izmantoju, lai skatītu, vai nepieciešamais elements ir redzams vai pieejams. Tas palīdz nodrošināt, ka darbības tiek veiktas tikai tad, kad lapā ir pieejami nepieciešamie dati vai elementi.
2. **Pandas**: Izmantoju pandas datu iegūšanai no Excel un ierakstīšanai atpakaļ Excel failā.
3. **Time**: Izmantoju, kad nepalīdzēja WEbDriverWait, mana gadījuma tas bija, lai uzgaidītu cenas atjaunināšanu.</br>

**Programmatūras izmantošanas metodes**
1. Projektu var izmantot regulārai kriptovalūtu portfeļa uzraudzībai.Jūs varat pārvaldīt savu portfeli, izsekojot pašreizējās cenas, izmaiņas dažādos laika periodos un kopējo peļņu/zaudējumus.
2. Pieņemt pārdomātus lēmumus par ieguldījumiem, analizējot pagātnes cenu izmaiņas un procentuālās izmaiņas.
3. Saglabāt datu arhīvu turpmākai analīzei un izsekot sava portfeļa izmaiņas dinamiku.</br>

**Programmatūras darbībā un rezultāts** </br>
[Video ieraksts](https://clipchamp.com/watch/3OZ0fB8jMTo)