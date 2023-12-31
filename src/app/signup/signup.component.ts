import { Component,OnInit } from '@angular/core';


@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})
export class SignupComponent  implements OnInit{


  type:string="password"
  isText: boolean=false;
  eyeIcon: string="fa-eye-slash";

  formdata = {name:"",email:"",password:""};
  submit=false;
  errorMessage="";
  constructor() { }
 
  ngOnInit(): void {
   
  }

  hideShowPass(){
    this.isText = !this.isText;
    this.isText ? this.eyeIcon = "fa-eye" : this.eyeIcon = "fa-eye-slash";
    this.isText ? this.type = "text": this.type = "password";
  }

  

}
