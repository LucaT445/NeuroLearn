def build_brain_figure():
    import trimesh
    import plotly.graph_objects as go

    # Load GLB
    glb_path = r"C:\Users\lucat\Downloads\brain.glb"
    scene = trimesh.load(glb_path, process=False)

    # Mappings
    mesh_region_dict = {
        "Material2_6": "Frontal Lobe",
        "Material2_2": "Parietal Lobe",
        "Material2_1": "Temporal Lobe",
        "Material2_5": "Occipital Lobe",
        "Material2": "Pituitary Gland",
        "Material2_4": "Brainstem",
        "Material2_9": "Cerebellum",
        "Material2_8": "Corpus Callosum"
    }

    description_dict = {
        "Frontal Lobe": "Responsible for the executive functions, movement, personality, decision making, behavior regulation. "
                        "It plays a crucial role in attention, problem-solving, voluntary motor control, and reward processing.",
        "Parietal Lobe": "Responsible for spatial awareness, sensory integration (touch, temperature, pain), and processing information "
                         "related to body position and navigation. It also plays a role in reading, mathematics, and coordination between vision and movement.",
        "Temporal Lobe": "Responsible for auditory processing, memory formation, and language comprehension. "
                         "It also contributes to emotion, facial recognition, and the interpretation of sounds and speech.",
        "Occipital Lobe": "The visual processing center of the brain. "
                          "It interprets visual input such as color, light, shape, and motion, and helps in recognizing objects and spatial orientation.",
        "Pituitary Gland": "The master gland of the human body. It regulates the release of hormones that control growth, metabolism, stress response, and reproductive functions. "
                           "It plays a key role in maintaining homeostasis by linking the nervous and endocrine systems.",
        "Brainstem": "Controls vital functions such as breathing, heart rate, and blood pressure. "
                     "It also facilitates the flow of messages between the brain and body and is essential for consciousness and basic survival reflexes.",
        "Cerebellum": "Responsible for coordination, balance, and fine motor control. It helps maintain posture, regulate voluntary movements, and ensure smooth, precise actions. It also plays a role in motor learning and timing.",
        "Corpus Callosum": "A thick bundle of nerve fibers that connects the left and right hemispheres of the brain, enabling communication and coordination between them. It plays a key role in integrating motor, sensory, and cognitive functions."
    }

    fig = go.Figure()

    for name, geom in scene.geometry.items():
        if not isinstance(geom, trimesh.Trimesh):
            continue

        region_name = mesh_region_dict.get(name, "Unknown Region")

        verts = geom.vertices
        faces = geom.faces

        if region_name == "Frontal Lobe":
            color = "red"
        elif region_name == "Temporal Lobe":
            color = "darkgreen"
        elif region_name == "Parietal Lobe":
            color = "yellow"
        elif region_name == "Occipital Lobe":
            color = "blue"
        elif region_name == "Pituitary Gland":
            color = "brown"
        elif region_name == "Brainstem":
            color = "orange"
        elif region_name == "Cerebellum":
            color = "purple"
        elif region_name == "Corpus Callosum":
            color = "black"
        else:
            color = "lightgrey"

        fig.add_trace(go.Mesh3d(
            x=verts[:, 0], y=verts[:, 1], z=verts[:, 2],
            i=faces[:, 0], j=faces[:, 1], k=faces[:, 2],
            color=color,
            opacity=1.0,
            name=region_name,
            hovertext=[region_name] * len(verts),   # one per vertex
            hoverinfo='text',
        ))

    fig.update_layout(
        title="NeuroLearn",
        scene=dict(
            xaxis_title="X", yaxis_title="Y", zaxis_title="Z",
            aspectmode="data"
        ),
        showlegend=False
    )

    return fig, description_dict









