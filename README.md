## Snabbkodat korpusverktyg för skumma ".tagged"-filer

### Användning

##### Förberedelser:
- Ladda ned filen `search.py``
- Lägg den i den mapp där du vill jobba
- Gör en mapp med de filer du vill söka i, lägg den i *samma* mapp som `search.py``

##### Navigera till rätt mapp i terminalen:
- Öppna terminalen och navigera till den mapp där `search.py` ligger genom att använda kommandot `cd`
*ELLER* (lättare sätt):
-  Öppna finder, gå till mappen där `script.py` ligger
- Högerklicka någonstans i mappen, välj "Ny terminal i mapp"
- (om det inte dyker upp som alternativ, testa att byta fram och tillbaka mellan att visa objekt som symboler och visa objekt som lista, prova sedan att högerklicka igen)
- ((jag vet inte varför, men det verkar funka på min dator))

##### Användning:
- Skriv `python3 search.py <namnet på mappen där korpusfilerna ligger>` i terminalen och tryck `enter`
- Skriv in den sekvens av taggar du vill söka efter (det kommer en prompt som säger hur du ska göra) och tryck `enter`
- Programmet kommer att skriva ut i terminalen hur många matchningar som gjordes, sammanlagt och i varje enskild fil. Det går att scrolla upp och ned i terminalen så att du kan läsa allt den har skrivit ut. 
- Programmet kommer att skapa en mapp som heter `resultat` i samma mapp som `search.py` ligger
- Alla meningar som matchar sökningen kommer att hamna i en fil i mappen `resultat`. Korpusfilerna söks igenom en åt gången, och namnet på filerna kommer att stå i resultatfilen, som ett slags rubrik till de matchningar som kommer från just den filen. 
- Resultatfilen kommer att heta samma sak som du sökte på, så att du kan göra flera olika sökningar utan att blanda ihop dem. 
- Om du söker igen på exakt samma sak så kommer filen få samma namn och de nya resultaten kommer att skriva över de gamla