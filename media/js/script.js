// -----------------------------------------------------------------------------------
// http://wowslider.com/
// JavaScript Wow Slider is a free software that helps you easily generate delicious 
// slideshows with gorgeous transition effects, in a few clicks without writing a single line of code.
// Last updated: 2011-10-27
//
//***********************************************
// Obfuscated by Javascript Obfuscator
// http://javascript-source.com
//***********************************************
function ws_basic(b,a,f){var e=jQuery;var d=f.children();var c=e('<div style="position:relative;"></div>');f.append(c);c.append(d);f.css({position:"relative",overflow:"hidden"});c.css({position:"relative",width:(b.outWidth*a.length)*1.1+"px",left:0,top:0});a.css({position:"static"});this.go=function(g){c.stop(true).animate({left:-e(a.get(g)).position().left},b.duration,"easeInOutExpo");return g}};// -----------------------------------------------------------------------------------
// http://wowslider.com/
// JavaScript Wow Slider is a free software that helps you easily generate delicious 
// slideshows with gorgeous transition effects, in a few clicks without writing a single line of code.
// Last updated: 2011-10-27
//
//***********************************************
// Obfuscated by Javascript Obfuscator
// http://javascript-source.com
//***********************************************
jQuery("#wowslider-container1").wowSlider({effect:"basic",prev:"",next:"",duration:20*100,delay:30*100,outWidth:980,outHeight:330,width:980,height:330,autoPlay:true,stopOnHover:true,loop:false,bullets:true,caption:false,controls:true});