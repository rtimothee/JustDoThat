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
if(!jQuery.fn.wowSlider){
	jQuery.fn.wowSlider=function(b){
		var i=this;
		var g=jQuery;
		
		b=g.extend({effect:function(f,d){
			var t=jQuery;d.each(function(H){
				if(!H){t(this).show()}
				else{t(this).hide()}
				});
			this.go=function(H,I){
				t(d.get(H)).fadeIn(f.duration);
				t(d.get(I)).fadeOut(f.duration);
				return H}
			},
			prev:"",
			next:"",
			duration:1000,
			delay:20*100,
			captionDuration:1000,
			outWidth:960,
			outHeight:360,
			width:960,
			height:360,
			caption:true,
			controls:true,
			autoPlay:true,
			bullets:true,
			stopOnHover:0,
			preventCopy:1}
			,b);
			
		b.loop=b.loop||Number.MAX_VALUE;
		var E=i.find(".ws_images>*");
		var v=E.length;b.stopOn=((b.stopOn||0)+v)%v;
		var D;
		if(b.preventCopy){
			D=g('<div><a href="#" style="display:none;position:absolute;left:0;top:0;width:100%;height:100%"></a></div>').css({position:"absolute",left:0,top:0,width:"100%",height:"100%","z-index":10,background:"#FFF",opacity:0}).appendTo(i).find("A").get(0)}E.each(function(f){var d=g(this).html()||"";
			var t=d.indexOf(">",d);
			if(t>=0){
				g(this).data("descr",d.substr(t+1));
				if(t<d.length-1){
					g(this).html(d.substr(0,t+1))
				}
			}
			g(this).css({"font-size":0})});
			var k=E.find("IMG");var a=0;
			function s(t,f,d){
				t=((t%v)+v)%v;
				if(a==t){
					return
				}
				var t=o.go(t,a,f,d);
				if(t<0){return}
				r(t);
				if(b.caption){
					j(E[t])
				}
				a=t;
				if(b.onStep){
					b.onStep(t)
				}
			}
			
			var C,A,e=0;
			var u=i.get(0);
			if(u.addEventListener){
				u.addEventListener("touchmove",function(t){
					if(e){
						var f=(C-t.touches[0].pageX)/20;
						var d=(A-t.touches[0].pageY)/20;
						if((Math.abs(f)>1)||(Math.abs(d)>1)){
							C=A=e=0;y(t,a+((f+d)>0?1:-1),f,d)
						}
					}
				},false);
				
				u.addEventListener("touchstart",function(d){
					if(d.touches.length==1){
						C=d.touches[0].pageX;A=d.touches[0].pageY;e=1}
					else{e=0}
				},false);
				
				u.addEventListener("touchend",function(d){
					e=0},false)
			}
			
			function r(f){
				if(b.bullets){
					n(f)}
				if(D){
					var d=E.get(f).href;
					if(d){
						D.setAttribute("href",d);
						D.setAttribute("target",E.get(f).target);
						D.style.display="block"
					}else{
						D.style.display="none"
					}
				}
			}
			var q;function z(){w();if(b.autoPlay){q=setTimeout(function(){s(a<v-1?a+1:0);if(a==b.stopOn&&!--b.loop){b.autoPlay=0}z()},b.delay+b.duration)}}function w(){if(q){clearTimeout(q)}q=null}function y(H,t,f,d){w();H.preventDefault();s(t,f,d);z()}g(k.get(0)).css("z-index",1);k.css("position","absolute");if(typeof b.effect=="string"){b.effect=window["ws_"+b.effect]}var o=new b.effect(b,k,g(".ws_images",i));E.find("IMG").css("visibility","visible");var p=c=g(".ws_images",i);var m="WOWSlider.com";c=m?g("<div></div>"):0;if(c){c.css({position:"absolute",right:"2px",bottom:"2px",padding:"0 0 0 0"});p.append(c)}if(c&&document.all){var B=g('<iframe src="javascript:false"></iframe>');B.css({position:"absolute",left:0,top:0,width:"100%",height:"100%",filter:"alpha(opacity=0)"});B.attr({scrolling:"no",framespacing:0,border:0,frameBorder:"no"});c.append(B)}var F=c?g(document.createElement("A")):c;if(F){F.css({position:"relative",display:"none","background-color":"#E4EFEB",color:"#837F80","font-family":"Lucida Grande,sans-serif","font-size":"11px","font-weight":"normal","font-style":"normal","-moz-border-radius":"5px","border-radius":"5px",padding:"1px 5px",width:"auto",height:"auto",margin:"0 0 0 0",outline:"none"});F.attr({href:"http://"+m.toLowerCase()});F.html(m);F.bind("contextmenu",function(d){return false});c.append(F)}if(b.controls){var x=g('<a href="#" class="ws_next">'+b.next+"</a>");var h=g('<a href="#" class="ws_prev">'+b.prev+"</a>");i.append(x);i.append(h);x.bind("click",function(d){y(d,a+1)});h.bind("click",function(d){y(d,a-1)})}function G(){var t=i.find(".ws_bullets>div");var L=g("a",t);L.click(function(M){y(M,g(M.target).index())});var J=L.find("IMG");if(J.length){var I=g('<div class="ws_bulframe"/>').appendTo(t);var f=g("<div/>").css({width:J.length+1+"00%"}).appendTo(g("<div/>").appendTo(I));J.appendTo(f);g("<span/>").appendTo(I);var H=-1;function K(N){if(N<0){N=0}g(L.get(H)).removeClass("ws_overbull");g(L.get(N)).addClass("ws_overbull");I.show();var O={left:L.get(N).offsetLeft-I.width()/2};var M={left:-J.get(N).offsetLeft};if(H<0){I.css(O);f.css(M)}else{if(!document.all){O.opacity=1}I.stop().animate(O,"fast");f.stop().animate(M,"fast")}H=N}L.hover(function(){K(g(this).index())});var d;t.hover(function(){if(d){clearTimeout(d);d=0}K(H)},function(){L.removeClass("ws_overbull");if(document.all){if(!d){d=setTimeout(function(){I.hide();d=0},400)}}else{I.stop().animate({opacity:0},{duration:"fast",complete:function(){I.hide()}})}});t.click(function(M){y(M,g(M.target).index())})}}function n(d){g(".ws_bullets A",i).each(function(f){if(f==d){g(this).addClass("ws_selbull")}else{g(this).removeClass("ws_selbull")}})}if(b.caption){$caption=g("<div class='ws-title' style='display:none'></div>");i.append($caption);$caption.bind("mouseover",function(d){w()});$caption.bind("mouseout",function(d){z()})}function j(d){var H=g("img",d).attr("title");var t=g(d).data("descr");var f=g(".ws-title",i);f.stop(1,1).stop(1,1).fadeOut(b.captionDuration/3,function(){if(H||t){f.html((H?"<span>"+H+"</span>":"")+(t?"<div>"+t+"</div>":""));l(f,{direction:"left",easing:"easeInOutExpo",complete:function(){if(g.browser.msie){f.get(0).style.removeAttribute("filter")}},duration:b.captionDuration})}})}if(b.bullets){G()}r(0);if(b.caption){j(E[0])}if(b.stopOnHover){this.bind("mouseover",function(d){w()});this.bind("mouseout",function(d){z()})}z();function l(K,P){var M={};var N=["position","top","bottom","left","right"];for(var L=0;L<N.length;L++){M[N[L]]=K[0].style[N[L]]}K.show();var J={width:K.outerWidth(true),height:K.outerHeight(true),"float":K.css("float"),overflow:"hidden",left:K.position().left,top:K.position().top,opacity:0},f=g("<div></div>").css({fontSize:"100%",background:"transparent",border:"none",margin:0,padding:0});K.wrap(f);f=K.parent();if(K.css("position")=="static"){f.css({position:"relative"});K.css({position:"relative"})}else{g.extend(J,{position:K.css("position"),zIndex:K.css("z-index")});K.css({position:"relative",top:0,left:0,right:"auto",bottom:"auto"})}f.css(J).show();var O=P.direction||"left";var t=(O=="up"||O=="down")?"top":"left";var H=(O=="up"||O=="left");var d=P.distance||(t=="top"?K.outerHeight({margin:true}):K.outerWidth({margin:true}));K.css(t,H?(isNaN(d)?"-"+d:-d):d);var I={};I[t]=(H?"+=":"-=")+d;f.animate({opacity:1},{duration:P.duration,easing:P.easing});K.animate(I,{queue:false,duration:P.duration,easing:P.easing,complete:function(){for(var Q in M){K[0].style[Q]=M[Q]}K.parent().replaceWith(K);if(P.complete){P.complete()}}})}return this}}jQuery.extend(jQuery.easing,{easeInOutExpo:function(e,f,a,h,g){if(f==0){return a}if(f==g){return a+h}if((f/=g/2)<1){return h/2*Math.pow(2,10*(f-1))+a}return h/2*(-Math.pow(2,-10*--f)+2)+a}});