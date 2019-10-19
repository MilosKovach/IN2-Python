Feature: Provera popusta na cenovniku

  Scenario Outline: Dodavanje korekcije cenovnika i provera cena

   Given Postoji cenovnik sa ID <CENOVNIK_ID>
   When Korisnik unese novu korekciju cenovnika:<KOREKCIJA_NAZIV>,<KOREKCIJA_TIP>,<KOREKCIJA_OBIM>,<KOREKCIJA_POPUST>
   And Korisnik osvezi stavke cenovnika
   Then Na stavci <STAVKA_NAZIVA> cena sa popustom treba da bude pravilno umanjena za <KOREKCIJA_POPUST> procenata

    Examples:
    | CENOVNIK_ID | KOREKCIJA_NAZIV  | KOREKCIJA_TIP | KOREKCIJA_OBIM | KOREKCIJA_POPUST | STAVKA_NAZIVA                 |
    | 2       	  | Martovski popust | Akcija        | Cenovnik       | 15               | pregled alergologa/imunologa |
