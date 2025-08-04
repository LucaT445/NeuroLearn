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

    region_color_dict = {
    "Frontal Lobe": "red",
    "Parietal Lobe": "yellow",
    "Temporal Lobe": "green",
    "Occipital Lobe": "blue",
    "Cerebellum": "purple",
    "Pituitary Gland": "brown",
    "Brainstem": "orange",
    "Corpus Callosum": "black"
}
    default_color = "lightgrey"

    description_dict = {
    "Frontal Lobe": {
        "name": "Frontal Lobe",
        "function": "Responsible for the executive functions, movement, personality, decision making, and behavior regulation.",
        "location": "Located in the front part of the cerebral cortex, right behind the forehead.",
        "examples": "Voluntary motor control, attention, problem solving, planning, reward processing, and inhibiting inappropriate behavior.",
        "disorders": [
            {
                "name": "Attention Deficit Hyperactivity Disorder (ADHD)",
                "description": "A condition characterized by executive dysfunction, causing symptoms such as difficulty regulating attention, poor working memory, trouble initiating and completing important tasks, and impulsive and hyperactive behavior."
            },
            {
                "name": "Frontal Lobe Syndrome",
                "description": "Can lead to personality changes, apathy, disinhibition, and poor judgment following damage to the frontal cortex."
            }
        ]
    },

    "Parietal Lobe": {
        "name": "Parietal Lobe",
        "function": "Responsible for spatial awareness and sensory integration (touch, temperature, pain), as well as coordination of visual input with movement.",
        "location": "Located behind the frontal lobe at the top of the brain.",
        "examples": "Navigating environments, recognizing objects by touch, solving math problems, reading maps.",
        "disorders": [
            {
                "name": "Gerstmann Syndrome",
                "description": "Includes difficulties with math, writing, distinguishing left from right, and recognizing fingers, due to left parietal damage."
            },
            {
                "name": "Hemispatial Neglect",
                "description": "A condition where a person is unaware of objects or even their own limbs on one side of the body, typically due to right parietal lobe damage."
            }
        ]
    },

    "Temporal Lobe": {
        "name": "Temporal Lobe",
        "function": "Handles auditory processing, memory formation, and language comprehension. It also contributes to emotional responses.",
        "location": "Located on the sides of the brain, near the temples, beneath the lateral fissure.",
        "examples": "Hearing and interpreting speech, recognizing faces, storing long-term memories.",
        "disorders": [
            {
                "name": "Wernicke’s Aphasia",
                "description": "A language comprehension disorder where speech is fluent but nonsensical, caused by left temporal damage."
            },
            {
                "name": "Temporal Lobe Epilepsy",
                "description": "A form of epilepsy involving seizures that originate in the temporal lobe and affect memory, emotion, and consciousness."
            }
        ]
    },

    "Occipital Lobe": {
        "name": "Occipital Lobe",
        "function": "The brain's visual processing center — it interprets information from the eyes.",
        "location": "Located at the back of the brain, behind the parietal and temporal lobes.",
        "examples": "Recognizing colors, detecting motion, identifying shapes, visual tracking.",
        "disorders": [
            {
                "name": "Cortical Blindness",
                "description": "Vision loss due to damage in the occipital cortex despite healthy eyes."
            },
            {
                "name": "Visual Agnosia",
                "description": "An inability to recognize objects visually, even though vision is intact."
            }
        ]
    },

    "Pituitary Gland": {
        "name": "Pituitary Gland",
        "function": "Regulates hormone secretion and connects the nervous system to the endocrine system.",
        "location": "A small, pea-shaped gland at the base of the brain, below the hypothalamus.",
        "examples": "Controlling growth, stress responses, metabolism, and reproductive functions.",
        "disorders": [
            {
                "name": "Pituitary Adenoma",
                "description": "A usually benign tumor that can lead to hormone imbalances and vision issues."
            },
            {
                "name": "Hypopituitarism",
                "description": "A condition where the pituitary fails to produce one or more essential hormones."
            }
        ]
    },

    "Brainstem": {
        "name": "Brainstem",
        "function": "Controls basic survival functions like breathing, heart rate, and blood pressure. Acts as a relay center between brain and body.",
        "location": "Connects the cerebrum to the spinal cord, located at the base of the brain.",
        "examples": "Regulating heartbeat, automatic breathing, maintaining consciousness, swallowing.",
        "disorders": [
            {
                "name": "Locked-In Syndrome",
                "description": "A condition where a person is conscious but unable to move or speak due to brainstem damage."
            },
            {
                "name": "Central Sleep Apnea",
                "description": "Occurs when the brainstem fails to send proper signals to control breathing."
            }
        ]
    },

    "Cerebellum": {
        "name": "Cerebellum",
        "function": "Responsible for coordination, balance, and fine-tuning motor activity.",
        "location": "Located under the occipital lobes, at the back of the brain near the brainstem.",
        "examples": "Balancing while walking, refining hand-eye coordination, smooth muscle control.",
        "disorders": [
            {
                "name": "Ataxia",
                "description": "A disorder that leads to poor coordination, imbalance, and unsteady movements."
            },
            {
                "name": "Cerebellar Degeneration",
                "description": "The progressive loss of neurons in the cerebellum, often leading to severe motor dysfunction."
            }
        ]
    },

    "Corpus Callosum": {
        "name": "Corpus Callosum",
        "function": "Connects the left and right hemispheres of the brain and enables communication between them.",
        "location": "A thick band of nerve fibers located in the center of the brain, between the two hemispheres.",
        "examples": "Sharing information between hemispheres, integrating cognitive, motor, and sensory tasks.",
        "disorders": [
            {
                "name": "Split-Brain Syndrome",
                "description": "Caused when the corpus callosum is severed, often during epilepsy treatment, leading to disrupted communication between hemispheres."
            },
            {
                "name": "Agenesis of the Corpus Callosum (ACC)",
                "description": "A condition in which the corpus callosum fails to develop properly, often resulting in cognitive and motor delays."
            }
        ]
    }
}


    fig = go.Figure()

    for name, geom in scene.geometry.items():
        if not isinstance(geom, trimesh.Trimesh):
            continue

        region_name = mesh_region_dict.get(name, "Unknown Region")

        verts = geom.vertices
        faces = geom.faces

        color = region_color_dict.get(region_name, default_color)


        fig.add_trace(go.Mesh3d(
            x=verts[:, 0], y=verts[:, 1], z=verts[:, 2],
            i=faces[:, 0], j=faces[:, 1], k=faces[:, 2],
            color=color,
            opacity=1.0,
            name=region_name,
            hovertext=[region_name] * len(verts),   # to ensure the name is displayed no matter where in the region the arrow is
            hoverinfo='text',
        ))

    fig.update_layout( # eliminates gridlines so that the brain is displayed on a blank canvas
    title="NeuroLearn",
    scene=dict(
        xaxis=dict(
            title="",
            showgrid=False,
            zeroline=False,
            showticklabels=False,
            showbackground=False   
        ),
        yaxis=dict(
            title="",
            showgrid=False,
            zeroline=False,
            showticklabels=False,
            showbackground=False   
        ),
        zaxis=dict(
            title="",
            showgrid=False,
            zeroline=False,
            showticklabels=False,
            showbackground=False   
        ),
        aspectmode="data",
        bgcolor="rgba(0,0,0,0)"            
    ),
    paper_bgcolor="rgba(0,0,0,0)",
    margin=dict(l=0, r=0, b=0, t=50)
)

    return fig, description_dict









