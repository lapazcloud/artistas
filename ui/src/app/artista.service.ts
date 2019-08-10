import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ArtistaService {

  apiUrl = "/function/obtener-artista";

  constructor(private http: HttpClient) { }

  getArtist() {
    return this.http.get(`${this.apiUrl}`);
  }
}
