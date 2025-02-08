console.log("Connected...");
//تعریف متغیرهای str
var Name,number;
Name="Omid";
number='09355073770';
//_________________//انواع پرینت___________________
// console.log(Name,number);
// document.write(number);
// window.alert(Name);
//_________________//متغیرهای دوگانه و چندگانه str___________________
var person={
    fname:"Omid",
    lname:"Jalali"
};
//(person.fname+" "+person.lname);
//__________________//متغیرهای عددی__________________
var Num=69;
var Num2=66;
//__________//متغیر های بولین(یا درست یا غلط)____________
// var isComplete=false;
var isEqual;
isEqual=(Num==Num2)
//_________________//آرایه ها(هم مقدار عددی هم اس تی آر و هم بولین دریافت میکنند)___________________
var names=new Array("Omid","Mostafa","Sadeq"); 
// console.log(names[0]);
var myarray=("Ojlato",20,true,"Kashmar",17.5);
//______________________
var color=["Red","Blue","Black","Orange","Yellow"];
color.reverse(); //از آخر به اول خواندن لیست
color.shift(); //خانه اول لیست رو حذف میکنه
color.unshift("Green"); //به اول لیست مقدار اضافه میکنه
color.pop(); //خانه آخر لیست رو حذف میکنه
color.push("White"); //به آخر لیست مقدار اضافه میکنه
//______________________
var newcolor=color.slice(); //از لیست کپی برداری میکنه و تغییرات ما روی کپی اعمال میشه
var result=color.indexOf("Black",0); //جستجو کردن در لیست با ذکر نام مورد نظر و اینکه از کجا شروع کنه
var arraystr=color.join(" | "); //تمام مقادیر لیست رو بهم متصل میکنه و به اس تی آر تبدیل میکنه و با علامت دلخواه از هم جدا میشن
//____________________________________