# Created by milosk at 21.3.2019.
Feature: Korisnik se loguje na sajt/novi korisnik

  Scenario Outline: Korisnik se loguje sa ispravnim podacima
    Given korisnik se loguje na stranicu "https://http://bg-ddordzo-01/dzo"
    When korisnik informacije za logovanje <KORISNIK>
    And korisnik unese sifru <SIFRA>
    Then korisnik je ulogovan


    Examples:
    | KORISNIK | SIFRA     |
    | jpejin   | 1234asdfa |
    | mgagic   | 1234asdd  |
    | dcirovic | 1234asdf  |
