#!/usr/bin/python

import dryscrape as ds
import sys

# Has the website code go here.
code = '''

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" dir="ltr" lang="en" xml:lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link rel="stylesheet" type="text/css" href="http://websites.bordengrammar.kent.sch.uk/moodle/theme/standard/styles.php" />
<link rel="stylesheet" type="text/css" href="http://websites.bordengrammar.kent.sch.uk/moodle/theme/prettysimple/styles.php" />


<link rel="schema.DC" href="http://purl.org/dc/elements/1.1/" />
<meta name="DC:Creator" content="DAaid Phillips" />
<meta name="DC:Title" content="Qulaity of Information" />


<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />



<!-- Made with executable version 6.x (Moodle 1.9.14 (Build: 20111010), hotpot-module v2.4.13) -->

<!-- The following insertion allows you to add your own code directly to this head tag from the configuration screen -->









<style type="text/css">


/* This is the CSS stylesheet used in the exercise. */
/* Elements in square brackets are replaced by data based on configuration settings when the exercise is built. */

/* BeginCorePageCSS */

/* Made with executable version 6.x (Moodle 1.9.14 (Build: 20111010), hotpot-module ) */


/* Hack to hide a nested Quicktime player from IE, which can't handle it. */
* html object.MediaPlayerNotForIE {
	display: none;
}

body{
	font-family: Geneva,Arial,sans-serif;
	background-color: #C0C0C0;
	color: #000000;

	margin-right: 5%;
	margin-left: 5%;
	font-size: small;
}

p{
	text-align: left;
	margin: 0px;
	font-size: 100%;
}

table,div,span,td{
	font-size: 100%;
	color: #000000;
}

div.Titles{
	padding: 0.5em;;
	text-align: center;
	color: #000000;
}

button{
	font-family: Geneva,Arial,sans-serif;
	font-size: 100%;
	display: inline;
}

.ExerciseTitle{
	font-size: 140%;
	color: #000000;
}

.ExerciseSubtitle{
	font-size: 120%;
	color: #000000;
}

div.StdDiv{
	background-color: #FFFFFF;
	text-align: center;
	font-size: 100%;
	color: #000000;
	padding: 0.5em;
	border-style: solid;
	border-width: 1px 1px 1px 1px;
	border-color: #000000;
	margin-bottom: 1px;
}

/* EndCorePageCSS */

.RTLText{
	text-align: right;
	font-size: 150%;
	direction: rtl;
	font-family: "Simplified Arabic", "Traditional Arabic", "Times New Roman", Geneva,Arial,sans-serif;
}

.CentredRTLText{
	text-align: center;
	font-size: 150%;
	direction: rtl;
	font-family: "Simplified Arabic", "Traditional Arabic", "Times New Roman", Geneva,Arial,sans-serif;
}

button p.RTLText{
	text-align: center;
}

.RTLGapBox{
	text-align: right;
	font-size: 150%;
	direction: rtl;
	font-family: "Times New Roman", Geneva,Arial,sans-serif;
}

.Guess{
	font-weight: bold;
}

.CorrectAnswer{
	font-weight: bold;
}

div#Timer{
	padding: 0.25em;
	margin-left: auto;
	margin-right: auto;
	text-align: center;
	color: #000000;
}

span#TimerText{
	padding: 0.25em;
	border-width: 1px;
	border-style: solid;
	font-weight: bold;
	display: none;
	color: #000000;
}

span.Instructions{

}

div.ExerciseText{

}

.FeedbackText, .FeedbackText span.CorrectAnswer, .FeedbackText span.Guess, .FeedbackText span.Answer{
	color: #000000;
}

.LeftItem{
	font-size: 100%;
	color: #000000;
	text-align: left;
}

.RightItem{
	font-weight: bold;
	font-size: 100%;
	color: #000000;
}

span.CorrectMark{

}

input, textarea{
	font-family: Geneva,Arial,sans-serif;
	font-size: 120%;
}

select{
	font-size: 100%;
}

div.Feedback {
	background-color: #C0C0C0;
	left: 33%;
	width: 34%;
	top: 33%;
	z-index: 1;
	border-style: solid;
	border-width: 1px;
	padding: 5px;
	text-align: center;
	color: #000000;
	position: absolute;
	display: none;
	font-size: 100%;
}




div.ExerciseDiv{
	color: #000000;
}

/* JMatch flashcard styles */
table.FlashcardTable{
	background-color: transparent;
	color: #000000;
	border-color: #000000;
	margin-left: 5%;
	margin-right: 5%;
	margin-top: 2em;
	margin-bottom: 2em;
	width: 90%;
	position: relative;
	text-align: center;
	padding: 0px;
}

table.FlashcardTable tr{
	border-style: none;
	margin: 0px;
	padding: 0px;
	background-color: #FFFFFF;
}

table.FlashcardTable td.Showing{
	font-size: 140%;
	text-align: center;
	width: 50%;
	display: table-cell;
	padding: 2em;
	margin: 0px;
	border-style: solid;
	border-width: 1px;
	color: #000000;
	background-color: #FFFFFF;
}

table.FlashcardTable td.Hidden{
	display: none;
}

/* JMix styles */
div#SegmentDiv{
	margin-top: 2em;
	margin-bottom: 2em;
	text-align: center;
}

a.ExSegment{
	font-size: 120%;
	font-weight: bold;
	text-decoration: none;
	color: #000000;
}

span.RemainingWordList{
	font-style: italic;
}

div.DropLine {
	position: absolute;
	text-align: center;
	border-bottom-style: solid;
	border-bottom-width: 1px;
	border-bottom-color: #000000;
	width: 80%;
}

/* JCloze styles */

.ClozeWordList{
	text-align: center;
	font-weight: bold;
}

div.ClozeBody{
	text-align: left;
	margin-top: 2em;
	margin-bottom: 2em;
	line-height: 2.0
}

span.GapSpan{
	font-weight: bold;
}

/* JCross styles */

table.CrosswordGrid{
	margin: auto auto 1em auto;
	border-collapse: collapse;
	padding: 0px;
	background-color: #000000;
}

table.CrosswordGrid tbody tr td{
	width: 1.5em;
	height: 1.5em;
	text-align: center;
	vertical-align: middle;
	font-size: 140%;
	padding: 1px;
	margin: 0px;
	border-style: solid;
	border-width: 1px;
	border-color: #000000;
	color: #000000;
}

table.CrosswordGrid span{
	color: #000000;
}

table.CrosswordGrid td.BlankCell{
	background-color: #000000;
	color: #000000;
}

table.CrosswordGrid td.LetterOnlyCell{
	text-align: center;
	vertical-align: middle;
	background-color: #ffffff;
	color: #000000;
	font-weight: bold;
}

table.CrosswordGrid td.NumLetterCell{
	text-align: left;
	vertical-align: top;
	background-color: #ffffff;
	color: #000000;
	padding: 1px;
	font-weight: bold;
}

.NumLetterCellText{
	cursor: pointer;
	color: #000000;
}

.GridNum{
	vertical-align: super;
	font-size: 66%;
	font-weight: bold;
	text-decoration: none;
	color: #000000;
}

.GridNum:hover, .GridNum:visited{
	color: #000000;
}

table#Clues{
	margin: auto;
	vertical-align: top;
}

table#Clues td{
	vertical-align: top;
}

table.ClueList{
  margin: auto;
}

td.ClueNum{
	text-align: right;
	font-weight: bold;
	vertical-align: top;
}

td.Clue{
	text-align: left;
}

div#ClueEntry{
	text-align: left;
	margin-bottom: 1em;
}

/* Keypad styles */

div.Keypad{
	text-align: center;
	display: none; /* initially hidden, shown if needed */
	margin-bottom: 0.5em;
}

div.Keypad button{
	font-family: Geneva,Arial,sans-serif;
	font-size: 120%;
	background-color: #ffffff;
	color: #000000;
	width: 2em;
}

/* JQuiz styles */

div.QuestionNavigation{
	text-align: center;
}

.QNum{
	margin: 0em 1em 0.5em 1em;
	font-weight: bold;
	vertical-align: middle;
}

textarea{
	font-family: Geneva,Arial,sans-serif;
}

.QuestionText{
	text-align: left;
	margin: 0px;
	font-size: 100%;
}

.Answer{
	font-size: 120%;
	letter-spacing: 0.1em;
}

.PartialAnswer{
	font-size: 120%;
	letter-spacing: 0.1em;
	color: #000000;
}

.Highlight{
	color: #000000;
	background-color: #ffff00;
	font-weight: bold;
	font-size: 120%;
}

ol.QuizQuestions{
	text-align: left;
	list-style-type: none;
}

li.QuizQuestion{
	padding: 1em;
	border-style: solid;
	border-width: 0px 0px 1px 0px;
}

ol.MCAnswers{
	text-align: left;
	list-style-type: upper-alpha;
	padding: 1em;
}

ol.MCAnswers li{
	margin-bottom: 1em;
}

ol.MSelAnswers{
	text-align: left;
	list-style-type: lower-alpha;
	padding: 1em;
}

div.ShortAnswer{
	padding: 1em;
}

.FuncButton {
	text-align: center;
	border-style: solid;

	border-left-color: #ffffff;
	border-top-color: #ffffff;
	border-right-color: #7f7f7f;
	border-bottom-color: #7f7f7f;
	color: #000000;
	background-color: #FFFFFF;

	border-width: 2px;
	padding: 3px 6px 3px 6px;
	cursor: pointer;
}

.FuncButtonUp {
	color: #FFFFFF;
	text-align: center;
	border-style: solid;

	border-left-color: #ffffff;
	border-top-color: #ffffff;
	border-right-color: #7f7f7f;
	border-bottom-color: #7f7f7f;

	background-color: #000000;
	color: #FFFFFF;
	border-width: 2px;
	padding: 3px 6px 3px 6px;
	cursor: pointer;
}

.FuncButtonDown {
	color: #FFFFFF;
	text-align: center;
	border-style: solid;

	border-left-color: #7f7f7f;
	border-top-color: #7f7f7f;
	border-right-color: #ffffff;
	border-bottom-color: #ffffff;
	background-color: #000000;
	color: #FFFFFF;

	border-width: 2px;
	padding: 3px 6px 3px 6px;
	cursor: pointer;
}

/*BeginNavBarStyle*/

div.NavButtonBar{
	background-color: #000000;
	text-align: center;
	margin: 2px 0px 2px 0px;
	clear: both;
	font-size: 100%;
}

.NavButton {
	border-style: solid;

	border-left-color: #7f7f7f;
	border-top-color: #7f7f7f;
	border-right-color: #000000;
	border-bottom-color: #000000;
	background-color: #000000;
	color: #C0C0C0;

	border-width: 2px;
	cursor: pointer;
}

.NavButtonUp {
	border-style: solid;

	border-left-color: #7f7f7f;
	border-top-color: #7f7f7f;
	border-right-color: #000000;
	border-bottom-color: #000000;
	color: #000000;
	background-color: #C0C0C0;

	border-width: 2px;
	cursor: pointer;
}

.NavButtonDown {
	border-style: solid;

	border-left-color: #000000;
	border-top-color: #000000;
	border-right-color: #7f7f7f;
	border-bottom-color: #7f7f7f;
	color: #000000;
	background-color: #C0C0C0;

	border-width: 2px;
	cursor: pointer;
}

/*EndNavBarStyle*/

a{
	color: #0000FF;
}

a:visited{
	color: #0000CC;
}

a:hover{
	color: #0000FF;
}

div.CardStyle {
	position: absolute;
	font-family: Geneva,Arial,sans-serif;
	font-size: 100%;
	padding: 5px;
	border-style: solid;
	border-width: 1px;
	color: #000000;
	background-color: #FFFFFF;
	left: -50px;
	top: -50px;
	overflow: visible;
}

.rtl{
	text-align: right;
	font-size: 140%;
}


</style>
<script type="text/javascript">

//<![CDATA[

<!--




function Client(){
//if not a DOM browser, hopeless
	this.min = false; if (document.getElementById){this.min = true;};

	this.ua = navigator.userAgent;
	this.name = navigator.appName;
	this.ver = navigator.appVersion;

//Get data about the browser
	this.mac = (this.ver.indexOf('Mac') != -1);
	this.win = (this.ver.indexOf('Windows') != -1);

//Look for Gecko
	this.gecko = (this.ua.indexOf('Gecko') > 1);
	if (this.gecko){
		this.geckoVer = parseInt(this.ua.substring(this.ua.indexOf('Gecko')+6, this.ua.length));
		if (this.geckoVer < 20020000){this.min = false;}
	}

//Look for Firebird
	this.firebird = (this.ua.indexOf('Firebird') > 1);

//Look for Safari
	this.safari = (this.ua.indexOf('Safari') > 1);
	if (this.safari){
		this.gecko = false;
	}

//Look for IE
	this.ie = (this.ua.indexOf('MSIE') > 0);
	if (this.ie){
		this.ieVer = parseFloat(this.ua.substring(this.ua.indexOf('MSIE')+5, this.ua.length));
		if (this.ieVer < 5.5){this.min = false;}
	}

//Look for Opera
	this.opera = (this.ua.indexOf('Opera') > 0);
	if (this.opera){
		this.operaVer = parseFloat(this.ua.substring(this.ua.indexOf('Opera')+6, this.ua.length));
		if (this.operaVer < 7.04){this.min = false;}
	}
	if (this.min == false){
		alert('Your browser may not be able to handle this page.');
	}

//Special case for the horrible ie5mac
	this.ie5mac = (this.ie&&this.mac&&(this.ieVer<6));
}

var C = new Client();

//for (prop in C){
//	alert(prop + ': ' + C[prop]);
//}



//CODE FOR HANDLING NAV BUTTONS AND FUNCTION BUTTONS

//
function NavBtnOver(Btn){
	if (Btn.className != 'NavButtonDown'){Btn.className = 'NavButtonUp';}
}

function NavBtnOut(Btn){
	Btn.className = 'NavButton';
}

function NavBtnDown(Btn){
	Btn.className = 'NavButtonDown';
}
//

function FuncBtnOver(Btn){
	if (Btn.className != 'FuncButtonDown'){Btn.className = 'FuncButtonUp';}
}

function FuncBtnOut(Btn){
	Btn.className = 'FuncButton';
}

function FuncBtnDown(Btn){
	Btn.className = 'FuncButtonDown';
}

function FocusAButton(){
	if (document.getElementById('CheckButton1') != null){
		document.getElementById('CheckButton1').focus();
	}
	else{
		if (document.getElementById('CheckButton2') != null){
			document.getElementById('CheckButton2').focus();
		}
		else{
			document.getElementsByTagName('button')[0].focus();
		}
	}
}




//CODE FOR HANDLING DISPLAY OF POPUP FEEDBACK BOX

var topZ = 1000;

function ShowMessage(Feedback){
	var Output = Feedback + '<br /><br />';
	document.getElementById('FeedbackContent').innerHTML = Output;
	var FDiv = document.getElementById('FeedbackDiv');
	topZ++;
	FDiv.style.zIndex = topZ;
	FDiv.style.top = TopSettingWithScrollOffset(30) + 'px';

	FDiv.style.display = 'block';

	ShowElements(false, 'input');
	ShowElements(false, 'select');
	ShowElements(false, 'object');
	ShowElements(true, 'object', 'FeedbackContent');

//Focus the OK button
	setTimeout("document.getElementById('FeedbackOKButton').focus()", 50);

//
}

function ShowElements(Show, TagName, ContainerToReverse){
// added third argument to allow objects in the feedback box to appear
//IE bug -- hide all the form elements that will show through the popup
//FF on Mac bug : doesn't redisplay objects whose visibility is set to visible
//unless the object's display property is changed

	//get container object (by Id passed in, or use document otherwise)
	TopNode = document.getElementById(ContainerToReverse);
	var Els;
	if (TopNode != null) {
		Els = TopNode.getElementsByTagName(TagName);
	} else {
		Els = document.getElementsByTagName(TagName);
	}

	for (var i=0; i<Els.length; i++){
		if (TagName == "object") {
			//manipulate object elements in all browsers
			if (Show == true){
				Els[i].style.visibility = 'visible';
				//get Mac FireFox to manipulate display, to force screen redraw
				if (C.mac && C.gecko) {Els[i].style.display = '';}
			}
			else{
				Els[i].style.visibility = 'hidden';
				if (C.mac && C.gecko) {Els[i].style.display = 'none';}
			}
		}
		else {
			// tagName is either input or select (that is, Form Elements)
			// ie6 has a problem with Form elements, so manipulate those
			if (C.ie) {
				if (C.ieVer < 7) {
					if (Show == true){
						Els[i].style.visibility = 'visible';
					}
					else{
						Els[i].style.visibility = 'hidden';
					}
				}
			}
		}
	}
}



function HideFeedback(){
	document.getElementById('FeedbackDiv').style.display = 'none';
	ShowElements(true, 'input');
	ShowElements(true, 'select');
	ShowElements(true, 'object');
	if (Finished == true){
		Finish();
	}
}


//GENERAL UTILITY FUNCTIONS AND VARIABLES

//PAGE DIMENSION FUNCTIONS
function PageDim(){
//Get the page width and height
	this.W = 600;
	this.H = 400;
	this.W = document.getElementsByTagName('body')[0].clientWidth;
	this.H = document.getElementsByTagName('body')[0].clientHeight;
}

var pg = null;

function GetPageXY(El) {
	var XY = {x: 0, y: 0};
	while(El){
		XY.x += El.offsetLeft;
		XY.y += El.offsetTop;
		El = El.offsetParent;
	}
	return XY;
}

function GetScrollTop(){
	if (typeof(window.pageYOffset) == 'number'){
		return window.pageYOffset;
	}
	else{
		if ((document.body)&&(document.body.scrollTop)){
			return document.body.scrollTop;
		}
		else{
			if ((document.documentElement)&&(document.documentElement.scrollTop)){
				return document.documentElement.scrollTop;
			}
			else{
				return 0;
			}
		}
	}
}

function GetViewportHeight(){
	if (typeof window.innerHeight != 'undefined'){
		return window.innerHeight;
	}
	else{
		if (((typeof document.documentElement != 'undefined')&&(typeof document.documentElement.clientHeight !=
     'undefined'))&&(document.documentElement.clientHeight != 0)){
			return document.documentElement.clientHeight;
		}
		else{
			return document.getElementsByTagName('body')[0].clientHeight;
		}
	}
}

function TopSettingWithScrollOffset(TopPercent){
	var T = Math.floor(GetViewportHeight() * (TopPercent/100));
	return GetScrollTop() + T;
}

//CODE FOR AVOIDING LOSS OF DATA WHEN BACKSPACE KEY INVOKES history.back()
var InTextBox = false;

function SuppressBackspace(e){
	if (InTextBox == true){return;}
	if (C.ie) {
		thisKey = window.event.keyCode;
	}
	else {
		thisKey = e.keyCode;
	}

	var Suppress = false;

	if (thisKey == 8) {
		Suppress = true;
	}

	if (Suppress == true){
		if (C.ie){
			window.event.returnValue = false;
			window.event.cancelBubble = true;
		}
		else{
			e.preventDefault();
		}
	}
}

if (C.ie){
	document.attachEvent('onkeydown',SuppressBackspace);
	window.attachEvent('onkeydown',SuppressBackspace);
}
else{
	if (window.addEventListener){
		window.addEventListener('keypress',SuppressBackspace,false);
	}
}

function ReduceItems(InArray, ReduceToSize){
	var ItemToDump=0;
	var j=0;
	while (InArray.length > ReduceToSize){
		ItemToDump = Math.floor(InArray.length*Math.random());
		InArray.splice(ItemToDump, 1);
	}
}

function Shuffle(InArray){
	var Num;
	var Temp = new Array();
	var Len = InArray.length;

	var j = Len;

	for (var i=0; i<Len; i++){
		Temp[i] = InArray[i];
	}

	for (i=0; i<Len; i++){
		Num = Math.floor(j  *  Math.random());
		InArray[i] = Temp[Num];

		for (var k=Num; k < (j-1); k++) {
			Temp[k] = Temp[k+1];
		}
		j--;
	}
	return InArray;
}

function WriteToInstructions(Feedback) {
	document.getElementById('InstructionsDiv').innerHTML = Feedback;

}




function EscapeDoubleQuotes(InString){
	return InString.replace(/"/g, '&quot;')
}

function TrimString(InString){
        var x = 0;

        if (InString.length != 0) {
                while ((InString.charAt(InString.length - 1) == '\u0020') || (InString.charAt(InString.length - 1) == '\u000A') || (InString.charAt(InString.length - 1) == '\u000D')){
                        InString = InString.substring(0, InString.length - 1)
                }

                while ((InString.charAt(0) == '\u0020') || (InString.charAt(0) == '\u000A') || (InString.charAt(0) == '\u000D')){
                        InString = InString.substring(1, InString.length)
                }

                while (InString.indexOf('  ') != -1) {
                        x = InString.indexOf('  ')
                        InString = InString.substring(0, x) + InString.substring(x+1, InString.length)
                 }

                return InString;
        }

        else {
                return '';
        }
}

function FindLongest(InArray){
	if (InArray.length < 1){return -1;}

	var Longest = 0;
	for (var i=1; i<InArray.length; i++){
		if (InArray[i].length > InArray[Longest].length){
			Longest = i;
		}
	}
	return Longest;
}

//UNICODE CHARACTER FUNCTIONS
function IsCombiningDiacritic(CharNum){
	var Result = (((CharNum >= 0x0300)&&(CharNum <= 0x370))||((CharNum >= 0x20d0)&&(CharNum <= 0x20ff)));
	Result = Result || (((CharNum >= 0x3099)&&(CharNum <= 0x309a))||((CharNum >= 0xfe20)&&(CharNum <= 0xfe23)));
	return Result;
}

function IsCJK(CharNum){
	return ((CharNum >= 0x3000)&&(CharNum < 0xd800));
}

//SETUP FUNCTIONS
//BROWSER WILL REFILL TEXT BOXES FROM CACHE IF NOT PREVENTED
function ClearTextBoxes(){
	var NList = document.getElementsByTagName('input');
	for (var i=0; i<NList.length; i++){
		if ((NList[i].id.indexOf('Guess') > -1)||(NList[i].id.indexOf('Gap') > -1)){
			NList[i].value = '';
		}
		if (NList[i].id.indexOf('Chk') > -1){
			NList[i].checked = '';
		}
	}
}

//EXTENSION TO ARRAY OBJECT
function Array_IndexOf(Input){
	var Result = -1;
	for (var i=0; i<this.length; i++){
		if (this[i] == Input){
			Result = i;
		}
	}
	return Result;
}
Array.prototype.indexOf = Array_IndexOf;

//IE HAS RENDERING BUG WITH BOTTOM NAVBAR
function RemoveBottomNavBarForIE(){
	if ((C.ie)&&(document.getElementById('Reading') != null)){
		if (document.getElementById('BottomNavBar') != null){
			document.getElementById('mod-hotpot-view').removeChild(document.getElementById('BottomNavBar'));
		}
	}
}




//HOTPOTNET-RELATED CODE

var HPNStartTime = (new Date()).getTime();
var SubmissionTimeout = 30000;
var Detail = ''; //Global that is used to submit tracking data

function Finish(){
//If there's a form, fill it out and submit it
	if (document.store != null){
		Frm = document.store;
		Frm.starttime.value = HPNStartTime;
		Frm.endtime.value = (new Date()).getTime();
		Frm.mark.value = Score;
		Frm.detail.value = Detail;
		Frm.submit();
	}
}





//JQUIZ CORE JAVASCRIPT CODE

var CurrQNum = 0;
var CorrectIndicator = ':-)';
var IncorrectIndicator = 'X';
var YourScoreIs = 'Your score is ';
var ContinuousScoring = true;
var CorrectFirstTime = 'Questions answered correctly first time: ';
var ShowCorrectFirstTime = true;
var ShuffleQs = false;
var ShuffleAs = false;
var DefaultRight = 'Correct!';
var DefaultWrong = 'Sorry! Try again.';
var QsToShow = 10;
var Score = 0;
var Finished = false;
var Qs = null;
var QArray = new Array();
var ShowingAllQuestions = false;
var ShowAllQuestionsCaption = 'Show all questions';
var ShowOneByOneCaption = 'Show questions one by one';
var State = new Array();
var Feedback = '';
var TimeOver = false;
var strInstructions = '';
var Locked = false;

//The following variable can be used to add a message explaining that
//the question is finished, so no further marking will take place.
var strQuestionFinished = '';

function CompleteEmptyFeedback(){
	var QNum, ANum;
	for (QNum=0; QNum<I.length; QNum++){
//Only do this if not multi-select
		if (I[QNum][2] != '3'){
  		for (ANum = 0; ANum<I[QNum][3].length; ANum++){
  			if (I[QNum][3][ANum][1].length < 1){
  				if (I[QNum][3][ANum][2] > 0){
  					I[QNum][3][ANum][1] = DefaultRight;
  				}
  				else{
  					I[QNum][3][ANum][1] = DefaultWrong;
  				}
  			}
  		}
		}
	}
}

function SetUpQuestions(){
	var AList = new Array();
	var QList = new Array();
	var i, j;
	Qs = document.getElementById('Questions');
	while (Qs.getElementsByTagName('li').length > 0){
		QList.push(Qs.removeChild(Qs.getElementsByTagName('li')[0]));
	}
	var DumpItem = 0;
	if (QsToShow > QList.length){
		QsToShow = QList.length;
	}
	while (QsToShow < QList.length){
		DumpItem = Math.floor(QList.length*Math.random());
		for (j=DumpItem; j<(QList.length-1); j++){
			QList[j] = QList[j+1];
		}
		QList.length = QList.length-1;
	}
	if (ShuffleQs == true){
		QList = Shuffle(QList);
	}
	if (ShuffleAs == true){
		var As;
		for (var i=0; i<QList.length; i++){
			As = QList[i].getElementsByTagName('ol')[0];
			if (As != null){
  			AList.length = 0;
				while (As.getElementsByTagName('li').length > 0){
					AList.push(As.removeChild(As.getElementsByTagName('li')[0]));
				}
				AList = Shuffle(AList);
				for (j=0; j<AList.length; j++){
					As.appendChild(AList[j]);
				}
			}
		}
	}

	for (i=0; i<QList.length; i++){
		Qs.appendChild(QList[i]);
		QArray[QArray.length] = QList[i];
	}

//Show the first item
	QArray[0].style.display = '';

//Now hide all except the first item
	for (i=1; i<QArray.length; i++){
		QArray[i].style.display = 'none';
	}
	SetQNumReadout();

	SetFocusToTextbox();
}

function SetFocusToTextbox(){
//if there's a textbox, set the focus in it
	if (QArray[CurrQNum].getElementsByTagName('input')[0] != null){
		QArray[CurrQNum].getElementsByTagName('input')[0].focus();
//and show a keypad if there is one
		if (document.getElementById('CharacterKeypad') != null){
			document.getElementById('CharacterKeypad').style.display = 'block';
		}
	}
	else{
  	if (QArray[CurrQNum].getElementsByTagName('textarea')[0] != null){
  		QArray[CurrQNum].getElementsByTagName('textarea')[0].focus();
//and show a keypad if there is one
			if (document.getElementById('CharacterKeypad') != null){
				document.getElementById('CharacterKeypad').style.display = 'block';
			}
		}
//This added for 6.0.4.11: hide accented character buttons if no textbox
		else{
			if (document.getElementById('CharacterKeypad') != null){
				document.getElementById('CharacterKeypad').style.display = 'none';
			}
		}
	}
}

function ChangeQ(ChangeBy){
//The following line prevents moving to another question until the current
//question is answered correctly. Uncomment it to enable this behaviour.
//	if (State[CurrQNum][0] == -1){return;}
	if (((CurrQNum + ChangeBy) < 0)||((CurrQNum + ChangeBy) >= QArray.length)){return;}
	QArray[CurrQNum].style.display = 'none';
	CurrQNum += ChangeBy;
	QArray[CurrQNum].style.display = '';
//Undocumented function added 10/12/2004
	ShowSpecialReadingForQuestion();
	SetQNumReadout();
	SetFocusToTextbox();
}

var HiddenReadingShown = false;
function ShowSpecialReadingForQuestion(){
//Undocumented function for showing specific reading text elements which change with each question
//Added on 10/12/2004
	if (document.getElementById('ReadingDiv') != null){
		if (HiddenReadingShown == true){
			document.getElementById('ReadingDiv').innerHTML = '';
		}
		if (QArray[CurrQNum] != null){
//Fix for 6.0.4.25
			var Children = QArray[CurrQNum].getElementsByTagName('div');
			for (var i=0; i<Children.length; i++){
			if (Children[i].className=="HiddenReading"){
					document.getElementById('ReadingDiv').innerHTML = Children[i].innerHTML;
					HiddenReadingShown = true;
//Hide the ShowAllQuestions button to avoid confusion
					if (document.getElementById('ShowMethodButton') != null){
						document.getElementById('ShowMethodButton').style.display = 'none';
					}
				}
			}
		}
	}
}

function SetQNumReadout(){
	document.getElementById('QNumReadout').innerHTML = (CurrQNum+1) + ' / ' + QArray.length;
	if ((CurrQNum+1) >= QArray.length){
		if (document.getElementById('NextQButton') != null){
			document.getElementById('NextQButton').style.visibility = 'hidden';
		}
	}
	else{
		if (document.getElementById('NextQButton') != null){
			document.getElementById('NextQButton').style.visibility = 'visible';
		}
	}
	if (CurrQNum <= 0){
		if (document.getElementById('PrevQButton') != null){
			document.getElementById('PrevQButton').style.visibility = 'hidden';
		}
	}
	else{
		if (document.getElementById('PrevQButton') != null){
			document.getElementById('PrevQButton').style.visibility = 'visible';
		}
	}
}

I=new Array();

I[0] = new Array();
I[0][0] = 100;
I[0][1] = '';
I[0][2] = '0';
I[0][3] = new Array();
I[0][3][0] = new Array('How easy the information is to understand','',0,0,1);
I[0][3][1] = new Array('The accuracy of the information','',0,0,1);
I[0][3][2] = new Array('How up-to-date the information is','',0,0,1);
I[0][3][3] = new Array('How much the information cost to produce','',1,100,1);

I[1] = new Array();
I[1][0] = 100;
I[1][1] = '';
I[1][2] = '0';
I[1][3] = new Array();
I[1][3][0] = new Array('High quality information reduces the risk when making decisions','',1,100,1);
I[1][3][1] = new Array('It is impossible to make decisions without high quality information','',0,0,1);
I[1][3][2] = new Array('Decisions can only be made using data','',0,0,1);
I[1][3][3] = new Array('Information is turned into data for decision making','',0,0,1);

I[2] = new Array();
I[2][0] = 100;
I[2][1] = '';
I[2][2] = '0';
I[2][3] = new Array();
I[2][3][0] = new Array('Accuracy','',0,0,1);
I[2][3][1] = new Array('Relevance for a particular use','',0,0,1);
I[2][3][2] = new Array('The completeness of the information','',0,0,1);
I[2][3][3] = new Array('Whether or not the information has been produced using ICT','',1,100,1);

I[3] = new Array();
I[3][0] = 100;
I[3][1] = '';
I[3][2] = '0';
I[3][3] = new Array();
I[3][3][0] = new Array('The information is not accurate','',0,0,1);
I[3][3][1] = new Array('The information is not easy to understand','',0,0,1);
I[3][3][2] = new Array('The information is incomplete','',0,0,1);
I[3][3][3] = new Array('The information has not been targeted correctly','',1,100,1);

I[4] = new Array();
I[4][0] = 100;
I[4][1] = '';
I[4][2] = '0';
I[4][3] = new Array();
I[4][3][0] = new Array('Incomplete','',0,0,1);
I[4][3][1] = new Array('Correctly targeted','',0,0,1);
I[4][3][2] = new Array('Not up-to-date','',1,100,1);
I[4][3][3] = new Array('Not easy to understand','',0,0,1);

I[5] = new Array();
I[5][0] = 100;
I[5][1] = '';
I[5][2] = '0';
I[5][3] = new Array();
I[5][3][0] = new Array('It is not relevant','',0,0,1);
I[5][3][1] = new Array('It is not up-to-date','',0,0,1);
I[5][3][2] = new Array('It is not complete','',0,0,1);
I[5][3][3] = new Array('It is not easy to understand','',1,100,1);

I[6] = new Array();
I[6][0] = 100;
I[6][1] = '';
I[6][2] = '0';
I[6][3] = new Array();
I[6][3][0] = new Array('Lack of user confidence','',1,100,1);
I[6][3][1] = new Array('Lack of user awareness','',0,0,1);
I[6][3][2] = new Array('Lack of targeting of the information','',0,0,1);
I[6][3][3] = new Array('Lack of completeness of the information','',0,0,1);

I[7] = new Array();
I[7][0] = 100;
I[7][1] = '';
I[7][2] = '0';
I[7][3] = new Array();
I[7][3][0] = new Array('Moving house','',0,0,1);
I[7][3][1] = new Array('Change of name','',0,0,1);
I[7][3][2] = new Array('Change of bank account details','',0,0,1);
I[7][3][3] = new Array('Change of car','',1,100,1);

I[8] = new Array();
I[8][0] = 100;
I[8][1] = '';
I[8][2] = '0';
I[8][3] = new Array();
I[8][3][0] = new Array('A web page containing information about a school','',0,0,1);
I[8][3][1] = new Array('Information on an intranet','',0,0,1);
I[8][3][2] = new Array('Paper-based records','',1,100,1);
I[8][3][3] = new Array('The Internet','',0,0,1);

I[9] = new Array();
I[9][0] = 100;
I[9][1] = '';
I[9][2] = '0';
I[9][3] = new Array();
I[9][3][0] = new Array('On-line information can be accessed by everyone in the organisation','',0,0,1);
I[9][3][1] = new Array('Keeping information on-line saves storage space','',0,0,1);
I[9][3][2] = new Array('It is much easier to find the information on-line','',0,0,1);
I[9][3][3] = new Array('Information sources on-line are more accurate','',1,100,1);


function StartUp(){
	RemoveBottomNavBarForIE();

//If there's only one question, no need for question navigation controls
	if (QsToShow < 2){
		document.getElementById('QNav').style.display = 'none';
	}

//Stash the instructions so they can be redisplayed
	strInstructions = document.getElementById('InstructionsDiv').innerHTML;







	CompleteEmptyFeedback();

	SetUpQuestions();
	ClearTextBoxes();
	CreateStatusArray();



//Check search string for q parameter
	if (document.location.search.length > 0){
		if (ShuffleQs == false){
			var JumpTo = parseInt(document.location.search.substring(1,document.location.search.length))-1;
			if (JumpTo <= QsToShow){
				ChangeQ(JumpTo);
			}
		}
	}
//Undocumented function added 10/12/2004
	ShowSpecialReadingForQuestion();
}

function ShowHideQuestions(){
	FuncBtnOut(document.getElementById('ShowMethodButton'));
	document.getElementById('ShowMethodButton').style.display = 'none';
	if (ShowingAllQuestions == false){
		for (var i=0; i<QArray.length; i++){
				QArray[i].style.display = '';
			}
		document.getElementById('Questions').style.listStyleType = 'decimal';
		document.getElementById('OneByOneReadout').style.display = 'none';
		document.getElementById('ShowMethodButton').innerHTML = ShowOneByOneCaption;
		ShowingAllQuestions = true;
	}
	else{
		for (var i=0; i<QArray.length; i++){
				if (i != CurrQNum){
					QArray[i].style.display = 'none';
				}
			}
		document.getElementById('Questions').style.listStyleType = 'none';
		document.getElementById('OneByOneReadout').style.display = '';
		document.getElementById('ShowMethodButton').innerHTML = ShowAllQuestionsCaption;
		ShowingAllQuestions = false;
	}
	document.getElementById('ShowMethodButton').style.display = 'inline';
}

function CreateStatusArray(){
	var QNum, ANum;
//For each item in the item array
	for (QNum=0; QNum<I.length; QNum++){
//Check if the question still exists (hasn't been nuked by showing a random selection)
		if (document.getElementById('Q_' + QNum) != null){
			State[QNum] = new Array();
			State[QNum][0] = -1; //Score for this q; -1 shows question not done yet
			State[QNum][1] = new Array(); //answers
			for (ANum = 0; ANum<I[QNum][3].length; ANum++){
				State[QNum][1][ANum] = 0; //answer not chosen yet; when chosen, will store its position in the series of choices
			}
			State[QNum][2] = 0; //tries at this q so far
			State[QNum][3] = 0; //incrementing percent-correct values of selected answers
			State[QNum][4] = 0; //penalties incurred for hints
			State[QNum][5] = ''; //Sequence of answers chosen by number
		}
		else{
			State[QNum] = null;
		}
	}
}



function CheckMCAnswer(QNum, ANum, Btn){
//if question doesn't exist, bail
	if (State[QNum].length < 1){return;}

//Get the feedback
	Feedback = I[QNum][3][ANum][1];

//Now show feedback and bail if question already complete
	if (State[QNum][0] > -1){
//Add an extra message explaining that the question
// is finished if defined by the user
		if (strQuestionFinished.length > 0){Feedback += '<br />' + strQuestionFinished;}
//Show the feedback
		ShowMessage(Feedback);
		return;
	}

//Hide the button while processing
	Btn.style.display = 'none';

//Increment the number of tries
	State[QNum][2]++;

//Add the percent-correct value of this answer
	State[QNum][3] += I[QNum][3][ANum][3];

//Store the try number in the answer part of the State array, for tr</brng purposes
	State[QNum][1][ANum] = State[QNum][2];
	if (State[QNum][5].length > 0){State[QNum][5] += ' | ';}
	State[QNum][5] += String.fromCharCode(65+ANum);

//Should this answer be accepted as correct?
	if (I[QNum][3][ANum][2] < 1){
//It's wrong

//Mark the answer
		Btn.innerHTML = IncorrectIndicator;

//Remove any previous score unless exercise is finished (6.0.3.8+)
		if (Finished == false){
			WriteToInstructions(strInstructions);
		}

//Check whether this leaves just one MC answer unselected, in which case the Q is terminated
		var RemainingAnswer = FinalAnswer(QNum);
		if (RemainingAnswer > -1){
//Behave as if the last answer had been selected, but give no credit for it
//Increment the number of tries
			State[QNum][2]++;

//Calculate the score for this question
			CalculateMCQuestionScore(QNum);

//Get the overall score and add it to the feedback
			CalculateOverallScore();
			if ((ContinuousScoring == true)||(Finished == true)){
				Feedback += '<br />' + YourScoreIs + ' ' + Score + '%.';
				WriteToInstructions(YourScoreIs + ' ' + Score + '%.');
			}
		}
	}
	else{
//It's right
//Mark the answer
		Btn.innerHTML = CorrectIndicator;

//Calculate the score for this question
		CalculateMCQuestionScore(QNum);

//Get the overall score and add it to the feedback
		if (ContinuousScoring == true){
			CalculateOverallScore();
			if ((ContinuousScoring == true)||(Finished == true)){
				Feedback += '<br />' + YourScoreIs + ' ' + Score + '%.';
				WriteToInstructions(YourScoreIs + ' ' + Score + '%.');
			}
		}
	}

//Show the button again
	Btn.style.display = 'inline';

//Finally, show the feedback
	ShowMessage(Feedback);

//Check whether all questions are now done
	CheckFinished();
}

function CalculateMCQuestionScore(QNum){
	var Tries = State[QNum][2] + State[QNum][4]; //include tries and hint penalties
	var PercentCorrect = State[QNum][3];
	var TotAns = GetTotalMCAnswers(QNum);
	var HintPenalties = State[QNum][4];

//Make sure it's not already complete

	if (State[QNum][0] < 0){
//Allow for Hybrids
		if (HintPenalties >= 1){
			State[QNum][0] = 0;
		}
		else{
//This line calculates the score for this question
			if (TotAns == 1){
				State[QNum][0] = 1;
			}
			else{
				State[QNum][0] = ((TotAns-((Tries*100)/State[QNum][3]))/(TotAns-1));
			}
		}
//Fix for Safari bug added for version 6.0.3.42 (negative infinity problem)
		if ((State[QNum][0] < 0)||(State[QNum][0] == Number.NEGATIVE_INFINITY)){
			State[QNum][0] = 0;
		}
	}
}

function GetTotalMCAnswers(QNum){
	var Result = 0;
	for (var ANum=0; ANum<I[QNum][3].length; ANum++){
		if (I[QNum][3][ANum][4] == 1){ //This is an MC answer
			Result++;
		}
	}
	return Result;
}

function FinalAnswer(QNum){
	var UnchosenAnswers = 0;
	var FinalAnswer = -1;
	for (var ANum=0; ANum<I[QNum][3].length; ANum++){
		if (I[QNum][3][ANum][4] == 1){ //This is an MC answer
			if (State[QNum][1][ANum] < 1){ //This answer hasn't been chosen yet
				UnchosenAnswers++;
				FinalAnswer = ANum;
			}
		}
	}
	if (UnchosenAnswers == 1){
		return FinalAnswer;
	}
	else{
		return -1;
	}
}





function CalculateOverallScore(){
	var TotalWeighting = 0;
	var TotalScore = 0;

	for (var QNum=0; QNum<State.length; QNum++){
		if (State[QNum] != null){
			if (State[QNum][0] > -1){
				TotalWeighting += I[QNum][0];
				TotalScore += (I[QNum][0] * State[QNum][0]);
			}
		}
	}
	if (TotalWeighting > 0){
		Score = Math.floor((TotalScore/TotalWeighting)*100);
	}
	else{
//if TotalWeighting is 0, no questions so far have any value, so
//no penalty should be shown.
		Score = 100;
	}
}

function CheckFinished(){
	var FB = '';
	var AllDone = true;
	for (var QNum=0; QNum<State.length; QNum++){
		if (State[QNum] != null){
			if (State[QNum][0] < 0){
				AllDone = false;
			}
		}
	}
	if (AllDone == true){

//Report final score and submit if necessary
		CalculateOverallScore();
		FB = YourScoreIs + ' ' + Score + '%.';
		if (ShowCorrectFirstTime == true){
			var CFT = 0;
			for (QNum=0; QNum<State.length; QNum++){
				if (State[QNum] != null){
					if (State[QNum][0] >= 1){
						CFT++;
					}
				}
			}
			FB += '<br />' + CorrectFirstTime + ' ' + CFT + '/' + QsToShow;
		}
		WriteToInstructions(FB);

		Finished == true;




		TimeOver = true;
		Locked = true;



		Finished = true;
		Detail = '<?xml version="1.0"?><hpnetresult><fields>';
		for (QNum=0; QNum<State.length; QNum++){
			if (State[QNum] != null){
				if (State[QNum][5].length > 0){
					Detail += '<field><fieldname>Question #' + (QNum+1) + '</fieldname><fieldtype>question-tracking</fieldtype><fieldlabel>Q ' + (QNum+1) + '</fieldlabel><fieldlabelid>QuestionTrackingField</fieldlabelid><fielddata>' + State[QNum][5] + '</fielddata></field>';
				}
			}
		}
		Detail += '</fields></hpnetresult>';
		setTimeout('Finish()', SubmissionTimeout);
	}

}









//-->

//]]>

</script>
<script src="http://websites.bordengrammar.kent.sch.uk/moodle/mod/hotpot/hotpot-full.js" type="text/javascript"></script>

<!--[if IE 7]>
    <link rel="stylesheet" type="text/css" href="http://websites.bordengrammar.kent.sch.uk/moodle/theme/standard/styles_ie7.css" />
<![endif]-->
<!--[if IE 6]>
    <link rel="stylesheet" type="text/css" href="http://websites.bordengrammar.kent.sch.uk/moodle/theme/standard/styles_ie6.css" />
<![endif]-->


    <meta name="keywords" content="moodle, AS_WJEC_ICT: T3 - Quality of Information " />
    <title>AS_WJEC_ICT: T3 - Quality of Information</title>
    <link rel="shortcut icon" href="http://websites.bordengrammar.kent.sch.uk/moodle/theme/prettysimple/favicon.ico" />
    <!--<style type="text/css">/*<![CDATA[*/ body{behavior:url(http://websites.bordengrammar.kent.sch.uk/moodle/lib/csshover.htc);} /*]]>*/</style>-->

<script type="text/javascript" src="http://websites.bordengrammar.kent.sch.uk/moodle/lib/javascript-static.js"></script>
<script type="text/javascript" src="http://websites.bordengrammar.kent.sch.uk/moodle/lib/javascript-mod.php"></script>
<script type="text/javascript" src="http://websites.bordengrammar.kent.sch.uk/moodle/lib/overlib/overlib.js"></script>
<script type="text/javascript" src="http://websites.bordengrammar.kent.sch.uk/moodle/lib/overlib/overlib_cssstyle.js"></script>
<script type="text/javascript" src="http://websites.bordengrammar.kent.sch.uk/moodle/lib/cookies.js"></script>
<script type="text/javascript" src="http://websites.bordengrammar.kent.sch.uk/moodle/lib/ufo.js"></script>
<script type="text/javascript" src="http://websites.bordengrammar.kent.sch.uk/moodle/lib/dropdown.js"></script>  

<script type="text/javascript" defer="defer">
//<![CDATA[
setTimeout('fix_column_widths()', 20);
//]]>
</script>
<script type="text/javascript">
//<![CDATA[
function openpopup(url, name, options, fullscreen) {
    var fullurl = "http://websites.bordengrammar.kent.sch.uk/moodle" + url;
    var windowobj = window.open(fullurl, name, options);
    if (!windowobj) {
        return true;
    }
    if (fullscreen) {
        windowobj.moveTo(0, 0);
        windowobj.resizeTo(screen.availWidth, screen.availHeight);
    }
    windowobj.focus();
    return false;
}

function uncheckall() {
    var inputs = document.getElementsByTagName('input');
    for(var i = 0; i < inputs.length; i++) {
        inputs[i].checked = false;
    }
}

function checkall() {
    var inputs = document.getElementsByTagName('input');
    for(var i = 0; i < inputs.length; i++) {
        inputs[i].checked = true;
    }
}

function inserttext(text) {
  text = ' ' + text + ' ';
  if ( opener.document.forms['theform'].message.createTextRange && opener.document.forms['theform'].message.caretPos) {
    var caretPos = opener.document.forms['theform'].message.caretPos;
    caretPos.text = caretPos.text.charAt(caretPos.text.length - 1) == ' ' ? text + ' ' : text;
  } else {
    opener.document.forms['theform'].message.value  += text;
  }
  opener.document.forms['theform'].message.focus();
}

function getElementsByClassName(oElm, strTagName, oClassNames){
	var arrElements = (strTagName == "*" && oElm.all)? oElm.all : oElm.getElementsByTagName(strTagName);
	var arrReturnElements = new Array();
	var arrRegExpClassNames = new Array();
	if(typeof oClassNames == "object"){
		for(var i=0; i<oClassNames.length; i++){
			arrRegExpClassNames.push(new RegExp("(^|\\s)" + oClassNames[i].replace(/\-/g, "\\-") + "(\\s|$)"));
		}
	}
	else{
		arrRegExpClassNames.push(new RegExp("(^|\\s)" + oClassNames.replace(/\-/g, "\\-") + "(\\s|$)"));
	}
	var oElement;
	var bMatchesAll;
	for(var j=0; j<arrElements.length; j++){
		oElement = arrElements[j];
		bMatchesAll = true;
		for(var k=0; k<arrRegExpClassNames.length; k++){
			if(!arrRegExpClassNames[k].test(oElement.className)){
				bMatchesAll = false;
				break;
			}
		}
		if(bMatchesAll){
			arrReturnElements.push(oElement);
		}
	}
	return (arrReturnElements)
}
//]]>
</script>

<!--Menu-->
    <script language="javascript" type="text/javascript" src="http://websites.bordengrammar.kent.sch.uk/moodle/theme/prettysimple/js/moomenu.js"></script>
<!--End of Menu-->
</head>

<body  onload="StartUp()"  class="mod-hotpot course-201 dir-ltr lang-en_utf8" id="mod-hotpot-view">

<div id="page">

    <div id="header" class=" clearfix">        <h1 class="headermain">&nbsp;</h1>
        <div class="headermenu"><div class="logininfo">You are logged in as <a  href="http://websites.bordengrammar.kent.sch.uk/moodle/user/view.php?id=354&amp;course=201">Calvin Collins</a>  (<a  href="http://websites.bordengrammar.kent.sch.uk/moodle/login/logout.php?sesskey=0DFbJ6YTXY">Logout</a>)</div></div>
    </div>    <div class="navbar clearfix">
        <div class="breadcrumb"><h2 class="accesshide " >You are here</h2> <ul>
<li class="first"><a  onclick="this.target='_top'" href="http://websites.bordengrammar.kent.sch.uk/moodle/">BGS-VLE</a></li><li> <span class="accesshide " >/&nbsp;</span><span class="arrow sep">&#x25BA;</span> <a  onclick="this.target='_top'" href="http://websites.bordengrammar.kent.sch.uk/moodle/course/view.php?id=201">AS_WJEC_ICT</a></li><li> <span class="accesshide " >/&nbsp;</span><span class="arrow sep">&#x25BA;</span> <a  onclick="this.target='_top'" href="http://websites.bordengrammar.kent.sch.uk/moodle/mod/hotpot/index.php?id=201">Hot Potatoes Quizzes</a></li><li> <span class="accesshide " >/&nbsp;</span><span class="arrow sep">&#x25BA;</span> T3 - Quality of Information</li></ul></div>
        <div class="navbutton"><div style="font-size:0.75em;"></div></div>
    </div>
    <!-- END OF HEADER -->
    <div id="content">



<div class="Titles">
	<h2 class="ExerciseTitle">Qulaity of Information</h2>

	<h3 class="ExerciseSubtitle">Quiz</h3>



</div>

<div id="InstructionsDiv" class="StdDiv">
	<div id="Instructions"></div>
</div>




<div id="MainDiv" class="StdDiv">

<div id="QNav" class="QuestionNavigation">

<p style="text-align: right;">
<button id="ShowMethodButton" class="FuncButton" onfocus="FuncBtnOver(this)" onblur="FuncBtnOut(this)" onmouseover="FuncBtnOver(this)" onmouseout="FuncBtnOut(this)" onmousedown="FuncBtnDown(this)" onmouseup="FuncBtnOver(this)" onclick="ShowHideQuestions(); return false;">Show all questions</button>
</p>

<div id="OneByOneReadout">
<button id="PrevQButton" class="FuncButton" onfocus="FuncBtnOver(this)" onblur="FuncBtnOut(this)" onmouseover="FuncBtnOver(this)" onmouseout="FuncBtnOut(this)" onmousedown="FuncBtnDown(this)" onmouseup="FuncBtnOver(this)" onclick="ChangeQ(-1); return false;">&lt;=</button>

<span id="QNumReadout" class="QNum">&nbsp;</span>

<button id="NextQButton" class="FuncButton" onfocus="FuncBtnOver(this)" onblur="FuncBtnOut(this)" onmouseover="FuncBtnOver(this)" onmouseout="FuncBtnOut(this)" onmousedown="FuncBtnDown(this)" onmouseup="FuncBtnOver(this)" onclick="ChangeQ(1); return false;">=></button>
<br />
</div>

</div>

<ol class="QuizQuestions" id="Questions">
<li class="QuizQuestion" id="Q_0" style="display: none;"><p class="QuestionText">Which one of these is not a measure of the quality of information?</p><ol class="MCAnswers">
<li id="Q_0_0"><button class="FuncButton" onfocus="FuncBtnOver(this)" onblur="FuncBtnOut(this)" onmouseover="FuncBtnOver(this)" onmouseout="FuncBtnOut(this)" onmousedown="FuncBtnDown(this)" onmouseup="FuncBtnOut(this)" id="Q_0_0_Btn" onclick="CheckMCAnswer(0,0,this)">&nbsp;&nbsp;?&nbsp;&nbsp;</button>&nbsp;&nbsp;How easy the information is to understand</li>
<li id="Q_0_1"><button class="FuncButton" onfocus="FuncBtnOver(this)" onblur="FuncBtnOut(this)" onmouseover="FuncBtnOver(this)" onmouseout="FuncBtnOut(this)" onmousedown="FuncBtnDown(this)" onmouseup="FuncBtnOut(this)" id="Q_0_1_Btn" onclick="CheckMCAnswer(0,1,this)">&nbsp;&nbsp;?&nbsp;&nbsp;</button>&nbsp;&nbsp;The accuracy of the information</li>
<li id="Q_0_2"><button class="FuncButton" onfocus="FuncBtnOver(this)" onblur="FuncBtnOut(this)" onmouseover="FuncBtnOver(this)" onmouseout="FuncBtnOut(this)" onmousedown="FuncBtnDown(this)" onmouseup="FuncBtnOut(this)" id="Q_0_2_Btn" onclick="CheckMCAnswer(0,2,this)">&nbsp;&nbsp;?&nbsp;&nbsp;</button>&nbsp;&nbsp;How up-to-date the information is</li>
<li id="Q_0_3"><button class="FuncButton" onfocus="FuncBtnOver(this)" onblur="FuncBtnOut(this)" onmouseover="FuncBtnOver(this)" onmouseout="FuncBtnOut(this)" onmousedown="FuncBtnDown(this)" onmouseup="FuncBtnOut(this)" id="Q_0_3_Btn" onclick="CheckMCAnswer(0,3,this)">&nbsp;&nbsp;?&nbsp;&nbsp;</button>&nbsp;&nbsp;How much the information cost to produce</li>
</ol></li>
<li class="QuizQuestion" id="Q_1" style="display: none;"><p class="QuestionText">The quality of information affects decision making. Which one of the following is the best reason for this?</p><ol class="MCAnswers">
<li id="Q_1_0"><button class="FuncButton" onfocus="FuncBtnOver(this)" onblur="FuncBtnOut(this)" onmouseover="FuncBtnOver(this)" onmouseout="FuncBtnOut(this)" onmousedown="FuncBtnDown(this)" onmouseup="FuncBtnOut(this)" id="Q_1_0_Btn" onclick="CheckMCAnswer(1,0,this)">&nbsp;&nbsp;?&nbsp;&nbsp;</button>&nbsp;&nbsp;High quality information reduces the risk when making decisions</li>
<li id="Q_1_1"><button class="FuncButton" onfocus="FuncBtnOver(this)" onblur="FuncBtnOut(this)" onmouseover="FuncBtnOver(this)" onmouseout="FuncBtnOut(this)" onmousedown="FuncBtnDown(this)" onmouseup="FuncBtnOut(this)" id="Q_1_1_Btn" onclick="CheckMCAnswer(1,1,this)">&nbsp;&nbsp;?&nbsp;&nbsp;</button>&nbsp;&nbsp;It is impossible to make decisions without high quality information</li>
<li id="Q_1_2"><button class="FuncButton" onfocus="FuncBtnOver(this)" onblur="FuncBtnOut(this)" onmouseover="FuncBtnOver(this)" onmouseout="FuncBtnOut(this)" onmousedown="FuncBtnDown(this)" onmouseup="FuncBtnOut(this)" id="Q_1_2_Btn" onclick="CheckMCAnswer(1,2,this)">&nbsp;&nbsp;?&nbsp;&nbsp;</button>&nbsp;&nbsp;Decisions can only be made using data</li>
<li id="Q_1_3"><button class="FuncButton" onfocus="FuncBtnOver(this)" onblur="FuncBtnOut(this)" onmouseover="FuncBtnOver(this)" onmouseout="FuncBtnOut(this)" onmousedown="FuncBtnDown(this)" onmouseup="FuncBtnOut(this)" id="Q_1_3_Btn" onclick="CheckMCAnswer(1,3,this)">&nbsp;&nbsp;?&nbsp;&nbsp;</button>&nbsp;&nbsp;Information is turned into data for decision making</li>
</ol></li>
<li class="QuizQuestion" id="Q_2" style="display: none;"><p class="QuestionText">Which one of these features of information does not affect the quality of information?</p><ol class="MCAnswers">
<li id="Q_2_0"><button class="FuncButton" onfocus="FuncBtnOver(this)" onblur="FuncBtnOut(this)" onmouseover="FuncBtnOver(this)" onmouseout="FuncBtnOut(this)" onmousedown="FuncBtnDown(this)" onmouseup="FuncBtnOut(this)" id="Q_2_0_Btn" onclick="CheckMCAnswer(2,0,this)">&nbsp;&nbsp;?&nbsp;&nbsp;</button>&nbsp;&nbsp;Accuracy</li>
<li id="Q_2_1"><button class="FuncButton" onfocus="FuncBtnOver(this)" onblur="FuncBtnOut(this)" onmouseover="FuncBtnOver(this)" onmouseout="FuncBtnOut(this)" onmousedown="FuncBtnDown(this)" onmouseup="FuncBtnOut(this)" id="Q_2_1_Btn" onclick="CheckMCAnswer(2,1,this)">&nbsp;&nbsp;?&nbsp;&nbsp;</button>&nbsp;&nbsp;Relevance for a particular use</li>
<li id="Q_2_2"><button class="FuncButton" onfocus="FuncBtnOver(this)" onblur="FuncBtnOut(this)" onmouseover="FuncBtnOver(this)" onmouseout="FuncBtnOut(this)" onmousedown="FuncBtnDown(this)" onmouseup="FuncBtnOut(this)" id="Q_2_2_Btn" onclick="CheckMCAnswer(2,2,this)">&nbsp;&nbsp;?&nbsp;&nbsp;</button>&nbsp;&nbsp;The completeness of the information</li>
<li id="Q_2_3"><button class="FuncButton" onfocus="FuncBtnOver(this)" onblur="FuncBtnOut(this)" onmouseover="FuncBtnOver(this)" onmouseout="FuncBtnOut(this)" onmousedown="FuncBtnDown(this)" onmouseup="FuncBtnOut(this)" id="Q_2_3_Btn" onclick="CheckMCAnswer(2,3,this)">&nbsp;&nbsp;?&nbsp;&nbsp;</button>&nbsp;&nbsp;Whether or not the information has been produced using ICT</li>
</ol></li>
<li class="QuizQuestion" id="Q_3" style="display: none;"><p class="QuestionText">A sales manager wants a printout of the value of	all the sales made to the twenty best customers in terms of the profit they make for the company. The clerk uses ICT to produce this information but gives the manager a list of the information for three hundred customers. Why is this not good quality information?</p><ol class="MCAnswers">
<li id="Q_3_0"><button class="FuncButton" onfocus="FuncBtnOver(this)" onblur="FuncBtnOut(this)" onmouseover="FuncBtnOver(this)" onmouseout="FuncBtnOut(this)" onmousedown="FuncBtnDown(this)" onmouseup="FuncBtnOut(this)" id="Q_3_0_Btn" onclick="CheckMCAnswer(3,0,this)">&nbsp;&nbsp;?&nbsp;&nbsp;</button>&nbsp;&nbsp;The information is not accurate</li>
<li id="Q_3_1"><button class="FuncButton" onfocus="FuncBtnOver(this)" onblur="FuncBtnOut(this)" onmouseover="FuncBtnOver(this)" onmouseout="FuncBtnOut(this)" onmousedown="FuncBtnDown(this)" onmouseup="FuncBtnOut(this)" id="Q_3_1_Btn" onclick="CheckMCAnswer(3,1,this)">&nbsp;&nbsp;?&nbsp;&nbsp;</button>&nbsp;&nbsp;The information is not easy to understand</li>
<li id="Q_3_2"><button class="FuncButton" onfocus="FuncBtnOver(this)" onblur="FuncBtnOut(this)" onmouseover="FuncBtnOver(this)" onmouseout="FuncBtnOut(this)" onmousedown="FuncBtnDown(this)" onmouseup="FuncBtnOut(this)" id="Q_3_2_Btn" onclick="CheckMCAnswer(3,2,this)">&nbsp;&nbsp;?&nbsp;&nbsp;</button>&nbsp;&nbsp;The information is incomplete</li>
<li id="Q_3_3"><button class="FuncButton" onfocus="FuncBtnOver(this)" onblur="FuncBtnOut(this)" onmouseover="FuncBtnOver(this)" onmouseout="FuncBtnOut(this)" onmousedown="FuncBtnDown(this)" onmouseup="FuncBtnOut(this)" id="Q_3_3_Btn" onclick="CheckMCAnswer(3,3,this)">&nbsp;&nbsp;?&nbsp;&nbsp;</button>&nbsp;&nbsp;The information has not been targeted correctly</li>
</ol></li>
<li class="QuizQuestion" id="Q_4" style="display: none;"><p class="QuestionText">A customer is told an item is in stock when it isn&#x2019;t. The customer orders the item and then complains about the delivery time. Information about stock details was which one of these?</p><ol class="MCAnswers">
<li id="Q_4_0"><button class="FuncButton" onfocus="FuncBtnOver(this)" onblur="FuncBtnOut(this)" onmouseover="FuncBtnOver(this)" onmouseout="FuncBtnOut(this)" onmousedown="FuncBtnDown(this)" onmouseup="FuncBtnOut(this)" id="Q_4_0_Btn" onclick="CheckMCAnswer(4,0,this)">&nbsp;&nbsp;?&nbsp;&nbsp;</button>&nbsp;&nbsp;Incomplete</li>
<li id="Q_4_1"><button class="FuncButton" onfocus="FuncBtnOver(this)" onblur="FuncBtnOut(this)" onmouseover="FuncBtnOver(this)" onmouseout="FuncBtnOut(this)" onmousedown="FuncBtnDown(this)" onmouseup="FuncBtnOut(this)" id="Q_4_1_Btn" onclick="CheckMCAnswer(4,1,this)">&nbsp;&nbsp;?&nbsp;&nbsp;</button>&nbsp;&nbsp;Correctly targeted</li>
<li id="Q_4_2"><button class="FuncButton" onfocus="FuncBtnOver(this)" onblur="FuncBtnOut(this)" onmouseover="FuncBtnOver(this)" onmouseout="FuncBtnOut(this)" onmousedown="FuncBtnDown(this)" onmouseup="FuncBtnOut(this)" id="Q_4_2_Btn" onclick="CheckMCAnswer(4,2,this)">&nbsp;&nbsp;?&nbsp;&nbsp;</button>&nbsp;&nbsp;Not up-to-date</li>
<li id="Q_4_3"><button class="FuncButton" onfocus="FuncBtnOver(this)" onblur="FuncBtnOut(this)" onmouseover="FuncBtnOver(this)" onmouseout="FuncBtnOut(this)" onmousedown="FuncBtnDown(this)" onmouseup="FuncBtnOut(this)" id="Q_4_3_Btn" onclick="CheckMCAnswer(4,3,this)">&nbsp;&nbsp;?&nbsp;&nbsp;</button>&nbsp;&nbsp;Not easy to understand</li>
</ol></li>
<li class="QuizQuestion" id="Q_5" style="display: none;"><p class="QuestionText">The manager asks for a credit report which contains lots of codes and numbers which she does not understand. The information is poor quality for which one of the following reasons? </p><ol class="MCAnswers">
<li id="Q_5_0"><button class="FuncButton" onfocus="FuncBtnOver(this)" onblur="FuncBtnOut(this)" onmouseover="FuncBtnOver(this)" onmouseout="FuncBtnOut(this)" onmousedown="FuncBtnDown(this)" onmouseup="FuncBtnOut(this)" id="Q_5_0_Btn" onclick="CheckMCAnswer(5,0,this)">&nbsp;&nbsp;?&nbsp;&nbsp;</button>&nbsp;&nbsp;It is not relevant</li>
<li id="Q_5_1"><button class="FuncButton" onfocus="FuncBtnOver(this)" onblur="FuncBtnOut(this)" onmouseover="FuncBtnOver(this)" onmouseout="FuncBtnOut(this)" onmousedown="FuncBtnDown(this)" onmouseup="FuncBtnOut(this)" id="Q_5_1_Btn" onclick="CheckMCAnswer(5,1,this)">&nbsp;&nbsp;?&nbsp;&nbsp;</button>&nbsp;&nbsp;It is not up-to-date</li>
<li id="Q_5_2"><button class="FuncButton" onfocus="FuncBtnOver(this)" onblur="FuncBtnOut(this)" onmouseover="FuncBtnOver(this)" onmouseout="FuncBtnOut(this)" onmousedown="FuncBtnDown(this)" onmouseup="FuncBtnOut(this)" id="Q_5_2_Btn" onclick="CheckMCAnswer(5,2,this)">&nbsp;&nbsp;?&nbsp;&nbsp;</button>&nbsp;&nbsp;It is not complete</li>
<li id="Q_5_3"><button class="FuncButton" onfocus="FuncBtnOver(this)" onblur="FuncBtnOut(this)" onmouseover="FuncBtnOver(this)" onmouseout="FuncBtnOut(this)" onmousedown="FuncBtnDown(this)" onmouseup="FuncBtnOut(this)" id="Q_5_3_Btn" onclick="CheckMCAnswer(5,3,this)">&nbsp;&nbsp;?&nbsp;&nbsp;</button>&nbsp;&nbsp;It is not easy to understand</li>
</ol></li>
<li class="QuizQuestion" id="Q_6" style="display: none;"><p class="QuestionText">A user of information has spotted that the information supplied by the ICT system often contains mistakes. This is a problem that causes which one of these?</p><ol class="MCAnswers">
<li id="Q_6_0"><button class="FuncButton" onfocus="FuncBtnOver(this)" onblur="FuncBtnOut(this)" onmouseover="FuncBtnOver(this)" onmouseout="FuncBtnOut(this)" onmousedown="FuncBtnDown(this)" onmouseup="FuncBtnOut(this)" id="Q_6_0_Btn" onclick="CheckMCAnswer(6,0,this)">&nbsp;&nbsp;?&nbsp;&nbsp;</button>&nbsp;&nbsp;Lack of user confidence</li>
<li id="Q_6_1"><button class="FuncButton" onfocus="FuncBtnOver(this)" onblur="FuncBtnOut(this)" onmouseover="FuncBtnOver(this)" onmouseout="FuncBtnOut(this)" onmousedown="FuncBtnDown(this)" onmouseup="FuncBtnOut(this)" id="Q_6_1_Btn" onclick="CheckMCAnswer(6,1,this)">&nbsp;&nbsp;?&nbsp;&nbsp;</button>&nbsp;&nbsp;Lack of user awareness</li>
<li id="Q_6_2"><button class="FuncButton" onfocus="FuncBtnOver(this)" onblur="FuncBtnOut(this)" onmouseover="FuncBtnOver(this)" onmouseout="FuncBtnOut(this)" onmousedown="FuncBtnDown(this)" onmouseup="FuncBtnOut(this)" id="Q_6_2_Btn" onclick="CheckMCAnswer(6,2,this)">&nbsp;&nbsp;?&nbsp;&nbsp;</button>&nbsp;&nbsp;Lack of targeting of the information</li>
<li id="Q_6_3"><button class="FuncButton" onfocus="FuncBtnOver(this)" onblur="FuncBtnOut(this)" onmouseover="FuncBtnOver(this)" onmouseout="FuncBtnOut(this)" onmousedown="FuncBtnDown(this)" onmouseup="FuncBtnOut(this)" id="Q_6_3_Btn" onclick="CheckMCAnswer(6,3,this)">&nbsp;&nbsp;?&nbsp;&nbsp;</button>&nbsp;&nbsp;Lack of completeness of the information</li>
</ol></li>
<li class="QuizQuestion" id="Q_7" style="display: none;"><p class="QuestionText">Which one of the following would not cause personal data to need updating?</p><ol class="MCAnswers">
<li id="Q_7_0"><button class="FuncButton" onfocus="FuncBtnOver(this)" onblur="FuncBtnOut(this)" onmouseover="FuncBtnOver(this)" onmouseout="FuncBtnOut(this)" onmousedown="FuncBtnDown(this)" onmouseup="FuncBtnOut(this)" id="Q_7_0_Btn" onclick="CheckMCAnswer(7,0,this)">&nbsp;&nbsp;?&nbsp;&nbsp;</button>&nbsp;&nbsp;Moving house</li>
<li id="Q_7_1"><button class="FuncButton" onfocus="FuncBtnOver(this)" onblur="FuncBtnOut(this)" onmouseover="FuncBtnOver(this)" onmouseout="FuncBtnOut(this)" onmousedown="FuncBtnDown(this)" onmouseup="FuncBtnOut(this)" id="Q_7_1_Btn" onclick="CheckMCAnswer(7,1,this)">&nbsp;&nbsp;?&nbsp;&nbsp;</button>&nbsp;&nbsp;Change of name</li>
<li id="Q_7_2"><button class="FuncButton" onfocus="FuncBtnOver(this)" onblur="FuncBtnOut(this)" onmouseover="FuncBtnOver(this)" onmouseout="FuncBtnOut(this)" onmousedown="FuncBtnDown(this)" onmouseup="FuncBtnOut(this)" id="Q_7_2_Btn" onclick="CheckMCAnswer(7,2,this)">&nbsp;&nbsp;?&nbsp;&nbsp;</button>&nbsp;&nbsp;Change of bank account details</li>
<li id="Q_7_3"><button class="FuncButton" onfocus="FuncBtnOver(this)" onblur="FuncBtnOut(this)" onmouseover="FuncBtnOver(this)" onmouseout="FuncBtnOut(this)" onmousedown="FuncBtnDown(this)" onmouseup="FuncBtnOut(this)" id="Q_7_3_Btn" onclick="CheckMCAnswer(7,3,this)">&nbsp;&nbsp;?&nbsp;&nbsp;</button>&nbsp;&nbsp;Change of car</li>
</ol></li>
<li class="QuizQuestion" id="Q_8" style="display: none;"><p class="QuestionText">Which one of the following is not an on-line source of information?</p><ol class="MCAnswers">
<li id="Q_8_0"><button class="FuncButton" onfocus="FuncBtnOver(this)" onblur="FuncBtnOut(this)" onmouseover="FuncBtnOver(this)" onmouseout="FuncBtnOut(this)" onmousedown="FuncBtnDown(this)" onmouseup="FuncBtnOut(this)" id="Q_8_0_Btn" onclick="CheckMCAnswer(8,0,this)">&nbsp;&nbsp;?&nbsp;&nbsp;</button>&nbsp;&nbsp;A web page containing information about a school</li>
<li id="Q_8_1"><button class="FuncButton" onfocus="FuncBtnOver(this)" onblur="FuncBtnOut(this)" onmouseover="FuncBtnOver(this)" onmouseout="FuncBtnOut(this)" onmousedown="FuncBtnDown(this)" onmouseup="FuncBtnOut(this)" id="Q_8_1_Btn" onclick="CheckMCAnswer(8,1,this)">&nbsp;&nbsp;?&nbsp;&nbsp;</button>&nbsp;&nbsp;Information on an intranet</li>
<li id="Q_8_2"><button class="FuncButton" onfocus="FuncBtnOver(this)" onblur="FuncBtnOut(this)" onmouseover="FuncBtnOver(this)" onmouseout="FuncBtnOut(this)" onmousedown="FuncBtnDown(this)" onmouseup="FuncBtnOut(this)" id="Q_8_2_Btn" onclick="CheckMCAnswer(8,2,this)">&nbsp;&nbsp;?&nbsp;&nbsp;</button>&nbsp;&nbsp;Paper-based records</li>
<li id="Q_8_3"><button class="FuncButton" onfocus="FuncBtnOver(this)" onblur="FuncBtnOut(this)" onmouseover="FuncBtnOver(this)" onmouseout="FuncBtnOut(this)" onmousedown="FuncBtnDown(this)" onmouseup="FuncBtnOut(this)" id="Q_8_3_Btn" onclick="CheckMCAnswer(8,3,this)">&nbsp;&nbsp;?&nbsp;&nbsp;</button>&nbsp;&nbsp;The Internet</li>
</ol></li>
<li class="QuizQuestion" id="Q_9" style="display: none;"><p class="QuestionText">Which one of the following is not a reason why many companies keep nearly all their information sources on-line?</p><ol class="MCAnswers">
<li id="Q_9_0"><button class="FuncButton" onfocus="FuncBtnOver(this)" onblur="FuncBtnOut(this)" onmouseover="FuncBtnOver(this)" onmouseout="FuncBtnOut(this)" onmousedown="FuncBtnDown(this)" onmouseup="FuncBtnOut(this)" id="Q_9_0_Btn" onclick="CheckMCAnswer(9,0,this)">&nbsp;&nbsp;?&nbsp;&nbsp;</button>&nbsp;&nbsp;On-line information can be accessed by everyone in the organisation</li>
<li id="Q_9_1"><button class="FuncButton" onfocus="FuncBtnOver(this)" onblur="FuncBtnOut(this)" onmouseover="FuncBtnOver(this)" onmouseout="FuncBtnOut(this)" onmousedown="FuncBtnDown(this)" onmouseup="FuncBtnOut(this)" id="Q_9_1_Btn" onclick="CheckMCAnswer(9,1,this)">&nbsp;&nbsp;?&nbsp;&nbsp;</button>&nbsp;&nbsp;Keeping information on-line saves storage space</li>
<li id="Q_9_2"><button class="FuncButton" onfocus="FuncBtnOver(this)" onblur="FuncBtnOut(this)" onmouseover="FuncBtnOver(this)" onmouseout="FuncBtnOut(this)" onmousedown="FuncBtnDown(this)" onmouseup="FuncBtnOut(this)" id="Q_9_2_Btn" onclick="CheckMCAnswer(9,2,this)">&nbsp;&nbsp;?&nbsp;&nbsp;</button>&nbsp;&nbsp;It is much easier to find the information on-line</li>
<li id="Q_9_3"><button class="FuncButton" onfocus="FuncBtnOver(this)" onblur="FuncBtnOut(this)" onmouseover="FuncBtnOver(this)" onmouseout="FuncBtnOut(this)" onmousedown="FuncBtnDown(this)" onmouseup="FuncBtnOut(this)" id="Q_9_3_Btn" onclick="CheckMCAnswer(9,3,this)">&nbsp;&nbsp;?&nbsp;&nbsp;</button>&nbsp;&nbsp;Information sources on-line are more accurate</li>
</ol></li>
</ol>




</div>



<div class="Feedback" id="FeedbackDiv">
<div class="FeedbackText" id="FeedbackContent"></div>
<button id="FeedbackOKButton" class="FuncButton" onfocus="FuncBtnOver(this)" onblur="FuncBtnOut(this)" onmouseover="FuncBtnOver(this)" onmouseout="FuncBtnOut(this)" onmousedown="FuncBtnDown(this)" onmouseup="FuncBtnOut(this)" onclick="HideFeedback(); return false;">&nbsp;OK&nbsp;</button>
</div>



<!-- BeginSubmissionForm --><form action="http://websites.bordengrammar.kent.sch.uk/moodle/mod/hotpot/attempt.php" method="post" id="store" onsubmit="this.target='_top';"><fieldset style="display:none"><input type="hidden" name="attemptid" value="3203" /><input type="hidden" name="starttime" value="" /><input type="hidden" name="endtime" value="" /><input type="hidden" name="mark" value="" /><input type="hidden" name="detail" value="" /><input type="hidden" name="status" value="" /></fieldset></form><!-- EndSubmissionForm -->

<script type="text/javascript">
//<![CDATA[
   var s = (typeof(window.onload)=='function') ? onload.toString() : '';
   if (s.indexOf('StartUp()')<0) {
       if (s=='') {
           window.onload = new Function('StartUp()');
       } else {
           window.onload_hotpot = onload;
           window.onload = new Function('window.onload_hotpot();'+'StartUp()');
       }
    }
//]]>
</script>
</div></div></body></html>
'''

def main():
    start = (code.find('I=new Array();'))
    end = (code.find('function StartUp()'))
    arrays = ''
    for x in range(start,end):
    	arrays+=code[x]
    print arrays
    arraylinesplit = arrays.splitlines()
    questionno=0
    weighting = str(100)
    #goes through the questions finding those with a weighting of 100
    for x in range(0, len(arraylinesplit)):
		#checks to see if it is correct answer
        if (weighting in arraylinesplit[x]) and (not ('= ' + weighting) in arraylinesplit[x]):
        	#Splits the arrays up and selects the question array
            stringarray = arraylinesplit[x].split('[')
            questiondigit = stringarray[3][0]
            answer = ''
            questionarray = ['A','B','C','D']
            answer = questionarray[int(questiondigit)]
            if questionno + 1 < 10:
                print ('0' + str(questionno + 1) + '       ' + answer)
            else:
                print (str(questionno + 1) + '       ' + answer)
            questionno += 1

if __name__ == '__main__':
    main()