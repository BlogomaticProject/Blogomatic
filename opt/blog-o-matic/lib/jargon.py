#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Dictionary of technical terms.
"""

__author__ = "Cristóbal Carnero Liñán"
__copyright__ = "Copyright 2011, GEB"
__credits__ = ["Cristóbal Carnero Liñán", ] # Code writers, bug reporters, suggestions, ...
__license__ = ""
__version__ = "0.0.1"
__maintainer__ = "Cristóbal Carnero Liñán"
__email__ = "ccarnerolinan@gmail.com"
__status__ = "Development" # "Prototype", "Development", "Production"


import sys 
import optparse

import logging
log = logging.getLogger("blogomatic.jargon")

import re

class Dictionary:

	def __init__(self, filename="../usr/share/medical_jargon.txt", phrases=[]):
		"""Read dictionary. Each line of the dictionary has this format:

			TERM1[=TERM11[=TERM12[...]]]
			TERM2[=TERM21[=TERM22[...]]]
			...
			TERMn[=TERMn1[=TERMn2[...]]]

		Where TERMi is equivalent to TERMij.

		TERMi is more relevant than TERMj if i<j.
		"""

		if phrases:
			self._phrases = phrases
		else:
			txt = open(filename).read().split("\n")
			self._phrases = [line.split("=") for line in txt[:-1]] # XXX [:-1] is to avoid a null as last item.

	def createSimplifiedDictionary(self, text):
		"""Create a new dictionary with only the terms that appears in the text.
		"""

		simpleText = text.lower()

		resultPhrases = []
		for phrases in self._phrases:
			for phrase in phrases:
				try:

					regex = re.compile(r"\b%s" % phrase.lower()) # Set a boundary at the beginning of a word, but not at the end.
					result = regex.search(simpleText) # XXX This will start searching from the beginning each time!

					if result:
						resultPhrases.append(phrases)
						# XXX This will not remove each match of the term. Doing this would be costly.
						break

				except: # XXX This is only to catch a exception from the "re.compile" line (for expressions with parenthesis, for example).
					log.warning("Error with a phrase from the dictionary: %s" % phrase)

		return Dictionary(phrases=resultPhrases)

	def getTags(self, text):
		"""Given the dictionary, search the keywords that appears in the text. The function returns the tags with the number of times the terms appears in the text, with this format:

			{TERM1: cTERM1, ..., TERMn: cTERM1}

		The search check that the term is not a sufix in the word in the text (for example "aging" in "imaging"), but doesn't check if the term is a prefix (for example "brain" in "brains").

		Each term in the text that matches with a term in the dictionary is deleted so it does not count more than once (for example, "postoperatory pain" is only count once, and not twice as "postoperatory pain" and "pain" tags).
		"""
		simpleText = text.lower()

		tags={}
		for phrases in self._phrases:
			count = 0

			for phrase in phrases:
				try:
					done = False
					start = 0

					regex = re.compile(r"\b%s" % phrase.lower()) # Set a boundary at the beginning of a word, but not at the end.
					while not done:

						result = regex.search(simpleText) # XXX This will start searching from the beginning each time!

						if result:
							count = count + 1
							simpleText = simpleText[:result.start()] + simpleText[result.end():]
						else:
							done = True

				except: # XXX This is only to catch a exception from the "re.compile" line (for expressions with parenthesis, for example).
					log.warning("Error with a phrase from the dictionary: %s" % phrase)

			if count:
				tags[phrases[0]] = count


		return tags

if __name__=="__main__":
	pass
