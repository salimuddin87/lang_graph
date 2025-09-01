# LangGraph
LangGraph Platform makes it easy to get your agent running in production

## LangGraph Platform components
1. **LangGraph Server**: The server defines an opinionated API and architecture that incorporates best practices for deploying agentic applications, allowing you to focus on building your agent logic rather than developing server infrastructure.
2. **LangGraph CLI**: LangGraph CLI is a command-line interface that helps to interact with a local LangGraph.
3. **LangGraph Studio**: LangGraph Studio is a specialized IDE that can connect to a LangGraph Server to enable visualization, interaction, and debugging of the application locally.
4. **Python/JS SDK**: The Python/JS SDK provides a programmatic way to interact with deployed LangGraph Applications.
5. **Remote Graph**: A RemoteGraph allows you to interact with any deployed LangGraph application as though it were running locally.
6. **LangGraph Control Plane**: The LangGraph Control Plane refers to the Control Plane UI where users create and update LangGraph Servers and the Control Plane APIs that support the UI experience.
7. **LangGraph Data Plane**: The LangGraph Data Plane refers to LangGraph Servers, the corresponding infrastructure for each server, and the “listener” application that continuously polls for updates from the LangGraph Control Plane.

![LangGraph Platform components](C:\Users\md_salimuddin_ansari\PycharmProjects\lang_graph\Images\langgraph-components.png)

## LangGraph Server
It offers an API for creating and managing agent-based applications.

## Notes
* When you deploy a **graph** with LangGraph Server, you are deploying a “blueprint” for an Assistant.
* LangGraph Server leverages a database (Postgres Only) for persistence and a task queue (Redis).
* Install `langgraph-cli[inmem]` and run `langgraph dev`, This will start the LangGraph Server locally, running in-memory. The server will run in watch mode, listening for and automatically restarting on code changes.
* Start server with debugging enabled `langgraph dev --debug-port 5678`.
![Debugpy](C:\Users\md_salimuddin_ansari\PycharmProjects\lang_graph\Images\langgraph-debugpy.png)


