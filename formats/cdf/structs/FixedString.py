class FixedString:
	"""Holds a string of a fixed size, given as an argument."""

# START_CLASS

	def __new__(cls, context, arg, template=None):
		return "\x00" * arg

	@staticmethod
	def from_stream(stream, context, arg, template=None):
		chars = stream.read(arg)
		return chars.decode(errors="surrogateescape")

	@staticmethod
	def to_stream(instance, stream, context, arg, template=None):
		encoded_instance = instance.encode(errors="surrogateescape")
		assert len(encoded_instance) == arg
		stream.write(encoded_instance)

	@staticmethod
	def get_size(instance, context, arg, template=None):
		return arg

	@classmethod
	def validate_instance(cls, instance, context, arg, template=None):
		assert isinstance(instance, str)
		assert len(instance.encode(errors="surrogateescape")) == arg

	get_field = None
	_get_filtered_attribute_list = None

	@staticmethod
	def from_value(value):
		return str(value)