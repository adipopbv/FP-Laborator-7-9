# Complexitatea algoritmilor

## Functia "get attendances with person id":

<code>

	def get_attendances_with_person_id(self, person_id: str):
	    attendances = []
	    if len(self.items) == 0:
	        raise EmptyRepoException
	    if type(person_id) != str:
	        raise NotStringParameterException
	    for attendance in self.items:
	        if attendance.person_id == person_id:
	            attendances.append(attendance)
	    return attendances

### Complexitate de memorie:

Algoritmul foloseste mai foloseste o lista auxiliara pe care o returneaza la iesire.

#### Caz favorabil:

Avem numarul minim de iteratii cand ``self.items`` este o lista vida sau cand ``person_id`` nu este un sir de caractere, in acest caz complezitatea fiind Θ(1).

#### Caz defavorabil:

Numarul de iteratii este in functie de numarul de elemente din ``self.items``. Astfel pentru ``n`` elemente in ``self.items``, numarul de iteratii va fi ``n``, si deci complexitatea este Θ(n).

