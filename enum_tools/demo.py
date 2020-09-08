# stdlib
from enum import IntEnum, IntFlag
from typing import List

# this package
import enum_tools.documentation
from enum_tools.documentation import document_enum

__all__ = ["People", "NoMethods", "NoMemberDoc", "StatusFlags"]

enum_tools.documentation.INTERACTIVE = True


@document_enum
class People(IntEnum):
	"""
	An enumeration of people.
	"""

	Bob = bob = 1  # noqa  # doc: A person called Bob  # doc: another doc # isort: ignore
	Alice = 2  # doc: A person called Alice
	Carol = 3  # doc: A person called Carol

	@classmethod
	def iter_values(cls):
		"""
		Iterate over the values of the Enum.
		"""

		return iter(cls)  # pragma: no cover

	@classmethod
	def as_list(cls) -> List:
		"""
		Return the Enum's members as a list.
		"""

		return list(cls)  # pragma: no cover


@document_enum
class NoMethods(IntEnum):
	"""
	An enumeration of people without any methods.
	"""

	Bob = bob = 1  # noqa  # doc: A person called Bob  # doc: another doc # isort: ignore
	Alice = 2  # doc: A person called Alice
	Carol = 3  # doc: A person called Carol


@document_enum
class NoMemberDoc(IntEnum):
	"""
	An enumeration of people without any member docstrings.
	"""

	Bob = bob = 1
	Alice = 2
	Carol = 3


@document_enum
class StatusFlags(IntFlag):
	"""
	An enumeration of status codes.
	"""

	Running = 1  # doc: The system is running.
	Stopped = 2  # doc: The system has stopped.
	Error = 4  # doc: An error has occurred.

	def has_errored(self) -> bool:
		"""
		Returns whether the operation has errored:
		"""

		return (self & 4) == self.Error
