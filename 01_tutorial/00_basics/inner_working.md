**hello_chai.cpython-310.pyc**

program -> Byte Code(.pyc file) -> python vm
            (mostly hidden)


1. Compile to Byte code(low level & platform independent)

    * Byte code runs faster
    * .pyc -> compiled python (frozen binaries)
    * __pycache__ 

    source change (diffing algorithm) & python version
    * hello_chai.cpython-310.pyc
        1. works only for imported files
        2. not for top level files

2. Python Virtual Machine PVM
    * code loop to iterate byte code
    * run time engine
    * also known as python interpreter

    Byte code is NOT machine code
    * python specific interpretation
    * cpython (standard implementation), jython (to work with java binaries), iron python, stackless (for concurrency), PyPy (for performance)
