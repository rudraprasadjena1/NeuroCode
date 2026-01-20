#scanner/export_graph.py
import json
import os


def export_dependency_graph(
    dependencies_path: str = "storage/dependencies.json",
    output_path: str = "storage/graph.json",
):
    if not os.path.exists(dependencies_path):
        raise FileNotFoundError(f"{dependencies_path} not found")

    with open(dependencies_path, "r", encoding="utf-8") as f:
        deps = json.load(f)

    nodes = []
    edges = []
    seen = set()

    for src, targets in deps.items():
        if src not in seen:
            nodes.append({"data": {"id": src}})
            seen.add(src)

        for dst in targets:
            if dst not in seen:
                nodes.append({"data": {"id": dst}})
                seen.add(dst)

            edges.append({
                "data": {
                    "source": src,
                    "target": dst
                }
            })

    graph = {
        "nodes": nodes,
        "edges": edges
    }

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(graph, f, indent=2)

    return graph
