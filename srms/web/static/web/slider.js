var imgarr=["j2.jpg","j3.jpg","j4.jpg","j5.jpg","j6.jpg"];
var i=0;
function slide()
{
  var img=document.getElementById("iimm");
  img.src="images/"+imgarr[i];
  i++;
  if(i==imgarr.length)
  {i=0;}
  window.setTimeout("slide()",2000);
  }  