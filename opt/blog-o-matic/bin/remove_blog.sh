#!/bin/bash -x
#!/bin/bash

# Removes a new blog.
#
# Parameters:
#	- Shortname

EXPECTED_ARGS=1
E_BADARGS=65

if [ $# -ne $EXPECTED_ARGS ]
then
	echo "Usage: `basename $0` [SHORTNAME]"
	exit $E_BADARGS
fi

. /etc/blog-o-maticrc
. $BLOGOMATICPATH/etc/blog.conf

BLOG_NAME=$1

cd $BLOG_DIR
cd $BLOG_NAME

TABLE_PREFIX=$(grep '$table_prefix' wp-config.php | sed "s/^[^']*'//g;s/_'.*$//g;")

mysql --host=$DB_HOST --user=$DB_USER --password=$DB_PW $DB_NAME << EOF
DROP TABLE ${TABLE_PREFIX}_commentmeta, ${TABLE_PREFIX}_comments, ${TABLE_PREFIX}_links, ${TABLE_PREFIX}_options, ${TABLE_PREFIX}_postmeta, ${TABLE_PREFIX}_posts, ${TABLE_PREFIX}_terms, ${TABLE_PREFIX}_term_relationships, ${TABLE_PREFIX}_term_taxonomy, ${TABLE_PREFIX}_usermeta, ${TABLE_PREFIX}_users;
EOF

cd ..

rm $BLOG_NAME -R
