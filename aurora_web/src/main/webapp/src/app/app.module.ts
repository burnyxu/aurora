import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { FormsModule }    from '@angular/forms';

import { AppComponent } from './app.component';
import { NavigatorComponent } from './navigator/navigator.component';
import { AdminComponent } from './admin/admin.component';
import { PredictorComponent } from './predictor/predictor.component';
import { StatasticsComponent } from './statastics/statastics.component';
import { MlService } from './ml.service';
import { HttpClientModule }    from '@angular/common/http';
import { HttpClientInMemoryWebApiModule } from 'angular-in-memory-web-api';
import { AppRoutingModule } from './app-routing.module';
import { SidebarComponent } from './sidebar/sidebar.component';
// import { InMemoryDataService }  from './in-memory-data.service';

@NgModule({
  declarations: [
    AppComponent,
    NavigatorComponent,
    AdminComponent,
    PredictorComponent,
    StatasticsComponent,
    SidebarComponent
  ],
  imports: [
    BrowserModule, 
    FormsModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [MlService],
  bootstrap: [AppComponent]
})
export class AppModule { }
