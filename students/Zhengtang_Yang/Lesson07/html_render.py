class Element:
	tagname = 'html'
	ident = {1:' '*2, 2:' '*4, 3:' '*6, 4:' '*8, 5:' '*10}

	def __init__(self,content=None):
		"""
		content is a string and defaults to Nothing

		"""
		if content is None:
			self.temp = ''
		else:
			self.temp = content

	def append(self,newcontent):
		self.temp = self.temp + '\n' + newcontent

	def render(self, file_out, cur_ind=""):
		# file_out.write('<!DOCTYPE html>')
		file_out.write(f'<{self.tagname}>' + self.temp + f'\n</{self.tagname}>')

class Html(Element):
	tagname = 'html'

	def __init__(self,content=None):
		Element.__init__(self,content)

	def append(self,body):
		self.temp = self.temp + '\n' + OtherElement.temp

class Body(Element):
	tagname = 'body'

	def __init__(self,content=None):
		Element.__init__(self,content)

	def append(self,paragraph):
		self.temp = self.temp + '\n' + paragraph.temp

class P(Element):
	tagname = 'p'

