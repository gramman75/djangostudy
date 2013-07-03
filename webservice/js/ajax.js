$(function() {
	$("#search").keyup(function() {
		$.ajax({
					url: '/blog/search',
					type: 'GET',
					data: {'search_text': $("#search").val()},
					success: function (data) {
						$("#search_result").html(data);
					},
					dataType : "html"
				});	
	} );
})

