"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const rxjs_1 = require("rxjs");
const operators_1 = require("rxjs/operators");
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
(0, rxjs_1.from)(persons)
    .pipe((0, operators_1.filter)((person) => locations.some((loc) => loc.person === person.id && loc.country === "Poland")), (0, operators_1.map)((person) => { var _a; return ((_a = ages.find((age) => age.person === person.id)) === null || _a === void 0 ? void 0 : _a.age) || 0; }), (0, operators_1.reduce)((acc, curr) => {
    acc.sum += curr;
    acc.count += 1;
    return acc;
}, { sum: 0, count: 0 }), (0, operators_1.map)(({ sum, count }) => (count > 0 ? sum / count : 0)))
    .subscribe((avgAge) => console.log("Średni wiek osób w Polsce:", avgAge));
