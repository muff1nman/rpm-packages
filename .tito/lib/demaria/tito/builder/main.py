from tito.builder import MockBuilder

class MockSigningBuilder(MockBuilder):
	"""Additionaly signs packages"""
	def run(self, options):
		print("Mock Signing Builder")
		artifacts = super(MockSigningBuilder, self).run(self,options)
		print("Mock Signing Builder")
		for a in artifacts:
			print(a)
		return artifacts
