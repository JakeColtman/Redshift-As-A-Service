from multiprocessing import Queue


def post_to_queues(queues, message):
    for queue in queues:
        queue.put(message)


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
