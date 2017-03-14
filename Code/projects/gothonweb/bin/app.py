import web
from gothonweb import map


urls=(
	'/game','GameEngine',
	'/start','Index',
	'/','Login',
	'/reset','Logout',
)

app=web.application(urls,globals())

#little hack so that debug mode works with sessions
if web.config.get('_session') is None:
	store=web.session.DiskStore('sessions')
	session=web.session.Session(app,store,initializer={'room':None,'count':0})
	web.config._session=session
else:
	session=web.config._session


render=web.template.render('templates/',base="layout")

allowed=(
	('admin','123456'),)

class Login(object):
	def GET(self):
		return render.login()
	def POST(self):
		i=web.input()
		username=i.get('username')
		passwd=i.get('passwd')
		if (username,passwd) in allowed:
			session.get('logged_in',False)
			session.logged_in=True
			assert web.seeother('/start')
		else:
			return '<h1>login error!!!<h1>login'	

class Index(object):
	def GET(self):
		if session.get('logged_in',False):
		#this is used to "setup" the session with starting values
			session.room=map.START
			web.seeother("/game")
		else:
			web.seeother("/")
class GameEngine(object):
	def GET(self):
		if session.get('logged_in',False):
			if session.room:
				session.count += 1	
				if session.room.name=="The End":
					return render.the_end(room=session.room)
				else:
					return render.show_room(room=session.room,count=session.count)
				return str(session.count)
			else :
				return render.you_died()
		else:
			web.seeother("/")
	def POST(self):
		form=web.input(action=None)
		#there's a bug here
		if session.room and form.action:
			session.room=session.room.go(form.action)
		web.seeother("/game")
if __name__=="__main__":
	app.run()
