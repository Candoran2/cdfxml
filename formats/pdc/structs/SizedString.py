class SizedString:

# START_CLASS

	def __new__(self, context=None, arg=0, template=None, set_default=True):
		return ''

	@staticmethod
	def from_stream(stream, context=None, arg=0, template=None):
		length = template.from_stream(stream)
		chars = stream.read(length)
		return chars.decode(errors="surrogateescape")

	@staticmethod
	def to_stream(instance, stream, context, arg=0, template=None):
		encoded_instance = instance.encode(errors="surrogateescape")
		template.to_stream(len(encoded_instance), stream, context)
		stream.write(encoded_instance)

	@staticmethod
	def get_size(instance, context, arg=0, template=None):
		string_len = len(instance.encode(errors="surrogateescape"))
		return template.get_size(string_len, context) + string_len

	get_field = None
	_get_filtered_attribute_list = None

	@staticmethod
	def fmt_member(instance, indent=0):
		return repr(instance)

	@classmethod
	def validate_instance(cls, instance, context=None, arg=0, template=None):
		assert isinstance(instance, str)
		template.validate_instance(instance.encode(errors="surrogateescape"), context)

	@staticmethod
	def from_value(value):
		return str(value)
