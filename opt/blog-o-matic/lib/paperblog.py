#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Blog classes.
"""

__author__ = "Cristóbal Carnero Liñán & Luis J. Ferrer"
__copyright__ = "Copyright 2011, GEB"
__credits__ = ["Cristóbal Carnero Liñán", ] # Code writers, bug reporters, suggestions, ...
__license__ = ""
__version__ = "0.0.2"
__maintainer__ = "Cristóbal Carnero Liñán"
__email__ = "ccarnerolinan@gmail.com"
__status__ = "Development" # "Prototype", "Development", "Production"


import sys 
import optparse

import logging
log = logging.getLogger("blogomatic.paperblog")

import wordpresslib

from pymongo import Connection


class Blog:

	def __init__(self, url, urlshort, admin, password, affinity=0.5, blogID=0):
		self._url = url
		self._urlshort = urlshort
		self._admin = admin
		self._password = password
		self._blogID = blogID

		self._affinity = affinity

		self._wp = wordpresslib.WordPressClient(self._url, self._admin, self._password)
		self._wp.selectBlog(self._blogID)

	def update(self, paper, dictionary, keywords, addCitation=False):
		"""Get a paper and a dictionary of technical jargon and post the paper in the blog with the right format. Also, calculates the tags from the title and abstract and set them in the post. Each custom field with the format "tag_TERM" will give the frecuency of this term in the text (title and abstract).

		Return True if posted or updated
		""" 

		if not paper.abstract():
			log.info("Skkiped paper with PMID %s: no abstract." % (paper.pmid(), ))
			return False
						
		
		# Conecta con la base de datos
		conn_ = Connection()
		db_ = conn_['blogomatic']
		
		# Se autentifica para acceder a la base de datos
		db_.authenticate('blogomatic','bnBN98cv.mongo')
		papers_ = db_['papers']			
	
		# Comprobamos en la coleccion papers de la base de datos si ya existe el PMID del articulo
		pDoc = papers_.find_one({'pmid': paper.pmid()})
				
		
		# Si ya existe el articulo en cualquier blog nos lo saltamos (OPCION 1)
		if pDoc != None:
		# Si ya existe el articulo en este blog en particular nos lo saltamos (OPCION 2)
		# if pDoc != None and pDoc['url'] == self._urlshort : 
			log.info("Skkiped paper with PMID %s: already exist in the database" % (paper.pmid(), ))
			db_.logout()
			conn_.disconnect()
			return False		
						
		
		# Guardamos el PMID del articulo en la base de datos
		paperDoc = {'pmid': paper.pmid(), 'url': self._urlshort}
		papers_.save(paperDoc)
		db_.logout()
		conn_.disconnect()
		
				
		log.info("Posting paper with PMID %s..." % (paper.pmid(), ))
		
		# Create a post
		post = wordpresslib.WordPressPost()

		post.title = paper.title()

		if addCitation:
			post.description = "<p>%s</p>\n<p>%s</p>" % (paper.abstract(), paper.getCitationLink())
		else:
			post.description = paper.abstract()

		post.excerpt = paper.getExcerpt()
		post.allowComments = False

		tags = dictionary.getTags(paper.title() + ". " + paper.abstract())

		kwTitle = 0
		for v in keywords.getTags(paper.title()).values():
			kwTitle += v

		kwAbstract = 0
		for v in keywords.getTags(paper.abstract()).values():
			kwAbstract += v

		post.customFields = {"citation": paper.getCitationLink(),
							 "year": paper.year(),
							 "keywords_in_title": kwTitle, "keywords_in_abstract": kwAbstract, "affinity": int(round(self._affinity*kwTitle + (1.0-self._affinity)*kwAbstract)),
							 "citations": paper.citations()}

		# Each keyword is attached in the post as "tag" and as "custom field" (to store the frequency of each term)
		# Remove "," and replace spaces for "-" in each tag name.
		post.tags = [t.replace(",", "").replace(" ", "-") for t in tags.keys()]
		for k, v in tags.items():
			post.customFields["tag_" + k.replace(",", "").replace(" ", "-")] = str(v)

		# Publish post
		postID = self._wp.newPost(post, True)

		# TODO Store "postID".

		log.info("... done.")

		return True


if __name__ =="__main__":
	pass
