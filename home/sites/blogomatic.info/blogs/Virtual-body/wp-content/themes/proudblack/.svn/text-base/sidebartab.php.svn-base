<div id="tab_wrapper">
		<div id="tab_heading">
			<ul id="buttons">
				<li>Latest</li>
        <li>Comments</li>
        <li>Tags</li>
  		</ul>
		</div>
		<div id="panes">
			<div id="tab_content">
  			<div>
					<ul> <!-- Latest entries -->
					<?php query_posts('showposts=7'); ?>
					<?php while (have_posts()) : the_post(); ?>
					<li><span class="title"><a href="<?php the_permalink() ?>" title="<?php the_title(); ?>"><?php the_title(); ?></a></span>
					<br />
					<!--span class="meta"><?php the_time('l, F j, Y G:i'); ?> - <a href="<?php the_permalink() ?>#commenting" title="Jump to the comments"><?php comments_number('0 Comments','1 Comment','% Comments'); ?></a></span--></li>
					<?php endwhile; ?>
					</ul>
				</div>
			<div>
			<ul> <!-- Latest comments -->
			<?php
						global $wpdb;
						$sql = "SELECT DISTINCT ID, post_title, post_password, comment_ID,
						comment_post_ID, comment_author, comment_date, comment_approved,
						comment_type,comment_author_url,
						SUBSTRING(comment_content,1,80) AS com_excerpt
						FROM $wpdb->comments
						LEFT OUTER JOIN $wpdb->posts ON ($wpdb->comments.comment_post_ID =
						$wpdb->posts.ID)
						WHERE comment_approved = '1' AND comment_type = '' AND
						post_password = ''
						ORDER BY comment_date DESC
						LIMIT 7";
						$comments = $wpdb->get_results($sql);
						$output = $pre_HTML;
						foreach ($comments as $comment) {
						$output .= "\n<li><span class='title comment_excerpt'><a href=\"" . get_permalink($comment->ID) .
						"#comment-" . $comment->comment_ID . "\" title=\"on " .
						$comment->post_title . "\">" .strip_tags($comment->com_excerpt).
						"...</a></span><br/>" . "<span class='meta'>Said ".strip_tags($comment->comment_author)
						." on ".strip_tags($comment->comment_date)."</span></li>";
						}
						$output .= $post_HTML;
						echo $output;?>
			</ul>
			</div>
			<div class="tags">

				<ul> <!-- Latest comments -->
	<li><?php wp_tag_cloud('smallest=11&largest=15&format=flat&orderby=count'); ?></li>
			</ul>
				</div>

			</div>
		</div>
	</div>
	<script type="text/javascript" charset="utf-8">
		window.addEvent('load', function () {
			slidingtabs = new SlidingTabs('buttons', 'panes');
		});
	</script>
	<div id="tab_bottom"></div>