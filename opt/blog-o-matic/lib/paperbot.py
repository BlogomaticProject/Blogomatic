#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Bot classes.
"""

__author__ = "Cristóbal Carnero Liñán"
__copyright__ = "Copyright 2011, GEB (Universidad de Málaga)"
__credits__ = ["Cristóbal Carnero Liñán", ] # Code writers, bug reporters, suggestions, ...
__license__ = ""
__version__ = "0.0.2"
__maintainer__ = "Cristóbal Carnero Liñán"
__email__ = "ccarnerolinan@gmail.com"
__status__ = "Development" # "Prototype", "Development", "Production"


import logging
log = logging.getLogger("blogomatic.paperbot")

import urllib2
import re
import hashlib
import random
from time import sleep

from Bio import Entrez
#Entrez.email = "A.N.Other@example.com"
#Entrez.tool = "blog-o-matic"
from Bio import Medline

import paper


#################################################################################
# From: https://github.com/venthur/gscholar

# fake google id (looks like it is a 16 elements hex)
google_id = hashlib.md5(str(random.random())).hexdigest()[:16]

GOOGLE_SCHOLAR_URL = "http://scholar.google.com"
HEADERS = {'User-Agent' : 'Mozilla/5.0',
		        'Cookie' : 'GSP=ID=%s:CF=4' % google_id }

def getCitations(title):
	"""Returns number of citations of the article.
	"""

	log.debug('Looking for citations for paper "%s"...' % title)

	sleep(random.randrange(5, 15))

	searchstr = '/scholar?num=1&q=' + urllib2.quote(title)
	url = GOOGLE_SCHOLAR_URL + searchstr
	request = urllib2.Request(url, headers=HEADERS)
	response = urllib2.urlopen(request)
	html = response.read()
	html.decode('ascii', 'ignore')

	citere = re.compile(r'<a href="(?:/scholar\?cites[^>]*)">Cited by (?P<number>\d+)</a>')
	cite = citere.search(html) # Only look for the first one.
	log.debug('... done.')
	if cite:
		return cite.group("number")
	else:
		return 0

#################################################################################


class SearchEngine:

	def __init__(self):
		self._done = True
		self._searchCount = 0

	def count(self):
		return self._searchCount

	def done(self):
		"""Return "True" if all results where obteined.
		"""
		return self._done

	def search(self, term="music", db="pubmed"):
		"""Produce a search, but don't return any result. Execute "fetch" to go obtaining results until "done".

		Returns "False" if error.
		"""
		try:
			searchHandle = Entrez.esearch(db=db, term=term, usehistory="y")
		except:
			self._done = True
			return False

		searchResult = Entrez.read(searchHandle)
		searchHandle.close()

		self._searchPosition = 0
		self._searchCount = int(searchResult["Count"])

		self._searchSession = searchResult["WebEnv"]
		self._queryKey = searchResult["QueryKey"]

		log.info("Found %i records." % (self._searchCount, ))

		self._done = (self._searchCount==0)

		return True

	def fetch(self, batchSize=100):
		"""Return a batch of results.
		"""
		if self._done:
			return []

		end = min(self._searchCount, self._searchPosition + batchSize)

		log.info("Downloading from %i to %i..." % (self._searchPosition+1, end))

		fetchHandle = Entrez.efetch(db="pubmed", rettype="medline", retmode="text", retstart=self._searchPosition, retmax=batchSize, webenv=self._searchSession, query_key=self._queryKey)
		result = Medline.parse(fetchHandle)

		papers = [paper.Paper(r) for r in result if r.get("PMID") is not None ]

		fetchHandle.close()

		log.info("... downloading done")

		self._searchPosition = self._searchPosition + batchSize

		if self._searchPosition >= self._searchCount:
			self._done = True
			log.info("Search ended.")

		return papers


class TestEngine:

	def __init__(self):
		self._done = True

	def done(self):
		"""Return "True" if all results where obteined.
		"""
		return self._done

	def search(self, term="music", db="../tests/PyPubmedBot/resultsMusic.txt"):
		"""Produce a search, but don't return any result. Execute "fetch" to go obtaining results until "done".
		"""

		self._file = open(db)

		self._done = False

		return True

	def fetch(self):
		"""Return a batch of results.
		"""
		
		if self._done:
			return []

		result = Medline.parse(self._file)

		papers = [paper.Paper(r) for r in result if r.get("PMID") is not None ]

		self._file.close()

		done = True

		return papers


if __name__=="__main__":
	pass
