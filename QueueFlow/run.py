from .FlowQueue import service, run_service, post_to_queues
from .Actions.Merge import merge
from .Actions.Vacuum import vacuum
from .Actions.Validate import validate

work_flow = {
    "merge": {"Success": ["validate", "vacuum"], "Failure": [], "Function": merge},
    "vacuum": {"Success": [], "Failure": [], "Function": vacuum},
    "validate": {"Success": [], "Failure": [], "Function": validate}
}




if __name__ == "__main__":
    print("Starting")