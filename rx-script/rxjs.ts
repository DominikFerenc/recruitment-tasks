import { from } from 'rxjs';
import { filter, map, reduce } from 'rxjs/operators';

let persons = [
  { id: 1, name: "Jan Kowalski" },
  { id: 2, name: "John Doe" },
  { id: 3, name: "Jarek Kaczka" },
];

let ages = [
  { person: 1, age: 18 },
  { person: 2, age: 24 },
  { person: 3, age: 666 },
];

let locations = [
  { person: 1, country: "Poland" },
  { person: 3, country: "Poland" },
  { person: 1, country: "USA" },
];

from(persons)
  .pipe(
    filter((person) =>
      locations.some(
        (loc) => loc.person === person.id && loc.country === "Poland"
      )
    ),
    map((person) => ages.find((age) => age.person === person.id)?.age || 0),
   
    reduce(
      (acc, curr) => {
        acc.sum += curr;
        acc.count += 1;
        return acc;
      },
      { sum: 0, count: 0 }
    ),
    map(({ sum, count }) => (count > 0 ? sum / count : 0))
  )
  .subscribe((avgAge) =>
    console.log("Średni wiek osób w Polsce:", avgAge)
  );