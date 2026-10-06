/* The Long Game: fictional training challenges, historical-style rendering.
 * Standalone deterministic simulation: no DOM, network, audio or saved-data access.
 * Pixel grids are intentional compositions, not console emulation. */
(function(root,factory){if(typeof module==='object'&&module.exports)module.exports=factory();else root.LongGameTrials=factory();})(typeof globalThis!=='undefined'?globalThis:this,function(){
'use strict';
var STAGES=[
 {name:'FIRST TOUCH',era:'PONG',w:160,h:120,target:3,limit:35,action:'Return with ↑ / ↓',hint:'Move the paddle ↑ / ↓. Return 3 balls; meet each ball at the white contact line.',craft:'160 × 120 · two-tone rectangles · stepped paddle and ball',verb:'Track'},
 {name:'FIND THE GAP',era:'2600',w:160,h:120,target:4,limit:35,action:'Dash',hint:'Choose the empty lane with ← / →. Survive 4 waves. Dash through once a wave passes the halfway stripe for +50.',craft:'160 × 120 · eight-color playfield · repeated scanline bands',verb:'Dodge'},
 {name:'OVER THE LINE',era:'8-BIT',w:256,h:192,target:4,limit:35,action:'Jump',hint:'Space / Jump clears a hurdle. Clear 4. Hold → to sprint for +25 per hurdle; release to slow down.',craft:'256 × 192 · tile map · hand-built sprite poses · parallax',verb:'Jump'},
 {name:'CALL THE PLAY',era:'16-BIT',w:320,h:240,target:3,limit:30,action:'Pass',hint:'Pick A / B / C with ← / →, then Space to pass to the OPEN route. The defense switches every beat. Complete 3.',craft:'320 × 240 · layered route windows · scaled pitch · sprite shadows',verb:'Read'},
 {name:'BEND THE SHOT',era:'POLYGON',w:480,h:360,target:3,limit:45,action:'Hold / release shot',hint:'Aim ← / → at the gold target. Hold Space / Shot; release in the green power band. Score 3. Power and aim both count.',craft:'480 × 360 · early-3D-inspired 2.5D · projected pitch and faceted limbs',verb:'Aim'},
 {name:'BEAT THE PRESS',era:'HD',w:960,h:540,target:4,limit:32,action:'Pass',hint:'Select a teammate ← / →, then Space to pass. Gold breaks a line (+150); white recycles safely (+75). Red is marked. Complete 4.',craft:'960 × 540 · smooth vectors · depth gradients · tactical passing lanes',verb:'Choose'},
 {name:'FIND YOUR RHYTHM',era:'ANIME',w:640,h:360,target:4,limit:30,action:'Strike',hint:'Match the direction shown, then Space / Strike as the ring meets the gold circle. Land 4 combinations. No flashing impacts.',craft:'640 × 360 · cel silhouettes · bold ink · timed pose changes',verb:'Combine'},
 {name:'KEEP THE MOMENT',era:'REAL',w:960,h:540,target:3,limit:45,action:'Shutter',hint:'Move the viewfinder with all four arrows. Align its center with the gold mark, stop to steady it, then press Space / Shutter. Frame 3 details.',craft:'960 × 540 · existing real photograph · camera framing · contact sheet',verb:'Frame'}
];
var clamp=function(v,a,b){return Math.max(a,Math.min(b,v));};
function create(era,pro){return {era:clamp(era|0,0,7),pro:!!pro,phase:'ready',elapsed:0,time:0,round:0,hits:0,lives:3,score:0,combo:0,feedback:'Ready when you are.',event:0,lastGood:false,cool:0,lane:1,paddle:.5,bx:.86,by:.28,wave:-.1,obstacle:1,jump:0,vy:0,aim:0,power:0,charging:false,beat:0,choice:'',x:.5,y:.5,vx:0,vyPhoto:0,shots:[],keys:{},prior:{},repeat:0};}
function start(s){if(s.phase==='ready'){s.phase='playing';s.feedback=STAGES[s.era].hint;s.event++;}}
function release(s){s.keys={};s.prior={};s.charging=false;s.power=0;}
function target(s){return [{x:.22,y:.46},{x:.73,y:.31},{x:.49,y:.73}][s.round%3];}
function openLane(s){if(s.era===1)return [0,2,1,0,2][s.round%5];if(s.era===3)return (s.round+Math.floor(s.elapsed/(s.pro?.85:1.25)))%3;return (s.round+Math.floor(s.elapsed/(s.pro?1.1:1.65)))%3;}
function direction(s){return ['left','up','right','down'][s.round%4];}
function finish(s,good,msg,points){if(s.phase!=='playing'||s.cool>0)return;s.event++;s.lastGood=good;s.flight={lane:s.lane,aim:s.aim,good:good};s.feedback=msg;if(good){s.hits++;s.combo++;s.score+=Math.round((points||100)*(s.pro?1.5:1));}else{s.lives--;s.combo=0;}s.round++;s.cool=.65;s.bx=.86;s.by=[.25,.7,.42,.78,.3][s.round%5];s.wave=-.1;s.obstacle=1;s.beat=0;s.choice='';s.charging=false;s.power=0;s.time=0;
 if(s.hits>=STAGES[s.era].target){s.phase='won';s.score+=s.lives*50;s.feedback='STAGE CLEAR · '+s.score+' points. '+s.lives+' chances kept.';}else if(s.lives<=0){s.phase='lost';s.feedback='ROUND OVER · '+msg+' Retry this era; earlier stages stay cleared.';}}
function act(s){if(s.phase!=='playing'||s.cool>0)return;var e=s.era,open=openLane(s);
 if(e===1){var good=s.lane===open&&s.wave>.42;finish(s,good,good?'GAP FOUND · early dash +150':s.wave<=.42?'Too early. Wait for the halfway stripe.':'Blocked lane. Read the gap before dashing.',150);}
 if(e===2&&s.jump===0){s.vy=1.14;s.feedback='Up and over.';s.event++;}
 if(e===3){finish(s,s.lane===open,s.lane===open?'OPEN ROUTE · completed pass':'Covered receiver. Read the OPEN window before passing.',125);}
 if(e===5){var support=(open+1)%3;finish(s,s.lane===open||s.lane===support,s.lane===open?'LINE BROKEN · +150':s.lane===support?'RECYCLED SAFELY · +75':'Intercepted. Red is marked; keep the ball moving.',s.lane===open?150:75);}
 if(e===6){var phase=s.beat/1.65,err=Math.abs(phase-.66),correct=s.choice===direction(s);var good=correct&&err<(s.pro?.095:.16);finish(s,good,!correct?'Direction first. Match the arrow, then strike.':good?(err<.055?'PERFECT SYNC · +175':'IN RHYTHM · +100'):phase<.66?'Early. Let the ring close in.':'Late. Strike as the rings meet.',err<.055?175:100);}
 if(e===7){var tg=target(s),near=Math.hypot(s.x-tg.x,s.y-tg.y)<(s.pro?.065:.095),steady=Math.hypot(s.vx,s.vyPhoto)<.07;var ok=near&&steady;if(ok)s.shots.push({x:s.x,y:s.y});finish(s,ok,ok?'MOMENT KEPT · a new frame in your contact sheet':!near?'Reframe. Move the center into the gold mark.':'Still moving. Release the arrows and settle before the shutter.',150);}}
function shot(s){if(s.phase!=='playing'||s.cool>0)return;var tg=[-.64,.64,0][s.round%3],aimOK=Math.abs(s.aim-tg)<(s.pro?.18:.27),powerOK=s.power>=.42&&s.power<=.78;finish(s,aimOK&&powerOK,aimOK&&powerOK?'IN THE CORNER · aim and power together':!aimOK?'Wide. Aim at the gold target before charging.':s.power<.42?'Underhit. Hold until the green power band.':'Overhit. Release before the bar leaves green.',150);}
function step(s,dt,input){dt=clamp(dt,0,.05);s.keys=input||{};if(s.phase!=='playing'){s.prior=Object.assign({},s.keys);return;}s.elapsed+=dt;s.time+=dt;
 if(s.elapsed>=STAGES[s.era].limit){s.phase='lost';s.feedback='TIME · Retry this era. Read the cue, then commit.';s.event++;return;}
 if(s.cool>0){s.cool=Math.max(0,s.cool-dt);s.prior=Object.assign({},s.keys);return;}
 var k=s.keys,rise=function(key){return !!k[key]&&!s.prior[key];},horizontal=(k.right?1:0)-(k.left?1:0),vertical=(k.down?1:0)-(k.up?1:0);
 if(s.era===1||s.era===3||s.era===5){s.repeat-=dt;if((rise('left')||rise('right')||s.repeat<=0)&&horizontal){s.lane=clamp(s.lane+horizontal,0,2);s.repeat=.24;}}
 if(s.era===0){s.paddle=clamp(s.paddle+vertical*dt*.78,.12,.88);s.bx-=dt*(s.pro?.42:.31)*(1+s.hits*.12);if(s.bx<=.13){var hit=Math.abs(s.paddle-s.by)<(s.pro?.115:.17);finish(s,hit,hit?'CLEAN RETURN · meet the next ball':'Ball missed. Move the paddle to meet its height.',100);}}
 if(s.era===1){s.wave+=dt*(s.pro?.43:.31);if(s.wave>=.82)finish(s,s.lane===openLane(s),s.lane===openLane(s)?'SAFE THROUGH · +100':'Tackle. Move into the empty lane.',100);}
 if(s.era===2){if(rise('up'))act(s);s.obstacle-=dt*(s.pro?.48:.35)*(k.right?1.3:1);s.jump=Math.max(0,s.jump+s.vy*dt);s.vy-=dt*2.7;if(s.jump===0)s.vy=0;if(s.obstacle<=.24){var clear=s.jump>(s.pro?.16:.12);finish(s,clear,clear?(k.right?'SPRINT CLEAR · +125':'HURDLE CLEAR · +100'):'Caught the hurdle. Jump when it approaches the dashed line.',k.right?125:100);}}
 if(s.era===4){s.aim=clamp(s.aim+horizontal*dt*1.05,-.95,.95);if(rise('action')){s.charging=true;s.power=0;}if(s.charging)s.power=clamp(s.power+dt*.72,0,1);if(!k.action&&s.prior.action&&s.charging)shot(s);}
 if(s.era===5&&s.time>(s.pro?4:6))finish(s,false,'The press arrived. Release the pass sooner.',0);
 if(s.era===6){['left','right','up','down'].forEach(function(d){if(rise(d))s.choice=d;});s.beat+=dt;if(s.beat>1.65)finish(s,false,'Beat missed. Choose the arrow, then meet the ring.',0);}
 if(s.era===7){s.vx+=(horizontal*.45-s.vx)*Math.min(1,dt*12);s.vyPhoto+=(vertical*.45-s.vyPhoto)*Math.min(1,dt*12);s.x=clamp(s.x+s.vx*dt,.08,.92);s.y=clamp(s.y+s.vyPhoto*dt,.15,.84);}
 if(rise('action')&&s.era!==4)act(s);
 s.prior=Object.assign({},k);
}
function render(g,s,photo,calm,assets){
 if(typeof LongGameVisuals==='undefined')throw new Error('The graphics module did not load. Reload the page to retry.');
 return LongGameVisuals.render(g,s,photo,calm,assets,{open:openLane(s),targetShot:[-.64,.64,0][s.round%3],photoTarget:target(s),direction:direction(s),targetCount:STAGES[s.era].target,verb:STAGES[s.era].verb});
}
if(typeof LongGameVisuals!=='undefined')STAGES.forEach(function(stage,i){stage.w=LongGameVisuals.profiles[i].w;stage.h=LongGameVisuals.profiles[i].h;stage.craft=LongGameVisuals.profiles[i].craft;});

return {stages:STAGES,create:create,start:start,step:step,release:release,render:render,openLane:openLane,target:target,direction:direction};
});
