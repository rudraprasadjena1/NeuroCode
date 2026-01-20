import json
import os

with open("storage/dependencies.json", "r", encoding="utf-8") as f:
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

os.makedirs("web", exist_ok=True)
with open("web/graph.json", "w", encoding="utf-8") as f:
    json.dump(graph, f, indent=2)

print("Graph exported to web/graph.json")
