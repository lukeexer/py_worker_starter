"""Main function."""
import time

from slib.init import SInit
from slib.config import SConfig
from slib.log import SLog
from slib.validate import SCheck

if __name__ == "__main__":
    SInit.init()

    print(SConfig.get_str_conf('example_1'))
    print(SConfig.get_int_conf('example_1'))
    print(SConfig.is_conf_exist('example_2'))

    print(SConfig.get_all_keys())
    print(SConfig.get_all_key_and_value_pairs())

    SCheck.check_int('input field 1', '10', 0, 100)
    SCheck.check_str('input field 1', 'str_val', 1, 20)

    for i in range(10000):
        time.sleep(1)

        SLog.debug('debug message')
        SLog.info('informational message')
        SLog.warning('warning')
        SLog.error('error message')
