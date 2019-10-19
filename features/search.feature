Feature: GTEST provera formiranja stavke uputa
  Scenario Outline: Kreiranje prvog Uputa osiguranika
	  Given postoji osiguranik sa ID brojem <ID_OSIGURANIKA>
	  And   postoji dokument sa ID brojem <ID_DOK>
	  And   postoji pokriće sa nazivom <ID_POKRICA>

      When korisnik unosi <STAVKA_CENA>, <TERMIN>, <DOKTOR>, <ID_POKRICA>
	  Then na pokriću rezervisan iznos treba da bude povecan za <IZNOS>

	  Examples:
	  | ID_OSIGURANIKA | ID_DOK | ID_POKRICA   | STAVKA_CENA | TERMIN | DOKTOR     | IZNOS |
	  | 20             | 1080   | Ambula       |   Fizija    | 1122   | Ivan Vujic | 16.96 |
	  | 1              | 1011   | Dijagnostika |   alergol   | 1130   | Ivan Vujic | 29.67 |