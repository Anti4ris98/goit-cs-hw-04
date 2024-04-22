import plotly.graph_objects as go
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


# Генерація точок
num_points = 10
points_x = np.array([1, 0, 0])
points_y = np.array([0, 1, 0])
points_z = np.array([0, 0, 1])


# Створення об'єкта "Figure" для 3D графіка
fig = go.Figure()


# Додавання точок у 3D простір
fig.add_trace(go.Scatter3d(
    x=points_x,
    y=points_y,
    z=points_z,
    mode='markers',
    marker=dict(
        size=6,
        color='blue',  # Колір точок
        opacity=1.0
    ),
    name='Random Points'
))


# Налаштування вигляду графіка
fig.update_layout(
    scene=dict(
        xaxis=dict(title='Вісь X'),
        yaxis=dict(title='Вісь Y'),
        zaxis=dict(title='Вісь Z')
    ),
    title='3D простір з точками',
)


# Відображення графіка
fig.show()