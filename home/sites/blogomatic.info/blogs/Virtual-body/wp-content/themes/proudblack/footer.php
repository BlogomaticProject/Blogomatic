<div id="footer" class="fullspan">
	<div class="container_16">
    	<div class="grid_16">
        <?php if ( get_option('pb_twit') ) { ?>
   			<div id="twitter" class="grid_6">
            <div id="twitter-content" class="clearfix">
     	        <div id="twitter-icon"><a href="http://www.twitter.com/<?php echo get_option('pb_twit'); ?>"><img src="<?php bloginfo('template_url'); ?>/images/twitter.gif" border="0" alt="Follow me on Twitter" /></a></div>
       	    </div>
            <p><ul id="twitter_update_list"><li></li></ul></p>
            </div>
          
        <?php } ?>
         <?php if ( get_option('pb_flickr') ) { ?>
   			<div id="flickr" class="grid_5">
            <h2>Flickr</h2>
				<ul class="flickr-ul clearfix">					        
            	<script type="text/javascript" src="http://www.flickr.com/badge_code_v2.gne?count=6&amp;display=latest&amp;size=s&amp;layout=x&amp;source=user&amp;user=<?php echo get_option('pb_flickr'); ?>"></script>	
				</ul>  
            </div>
          
        <?php } ?>
        
   			<!--div id="lifestream" class="grid_5">
					<h2 id ="lifestreamh2">Lifestream</h2><?//php lifestream(); ?>
        </div-->
          
       <div id="copyright" class="grid_16">&copy; 2009 <?php echo get_option('pb_copyright'); ?> . Proudblack theme by <a href="http://iacobionut.com">Iacob Ionut. </a>
       	<?php wp_loginout(); ?>
        </div>
    </div>
</div>

</div><!-- WRAP -->
<?php wp_footer(); ?>
<?php if ( get_option('pb_twit') ) { ?>
<script type="text/javascript" src="http://twitter.com/javascripts/blogger.js"></script>
<script type="text/javascript" src="http://twitter.com/statuses/user_timeline/<?php echo get_option('pb_twit'); ?>.json?callback=twitterCallback2&amp;count=2"></script>
<?php } ?>
</body>
</html>
