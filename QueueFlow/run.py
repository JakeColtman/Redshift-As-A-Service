from FlowQueue import start_flow
from Actions.Merge import merge
from Actions.Vacuum import vacuum
from Actions.Validate import validate
from EndPoint import random_delay_messages
from multiprocessing import Process

flow = {
    "merge": {"Success": ["validate", "vacuum"], "Failure": [], "Function": merge},
    "vacuum": {"Success": [], "Failure": [], "Function": vacuum},
    "validate": {"Success": [], "Failure": [], "Function": validate}
}


if __name__ == "__main__":
    print("Starting")
    queue_lookup, processes = start_flow(flow)
    queue_lookup["merge"].put("Hello")
    p = Process(target=random_delay_messages, args=(queue_lookup["merge"],))
    p.start()