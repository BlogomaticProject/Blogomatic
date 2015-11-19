#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Paper classes.
"""

__author__ = "Cristóbal Carnero Liñán"
__copyright__ = "Copyright 2011, GEB (Universidad de Málaga)"
__credits__ = ["Cristóbal Carnero Liñán", ] # Code writers, bug reporters, suggestions, ...
__license__ = ""
__version__ = "0.0.2"
__maintainer__ = "Cristóbal Carnero Liñán"
__email__ = "ccarnerolinan@gmail.com"
__status__ = "Development" # "Prototype", "Development", "Production"


import sys 
import optparse

import logging
log = logging.getLogger("blogomatic.paper")


class Author:

	def __init__(self, name):
		nameList = name.split(" ")
		
		if len(nameList) < 2:
			self._firstname = ""
		else:
			self._firstname = nameList[1]

		self._lastname = nameList[0]

	def __str__(self):
		if self._firstname:
			return "%s, %s" % (self._lastname, self._firstname)
		else:
			return self._lastname


class Authors:

	def __init__(self, names):
		self._authors = [Author(i) for i in names]

	def __str__(self):
		"""Return a string with the name of the main author and "et al." if there is more than one author.
		"""
		if not self._authors:
			return ""

		if len(self._authors) == 1:
			# Another option will be: "AUTHOR1; AUTHOR2 & AUTHOR3"
			return "%s et al." % (self._authors[0], )
		else:
			return str(self._authors[0])


class Paper:

	def __init__(self, record, citations=0):
		"""Create a Paper from the result of a parse from Biopython.
		"""
		self._excerptLength = 540 # Configure.

		self._citations = citations

		self._pmid = int(record["PMID"])

		self._title = record["TI"]

		if "AB" in record:
			self._abstract = record["AB"]
		else:
			self._abstract = ""
			log.warning("No abstract for paper with PMID=%s." % self._pmid)

		if "AU" in record:
			self._authors = Authors(record["AU"])
		else:
			self._authors = Authors([])
			log.warning("No authors for paper with PMID=%s." % self._pmid)

		self._year = record["DP"].split(" ")[0] # Only take the year from the "publish year".

		if "SO" in record:
			source = record["SO"]
			self._source = "%s, %s" % (source.split(".")[0], source.split(";")[-1]) # Reformat the "source" to macth previous prototypes.
		else:
			self._source = ""
			log.warning("No source for paper with PMID=%s." % self._pmid)

	def pmid(self):
		return self._pmid

	def title(self):
		return self._title

	def abstract(self):
		return self._abstract

	def year(self):
		return int(self._year)

	def citations(self):
		return self._citations

	def getCitationLink(self):
		"""Return a HTML link to the PubMed page for this paper.
		"""
		if self._source:
			return '<a href="http://www.ncbi.nlm.nih.gov/pubmed/%i" target="_blank">%s (%s) %s <em>%s</em></a>' % (self._pmid, self._authors, self._year, self._title, self._source)
		else:
			return '<a href="http://www.ncbi.nlm.nih.gov/pubmed/%i" target="_blank">%s (%s) %s</a>' % (self._pmid, self._authors, self._year, self._title)

	def getExcerpt(self):
		"""Return an excerpt from the abstract.
		"""
		if len(self._abstract) <= self._excerptLength:
			return self._abstract
		else:
			return self._abstract[:self._abstract.find(" ", self._excerptLength)]


if __name__=="__main__":
	pass
