from nitro.service.options import options


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

def get_pagination_all(resource_client, client):
    result_list = []
    page_count = 1
    api_options = options()
    api_options.pagesize = 100
    api_options.pageno = page_count
    try:
        while 1:
            result = resource_client.get(client, option_=api_options)
            for obj in result:
                # This is crucil, since last page item is has empty name
                if hasattr(obj,'name') and obj.name != "":
                    result_list.append(obj)
            # result_list.extend(result)
            page_count = page_count + 1
            api_options.pageno = page_count
            if not result or len(result) == 0 or len(result) == 1:
                break
    except:
        pass
    return result_list
