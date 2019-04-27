class Issue(object):
	"""docstring for Issue"""
	def __init__(self, id="", summary="", assignee="", status=""):
		super(Issue, self).__init__()
		self.id = id
		self.summary = summary
		self.assignee = assignee
		self.status = status