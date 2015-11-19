<?php 

get_header(); 

 
global $query_string;

$videoPost = '&meta_key=video';
if (is_tag()){
	$tag_obj = $wp_query->get_queried_object();	
	$tag = '&meta_key=tag_'.strtolower($tag_obj->slug).'&orderby=meta_value_num';
}

?>
<div id="content" class="fullspan">
 	<div class="container_16">

		<div id="main" class="grid_11">
	 		<?php	query_posts($query_string.$videoPost.'&posts_per_page=-1');
 					if (have_posts()){ 
 						$_SESSION['playlist'] = $query_string.'&posts_per_page=-1';;
						include (TEMPLATEPATH . '/videoblog.php'); 						
					}?>	
    		<div id="main-top"></div>
				
           <div id="main-area" class="clearfix">
           <?php query_posts($query_string.'&meta_key=affinity&orderby=meta_value_num&order=desc');
           if (have_posts()) : ?>
           <?php global $wp_query;	$total_results = $wp_query->found_posts; global $post;?>
           <div class="cat-header">
           	<h2>Total results: <?php echo $total_results; ?> </h2>
           </div>	
            	<?php while (have_posts()) : the_post();?>	
            	
									<div class="post">
										<h2 class="post-title"><a title="<?php the_title(); ?>" href="<?php the_permalink() ?>" rel="bookmark"><?php the_title(); ?></a></h2>
                    <div class="post-meta-top">
											<?php if ('open' == $post->comment_status) : ?>
                    		<div class="post-comments"><?php comments_popup_link(__('No Comments'), __('1 Comment'), __('% Comments')); ?></div>
                    	<?php endif; ?>	
                    </div>
										
										<?php $video = get_post_meta($post->ID,'video',true);
										if (! empty($video)){?>
											<div class="video-icon"><a href="<?php the_permalink() ?>"><img src="wp-content/themes/proudblack/images/videoIcon.jpg"></a></div>	
										<?php	}else{ ?>	
											<div class="post-category"></div>	
										<?php } ?>
											
                    <div class="entry">	
                    	<?php if(! empty($post->post_excerpt))
                    					 the_excerpt();
                    				else
                    					 the_content(); ?>
                    <?php if( function_exists('ADDTOANY_SHARE_SAVE_KIT') ) { ADDTOANY_SHARE_SAVE_KIT(); } ?>					 
                    </div>
										<?php
										/*$posttags = get_the_tags();
										if ($posttags) {*/?>
				  					<div class="post-meta"><?php the_tags('<p>',' ','</p>'); ?></div> 
				  					<?php
										/*}*/
										?>
			    				</div>
            	<?php endwhile; ?>
              <div class="navigation clearfix">
								<div class="alignleft"><?php next_posts_link('&laquo; Older Entries') ?></div>
								<div class="alignright"><?php previous_posts_link('Newer Entries &raquo;') ?></div>
							</div>
            <?php else : ?>
			       	<div class="post">
			       			<div class="entry"><p class="center"> Sorry, but there are no results for your search.</p></div>
              </div>
            <?php endif; ?>
            
           </div>
        <div id="main-bottom"></div>
            
		</div>
 		<?php get_sidebar(); ?>
	</div>

</div>
<div class="clearfix"></div>
<?php get_footer(); ?>
