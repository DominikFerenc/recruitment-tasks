import { Component } from '@angular/core';

@Component({
  selector: 'app-car-list',
  templateUrl: './car-list.component.html',
  styleUrl: './car-list.component.css'
})

export class CarListComponent {
  newCar: String = '';
  cars: String[] = JSON.parse(localStorage.getItem('cars') || '[]');
  selectedCar: String | null = null;

  addCar() {
    if (this.newCar) {
      this.cars.push(this.newCar);
      localStorage.setItem('cars', JSON.stringify(this.cars));
      this.newCar = '';
    }
  }

  viewDetails(car: String) {
    this.selectedCar = car;
    console.log('Viewing details for:', car);
  }
}