# Created by milosk at 25.3.2019.
Feature: Provera Radnog vremena

  Scenario Outline: Dodavanje radnog vremena i provera statusa
    Given Postoji PU sa Matičnim brojem <PU_MB>
    When Korisnik dodaje novo radno vreme za PU: <RADNI_DAN>, <TERMIN_OD>, <TERMIN_DO>
    Then Na stranici sa detaljima PU <PU_MB> treba proveriti status <STATUS>
Examples:
      | PU_MB	      | RADNI_DAN     | TERMIN_OD | TERMIN_DO | STATUS   |
	  | 4106406309000 | Radnim danima | 0900      | 1700      | Otvoren  |
	  | 4106965704000 | Radnim danima | 0600      | 0700      | Zatvoren |
	  | 4100518206000 | Radnim danima | 0000      | 2359      | Otvoren  |
	  | 4106406309007 | Subota        | 0600      | 0700      | Zatvoren |

