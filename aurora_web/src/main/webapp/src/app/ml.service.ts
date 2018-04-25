import { Injectable } from '@angular/core';
import { InMemoryDbService } from 'angular-in-memory-web-api';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs/Observable';
import { of } from 'rxjs/observable/of';
import { catchError, map, tap } from 'rxjs/operators';


const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable()
export class MlService {

  //private heroesUrl = 'api/heroes';
  private localUrl = 'http://localhost:9000/callpy';
  private localPredictUlr = 'http://localhost:9000/callpredict';
  constructor(private http: HttpClient
    //,private messageService: MessageService
  ) { }

  getPredict(desc: string): Observable<string> {
    let url = this.localPredictUlr + "/?desc=" + desc;
    return this.http.get(url, { responseType: 'text' }, ).pipe(
      tap(_ => console.info("test1")),
      catchError(this.handleError<string>("test error")))
      ;
  }
  private handleError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {
      console.info("1");
      // TODO: send the error to remote logging infrastructure
      console.error(error); // log to console instead

      // TODO: better job of transforming error for user consumption
      //this.log(`${operation} failed: ${error.message}`);

      // Let the app keep running by returning an empty result.
      return of(result as T);
    };
  }


}
