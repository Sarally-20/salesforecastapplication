import { Component,OnInit,NgModule } from '@angular/core';
import { Router, RouterLink, Routes } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { DashboardComponent } from '../dashboard/dashboard.component';


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit{
[x: string]: any;
  email=""
  password=""
   My_name = "Dhanush";
  My_pass ="12345678";
  Isvalid = false;
  type:string="password"
  isText: boolean=false;
  eyeIcon: string="fa-eye-slash";

  

  constructor(private http:HttpClient, private router:Router) { }
  
  ngOnInit(): void {
   
  }

  submit(){
    //call login service
    
  }
      
  LoginForm = new FormGroup(
    {
      UserName : new FormControl('',Validators.required),
      PassWord : new FormControl('',Validators.required)
    }
  )

  hideShowPass(){
    this.isText = !this.isText;
    this.isText ? this.eyeIcon = "fa-eye" : this.eyeIcon = "fa-eye-slash";
    this.isText ? this.type = "text": this.type = "password";
  }
  check(){
    if(this.email=="dhanush@gmail.com" && this.password=="12345678"){
      window.location.replace("/dashboard");
    }else{
      alert("Invalid credentials");
    }
  }
  
}
