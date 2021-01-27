var list =  ["8","14","15","24","26","82","88","104","85"];
function doit(num){
	var css = "body > div:nth-child(1) > section.h5-act-votePage-templetBox > section.h5ActTemplet-voteBox > section > ul > li:nth-child("+ list[num] + ") > div > div.c-vote-btn";
	if(list[num] == "85")
	{
		console.log("你已经完成训练生许杨玉琢的投票");
	}
	else
	{
		console.log("你已经完成序号为："+list[num]+"的训练生的投票");
	}
	var clickit = document.querySelector(css);
	clickit.click();
}
var count = 0;
function vote()
{
	console.log(count);
	doit(count);
	count++;
	if(count<9)
	{
		setTimeout(vote,2000+count*100)
	}
}
vote();