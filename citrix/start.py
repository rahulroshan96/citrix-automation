import sys
import pathlib
import time

cwd_path = pathlib.Path(__file__).parent.resolve().parent
cwd_path = cwd_path.as_posix()
sys.path.insert(0, cwd_path)
from citrix.builer import Builder
from citrix.logger.citrix_logger import get_logger
from arguments.arguments_settings import Argument


if __name__ == '__main__':
    cli_args = Argument().set_arguments()
    ct_logger = get_logger()
    builder = Builder()
    builder = builder.set_args(cli_args).set_logger(ct_logger).set_client() \
        .setup_resource_clients().build()
    c_time = time.time()
    builder.execute()
    e_time = time.time() - c_time
    builder.save_output()
