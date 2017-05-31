/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
//
//function required(inputtx)   
//   {  
//     if (inputtx.value.length == 0)  
//      {   
//         alert("message");        
//         return false;   
//      }       
//      return true;   
//    } 
function required()  
{  
var empt = document.forms["form1"]["text1"].value;  
if (empt == "")  
{  
alert("Please fill up missing fields");  
return false;  
}  
else   
{  
alert('Code has accepted : you can try another');  
return true;   
}  
}  