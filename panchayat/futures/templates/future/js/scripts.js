
(function($) {
    "use strict"; 
		
	/* PRELOADER */
	$(window).load(function() {
		var preloaderFadeOutTime = 500;
		function hidePreloader() {
			var preloader = $('.spinner-wrapper');
			setTimeout(function() {
				preloader.fadeOut(preloaderFadeOutTime);
			}, 500);
		}
		hidePreloader();
	});
	
	
	/* STYLE SWITCHER */
	$('#toggle-switcher').on('click', function(){
		if($(this).hasClass('opened')){
			$(this).removeClass('opened');
			$('#style-switcher').animate({'right':'-240px'});
		}else{
			$(this).addClass('opened');
			$('#style-switcher').animate({'right':'0px'});
		}
	});

	
	/* NAVBAR SCRIPTS */
	//jQuery to collapse the navbar on scroll
	$(window).scroll(function() {
		if ($(".navbar").offset().top > 50) {
			$(".navbar-fixed-top").addClass("top-nav-collapse");
		} else {
			$(".navbar-fixed-top").removeClass("top-nav-collapse");
		}
	});

	//jQuery for page scrolling feature - requires jQuery Easing plugin
	$(function() {
		$(document).on('click', 'a.page-scroll', function(event) {
			var $anchor = $(this);
			$('html, body').stop().animate({
				scrollTop: $($anchor.attr('href')).offset().top
			}, 800, 'easeInOutExpo');
			event.preventDefault();
		});
	});
    // closes the responsive menu on menu item click
    $(".navbar-nav li a").on("click", function(event) {
    if (!$(this).parent().hasClass('dropdown'))
        $(".navbar-collapse").collapse('hide');
	});
	
	
	/* COUNTDOWN TIMER */
	$('#clock').countdown('2019/12/27 08:50:56') /* change here your "countdown to" date */
	.on('update.countdown', function(event) {
		var format = '<span class="counter-number">%D<br><span class="timer-text">Days</span></span><span class="separator">:</span><span class="counter-number">%H<br><span class="timer-text">Hours</span></span><span class="separator">:</span><span class="counter-number">%M<br><span class="timer-text">Minutes</span></span><span class="separator">:</span><span class="counter-number">%S<br><span class="timer-text">Seconds</span></span>';
			
		$(this).html(event.strftime(format));
	})
	.on('finish.countdown', function(event) {
	$(this).html('This offer has expired!')
		.parent().addClass('disabled');
	});
	
	
	/* BACK TO TOP BUTTON */
    // create the back to top button
    $('body').prepend('<a href="body" class="back-to-top page-scroll">Back to Top</a>');
    var amountScrolled = 700;
    $(window).scroll(function() {
        if ($(window).scrollTop() > amountScrolled) {
            $('a.back-to-top').fadeIn('500');
        } else {
            $('a.back-to-top').fadeOut('500');
        }
    });
	
	
	/* DETAILS IMAGE GALLERY SWIPER */
	var MySwiper = new Swiper('.my-swiper-container', {
		pagination: '.swiper-pagination',
		paginationClickable: true,
		loop: false,
		autoplayDisableOnInteraction: false,
		autoplay: 3500,
		nextButton: '.swiper-button-next',
		prevButton: '.swiper-button-prev'
    });
	
		
	/* MAGNIFIC POPUP FOR DETAILS IMAGE GALLERY SWIPER */
	$('.popup-link').magnificPopup({
		removalDelay: 300,
		type: 'image',
		callbacks: {
			beforeOpen: function() {
				this.st.image.markup = this.st.image.markup.replace('mfp-figure', 'mfp-figure ' + this.st.el.attr('data-effect'));
			},
			
			beforeClose: function() {
				$('.mfp-figure').addClass('fadeOut');
			}
		},
		gallery:{
			enabled:true //enable gallery mode
		}
	});
	
	
	/* MAGNIFIC POPUP FOR INSTRUCTOR AND TERMS & CONDITIONS DETAILS */
	$('.popup-with-move-anim').magnificPopup({
		type: 'inline',
		
		fixedContentPos: false, /* keep it false to avoid html tag shift with margin-right: 17px */
		fixedBgPos: true,

		overflowY: 'auto',

		closeBtnInside: true,
		preloader: false,
		
		midClick: true,
		removalDelay: 300,
		mainClass: 'my-mfp-slide-bottom'
	});

		
	/* COUNTERUP - STATISTICS */
    $('.counter').counterUp({
        delay: 10,
        time: 1200
    });
	
	
	/* REGISTRATION FORM */
    $("#RegistrationForm").validator().on("submit", function(event) {
    	if (event.isDefaultPrevented()) {
            // handle the invalid form...
            formError();
            submitMSG(false, "Check if all fields are filled in!");
        } else {
            // everything looks good!
            event.preventDefault();
            submitForm();
        }
    });

    function submitForm() {
        // initiate variables with form content
		var firstname = $("#firstname").val();
        var lastname = $("#lastname").val();
        var email = $("#email").val();
        var phone = $("#phone").val();
		var terms = $("#terms").val();
		
        $.ajax({
            type: "POST",
            url: "php/registrationform-process.php",
            data: "firstname=" + firstname + "&lastname=" + lastname + "&phone=" + phone + "&email=" + email + "&terms=" + terms, 
            success: function(text) {
                if (text == "success") {
                    formSuccess();
                } else {
                    formError();
                    submitMSG(false, text);
                }
            }
        });
	}

    function formSuccess() {
        $("#RegistrationForm")[0].reset();
        submitMSG(true, "You Are Registered!")
    }

    function formError() {
        $("#RegistrationForm").removeClass().addClass('shake animated').one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend', function() {
            $(this).removeClass();
        });
	}

    function submitMSG(valid, msg) {
        if (valid) {
            var msgClasses = "h3 text-center tada animated text-success";
        } else {
            var msgClasses = "h3 text-center text-danger";
        }
        $("#msgSubmit").removeClass().addClass(msgClasses).text(msg);
	}
	

	/* CONTACT FORM */
   $("#ContactForm").validator().on("submit", function(event) {
        if (event.isDefaultPrevented()) {
            // handle the invalid form...
            formCError();
            submitCMSG(false, "Check if all fields are filled in!");
        } else {
            // everything looks good!
            event.preventDefault();
            submitCForm();
        }
    });

    function submitCForm() {
        // initiate variables with form content
        var cname = $("#cname").val();
        var cemail = $("#cemail").val();
		var cmessage = $("#cmessage").val();

        $.ajax({
            type: "POST",
            url: "php/contactform-process.php",
            data: "name=" + cname + "&email=" + cemail + "&message=" + cmessage, 
            success: function(text) {
                if (text == "success") {
                    formCSuccess();
                } else {
                    formCError();
                    submitCMSG(false, text);
                }
            }
        });
    }

    function formCSuccess() {
        $("#ContactForm")[0].reset();
        submitCMSG(true, "Message Submitted!")
    }

    function formCError() {
        $("#ContactForm").removeClass().addClass('shake animated').one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend', function() {
            $(this).removeClass();
        });
    }

    function submitCMSG(valid, msg) {
        if (valid) {
            var msgClasses = "h3 text-center tada animated text-success";
        } else {
            var msgClasses = "h3 text-center text-danger";
        }
        $("#cmsgSubmit").removeClass().addClass(msgClasses).text(msg);
    }
	
		
	/* REMOVES LONG FOCUS ON BUTTONS */
	$(".button, a, button").mouseup(function(){
		$(this).blur();
	});
	

	/* PAYMENT METHOD RADIO BUTTONS */
	$(function () {
		$('input:radio').on('click', function (e) {
			e.stopPropagation();
			$('li').removeClass('active')
			$(this).parent().parent().addClass('active');
			var tabpane = $(this).parent().attr('aria-controls');
			$('.tab-content').children().removeClass('active');
			$('#' + tabpane).addClass('active');
		});
		$('a').on('click', function (e) {
			$(this).find("input[type=radio]").trigger('click');
		});
	});


	/* NORMALIZE CAROUSEL HEIGHTS */
	// pass in Bootstrap Carousel items
	$.fn.carouselHeights = function() {
		var items = $(this), //grab all slides
			heights = [], //create empty array to store height values
			tallest; //create variable to make note of the tallest slide

		var normalizeHeights = function() {

			items.each(function() { //add heights to array
				heights.push($(this).height()); 
			});
			tallest = Math.max.apply(null, heights); //cache largest value
			items.each(function() {
				$(this).css('min-height',tallest + 'px');
			});
		};

		normalizeHeights();

		$(window).on('resize orientationchange', function () {
			//reset vars
			tallest = 0;
			heights.length = 0;

			items.each(function() {
				$(this).css('min-height','0'); //reset min-height
			}); 
			normalizeHeights(); //run it again 
		});
	};

	jQuery(function($){
		$(window).on('load', function(){
			$('#quote .item').carouselHeights();
		});
	});
	
})(jQuery);
