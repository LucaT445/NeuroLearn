import trimesh
import plotly.graph_objects as go

ply_path = r"C:\Users\lucat\Downloads\brain_backup.ply"

mesh = trimesh.load_mesh(ply_path)

# Gets vertices, faces, and vertex colors from the brain mesh
vertices = mesh.vertices
faces = mesh.faces

vertex_colors = mesh.visual.vertex_colors[:, :3] / 255.0  # Normalize to 0-1 range for Plotly

fig = go.Figure(data=[go.Mesh3d(
    x=vertices[:, 0], y=vertices[:, 1], z=vertices[:, 2],
    i=faces[:, 0], j=faces[:, 1], k=faces[:, 2],
    vertexcolor=vertex_colors, 
    opacity=0.9  # Adjust opacity as needed
)])

fig.update_layout(
    title="Brain Visualization",
    scene=dict(
        xaxis_title="X-axis",
        yaxis_title="Y-axis",
        zaxis_title="Z-axis",
        camera=dict(
            eye=dict(x=1.5, y=1.5, z=1.5), 
            up=dict(x=0, y=1, z=0)
        ),
        aspectmode='data',
        bgcolor="forestgreen"
    ),
    paper_bgcolor="forestgreen"
)

fig.show()
