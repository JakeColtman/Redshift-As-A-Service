from multiprocessing import Queue, Process


def post_to_queues(queues, message):
    for queue in queues:
        queue.put(message)


def create_queues(flow):
    queues = {}
    for flow in flow:
        queues[flow] = Queue()
    return queues


def service(process_function):
    def run_service(queue, success_queues, failure_queues):
        while True:
            table = queue.get()
            try:
                if process_function(table):
                    post_to_queues(success_queues, table)
                else:
                    post_to_queues(failure_queues, table)
            except:
                post_to_queues(failure_queues, table)

    return run_service


def run_service(queue: Queue, success_queues, failure_queues, processing_function):
    service(processing_function)(queue, success_queues, failure_queues)


def start_flow(flow):
    queue_lookup = create_queues(flow)
    processes = []
    for q in flow:
        success_queues = [queue_lookup[x] for x in flow[q]["Success"]]
        failure_queues = [queue_lookup[x] for x in flow[q]["Failure"]]
        processes.append(Process(target=run_service, args=(queue_lookup[q],success_queues, failure_queues, flow[q]["Function"])))
        processes[-1].start()
    return queue_lookup, processes
