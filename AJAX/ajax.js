//__________________Ajaxs by txt file__________________
const buttom=document.getElementById("1");
const tdiv=document.getElementById("2");
function loading() {
    var xhr=new XMLHttpRequest();
    xhr.open("GET","test.txt",true);
    console.log("ReadyState: ",xhr.readyState);
    xhr.onprogress=function() {
        console.log("ReadyState: ",xhr.readyState);
    };xhr.onload=function() {
        if(xhr.status==200) {
            console.log("ReadyState: ",xhr.readyState);
            tdiv.innerHTML=this.responseText;
        };
        // xhr.onreadystatechange=function() {
        //     if(this.readyState==4 & this.status==200) {
        //         tdiv.innerHTML=this.responseText;
        //     }
        // }
    };xhr.send();
};buttom.addEventListener('click',loading);
//__________________Ajax Reading XML__________________
const btn=document.getElementById("btn");
function LoadDoc() {
    var xhr=new XMLHttpRequest();
    xhr.open('GET','cd-collection.xml',true);
    xhr.onload=function() {
        loadXML(this);
    };xhr.send();
};let loadXML=xml => {
    const xmlDoc=xml.responseXML;
    const cd=xmlDoc.getElementsByTagName("CD");
    let tab="<tr> <th>Artist</th> <th>Title</th> </tr>";
    for(let i=0;i<cd.length;i++) {
        tab+="<tr> <td>"+
        cd[i].getElementsByTagName("ARTIST")[0].childNodes[0].nodeValue+       
        "</td> <td>"+
        cd[i].getElementsByTagName("TITLE")[0].childNodes[0].nodeValue+
        "</td> </tr>";
    };document.getElementById("tbl").innerHTML=tab;
};btn.addEventListener('click',LoadDoc);
//__________________Ajax Post Request Form__________________
const fn=document.getElementById("FirstName");
const ln=document.getElementById("LirstName");
const jt=document.getElementById("JobTitle");
const form=document.getElementById("frmSend");
function sdate() {
    var xhr=new XMLHttpRequest();
    var params='FirstName= '+fn.value+'&'+'LastName= '+ln.value+'&'+'JobTitle= '+jt.value;
    xhr.open('POST','http://localhost:7006/api/persons/adduser',true);
    xhr.setRequestHeader('Content-type','application/x-www-form-urlencoded');
    xhr.send(params);
};form.addEventListener('submit',sdate)
//__________________Ajax Fetch Api__________________
const btn0=document.getElementById("getfetch");
function gtxt() {
    fetch('sample.txt').then(
        res => res.text()
    ).then(
        data => console.log(data))
};btn0.addEventListener('click',gtxt)
//__________________Ajax__________________
//const b=document.getElementById("getfetch");
function gus() {
    fetch("user.json").then(
        res => res.json().then(
            json => {
                let output='';
                json.forEach(user => {
                    output+=`<ul> <li>${user.ID}</li> 
                    <li>${user.Name}</li> 
                    <li>${user.Email}</li> </ul>`;
                });document.getElementById("output").innerHTML=output;
            }));
};gus(); //b.addEventListener('click',gus)