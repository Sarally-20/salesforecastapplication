import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
 period=""
 n=""
 file:any|null;
updatefile(){
   var  f=<HTMLInputElement>(document.getElementById("formFile"));
   if(f.files){
   this.file=f.files[0];
   }
}
send(){
    var xhr = new XMLHttpRequest();
      xhr.open('POST', 'http://127.0.0.1:5000/upload');
      xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
          console.log('Data sent successfully!');
        }
      };
      
      var formData = new FormData();
      formData.append('period', this.period);
      formData.append('count', this.n);
      formData.append('file', this.file);
      xhr.send(formData);
      xhr.onload=function(){
        window.open('http://127.0.0.1:5000/image','Forecast');
     }
    }

  

  constructor( ) { }
 
  ngOnInit(): void {
    
  }

}