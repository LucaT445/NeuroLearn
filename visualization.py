import trimesh
import numpy as np
import plotly.graph_objects as go

# Path to your brain STL file
stl_path = r"C:\Users\lucat\Downloads\brain.stl"

# Load the STL file using trimesh
mesh = trimesh.load_mesh(stl_path)

# Extract vertices and faces from the mesh
vertices = mesh.vertices
faces = mesh.faces

# Set all vertices to black
colors = np.zeros((len(vertices), 3))  # Default black for all vertices


# Create the 3D mesh visualization
fig = go.Figure(data=[go.Mesh3d(
    x=vertices[:, 0], y=vertices[:, 1], z=vertices[:, 2],
    i=faces[:, 0], j=faces[:, 1], k=faces[:, 2],
    vertexcolor=colors,  # Assign vertex colors
    opacity=0.25  # semi-opaque
)])

# Add layout details
fig.update_layout(
    title="3D Brain Visualization",
    scene=dict(
        xaxis_title="X-axis",
        yaxis_title="Y-axis",
        zaxis_title="Z-axis",
        camera=dict(
            eye=dict(x=0, y=0, z=2),  # Position camera above brain for top view
            up=dict(x=0, y=1, z=0)     # Orient "up" direction
        ),
        aspectmode='data'  # Equal aspect ratio
    )
)

# Show the visualization
fig.show()
