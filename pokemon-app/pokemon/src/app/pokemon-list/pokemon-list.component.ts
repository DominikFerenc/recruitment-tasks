import { Component, OnInit } from '@angular/core';
import { PokemonService } from '../pokemon.service';

interface Pokemon {
  name: string;
  url: string;
}

interface PokemonApiResponse {
  count: number;
  next: string;
  previous: string;
  results: Pokemon[];
}

@Component({
  selector: 'app-pokemon-list',
  templateUrl: './pokemon-list.component.html',
  styleUrls: ['./pokemon-list.component.css']
})
export class PokemonListComponent implements OnInit {
  pokemons: Pokemon[] = [];
  currentPage: number = 1;
  limit: number = 10;
  offset: number = 0;
  totalPokemons: number = 0;

  constructor(private pokemonService: PokemonService) {}

  ngOnInit(): void {
    this.fetchPokemons();
  }

  fetchPokemons(): void {
    this.pokemonService.getPokemons(this.limit, this.offset)
      .then((data: PokemonApiResponse) => {
        this.pokemons = data.results;
        this.totalPokemons = data.count;
      })
      .catch((error) => {
        console.error('Error fetching Pokemons:', error);
      });
  }

  nextPage(): void {
    if (this.offset + this.limit < this.totalPokemons) {
      this.currentPage++;
      this.offset += this.limit;
      this.fetchPokemons();
    }
  }

  previousPage(): void {
    if (this.offset > 0) {
      this.currentPage--;
      this.offset -= this.limit;
      this.fetchPokemons();
    }
  }

  get totalPages(): number {
    return Math.ceil(this.totalPokemons / this.limit);
  }
}