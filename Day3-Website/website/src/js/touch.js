//touch.js
//for sending emails
//<a href="mailto:nobody@fake.address.com">Mr Nobody</a>
//Needs to be recoded as:
//<script>mail2("nobody","fake.address",0,"","Mr Nobody")</script>


// declare mixing vars
var tch_ = new Array()
tch_[0] = "com";
tch_[1] = "org";
tch_[2] = "net";
tch_[3] = "ws";
tch_[4] = "info";
tch_[5] = "edu";
tch_[10] = "co.uk";
tch_[11] = "org.uk";
tch_[12] = "gov.uk";
tch_[13] = "ac.uk";
var topDom_ = 13;
var m_ = "mailto:";
var a_ = "@";
var d_ = ".";

// Coding algorithm
// pc -2  is encrypted domain
// 
function touch(name, dom, pc, params)
{
	var s = e(name,dom,pc);
	document.write('<a href="'+m_+s+params+'"target="blank">'+s+' </a>');
}
function touch2(name, dom, pc, params, display)
{
	document.write('<a href="'+m_+e(name,dom,pc)+params+'"target="blank">'+display+'</a>');
}
function touch3(name, dom, pc, params)
{
	document.write('<a href="'+m_+e(name,dom,pc)+params+'" target="blank"><i class="fa fa-inbox"></i></a>');
}
function touch4(name, dom, pc, params, display)
{
	document.write('<a href="'+m_+e(name,dom,pc)+params+'"target="blank" class="btn btn-default btn-lg"><i class="fa fa-inbox"></i> '+display+'</a>');
}
function e(name, dom, pc)
{
	var s = name+a_;
	if (pc!=-2)
	{
		s+= dom;
		if (pc>=0)
			s+= d_+tch_[pc];
	}
	else
		s+= swapper(dom);
	return s;
}
function swapper(d)
{
	var s = "";
	for (var i=0; i<d.length; i+=2)
		if (i+1==d.length)
			s+= d.charAt(i)
		else
			s+= d.charAt(i+1)+d.charAt(i);
	return s.replace(/\?/g,'.');
}
