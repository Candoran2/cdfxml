from generated.base_struct import BaseStruct
from generated.base_struct import BaseStruct
from generated.formats.cdf.basic import Biguint32


class ExportString(BaseStruct):


# START_CLASS

	def __new__(self, context, arg=0, template=None, set_default=True):
		return ''

	@staticmethod
	def from_stream(stream, context=None, arg=0, template=None):
		length = Biguint32.from_stream(stream)
		chars = stream.read(length)[:-1]
		return chars.decode(errors="surrogateescape")

	@staticmethod
	def to_stream(instance, stream, context, arg=0, template=None):
		instance = instance + '\x00'
		encoded_instance = instance.encode(errors="surrogateescape")
		length = len(encoded_instance)
		Biguint32.to_stream(length, stream, context)
		stream.write(encoded_instance)

	@staticmethod
	def get_size(instance, context, arg=0, template=None):
		string_len = len(instance.encode(errors="surrogateescape")) + 1
		return Biguint32.get_size(string_len, context) + string_len

	@classmethod
	def validate_instance(cls, instance, context=None, arg=0, template=None):
		assert isinstance(instance, str)
		Biguint32.validate_instacne(len((instance + '\x00').encode(errors="surrogateescape")), context)

	get_field = None
	_get_filtered_attribute_list = None

	@staticmethod
	def from_value(value):
		return str(value)
