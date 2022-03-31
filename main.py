# pylint: disable=W0703
"""Main function."""
import traceback
import time

from slib.init import SInit
from slib.log import SLog

if __name__ == "__main__":
    try:
        SInit.init()

        for i in range(10000):
            time.sleep(1)

            SLog.debug('debug message')
            SLog.info('informational message')
            SLog.warning('warning')
            SLog.error('error message')

    except Exception as e:
        SLog.error(e)
        SLog.error(traceback.format_exc())

        print(e)
        print(traceback.format_exc())
