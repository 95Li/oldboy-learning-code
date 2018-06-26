function get_date(){
   var d=new Date();
   var year=d.getFullYear();
   var month=d.getMonth()+1;
   var date = d.getDate();
   var hours = d.getHours();
   var min = d.getMinutes();
   var days = d.getDay();
   switch (days){
      case 0:
           day="星期日";
           break;
      case 1:
           day="星期一";
           break;
    case 2:
           day="星期二";
           break;
    case 3:
           day="星期三";
           break;
    case 4:
           day="星期四";
           break;
    case 5:
           day="星期五";
           break;
    case 6:
           day="星期六";
           break;
    }
 var time=year+"-"+month+"-"+date+" "+hours+":"+min+"  "+day

return time

}

console.log(get_date())