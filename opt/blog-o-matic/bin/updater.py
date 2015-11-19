#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Updates a blog from a search in PubMed.

Now the blog is identified by the XML-RPC URL, and it needs the search, admin login info,... In the future the parameter will be only the ID of the blob.
"""

__author__ = "Cristóbal Carnero Liñán"
__copyright__ = "Copyright 2011, GEB (Universidad de Málaga)"
__credits__ = ["Cristóbal Carnero Liñán", ] # Code writers, bug reporters, suggestions, ...
__license__ = "GPL"
__version__ = "0.0.2"
__maintainer__ = "Cristóbal Carnero Liñán"
__email__ = "ccarnerolinan@gmail.com"
__status__ = "Development" # "Prototype", "Development", "Production"


import sys 
import os
import optparse
import datetime

import logging.config
logging.config.fileConfig(os.environ['BLOGOMATICPATH']+"/etc/logging.conf")

import logging
log = logging.getLogger("blogomatic.updater")

import jargon
import paperbot
import paperblog


def processCommandLine():
	parser = optparse.OptionParser(usage="%prog [options]", version="%prog "+__version__)
	parser.add_option("-s", "--search", dest="search", default="", help="search")
	parser.add_option("-u", "--url", dest="url", default="", help="URL of the XML-RPC service of the blog")
	parser.add_option("-r", "--urlshort", dest="urlshort", default="", help="URL of the blog")
	parser.add_option("-a", "--admin", dest="admin", default="", help="user administrator of the blog")
	parser.add_option("-p", "--password", dest="password", default="", help="password of the user administrator")
	parser.add_option("-j", "--jargon-file", dest="jargonFile", default=os.environ['BLOGOMATICPATH']+"/usr/share/medical_jargon.txt", help="dictionary of technical terms")
	parser.add_option("-l", "--limit", dest="limit", default=999999, help="limit of posts")
	parser.add_option("-c", "--citation", action="store_true", dest="citation", default=False, help="add citation link in the body of the article")
	parser.add_option("--affinity", type="float", dest="affinity", default=0.6, help="weight of the title in the affinity calculation")

	(options, args) = parser.parse_args()


	if not (options.search and options.url and options.urlshort and options.admin and options.password):
		parser.error("you should indicate the search, url, urlshort, user admin and password")

	return (options, args)

  
def main():
	(options, args) = processCommandLine()

	t1 = datetime.datetime.now()

	log.info('Updating blog with search "%s".' % options.search)

	blog = paperblog.Blog(options.url, options.urlshort, options.admin, options.password, options.affinity)

	searcher = paperbot.SearchEngine()

	if not searcher.search(options.search):
		log.error('Error searching: "%s".' % options.search)
		return -1

	keywords = jargon.Dictionary(phrases=[[i] for i in options.search.split(" ")])
	dictionary = jargon.Dictionary(options.jargonFile)

	papersCount = 0;
	postsCount = 0;

	# Perform a quick start up
	log.info("Starting up...")
	papers = searcher.fetch(10) # This is the number of posts in the index of the blog

	# XXX This could be avoided in the start up
	log.info("Pre-processing dictionary...")
	text = "\n".join([p.title()+". "+p.abstract() for p in papers])
	simplifiedDictionary = dictionary.createSimplifiedDictionary(text)
	log.info("... pre-processing dictionary done.")


	for p in papers:
		if blog.update(p, simplifiedDictionary, keywords, options.citation):
			postsCount += 1

		papersCount += 1
		log.info("[%s%%]" % ((100*papersCount)/searcher.count()))
	
		if postsCount >= int(options.limit):
			log.warning('Limit of %i reached.' % options.limit)
			break

	log.info("... starting up done.")

	# Perform a search in batches
	while (not searcher.done()) and (postsCount < options.limit):
		papers = searcher.fetch()

		log.info("Pre-processing dictionary...")
		text = "\n".join([p.title()+". "+p.abstract() for p in papers])
		simplifiedDictionary = dictionary.createSimplifiedDictionary(text)
		log.info("... pre-processing dictionary done.")

		for p in papers:
			if blog.update(p, simplifiedDictionary, keywords, options.citation):
				postsCount += 1

			papersCount += 1
			log.info("[%s%%]" % ((100*papersCount)/searcher.count()))
		
			if postsCount >= int(options.limit):
				log.warning('Limit of %i reached.' % options.limit)
				break

	log.info('... updating for search "%s" finished.' % (options.search))

	t2 = datetime.datetime.now()
	log.info('Posted %i papers of %i, in %s.' % (postsCount, searcher.count(), t2-t1))

	return 0
  

if __name__=="__main__":
	sys.exit(main())
