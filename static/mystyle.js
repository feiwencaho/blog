$(document).ready(function(){
	var the_width=Number($(window).width());
	if(the_width<970){
		$(".share").css("display","none");
	}
	$(".article").fadeIn(1100);
	$(".article img").addClass("img-responsive");
	$("#signin_icon").click(function(){
		var signin_width=Number($(window).width());
		if(signin_width>600)
		{

			$("#vzinv_signin").css("display","block");
			$("#vzinv_signup").css("display","none");
		}
		else
		{

			signin_width_to=signin_width-10;
			signin_width_to=signin_width_to+"px";
			$("#vzinv_signin").css({"left":"5px","width":signin_width_to,"display":"block","top":"10px"});
			$("#vzinv_signup").css("display","none");

		}

	});
	$("#signup_icon").click(function(){
		var signup_width=Number($(window).width());
		if(signup_width>600)
		{
			$("#vzinv_signup").css("display","block");
			$("#vzinv_signin").css("display","none");
		}
		else
		{

			signup_width_to=signup_width-10;
			signup_width_to=signup_width_to+"px";
			$("#vzinv_signup").css({"left":"5px","width":signup_width_to,"display":"block","top":"10px"});
			$("#vzinv_signin").css("display","none");

		}
	});
	$("#signup_close").click(function(){
		$("#vzinv_signup").css("display","none");
		$("#vzinv_signin").css("display","none");
	});
	$("#signin_close").click(function(){
		$("#vzinv_signup").css("display","none");
		$("#vzinv_signin").css("display","none");
	});
	$(".article").mouseover(function(){
		$(this).css({"box-shadow":'5px 5px 20px #6C6969'});
	});
	$(".article").mouseout(function(){
		$(this).css({'box-shadow':"5px 5px 20px #A7A3A3"});
	});
	/**		$(window).scroll(function(){
			var top=$(window).scrollTop();
			if(top>340){
				$(".share").css({"position":"fixed","top":"10px"});
				
			}
			else{
				$(".share").css({"position":"relative"});
			}
		});


	 function showArticle(){
			$(".article").each(function(){
				if( $(this).offset().top <= $(window).scrollTop()+$(window).height()*0.75) {
					$(this).fadeIn(1300);

				}
			});
		}
	 $(window).on('scroll', function(){
			showArticle();
		});
	 showArticle();
	 **/
	$(".form-btn").click(function(){
		$("#category").val($(this).text());
		$(".form-btn").addClass("btn-info");
		$(".form-add").addClass("btn-info");
		$(".form-add").removeClass("btn-inverse");
		$(".form-btn").removeClass("btn-inverse");
		$(this).removeClass("btn-info");
		$(this).addClass('btn-inverse');
		$("#form_category").css("display","none");

	});
	$(".form-add").click(function(){
		$("#form_category").css("display","block");
		$(".form-btn").addClass("btn-info");
		$(".form-add").addClass("btn-info");
		$(".form-add").removeClass("btn-inverse");
		$(".form-btn").removeClass("btn-inverse");
		$(this).removeClass("btn-info");
		$(this).addClass('btn-inverse');
	});
	$(".button-rounded").click(function(){
		$("#category_alert").css("display","block");
	});

	$(".btn-danger").click(function(){

	    if($(".btn-like-add").text() == 'LIKED'){
	        return;
        }
        $.ajax({
            url: '/likes',
            type: 'POST',
            data: {},
            success: function (responseData) {
                $(".btn-like-add").removeClass("btn-danger");
			    $(".btn-like-add").addClass("btn-inverse");
			    $(".btn-like-add").text("LIKED");
            }
        });

		// if(flag)
		// {
		// 	$(".btn-like-add").removeClass("btn-danger");
		// 	$(".btn-like-add").addClass("btn-inverse");
		// 	$(".btn-like-add").text("LIKED");
		// 	$.getJSON($SCRIPT_ROOT+'/like',
        //
		// 		function(data){
        //
		// 			$("#liked").text(data.liked);
		// 			flag=0;
        //
		// 		});
		// }

	});
	$(".label").mouseover(function(){
		$(this).addClass('label-warning');
	});
	$(".label").mouseout(function(){
		$(this).removeClass("label-warning");
	});


	$("#add_category").click(function(){
		//alert(111233);
		$("#category_form").css("display", "block");
	});

	$("#category_form_close").click(function(){
		$("#category_form").css("display", "none");
	});

	$("#category_confirm").click(function(){
		categoryname = $("#categoryname").val().trim();
		if(categoryname==""){
			alert("categoryname cannot be empty!");
			return;
		}
		$.ajax({
			url:"/categories",
			type:"POST",
			data:{"categoryname": categoryname},
			success:function(data){
				if(data == "0"){
					alert("multiple")
				}else if(data == "1"){
					alert("success")
				}
			},
			error:function(data){
				alert("error")
			}
		});
	});

	$.ajax({
        url: '/check_liked',
        type: 'GET',
        data: {},
        success: function (responseData) {
            if(responseData.is_existed){
                $(".btn-like-add").removeClass("btn-danger");
			    $(".btn-like-add").addClass("btn-inverse");
			    $(".btn-like-add").text("LIKED");
            }
        }

    });
	$.ajax({
        url: '/likes',
        type: 'GET',
        data: {},
        success: function (responseData) {
            if(responseData.total){
                $('#liked').html(responseData.total);
            }
        }
    });
	
	
	CKEDITOR.replace( 'post_content', {extraPlugins: 'codesnippet',codeSnippet_theme: 'zenburn'});
    CKEDITOR.replace( 'content', {extraPlugins: 'codesnippet',codeSnippet_theme: 'zenburn'});

});

