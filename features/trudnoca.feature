Feature: Provera upozorenja za Trudnoću
    Scenario Outline: Dodavanje dijagnoze za trudnoću
      Given Postoji OS sa ID <OS_ID> i Dokument na tom OS sa ID <DOK_ID>
      And postoji bar jedna stavka na tom dokumentu
      When  Korisnik doda novu dijagnozu <DIJAGNOZA_OZNAKA> na stavku
      Then  Na profilu osiguranika <OSIGURANIK_ID> treba da stoji upozorenje "Osiguranik je u drugom stanju..."
  
      Examples:
      | OSIGURANIK_ID | OS_ID | DOK_ID | DIJAGNOZA_OZNAKA |
      | 1 	          | 5002  | 1120   | O00              |