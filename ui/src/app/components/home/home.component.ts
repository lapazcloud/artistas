import { Component, OnInit } from '@angular/core';
import { ArtistaService } from '../../artista.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})

export class HomeComponent implements OnInit {
  artist;
  isLoading;
  isReady;

  constructor(private artistaService: ArtistaService) { }

  ngOnInit() {
    this.isLoading = true;
    this.isReady = false;
    this.artistaService.getArtist().
    subscribe(
      artist => {
        this.isLoading = false;
        this.artist = artist;
        this.isReady = true;
      });
  }

  reloadPage() {
    this.ngOnInit();
  }

}
