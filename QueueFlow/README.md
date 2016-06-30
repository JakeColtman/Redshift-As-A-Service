# QueueFlow

Many data processing systems can be represented as the final result of small indep functions passing.  This idea is generally good practice and has inspired much of functional programming.
 
Smaller functions are easier to understand, simpler to write and more testable.  Moreover, if a system is made out of small units interacting, we can easily move up and down layers of abstraction.

QueueFlow is a sketch of a system that separates out the different layers.  You write functions that do one specific thing, and doesn't have to worry about how it will be use.  Then you create 
a config file that specifies how these functions should be glued together.

In addition to the general advantages above, this decoupling of function code from system design makes it much easier to allow domain experts to apply their knowledge.  Where a domain expert
may not understand the code itself, they have expert knowledge of how the components fit together.

## Useage

Firstly define a series of functions that take one variable input and return a boolean.  Generally return True if all is well and False otherwise.

Note that the messages being passed around is enitrely immutable.  Any message coming into the system will be passed around unaltered until it is finished.

Once you're happy with your functions, to stitch them together we define a config dictionary:

``` python
    flow = {
        "merge": {"Success": ["validate", "vacuum"], "Failure": [], "Function": merge},
        "vacuum": {"Success": [], "Failure": [], "Function": vacuum},
        "validate": {"Success": [], "Failure": [], "Function": validate}
    }
```

Every entry in the config dictionary is a step in the flow.  Each step has three parameters.  Success queues are queues that will recieve the message if the step is successful in processing
the message.  Similarly failure queues will recieve the message if there's a failure.

Finally Function is the function that will be run on the message.

To start the whole engine running, simply add:

```
    queue_lookup, processes = start_flow(flow)
```

This returns a dictionary of step name to the associated queue and a list of all of the processes

