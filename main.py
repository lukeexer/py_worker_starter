# pylint: disable=W0703
"""Main function."""
import traceback

from slib.init import SInit
from slib.log import SLog

if __name__ == "__main__":
    try:
        SInit.init()
    except Exception as e:
        SLog.error(e)
        SLog.error(traceback.format_exc())

        print(e)
        print(traceback.format_exc())
