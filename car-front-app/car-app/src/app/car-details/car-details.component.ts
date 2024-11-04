import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-car-details',
  templateUrl: './car-details.component.html',
  styleUrl: './car-details.component.css'
})
export class CarDetailsComponent {
  @Input() car: String = '';
  newPart: String = '';
  newCost: number = 0;
  services: { part: String; cost: number }[] = [];
  isOpen: boolean = false;

  addService() {
    if (this.newPart && this.newCost !== null && this.newCost > 0) {
      this.services.push({ part: this.newPart, cost: this.newCost });
      this.newPart = '';
      this.newCost = 0;
    }
  }

  removeService(serviceToRemove: { part: String; cost: number }) {
    this.services = this.services.filter(service => service !== serviceToRemove);
  }

  toggleModal() {
    this.isOpen = !this.isOpen;
  }
}
