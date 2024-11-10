# Vai Srivastava - 0106
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx


def nodes():
    """plot the network of contiguous u.s. states

    inputs: none
    outputs: none
    returns: none
    """
    G = nx.read_edgelist("./contiguous-usa.dat", nodetype=str)

    pos = nx.spring_layout(G, seed=1)
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=1500,
        node_color="skyblue",
        font_size=10,
        font_weight="bold",
        font_color="black",
        edge_color="grey",
    )

    plt.title("Network of U.S. States")
    plt.show()


def plot_paths(G, source, target):
    """plot the shortest path between source and target states

    inputs:
        G: graph object
        source: starting state (str)
        target: destination state (str)
    outputs: none
    returns: none
    """
    shortest = nx.shortest_path(G, source, target)
    astar = nx.astar_path(G, source, target)
    dijkstra = nx.dijkstra_path(G, source, target)

    # get positions for nodes
    pos = nx.spring_layout(G, seed=1)
    # get edges in the dijkstra path
    path_edges = list(zip(dijkstra, dijkstra[1:]))

    # draw the graph
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=1500,
        node_color="skyblue",
        font_size=10,
        font_weight="bold",
        font_color="black",
        edge_color="grey",
    )
    # highlight the path edges in red
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="red", width=2)

    plt.title(f"Dijkstra Path from {source} to {target}")
    plt.show()


def weights(showplot=True):
    """add random weights to the graph edges and plot the weighted graph

    inputs:
        showplot: bool, if True plots the weighted graph (default: True)
    outputs: none
    returns:
        G: the weighted graph
    """
    G = nx.read_edgelist("./contiguous-usa.dat", nodetype=str)
    # assign random weights to edges
    for u, v in G.edges():
        G[u][v]["weight"] = np.random.randint(0, 15)
    # write the weighted graph to a file
    with open("./contiguous-usa-weighted.dat", "w") as file:
        for u, v, data in G.edges(data=True):
            weight = data["weight"]
            file.write(f"{u} {v} {weight}\n")

    if showplot:
        # draw the graph with edge weights
        pos = nx.spring_layout(G, seed=1)

        nx.draw(
            G,
            pos,
            with_labels=True,
            node_size=1500,
            node_color="skyblue",
            font_size=10,
            font_weight="bold",
            font_color="black",
            edge_color="grey",
        )
        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

        plt.title("Network of U.S. States with Edge Weights")
        plt.show()

    return G


def oregon_trail():
    """play an interactive game to travel from one state to another

    inputs: none
    outputs: none
    returns: none
    """
    G = weights(showplot=False)

    print("Now starting Oregon Trail game\n")
    print("note: enter `q` into any input field to quit the game")

    sourceog = input("What state are you starting from?\n> ")
    if "q" in sourceog:
        print("Game exited.")
        return
    targetog = input("What state are you heading to?\n> ")
    if "q" in targetog:
        print("Game exited.")
        return

    try:
        dijkstra_path = nx.dijkstra_path(G, sourceog, targetog)
        dijkstra_path_weight = nx.dijkstra_path_length(G, sourceog, targetog)
    except nx.NetworkXNoPath:
        print(f"No path exists between {sourceog} and {targetog}.")
        return

    print(f"\nStarting your journey from {sourceog} to {targetog}!\n")
    sourcecurrent = sourceog
    user_path = [sourcecurrent]
    user_path_weight = 0

    while sourcecurrent != targetog:
        neighbors = list(G.neighbors(sourcecurrent))
        print(f"\nYou are currently in {sourcecurrent}. You can travel to:")
        for neighbor in neighbors:
            print(f"- {neighbor}")

        next_state = input("\nWhere would you like to go next?\n> ")
        if "q" in next_state:
            print("Game exited.")
            return
        elif next_state not in neighbors:
            print("Invalid choice. Please select a neighboring state.")
            continue

        user_path.append(next_state)
        user_path_weight += G[sourcecurrent][next_state]["weight"]
        sourcecurrent = next_state

    if user_path == dijkstra_path or user_path_weight == dijkstra_path_weight:
        print(
            "\nCongratulations! You've reached your destination following the optimal path."
        )
    else:
        print("\nYou reached your destination, but you didn't take the optimal path.")

    # plot the user's path and the optimal path
    pos = nx.spring_layout(G, seed=1)
    plt.figure(figsize=(12, 8))

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=1500,
        node_color="skyblue",
        edge_color="grey",
    )

    # draw the optimal path in red
    dijkstra_edges = list(zip(dijkstra_path, dijkstra_path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=dijkstra_edges, edge_color="red", width=2)
    nx.draw_networkx_nodes(
        G,
        pos,
        nodelist=dijkstra_path,
        node_color="red",
        node_size=1500,
        label="Dijkstra Path",
    )

    # draw the user's path in blue
    user_edges = list(zip(user_path, user_path[1:]))
    nx.draw_networkx_edges(
        G, pos, edgelist=user_edges, edge_color="blue", width=2, style="dashed"
    )
    nx.draw_networkx_nodes(
        G, pos, nodelist=user_path, node_color="blue", node_size=1500, label="User Path"
    )

    plt.title(f"Journey from {sourceog} to {targetog}")
    plt.legend(["Dijkstra Path", "User Path"])
    plt.show()


if __name__ == "__main__":
    # 3.1
    nodes()

    # 3.2
    G = nx.read_edgelist("./contiguous-usa.dat", nodetype=str)
    plot_paths(G, "CA", "NY")

    # 3.3
    weights()

    # 3.4
    oregon_trail()
