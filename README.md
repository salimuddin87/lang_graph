# lang_graph

## Intial Setup
* C:\PycharmProjects\lang_graph>uv init
```ignorelang
Initialized project `lang-graph`
```

* C:\PycharmProjects\lang_graph>uv venv
```
Using CPython 3.12.10 interpreter at: C:\Users\md_salimuddin_ansari\AppData\Local\Programs\Python\Python312\python.exe
Creating virtual environment at: .venv
Activate with: .venv\Scripts\activate
```

* (lang_graph) C:\PycharmProjects\lang_graph>uv add -r requirements.txt
```ignorelang
Resolved 36 packages in 3.27s
Prepared 24 packages in 6.63s
Installed 35 packages in 1.84s
 + annotated-types==0.7.0                                                                                                                                                                                                               
...
```
* C:\PycharmProjects\lang_graph>uv add ipykernel
```ignorelang
Resolved 69 packages in 2.84s
Prepared 26 packages in 6.77s
Installed 28 packages in 2.27s
```
## Component of LangGraph
1. Edge: 
2. Node: 
3. state: 

## There are 2 ways to solve a problem in LangGraph
1. Graph API <START, END, Node, Edge, State>
   - This is the low-level API that allows you to build and manipulate graphs directly.
   - It provides fine-grained control over the graph structure and execution flow.
   - You can create nodes, edges, and manage their states explicitly.
   - StateGraph is a specific type of graph that focuses on managing the state of nodes and edges.
2. Function API
    - This is a higher-level API that abstracts away some of the complexities of graph management.
    - It allows you to define functions that can be executed within the graph context.
    - You can use decorators to define nodes and edges, making it easier to work with graphs without dealing with low-level details.
    - Function API is more user-friendly and suitable for most use cases, especially for those who prefer a more declarative approach.

## To use Jupyter Notebook
1. (venv) C:\PycharmProjects\lang_graph>python -m ipykernel install --user --name=lang_graph
2. Open Jupyter Notebook and select the kernel named `lang_graph` to ensure you're using the correct virtual environment.
3. You can now run your notebooks with the packages installed in the `lang_graph` virtual environment.
4. To list all available kernels, you can use the command:
   ```
   jupyter kernelspec list
   ```
5. To uninstall a kernel, use the command:
   ```
    jupyter kernelspec uninstall <kernel_name>
    ```


