<!DOCTYPE html>
<html lang="en-US">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name='description' content='Gender Fair - Search'>
        <meta name='author' content='Gender Fair'>
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=0">
        <title>Gender Fair - Company Search</title>
        <link href="css/theme.css" rel="stylesheet" type="text/css">
        <link href="css/cards.css" rel="stylesheet" type="text/css">
        <link rel="stylesheet" id="web-fonts-css" href="https://fonts.googleapis.com/css?family=Raleway:400,400italic,500,600,700,800,900" type="text/css" media="all">
    </head>
    <body>
        <!--START container-->
        <div id="#searchcontainer" class="maincontainer">
            <div>
                <h2>Family ipsum dolor sit amet, consectetur adipiscing elit.</h2>
            </div>
            <form id="form" action="" onsubmit="return false">
                <input type="text" id="txtSearch" name="txtSearch" spellcheck="false" value="" size="40" placeholder="Insert text to search">
                <input id="submit" type="button" name="submit" value="Search">
                <div id="lblError" class="label-error"></div>
                <div id="lblSearch" class="label-search">Searching...
                    <div id="loader"></div>
                </div>
            </form>
            <div id="title-results" class="title"></div>
            <div id="search-results" class="cardscontainer"></div>
            <div id="title-suggested" class="title"></div>
            <div id="search-suggested" class="cardscontainer"></div>
            <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
            <script type="text/javascript">
                var _0x18b8=['application/json','which','<div\x20class=\x27divider\x27></div>','<div\x20class=\x27company-row\x27>','#lblError','keypress','category','Only\x20Alphabets\x20and\x20Numbers\x20allowed.','http://accessocasa.ddns.net:3030/api/Search','GENDER\x20FAIR','\x27></div><div\x20class=\x27data-container\x27><p\x20class=\x27company-name\x27>','val','#title-suggested','</p><div\x20class=\x27isgf-container\x27><img\x20class=\x27company-icon\x27\x20src=\x27images/','#search-results','getElementsByTagName','length','#txtSearch','scrollHeight','fail','css','Please\x20enter\x20at\x20least\x20three\x20characters.','<h3>Uh\x20Oh!\x20We\x20cannot\x20find\x20anything\x20related\x20to\x20\x27','flex','isGenderFair','default','name','ready','NOT\x20GENDER\x20FAIR','keyCode','images/no-logo-placeholder.png','display','POST','click','stringify','html','done','#search-suggested','<div\x20class=\x27company-column\x27><div\x20class=\x27company-card\x27><div\x20class=\x27img-container\x27><img\x20src=\x27','Please\x20retry.','ajax','company-isGF','</div>','\x27</h3><div\x20class=\x27divider\x27></div>','none','#lblSearch','postMessage','#submit','setHeight','company-isGF\x20not','#title-results','icon-rr-gender-fair.svg','parent','each','results','logo','trim','cursor'];(function(_0x13cb88,_0x18b852){var _0x16dbc7=function(_0x4411b2){while(--_0x4411b2){_0x13cb88['push'](_0x13cb88['shift']());}};_0x16dbc7(++_0x18b852);}(_0x18b8,0x122));var _0x16db=function(_0x13cb88,_0x18b852){_0x13cb88=_0x13cb88-0x0;var _0x16dbc7=_0x18b8[_0x13cb88];return _0x16dbc7;};var _0x146c74=_0x16db;$(document)[_0x146c74('0x1b')](function(){var _0x2426f5=_0x146c74,_0x4411b2=document[_0x2426f5('0xf')](_0x2426f5('0x23'))[0x0][_0x2426f5('0x12')];function _0x4c01a2(){var _0x3b11ad=_0x2426f5,_0x344aac=document[_0x3b11ad('0xf')]('html')[0x0][_0x3b11ad('0x12')];window[_0x3b11ad('0x34')][_0x3b11ad('0x2e')]([_0x3b11ad('0x30'),_0x344aac],'*');}$(_0x2426f5('0x11'))['keypress'](function(_0x1b0f71){var _0xfa7473=_0x2426f5,_0x570872=_0x1b0f71[_0xfa7473('0x1d')]||_0x1b0f71['which'],_0x48821f=/^[A-Za-z0-9\r ]+$/;$(_0xfa7473('0x4'))[_0xfa7473('0x23')]('');var _0x325be3=_0x48821f['test'](String['fromCharCode'](_0x570872));return!_0x325be3&&$(_0xfa7473('0x4'))[_0xfa7473('0x23')](_0xfa7473('0x7')),_0x325be3;}),$(_0x2426f5('0x11'))[_0x2426f5('0x5')](function(_0x3f8883){var _0x5720ac=_0x2426f5;if(_0x3f8883[_0x5720ac('0x1')]==0xd)return _0x2577b3(),![];}),$(_0x2426f5('0x2f'))['on'](_0x2426f5('0x21'),function(){_0x2577b3();});function _0x2577b3(){var _0x1987b6=_0x2426f5,_0x32521c=$(_0x1987b6('0x11'))[_0x1987b6('0xb')]();_0x32521c=_0x32521c[_0x1987b6('0x38')](),$(_0x1987b6('0x11'))['val'](_0x32521c);if(_0x32521c[_0x1987b6('0x10')]<0x3)return $(_0x1987b6('0x4'))[_0x1987b6('0x23')](_0x1987b6('0x15')),![];window[_0x1987b6('0x34')]['postMessage']([_0x1987b6('0x30'),_0x4411b2],'*'),$('#title-results')[_0x1987b6('0x23')](''),$(_0x1987b6('0xe'))[_0x1987b6('0x23')](''),$(_0x1987b6('0xc'))[_0x1987b6('0x23')](''),$(_0x1987b6('0x25'))[_0x1987b6('0x23')](''),$('#lblError')['html'](''),$('*')['css']('cursor','progress'),$(_0x1987b6('0x2d'))[_0x1987b6('0x14')](_0x1987b6('0x1f'),_0x1987b6('0x17'));var _0x29511d={'url':_0x1987b6('0x8'),'method':_0x1987b6('0x20'),'timeout':0x0,'headers':{'Content-Type':_0x1987b6('0x0')},'data':JSON[_0x1987b6('0x22')]({'text':_0x32521c})};$[_0x1987b6('0x28')](_0x29511d)[_0x1987b6('0x24')](function(_0x49ea99){var _0x2963d3=_0x1987b6;$('*')[_0x2963d3('0x14')](_0x2963d3('0x39'),_0x2963d3('0x19')),$('#lblSearch')[_0x2963d3('0x14')]('display',_0x2963d3('0x2c'));var _0x48ad51='';$[_0x2963d3('0x35')](_0x49ea99,function(_0x78a6f9,_0x592cc4){var _0xff2df3=_0x2963d3;_0x48ad51='';for(var _0x248b1b=0x0;_0x248b1b<_0x592cc4[_0xff2df3('0x10')];_0x248b1b++){var _0xd8ac4a=_0x592cc4[_0x248b1b],_0x1a4e65='',_0x271be5='',_0xd278b2='',_0x26dbc3=_0xd8ac4a[_0xff2df3('0x37')];_0xd8ac4a[_0xff2df3('0x18')]==='Y'?(_0x1a4e65=_0xff2df3('0x33'),_0x271be5=_0xff2df3('0x9'),_0xd278b2=_0xff2df3('0x29')):(_0x1a4e65='icon-rr-not-gender-fair.svg',_0x271be5=_0xff2df3('0x1c'),_0xd278b2=_0xff2df3('0x31')),_0x26dbc3[_0xff2df3('0x10')]===0x0&&(_0x26dbc3=_0xff2df3('0x1e')),_0x48ad51+=_0xff2df3('0x26')+_0x26dbc3+_0xff2df3('0xa')+_0xd8ac4a[_0xff2df3('0x1a')]+'</p><p\x20class=\x27company-category\x27>'+_0xd8ac4a[_0xff2df3('0x6')]+_0xff2df3('0xd')+_0x1a4e65+'\x27><p\x20class=\x27'+_0xd278b2+'\x27>'+_0x271be5+'</p></div></div></div></div>';}if(_0x78a6f9===_0xff2df3('0x36')&&_0x48ad51['length']>0x0)$(_0xff2df3('0x32'))['html'](''),_0x48ad51=_0xff2df3('0x3')+_0x48ad51+_0xff2df3('0x2a'),$(_0xff2df3('0xe'))['html'](_0x48ad51+_0xff2df3('0x2'));else _0x78a6f9===_0xff2df3('0x36')&&_0x48ad51[_0xff2df3('0x10')]==0x0&&$(_0xff2df3('0x32'))[_0xff2df3('0x23')](_0xff2df3('0x16')+_0x32521c+_0xff2df3('0x2b'));_0x78a6f9==='suggested'&&_0x48ad51[_0xff2df3('0x10')]>0x0&&($(_0xff2df3('0xc'))[_0xff2df3('0x23')]('<h3>Explore\x20Gender\x20Fair\x20options:</h3>'),_0x48ad51=_0xff2df3('0x3')+_0x48ad51+_0xff2df3('0x2a'),$(_0xff2df3('0x25'))[_0xff2df3('0x23')](_0x48ad51));}),_0x4c01a2();})[_0x1987b6('0x13')](function(){var _0x487db6=_0x1987b6;$('*')[_0x487db6('0x14')](_0x487db6('0x39'),'default'),$(_0x487db6('0x2d'))[_0x487db6('0x14')](_0x487db6('0x1f'),_0x487db6('0x2c')),$(_0x487db6('0x4'))['html'](_0x487db6('0x27'));});}});
            </script>
        </div>
        <!--END container-->
    </body>
</html>
