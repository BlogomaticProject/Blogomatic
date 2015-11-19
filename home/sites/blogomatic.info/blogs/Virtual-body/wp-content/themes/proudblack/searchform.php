<form id="searchform" method="get" action="<?php bloginfo('home'); ?>/">
    		<div id="applesearch">
            
					<span class="sbox_l"></span>
					<span class="sbox"><input type="search" name="s" id="srch_fld" placeholder="<?php _e('') ?>" autosave="applestyle_srch" results="10" onkeyup="applesearch.onChange('srch_fld','srch_clear')" value="<?php _e('') ?>"  x-webkit-speech speech onwebkitspeechchange="this.form.submit();"/></span>
					<span class="sbox_r" id="srch_clear"></span>

				</div>
</form>
<!--form id="searchform" method="get" action="<?php bloginfo('home'); ?>/">
    		<div id="applesearch">
            
					<span class="sbox_l"></span>
					<span class="sbox"><input type="search" name="s" id="srch_fld" placeholder="Search..." autosave="applestyle_srch" results="10" onkeyup="applesearch.onChange('srch_fld','srch_clear')" value="" /></span>
					<span class="sbox_r" id="srch_clear"></span>
        	
				</div>
</form-->