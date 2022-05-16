DELETE_STALE_SERVERS = 'delete_stale_servers'


def ask_before_run(logger):
    logger.info("Do you want to continue ? (y/n)")
    x = input()
    if x.lower() in ['y', 'n'] and x.lower() == 'y':
        return True
    return False

def read_input_file(input_file, logger):
    vsnames_list = []
    try:
        with open(input_file) as file:
            for line in file:
                if "," in line:
                    x = line.split(',')
                    vsnames_list.append(x[0].rstrip())
                else:
                    vsnames_list.append(line.rstrip())
    except Exception as e:
        logger.error("Error while reading input file %s", str(e))
    return vsnames_list
