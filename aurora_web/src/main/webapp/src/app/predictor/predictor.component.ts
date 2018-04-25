import { Component, OnInit } from '@angular/core';
import { MlService } from '../ml.service';

@Component({
  selector: 'app-predictor',
  templateUrl: './predictor.component.html',
  styleUrls: ['./predictor.component.css']
})
export class PredictorComponent implements OnInit {

  predictResult: string;
  caseDescription: string;

  constructor(private mlService: MlService) { }

  ngOnInit() {
    this.caseDescription = "";
    this.predictResult = "initial";
  }

  getPredict(): void {
    this.predictResult = null;
    this.mlService.getPredict(this.caseDescription).subscribe(result =>
      this.predictResult = result
      //console.info(result)
    );
  }
}
