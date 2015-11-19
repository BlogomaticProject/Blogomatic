# -*- coding: utf-8 -*-

from subprocess import Popen, PIPE
from pymongo import Connection
import web

import smtplib

urls = (
	'/','Index',
	'/create','Create',
	'/update','Update',
	'/delete','Delete',
	'/search','Search',
	'/register','Register',
	'/recovery','Recovery',
	'/createBlog','CreateBlog',
	'/updateBlog','UpdateBlog',
	'/deleteBlog','DeleteBlog',
	'/searchBlog','SearchBlog',
	'/registerUser','RegisterUser',
	'/psswdRecovery','PsswdRecovery',
)

app = web.application(urls,globals())
application = app.wsgifunc()


class Index:
	# Muestra en pantalla la pagina "home" presentando un listado de los blogs actuales
	def GET(self):
		render = web.template.render('/home/sites/blogomatic.info/templates',cache=False)
		web.header('Content-Type','text/html')
		return render.index(self.getBlogs())

	def getBlogs(self):
		# Conecta con la base de datos
		conn_ = Connection()
		db_ = conn_['blogomatic']
		ret = []
		
		try:
			# Se autentifica para acceder a la base de datos
			db_.authenticate('blogomatic','bnBN98cv.mongo')
			blogs_ = db_['blogs']

			for blog in blogs_.find().sort('title', 1):
				ret.append((blog['url'],blog['title']))

		except TypeError:
			ret = ['error']
		
		finally:
			db_.logout()
			conn_.disconnect()
			return ret


class Create:
	# Muestra en pantalla la pagina "create"
	def GET(self):
		render = web.template.render('/home/sites/blogomatic.info/templates',cache=False)
		msg = ''
		web.header('Content-Type','text/html')
		return render.create(msg)


class Update:
	# Muestra en pantalla la pagina "update" aportando un listado de los blogs actuales
	def GET(self):
		render = web.template.render('/home/sites/blogomatic.info/templates',cache=False)
		msg = ''
		web.header('Content-Type','text/html')
		return render.update(msg,self.getBlogs())

	def getBlogs(self):
		# Conecta con la base de datos
		conn_ = Connection()
		db_ = conn_['blogomatic']
		ret = []
		
		try:
			# Se autentifica para acceder a la base de datos
			db_.authenticate('blogomatic','bnBN98cv.mongo')
			blogs_ = db_['blogs']
			
			for blog in blogs_.find().sort('title', 1):
				ret.append(blog['title'])

		except TypeError:
			ret = ['error']
		
		finally:
			db_.logout()
			conn_.disconnect()
			return ret

		
class Delete:
	# Muestra en pantalla la pagina "delete" aportando un listado de los blogs actuales
	def GET(self):
		render = web.template.render('/home/sites/blogomatic.info/templates',cache=False)
		msg = ''
		web.header('Content-Type','text/html')
		return render.delete(msg,self.getBlogs())

	def getBlogs(self):
		# Conecta con la base de datos
		conn_ = Connection()
		db_ = conn_['blogomatic']
		ret = []
		
		try:
			# Se autentifica para acceder a la base de datos
			db_.authenticate('blogomatic','bnBN98cv.mongo')
			blogs_ = db_['blogs']

			for blog in blogs_.find().sort('title', 1):
				ret.append(blog['title'])

		except TypeError:
			ret = ['error']
		
		finally:
			db_.logout()
			conn_.disconnect()
			return ret

			
class Search:
	# Muestra en pantalla la pagina "search"
	def GET(self):
		render = web.template.render('/home/sites/blogomatic.info/templates',cache=False)
		msg = ''
		web.header('Content-Type','text/html')
		return render.search(msg)


						
class Register:
	# Muestra en pantalla la pagina "register"
	def GET(self):
		render = web.template.render('/home/sites/blogomatic.info/templates',cache=False)
		msg = ''
		web.header('Content-Type','text/html')
		return render.register(msg)


class Recovery:
	# Muestra en pantalla la pagina de recuperacion de clave
	def GET(self):
		render = web.template.render('/home/sites/blogomatic.info/templates',cache=False)
		msg = ''
		web.header('Content-Type','text/html')
		return render.recovery(msg)


class CreateBlog:
	def POST(self):
		render = web.template.render('/home/sites/blogomatic.info/templates',cache=False)
		i = web.input()
		err = self.createBlog(i)
		msg = ''

		if not(err):
			msg = 'Commited create blog.'
			web.header('Content-Type','text/html')
			return render.success(msg)
		else:
			msg = 'Sorry, the blog already exists, incorrect field format or authorization data.'
			web.header('Content-Type','text/html')
			return render.fail(msg)

	def createBlog(self,params):
		# Conecta con la base de datos
		conn_ = Connection()
		db_ = conn_['blogomatic']
		err = False
		
		try:
			# Se autentifica para acceder a la base de datos
			db_.authenticate('blogomatic','bnBN98cv.mongo')
			inv_ = db_['invitations']
			blogs_ = db_['blogs']
			
			
			# Nos aseguramos de que ningun campo se encuentra vacio
			if params['title'] == "" or params['url'] == ""  or params['keywords'] == ""  or (' ' in params['url']) :
				err = True
			
			else:
				# Comprobamos el usuario
				uDoc = inv_.find_one({'email': params['email']})
				
				if uDoc != None and uDoc['instances'] > 0:
					# Comprobamos la clave
					password = uDoc['password']
					if password == params['password']:
						# Ahora podemos comprobar que no existe un blog con el mismo titulo y url
						bDocTitle = blogs_.find_one({'title': params['title']})
						bDocUrl = blogs_.find_one({'url': params['url']})

						# Si es vacio significa que podemos crear el solicitado
						if bDocTitle == None and bDocUrl == None:
							# Llama al script del sistema para crear el blog
							# Saca el path del script del fichero de configuracion
							proc = Popen('/opt/blog-o-matic/bin/create_blog.sh "%s" "%s" "%s" >> /opt/blog-o-matic/var/log/create_blog.log 2>&1' % (params['title'], params['url'], params['keywords']), shell=True, stdout=PIPE)						

							bDoc = {'email': params['email'],'url': params['url'],'title': params['title']}
							blogs_.save(bDoc)
				
							inst = uDoc['instances']
							uDoc['instances'] = inst - 1

							inv_.save(uDoc)
						else:
							err = True
					else:
						err = True

				else:
					err = True
					
		except TypeError:
			err = True
		except:
			err = True
		finally:
			db_.logout()
			conn_.disconnect()
			return err


class UpdateBlog:
	def POST(self):
		render = web.template.render('/home/sites/blogomatic.info/templates',cache=False)
		i = web.input()
		err = self.updateBlog(i)
		msg = ''

		if not(err):
			msg = 'Commited update blog.'
			web.header('Content-Type','text/html')
			return render.success(msg)
		else:
			msg = 'Sorry, incorrect field format or authorization data.'
			web.header('Content-Type','text/html')
			return render.fail(msg)

	def updateBlog(self,params):
		# Conecta con la base de datos
		conn_ = Connection()
		db_ = conn_['blogomatic']
		err = False
		
		try:
			# Se autentifica para acceder a la base de datos
			db_.authenticate('blogomatic','bnBN98cv.mongo')
			inv_ = db_['invitations']
			blogs_ = db_['blogs']
						
			# Nos aseguramos de que ningun campo se encuentra vacio
			if params['title'] == "" or params['keywords'] == "":
				err = True
			
			else:
				# Comprobamos el usuario
				uDoc = inv_.find_one({'email': params['email']})
				
				if uDoc != None:
					# Comprobamos la clave
					password = uDoc['password']
					if password == params['password']:
					
						bDoc = blogs_.find_one({'title': params['title']})
						urlUpdate = bDoc['url']
						
						# Llama al script del sistema para actualizar el blog
						# Saca el path del script del fichero de configuracion
						proc = Popen('/opt/blog-o-matic/bin/update_blog.sh "%s" "%s" >> /opt/blog-o-matic/var/log/update_blog.log 2>&1' % (urlUpdate, params['keywords']), shell=True, stdout=PIPE)						
						
					else:
						err = True

				else:
					err = True
					
		except TypeError:
			err = True
		except:
			err = True
		finally:
			db_.logout()
			conn_.disconnect()
			return err			
			
			
class DeleteBlog:
	def POST(self):
		render = web.template.render('/home/sites/blogomatic.info/templates',cache=False)
		i = web.input()
		err = self.deleteBlog(i)
		msg = ''

		if not(err):
			msg = 'Commited delete blog.'
			web.header('Content-Type','text/html')
			return render.success(msg)
		else:
			msg = 'Failed delete blog.'
			web.header('Content-Type','text/html')
			return render.fail(msg)
	
	def deleteBlog(self,params):
		# Conecta con la base de datos
		conn_ = Connection()
		db_ = conn_['blogomatic']
		err = False
		
		try:
			# Se autentifica para acceder a la base de datos
			db_.authenticate('blogomatic','bnBN98cv.mongo')
			inv_ = db_['invitations']
			blogs_ = db_['blogs']
			papers_ = db_['papers']
			bDoc = blogs_.find_one({'title': params['title']})
			urlDelete = bDoc['url']
			
			# Comprobamos el usuario
			uDoc = inv_.find_one({'email': params['email']})
			
			if uDoc != None and uDoc['instances'] > 0:
				# Comprobamos la clave
				password = uDoc['password']
				if password == params['password']:
					# Aqui ejecutamos el shell script
					# Saca el path del script del fichero de configuracion
					proc = Popen('/opt/blog-o-matic/bin/remove_blog.sh "%s" >> /opt/blog-o-matic/var/log/remove_blog.log 2>&1' % urlDelete, shell=True, stdout=PIPE)

					blogs_.remove(bDoc)
					
					inst = uDoc['instances']
					uDoc['instances'] = inst + 1

					inv_.save(uDoc)
					
					# Eliminamos todos los PMID de los articulos asociados a esa url
					papers_.remove({'url': urlDelete})
			
				else:
					err = True	
			
			else:
				err = True

		except TypeError:
			err = True
		except:
			err = True
		finally:
			db_.logout()
			conn_.disconnect()
			return err


class SearchBlog:
	def POST(self):
		render = web.template.render('/home/sites/blogomatic.info/templates',cache=False)
		i = web.input()
		blogs = self.searchBlog(i)
		data = []

		if blogs != {}:
			
			web.header('Content-Type','text/html')
			
			for v,k in blogs.iteritems():
				data.append((v, k))

			return render.searchsuccess(data)

		else:
			msg = 'There are no results that match your criteria.'
			web.header('Content-Type','text/html')
			return render.fail(msg)


	def searchBlog(self,params):
		# Conecta con la base de datos
		conn_ = Connection()
		db_ = conn_['blogomatic']
		ret = {}
		
		try:
			# Se autentifica para acceder a la base de datos
			db_.authenticate('blogomatic','bnBN98cv.mongo')					
			blogs_ = db_['blogs']
			keywords = params['search'].split(' ')

			for keyword in keywords:
				# Hace una busqueda por palabra clave ignorando mayusculas o minusculas
				for blog in blogs_.find({'title': {'$regex': keyword, '$options':'i'}}):
					ret[blog['url']] = blog['title']
					
		except TypeError:
			ret = {}
		except:
			ret = {}
		finally:
			db_.logout()
			conn_.disconnect()
			return ret			
			
			
class RegisterUser:
	def POST(self):
		render = web.template.render('/home/sites/blogomatic.info/templates',cache=False)
		i = web.input()
		err = self.registerUser(i)
		msg = ''

		if not(err):
			msg = 'A user account was created.'
			web.header('Content-Type','text/html')
			return render.success(msg)
		else:
			msg = 'Sorry, user already exists or incorrect field format.'
			web.header('Content-Type','text/html')
			return render.fail(msg)


	def registerUser(self,params):
		# Conecta con la base de datos
		conn_ = Connection()
		db_ = conn_['blogomatic']
		err = False
		
		try:
			# Se autentifica para acceder a la base de datos
			db_.authenticate('blogomatic','bnBN98cv.mongo')
			inv_ = db_['invitations']

			# Nos aseguramos de que tanto el email como la clave cumplen una longitud minima
			if len(params['email']) < 3 or not('@' in params['email'] ) or len(params['password']) < 6 :
				err = True
			
			else:
				uDoc = inv_.find_one({'email': params['email']})
			
				if uDoc == None:
					# Guardamos el usuario y su clave y limitamos su numero maximo de blogs a 20
					uDoc = {'email': params['email'],'password': params['password'],'instances': 20}
					inv_.save(uDoc)

				else:
					err = True
					
		except TypeError:
			err = True
		except:
			err = True
		finally:
			db_.logout()
			conn_.disconnect()
			return err
			
			
class PsswdRecovery:
	def POST(self):
		render = web.template.render('/home/sites/blogomatic.info/templates',cache=False)
		i = web.input()
		err = self.psswdRecovery(i)
		msg = ''

		if not(err):
			msg = 'Your password has been sent to your email address.'
			web.header('Content-Type','text/html')
			return render.success(msg)
		else:
			msg = 'Sorry, invalid email address or the message could not be sent.'
			web.header('Content-Type','text/html')
			return render.fail(msg)


	def psswdRecovery(self,params):
		# Conecta con la base de datos
		conn_ = Connection()
		db_ = conn_['blogomatic']
		err = False
		
		try:
			# Se autentifica para acceder a la base de datos
			db_.authenticate('blogomatic','bnBN98cv.mongo')
			inv_ = db_['invitations']

			uDoc = inv_.find_one({'email': params['email']})
			
			if uDoc != None:
								
				user = uDoc['email']
				password = uDoc['password']
				
				# Definimos las variables para el envio del mensaje
				fromaddr = "infoblogomatic@gmail.com"
				toaddrs = user
				subject = "Message from Blog-o-Matic website"
				message = "Hi! This is your Blog-o-Matic password account:  " + password				
				msg = 'Subject: %s\n\n%s' % (subject, message)
								
				# Creamos un objeto smtp y realizamos el envio
				try: 
					server = smtplib.SMTP('localhost')
					server.set_debuglevel(1)
					server.sendmail(fromaddr, toaddrs, msg)
					server.quit()					
				except: 
					err = True			
			else:
				err = True
					
		except TypeError:
			err = True
		except:
			err = True
		finally:
			db_.logout()
			conn_.disconnect()
			return err


