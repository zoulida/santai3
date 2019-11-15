__author__ = 'zoulida'

from enum import Enum


class CustomEnum(Enum):
    def __repr__(self):
        return "%s.%s" % (
            self.__class__.__name__, self._name_)

# noinspection PyPep8Naming
class FILEPATH(CustomEnum):
    TickDataDIRwin = 'F:\\stock_data\\tick_CVS_data\\'
    DayDataDIRwin = 'F:\\stock_data\\day_CVS_data\\'
