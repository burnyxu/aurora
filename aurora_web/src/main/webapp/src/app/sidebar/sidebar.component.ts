import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.css']
})
export class SidebarComponent implements OnInit {
  activeid: String;

  constructor() {
  }

  selectItem(item: string) {
    this.activeid = item;
  }

  caculateClasses(id: string) {
    if (id == this.activeid) {
      return "active";
    }
    else
      return ""
  }

  ngOnInit() {
    this.activeid = "sidepredict"
  }

}
