<?php get_header();

global $query_string;

$video = '&meta_key=video';
if (is_tag()){
	$tag_obj = $wp_query->get_queried_object();	
	$tag = '&meta_key=tag_'.strtolower($tag_obj->slug).'&orderby=meta_value_num';
}
?>
<div id="content" class="fullspan">

 	<div class="container_16">
		
		<div id="main" class="grid_11">
 		<?php if (is_tag()){
						query_posts($query_string.$tag.$video);
	 					if (have_posts()){ 
	 						$_SESSION['playlist'] = $query_string.$tag.$video;
							include (TEMPLATEPATH . '/videoblog.php'); 						
						} 				
	 				}else{
	 					query_posts($query_string.$video);
	 					if (have_posts()){ 
	 						$_SESSION['playlist'] = $query_string.$video;
							include (TEMPLATEPATH . '/videoblog.php'); 						
						}
					}?>			
    		<div id="main-top"></div> 
        <div id="main-area" class="clearfix">
            <div class="cat-header">
            <?php  query_posts($query_string.$tag);
            		if (have_posts()) : ?>
								<?php global $wp_query;	$total_results = $wp_query->found_posts; global $post;?>
								<?php $post = $posts[0]; // Hack. Set $post so that the_date() works. ?>
						    <?php /* If this is a category archive */ if (is_category()) { ?>
								<h2><?php echo $total_results; ?> Archive for the &#8216;<?php single_cat_title(); ?>&#8217; Category</h2>
								<?php /* If this is a tag archive */ } elseif( is_tag() ) { ?>
								<h2><?php echo $total_results; ?> Posts Tagged &#8216;<?php single_tag_title(); ?>&#8217;</h2>
								<?php /* If this is a daily archive */ } elseif (is_day()) { ?>
								<h2>Archive for <?php the_time('F jS, Y'); ?></h2>
								<?php /* If this is a monthly archive */ } elseif (is_month()) { ?>
								<h2>Archive for <?php the_time('F, Y'); ?></h2>
								<?php /* If this is a yearly archive */ } elseif (is_year()) { ?>
								<h2>Archive for <?php the_time('Y'); ?></h2>
								<?php /* If this is an author archive */ } elseif (is_author()) { ?>
								<h2>Author Archive</h2>
								<?php /* If this is a paged archive */ } elseif (isset($_GET['paged']) && !empty($_GET['paged'])) { ?>
								<h2>Blog Archives</h2>
								<?php } ?>
						</div><!-- /div cat-header -->
            <?php while (have_posts()) : the_post(); 
            	//setup_postdata($post); ?>	
							<div class="post">
								<!-- title -->
								<h2 class="post-title"><a title="<?php the_title(); ?>" href="<?php the_permalink() ?>" rel="bookmark"><?php the_title(); ?></a></h2>
                <!-- comments -->
                <div class="post-meta-top">
								<!--div class="post-date"><?php the_time('l, jS F Y'); ?></div-->
                <?php if ('open' == $post->comment_status) : ?>
                		<div class="post-comments"><?php comments_popup_link(__('No Comments'), __('1 Comment'), __('% Comments')); ?></div>
                <?php endif; ?>	
                </div>
                <!-- video -->
                <?php $video = get_post_meta($post->ID,'video',true);
								if (! empty($video)){?>
									<div class="video-icon"><a href="<?php the_permalink() ?>"><img src="wp-content/themes/proudblack/images/videoIcon.jpg"></a></div>	
								<?php	}else{ ?>	
									<div class="post-category"><?php //the_category(' '); ?></div>	
								<?php } ?>
								<!-- entry -->
                <div class="entry">	
								<?php if ($post->post_excerpt != '') 
												 the_excerpt();
											else
													the_content(); ?>
								<!-- share -->					
								<?php if( function_exists('ADDTOANY_SHARE_SAVE_KIT') ) { ADDTOANY_SHARE_SAVE_KIT(); } ?>					
                </div>
                <!-- tags -->
								<div class="post-meta"><?php the_tags('<p>',' ','</p>'); ?></div>
			    		</div><!-- /div post -->
			    		
            <?php endwhile; ?>
            <div class="navigation clearfix">
						<div class="alignleft"><?php next_posts_link('&laquo; Older Entries') ?></div>
						<div class="alignright"><?php previous_posts_link('Newer Entries &raquo;') ?></div>
						</div>
           <?php else : ?>
			        <h2 class="center">Not Found</h2>
							<p class="center">Sorry, but you are looking for something that isn't here.</p>
					</div><!-- /div cat-header -->
           <?php endif; ?>
           
        </div><!-- /div main-area --> 
        <div id="main-bottom"></div>
            
		</div><!-- /div main -->
    <?php get_sidebar(); ?>
  </div><!-- /div container_16 -->

</div><!-- /div content -->
<div class="clearfix"></div>
<?php get_footer(); ?>
