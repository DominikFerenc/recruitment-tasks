import { Injectable } from '@angular/core';

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

@Injectable({
  providedIn: 'root'
})
export class PokemonService {
  private apiUrl = 'https://pokeapi.co/api/v2/pokemon';

  getPokemons(limit: number, offset: number): Promise<PokemonApiResponse> {
    const url = `${this.apiUrl}?limit=${limit}&offset=${offset}`;
    return fetch(url)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      });
  }

  getPokemonDetails(name: string): Promise<any> {
    return fetch(`https://pokeapi.co/api/v2/pokemon/${name}`)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      });
  }
}
