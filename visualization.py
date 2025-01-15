import trimesh
import numpy as np
import plotly.graph_objects as go

stl_path = r"C:\Users\lucat\Downloads\brain.stl"

mesh = trimesh.load_mesh(stl_path)

# Gets vertices and face data from the brain mesh
vertices = mesh.vertices
faces = mesh.faces

colors = np.zeros((len(vertices), 3))  


# Creates the 3D mesh visualization
fig = go.Figure(data=[go.Mesh3d(
    x=vertices[:, 0], y=vertices[:, 1], z=vertices[:, 2],
    i=faces[:, 0], j=faces[:, 1], k=faces[:, 2],
    vertexcolor=colors,  
    opacity=0.25  # Low opacity is used to view the internal regions of the brain
)])

fig.update_layout(
    title="Brain Visualization",
    scene=dict(
        xaxis_title="X-axis",
        yaxis_title="Y-axis",
        zaxis_title="Z-axis",
        camera=dict(
            eye=dict(x=0, y=0, z=2),  # Position camera above brain for top view
            up=dict(x=0, y=1, z=0)     
        ),
        aspectmode='data',  
        bgcolor="forestgreen"
    ),
    paper_bgcolor="forestgreen"

)


fig.show()
