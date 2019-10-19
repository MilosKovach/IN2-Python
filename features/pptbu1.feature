Feature: Provera pokrića tipa 'Broj usluga'

  Scenario: Korišćenje pokrića tipa 'Broj usluga'
    Given Postoji Osigurani slučaj 5004 i na njemu dokument sa ID 993
    And Dokument se odnosi na Osiguranika OKTAVIJAN GAGIĆ
    And Za tog osiguranika postoji pokriće Dijagnostika CT,sa merom limita,Broj usluga,iskorisceno
    When Korisnik doda novu stavku dokumenta: Color Doppler magistralnih arterija vrata, 1100, Petar Petrovic, Dijagnostika CT
    Then Na Pokrićima, za Dijagnostiku CT treba u koloni Iskorišćeno da stoji 1
    And Dijagnostika CT treba da bude obojena crvenom bojom
    